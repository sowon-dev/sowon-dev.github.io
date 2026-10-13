import os
import glob
import re

# 작성자님이 직접 정의하거나 승인해주신 고품질 기준 예시들 (100% 보존)
VERIFIED_SUMMARIES = {
    '250103cahe-control.md': '메타데이터 설정시 캐싱 방지 가능하지만 불필요한 트래픽을 많이 유발할 수 있으므로 정적 리소스 버전 명시 추가 추천',
    '241209batch-service-restart.md': '배포 관리자가 수동으로 야간에 서버를 재시작하는 번거로움을 해결하기 위해 Batch 스크립트(.bat)와 윈도우 작업 스케줄러를 활용해 특정 시간에 서버가 자동 재시작되도록 설정하는 방법 공유.\n단순 재시작이 아니라, 로그 파일을 통해 서비스가 정상적으로 중지되었는지 상태를 확인한 후 안전하게 재시작하도록 스크립트 구성.',
    '210721woowacourse-architecture.md': "시스템 무결성보다 개발팀의 협력을 이끄는 'Architectus Oryzus'형 아키텍트의 역할과 지속적인 학습의 중요성 확인.\n레거시 개편 및 MSA 도입 등 4가지 실무 사례를 바탕으로 CI/CD, DDD, 애자일 방법론 등을 적용해 문제를 해결하는 구체적인 접근 순서 정리.",
    '241023oracleDB-call-procedure.md': '오라클 DB에서 프로시저의 DBMS_OUTPUT.PUT_LINE 메시지를 콘솔에서 확인하려면 출력 기능 활성화가 필수적이다.\nPL/SQL 블록을 실행하기 전 최상단에 SET SERVEROUTPUT ON; 명령어를 선언해야 결과값이 정상적으로 표시된다.',
    '241129utterances.md': '헥소(Hexo) 블로그의 기존 페이스북 댓글 기능을 깃허브(GitHub) 아이디로 로그인하여 사용할 수 있는 utterances로 교체하는 방법을 정리한 글이다.\ncomment.jsx에 utterances 스크립트를 추가하고, _config.yml에서 페이스북 앱 ID만 제거하는 방식으로 댓글 시스템을 간단히 전환할 수 있다.',
    '241129java-util-properties.md': 'java.util.Properties는 문자열 기반의 키-값 쌍을 다루며 실행 중에도 설정값을 동적으로 변경할 수 있는 자바 내부 메모리 객체다.\n반면 .properties 파일은 애플리케이션 구동 시 초기 설정 정보를 제공하는 정적 외부 파일로, 상황과 목적에 맞게 두 방식을 적절히 구분하여 활용할 수 있다.',
    '241023oracle-query-pivot.md': '동적 또는 유동적인 코드로 인해 GROUP BY로 해결하기 어려운 다중 컬럼 집계 문제를 오라클 PIVOT 함수로 해결하는 방법이다.\nROW_NUMBER 또는 RANK 윈도우 함수로 순번을 부여한 뒤 PIVOT을 적용하여 행 데이터를 유연하게 열로 전환할 수 있다.'
}

def clean_inline_md(text):
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    text = re.sub(r'`([^`]+)`', r'\1', text)
    text = re.sub(r'\*\*([^\*]+)\*\*', r'\1', text)
    text = re.sub(r'\*([^\*]+)\*', r'\1', text)
    text = re.sub(r'[\r\n\t]+', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def parse_post_structure(body):
    body_no_code = re.sub(r'```[\s\S]*?```', '', body)
    lines = body_no_code.split('\n')
    
    sections = []
    current_sec = {'title': 'intro', 'lines': []}
    
    for l in lines:
        stripped = l.strip()
        if not stripped:
            continue
        if stripped.startswith('#'):
            if current_sec['lines']:
                sections.append(current_sec)
            sec_title = clean_inline_md(re.sub(r'^#+\s*', '', stripped))
            current_sec = {'title': sec_title, 'lines': []}
        elif not stripped.startswith('|') and not stripped.startswith('!['):
            cleaned = clean_inline_md(stripped)
            if len(cleaned) >= 12 and not any(skip in cleaned for skip in ['http://', 'https://', 'github.com', '참고자료', '출처', '참고 블로그']):
                current_sec['lines'].append(cleaned)
                
    if current_sec['lines']:
        sections.append(current_sec)
        
    return sections

def extract_code_keywords(body):
    # Extract distinctive identifiers from code blocks or commands
    code_blocks = re.findall(r'```(?:\w+)?\s*([\s\S]*?)```', body)
    keywords = []
    for cb in code_blocks:
        found = re.findall(r'\b([A-Z_]{3,}|@\w+|[A-Za-z0-9_]+\.[A-Za-z0-9_]+)\b', cb)
        for f in found:
            if f not in ['NULL', 'TRUE', 'FALSE', 'SELECT', 'FROM', 'WHERE', 'AND', 'OR', 'SET'] and f not in keywords:
                keywords.append(f)
                if len(keywords) >= 5:
                    break
        if len(keywords) >= 5:
            break
    return keywords

def generate_user_style_tldr(filename, title, body):
    if filename in VERIFIED_SUMMARIES:
        return VERIFIED_SUMMARIES[filename]
        
    clean_title = re.sub(r'^\[.*?\]\s*', '', title).strip()
    sections = parse_post_structure(body)
    all_lines = [l for sec in sections for l in sec['lines']]
    code_kws = extract_code_keywords(body)
    
    # Context 1: Algorithm / Coding Test
    if any(k in filename.lower() or k in title.lower() for k in ['al-', 'backjoon', 'leetcode', 'programmers', 'c10', 'l0']):
        # Find lines about Scanner vs BufferedReader, loop, data structure, memory/time
        approaches = [l for l in all_lines if any(x in l for x in ['풀이', '사용', '배열', '방식', '접근', '효율', '알고리즘', '시간', '메모리', 'Scanner', 'BufferedReader', 'Map', 'Set'])]
        line1 = f"'{clean_title}' 알고리즘 문제 해결을 위한 최적의 자료구조와 풀이 접근법을 정리한 내용이다."
        if approaches:
            line2 = approaches[0]
            if not line2.endswith('.'): line2 += '을 적용해 효율성을 높일 수 있다.'
            elif not (line2.endswith('다.') or line2.endswith('함.') or line2.endswith('음.')): line2 += '을 확인했다.'
        else:
            line2 = "입출력 최적화 및 시간/공간 복잡도를 고려한 구현 코드로 통과할 수 있다."
        return f"{line1}\n{line2}"

    # Context 2: Error & Troubleshooting
    if any(k in title.lower() or k in filename.lower() for k in ['오류', '에러', 'error', 'exception', '트러블', '해결', 'fail']):
        causes = [l for l in all_lines if any(x in l for x in ['원인', '문제', '이유', '발생', '에러', '안 되', '실패'])]
        solutions = [l for l in all_lines if any(x in l for x in ['해결', '수정', '설정', '추가', '변경', '처리', '조치'])]
        
        line1 = ""
        if causes:
            c_text = causes[0]
            if not c_text.endswith('.'): c_text += '으로 인해 오류가 발생했다.'
            elif '발생' not in c_text and '원인' not in c_text: c_text = f"{c_text} 문제 원인을 분석했다."
            line1 = c_text
        else:
            line1 = f"'{clean_title}' 실행 및 배포 과정에서 발생하는 에러 원인을 분석한 글이다."
            
        line2 = ""
        if solutions:
            s_text = solutions[0]
            if not s_text.endswith('.'): s_text += '을 적용하여 문제를 해결할 수 있다.'
            line2 = s_text
        else:
            line2 = "관련 설정값 및 소스 코드 수정을 통해 오류를 정상적으로 해결할 수 있다."
            
        res = f"{line1}\n{line2}"
        if len(res) <= 190:
            return res
        return f"'{clean_title}' 발생 시 원인을 파악하고 관련 설정을 수정하여 문제를 해결하는 방법이다.\n원인 분석에 따른 세부 수정 사항과 주의점을 파악하여 정상적인 동작을 구현할 수 있다."

    # Context 3: Comparison (vs, 차이)
    if any(k in title.lower() or k in filename.lower() for k in ['vs', '차이', '비교', 'diff']):
        # Find contrast sentences
        diff_lines = [l for l in all_lines if any(x in l for x in ['차이', '비교', '장점', '단점', '특징', '반면', '다르', '권장'])]
        line1 = f"'{clean_title}'의 핵심 개념과 동작 방식의 차이점을 분석하고 비교 정리한 글이다."
        if diff_lines:
            line2 = diff_lines[0]
            if not line2.endswith('.'): line2 += '을 비교하여 상황에 맞게 적용할 수 있다.'
        else:
            line2 = "동작 원리와 사용 환경의 차이를 파악하여 프로젝트 목적에 맞는 적절한 방식을 선택할 수 있다."
        return f"{line1}\n{line2}"

    # Context 4: Review / Webinar / Retrospective
    if any(k in title.lower() or k in filename.lower() for k in ['후기', '회고', '세미나', '웨비나', '강의', 'review']):
        insights = [l for l in all_lines if any(x in l for x in ['배운', '느낀', '중요', '역할', '실무', '접근', '아키텍트', '개발자', '이해'])]
        line1 = f"'{clean_title}'에 참여하고 주요 발표 내용과 배운 점을 정리한 글이다."
        line2 = insights[0] if insights else "실무 적용 사례를 통해 개발자의 역할과 협업, 지속적인 학습의 중요성을 확인할 수 있다."
        if not line2.endswith('.'): line2 += '을 확인했다.'
        return f"{line1}\n{line2}"

    # Context 5: Technical How-to / Guide / Concepts
    tech_sents = [l for l in all_lines if any(x in l for x in ['방법', '설정', '기능', '사용', '작성', '구현', '원리', '제공', '필요'])]
    line1 = f"{clean_title}의 개념과 동작 원리를 살펴보고 실무 적용 방법을 정리한 글이다."
    if tech_sents:
        # Choose the most specific sentence
        specific = tech_sents[0]
        if len(tech_sents) > 1 and len(specific) < 30:
            specific = tech_sents[1]
        line2 = specific
        if not line2.endswith('.'): line2 += '을 활용할 수 있다.'
    else:
        line2 = "필수적인 설정 과정과 예제 코드를 바탕으로 상황에 맞게 유연하게 적용할 수 있다."

    return f"{line1}\n{line2}"

def format_tldr_block(tldr_text):
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
    updated = 0
    
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

        body_cleaned = re.sub(r'<div class="notification is-tldr">[\s\S]*?</div>\s*', '', body).strip()
        body_cleaned = re.sub(r'<!-- more -->\s*', '', body_cleaned).strip()

        tldr_text = generate_user_style_tldr(filename, title, body_cleaned)
        tldr_block = format_tldr_block(tldr_text)

        new_content = f"---{frontmatter}---\n\n{tldr_block}\n\n<!-- more -->\n\n{body_cleaned}\n"
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        updated += 1

    print(f"Successfully overhauled TL;DR in all {updated} posts in user's style.")

if __name__ == '__main__':
    process_all_posts()
