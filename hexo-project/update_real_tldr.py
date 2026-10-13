import os
import glob
import re

CUSTOM_EXEMPLARS = {
    '250103cahe-control.md': '메타데이터 설정시 캐싱 방지 가능하지만 불필요한 트래픽을 많이 유발할 수 있으므로 정적 리소스 버전 명시 추가 추천',
    '241209batch-service-restart.md': '배포 관리자가 수동으로 야간에 서버를 재시작하는 번거로움을 해결하기 위해 Batch 스크립트(.bat)와 윈도우 작업 스케줄러를 활용해 특정 시간에 서버가 자동 재시작되도록 설정하는 방법 공유.\n단순 재시작이 아니라, 로그 파일을 통해 서비스가 정상적으로 중지되었는지 상태를 확인한 후 안전하게 재시작하도록 스크립트 구성.',
    '210721woowacourse-architecture.md': "시스템 무결성보다 개발팀의 협력을 이끄는 'Architectus Oryzus'형 아키텍트의 역할과 지속적인 학습의 중요성 확인.\n레거시 개편 및 MSA 도입 등 4가지 실무 사례를 바탕으로 CI/CD, DDD, 애자일 방법론 등을 적용해 문제를 해결하는 구체적인 접근 순서 정리."
}

def clean_markdown_text(text):
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    text = re.sub(r'`([^`]+)`', r'\1', text)
    text = re.sub(r'\*\*([^\*]+)\*\*', r'\1', text)
    text = re.sub(r'\*([^\*]+)\*', r'\1', text)
    text = re.sub(r'[\\#*_\-~>|]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_meaningful_sentences(body):
    body_no_code = re.sub(r'```[\s\S]*?```', '', body)
    body_no_html = re.sub(r'<[^>]+>', '', body_no_code)
    
    lines = body_no_html.split('\n')
    valid_sentences = []
    
    for line in lines:
        line_str = line.strip()
        if not line_str or line_str.startswith('|') or line_str.startswith('#'):
            continue
        line_clean = clean_markdown_text(line_str)
        if len(line_clean) < 15:
            continue
        if any(skip in line_clean for skip in ['http://', 'https://', 'github.com', '참고링크', '참고자료', '출처']):
            continue
        valid_sentences.append(line_clean)
        
    return valid_sentences

def summarize_post(filename, title, body):
    if filename in CUSTOM_EXEMPLARS:
        return CUSTOM_EXEMPLARS[filename]
        
    sentences = extract_meaningful_sentences(body)
    clean_title = re.sub(r'^\[.*?\]\s*', '', title).strip()
    
    # 1. Algorithm / Problem Solving
    if any(k in filename.lower() or k in title.lower() for k in ['al-', 'backjoon', 'leetcode', 'programmers', 'c10', 'l0']):
        time_or_mem = [s for s in sentences if any(x in s for x in ['시간', '메모리', '성능', '복잡도', '효율', '풀이'])]
        takeaway = time_or_mem[0] if time_or_mem else (sentences[-1] if sentences else '')
        if takeaway and len(takeaway) < 100:
            return f"'{clean_title}' 문제 해결을 위한 핵심 알고리즘 및 구현 접근법 정리.\n{takeaway}."
        return f"'{clean_title}' 알고리즘 문제 해결 과정 및 구현 코드와 시간/공간 복잡도 최적화 방법 정리."

    # 2. Troubleshooting / Error
    if any(k in title.lower() or k in filename.lower() for k in ['오류', '에러', 'error', 'exception', '트러블', '해결', 'fail']):
        cause_sents = [s for s in sentences if any(x in s for x in ['원인', '문제', '이유', '발생', '에러', '때문'])]
        sol_sents = [s for s in sentences if any(x in s for x in ['해결', '수정', '조치', '해법', '방법', '처리'])]
        line1 = cause_sents[0] if cause_sents else f"'{clean_title}' 발생 원인 분석"
        line2 = sol_sents[0] if sol_sents else "원인 해결을 위한 설정 변경 및 트러블슈팅 조치 방법 정리"
        if not line1.endswith('.'): line1 += '.'
        if not line2.endswith('.'): line2 += '.'
        res = f"{line1}\n{line2}"
        if len(res) <= 180:
            return res
        return f"'{clean_title}' 발생 원인 및 설정/코드 수정을 통한 트러블슈팅 해결 과정 정리."

    # 3. Comparison (VS / 차이)
    if any(k in title.lower() or k in filename.lower() for k in ['vs', '차이', '비교', 'diff']):
        comp_sents = [s for s in sentences if any(x in s for x in ['차이', '비교', '장점', '단점', '특징', '상황', '권장'])]
        sub = comp_sents[0] if comp_sents else "각각의 핵심 차이점과 실무 활용 기준"
        if not sub.endswith('.'): sub += '.'
        return f"'{clean_title}'의 핵심 개념 및 동작 원리 차이점 비교 분석.\n{sub}"

    # 4. Review / Retrospective
    if any(k in title.lower() or k in filename.lower() for k in ['후기', '회고', '세미나', '웨비나', '강의', 'review']):
        rev_sents = [s for s in sentences if any(x in s for x in ['배운', '느낀', '중요', '생각', '정리', '성장', '경험'])]
        t1 = rev_sents[0] if rev_sents else (sentences[0] if sentences else '주요 핵심 내용')
        if not t1.endswith('.'): t1 += '.'
        return f"'{clean_title}' 참여 및 학습 과정에서 얻은 인사이트 정리.\n{t1}"

    # 5. General Tech / How-to
    # Pick the most informative 1~2 sentences
    good_sents = [s for s in sentences if any(x in s for x in ['방법', '설정', '기능', '사용', '원리', '구현', '이유', '핵심'])]
    if good_sents:
        first = good_sents[0]
        second = good_sents[1] if len(good_sents) > 1 and len(first) < 80 else ''
        if not first.endswith('.'): first += '.'
        if second and not second.endswith('.'): second += '.'
        res = f"{first}\n{second}".strip() if second else first
        if len(res) <= 180:
            return res

    if sentences:
        s1 = sentences[0]
        if not s1.endswith('.'): s1 += '.'
        if len(s1) <= 150:
            return s1

    return f"'{clean_title}'의 개념과 동작 원리 및 실무 활용 방법 핵심 정리."

def format_tldr_block(tldr_text):
    # Ensure it's max 2 lines
    lines = [l.strip() for l in tldr_text.strip().split('\n') if l.strip()]
    if len(lines) > 2:
        lines = lines[:2]
    content = '\n    '.join(lines)
    return f'''<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">{content}</p>
</div>'''

def process_all_posts():
    posts = glob.glob('source/_posts/*.md')
    print(f"Total posts to process: {len(posts)}")
    updated_count = 0

    for path in posts:
        filename = os.path.basename(path)
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            raw = f.read()

        parts = raw.split('---', 2)
        if len(parts) < 3:
            continue

        frontmatter = parts[1]
        body = parts[2]

        title_match = re.search(r'^title:\s*["\']?(.*?)["\']?$', frontmatter, re.M)
        title = title_match.group(1).strip() if title_match else filename.replace('.md', '')

        # Strip old tldr block
        body_cleaned = re.sub(r'<div class="notification is-tldr">[\s\S]*?</div>\s*', '', body).strip()
        body_cleaned = re.sub(r'<!-- more -->\s*', '', body_cleaned).strip()

        # Generate summary
        summary = summarize_post(filename, title, body_cleaned)
        tldr_block = format_tldr_block(summary)

        # Assemble new post
        new_content = f"---{frontmatter}---\n\n{tldr_block}\n\n<!-- more -->\n\n{body_cleaned}\n"
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        updated_count += 1

    print(f"Successfully updated TL;DR in {updated_count} posts.")

if __name__ == '__main__':
    process_all_posts()
