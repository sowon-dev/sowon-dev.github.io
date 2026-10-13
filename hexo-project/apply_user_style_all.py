import os
import glob
import re

# 사용자가 직접 작성하거나 승인한 기준 예시 (100% 보존)
EXEMPLARS = {
    '250103cahe-control.md': '메타데이터 설정시 캐싱 방지 가능하지만 불필요한 트래픽을 많이 유발할 수 있으므로 정적 리소스 버전 명시 추가 추천',
    '241209batch-service-restart.md': '배포 관리자가 수동으로 야간에 서버를 재시작하는 번거로움을 해결하기 위해 Batch 스크립트(.bat)와 윈도우 작업 스케줄러를 활용해 특정 시간에 서버가 자동 재시작되도록 설정하는 방법 공유.\n단순 재시작이 아니라, 로그 파일을 통해 서비스가 정상적으로 중지되었는지 상태를 확인한 후 안전하게 재시작하도록 스크립트 구성.',
    '210721woowacourse-architecture.md': "시스템 무결성보다 개발팀의 협력을 이끄는 'Architectus Oryzus'형 아키텍트의 역할과 지속적인 학습의 중요성 확인.\n레거시 개편 및 MSA 도입 등 4가지 실무 사례를 바탕으로 CI/CD, DDD, 애자일 방법론 등을 적용해 문제를 해결하는 구체적인 접근 순서 정리.",
    '241023oracleDB-call-procedure.md': '오라클 DB에서 프로시저의 DBMS_OUTPUT.PUT_LINE 메시지를 콘솔에서 확인하려면 출력 기능 활성화가 필수적이다.\nPL/SQL 블록을 실행하기 전 최상단에 SET SERVEROUTPUT ON; 명령어를 선언해야 결과값이 정상적으로 표시된다.',
    '241129utterances.md': '헥소(Hexo) 블로그의 기존 페이스북 댓글 기능을 깃허브(GitHub) 아이디로 로그인하여 사용할 수 있는 utterances로 교체하는 방법을 정리한 글이다.\ncomment.jsx에 utterances 스크립트를 추가하고, _config.yml에서 페이스북 앱 ID만 제거하는 방식으로 댓글 시스템을 간단히 전환할 수 있다.',
    '241129java-util-properties.md': 'java.util.Properties는 문자열 기반의 키-값 쌍을 다루며 실행 중에도 설정값을 동적으로 변경할 수 있는 자바 내부 메모리 객체다.\n반면 .properties 파일은 애플리케이션 구동 시 초기 설정 정보를 제공하는 정적 외부 파일로, 상황과 목적에 맞게 두 방식을 적절히 구분하여 활용할 수 있다.',
    '241023oracle-query-pivot.md': '동적 또는 유동적인 코드로 인해 GROUP BY로 해결하기 어려운 다중 컬럼 집계 문제를 오라클 PIVOT 함수로 해결하는 방법이다.\nROW_NUMBER 또는 RANK 윈도우 함수로 순번을 부여한 뒤 PIVOT을 적용하여 행 데이터를 유연하게 열로 전환할 수 있다.',
    '221121JS-webstorage.md': '브라우저 저장소인 localStorage와 sessionStorage는 문자열 기반의 Key-Value 데이터를 클라이언트에 저장하며 CSRF로부터 안전하다.\n반면 쿠키는 요청마다 서버로 자동 전송되고 세션은 서버 메모리를 소비하므로 데이터 영구성과 목적에 맞게 분리해 활용해야 한다.',
    '220906Tomcat-vs-Apatch.md': '웹 서버(Apache)는 HTTP 요청을 받아 HTML, 이미지 등 정적 컨텐츠를 클라이언트에 제공하는 역할을 담당한다.\n반면 WAS(Tomcat)는 DB 조회나 비즈니스 로직 등 동적 처리를 담당하며, 부하 분산과 보안을 위해 두 서버를 분리 구축하는 것이 권장된다.',
    '210802Pattern-regexp.md': 'Spring Validation의 @NotNull, @NotBlank 어노테이션으로 해결하기 어려운 NULL 허용 및 공백 차단 조건을 @Pattern 정규표현식으로 구현한 사례다.\n정규식 선언 시 글자수 범위({0,64})를 명시해야 단일 문자가 아닌 전체 문자열에 대해 유효성 검사가 정상적으로 통과된다.'
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

def parse_post_sections(body):
    body_no_code = re.sub(r'```[\s\S]*?```', '', body)
    lines = body_no_code.split('\n')
    sections = []
    current_sec = {'title': 'intro', 'lines': []}
    
    for l in lines:
        s = l.strip()
        if not s: continue
        if s.startswith('#'):
            if current_sec['lines']:
                sections.append(current_sec)
            sec_title = clean_inline_md(re.sub(r'^#+\s*', '', s))
            current_sec = {'title': sec_title, 'lines': []}
        elif not s.startswith('|') and not s.startswith('!['):
            cleaned = clean_inline_md(s)
            if len(cleaned) >= 10 and not any(skip in cleaned for skip in ['http://', 'https://', 'github.com', '출처', '참고자료', '참고 블로그']):
                current_sec['lines'].append(cleaned)
    if current_sec['lines']:
        sections.append(current_sec)
    return sections

def generate_tldr(filename, title, body):
    if filename in EXEMPLARS:
        return EXEMPLARS[filename]
        
    clean_title = re.sub(r'^\[.*?\]\s*', '', title).strip()
    sections = parse_post_sections(body)
    all_lines = [l for sec in sections for l in sec['lines']]
    
    # 1. Algorithm
    if any(k in filename.lower() or k in title.lower() for k in ['al-', 'backjoon', 'leetcode', 'programmers', 'c10', 'l0']):
        approaches = [l for l in all_lines if any(x in l for x in ['풀이', '접근', '자료구조', 'Scanner', 'BufferedReader', '배열', '시간', '메모리', '효율', '코드'])]
        line1 = f"'{clean_title}' 알고리즘 문제의 요구사항을 분석하고 최적의 자료구조와 연산 방식을 적용해 구현한 풀이다."
        if approaches:
            line2 = approaches[0]
            if not line2.endswith('.'): line2 += '을 확인했다.'
            elif not any(line2.endswith(x) for x in ['다.', '함.', '음.']): line2 += '을 적용해 성능을 최적화했다.'
        else:
            line2 = "시간 복잡도와 메모리 사용량을 고려한 효율적인 구현 코드로 문제를 통과할 수 있다."
        return f"{line1}\n{line2}"

    # 2. Trouble / Error
    if any(k in title.lower() or k in filename.lower() for k in ['오류', '에러', 'error', 'exception', '트러블', '해결', 'fail']):
        causes = [l for l in all_lines if any(x in l for x in ['원인', '문제', '이유', '발생', '에러', '안 되', '때문'])]
        solutions = [l for l in all_lines if any(x in l for x in ['해결', '수정', '설정', '추가', '변경', '처리', '조치'])]
        line1 = causes[0] if causes else f"'{clean_title}' 실행 및 개발 과정에서 발생하는 오류 현상과 원인을 분석한 글이다."
        if not line1.endswith('.'): line1 += ' 원인을 파악했다.'
        elif not any(line1.endswith(x) for x in ['다.', '함.', '음.']): line1 += '으로 인해 문제가 발생했다.'
        
        line2 = solutions[0] if solutions else "관련 환경 설정과 코드를 알맞게 수정하여 정상적으로 동작하도록 해결할 수 있다."
        if not line2.endswith('.'): line2 += '을 통해 문제를 해결할 수 있다.'
        elif not any(line2.endswith(x) for x in ['다.', '함.', '음.']): line2 += ' 조치를 적용했다.'
        return f"{line1}\n{line2}"

    # 3. Comparison
    if any(k in title.lower() or k in filename.lower() for k in ['vs', '차이', '비교', 'diff']):
        diff_lines = [l for l in all_lines if any(x in l for x in ['차이', '비교', '장점', '단점', '특징', '반면', '다르', '권장'])]
        line1 = f"'{clean_title}'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다."
        if diff_lines:
            line2 = diff_lines[0]
            if not line2.endswith('.'): line2 += '의 차이를 고려하여 상황에 맞게 적용해야 한다.'
        else:
            line2 = "동작 원리와 장단점을 비교 파악하여 프로젝트 개발 상황에 적합한 방식을 선택할 수 있다."
        return f"{line1}\n{line2}"

    # 4. Review / Retrospective
    if any(k in title.lower() or k in filename.lower() for k in ['후기', '회고', '세미나', '웨비나', '강의', 'review']):
        insights = [l for l in all_lines if any(x in l for x in ['배운', '느낀', '중요', '역할', '실무', '접근', '아키텍트', '개발자', '이해'])]
        line1 = f"'{clean_title}'에 참여하고 주요 발표 내용과 배운 점을 정리한 글이다."
        line2 = insights[0] if insights else "실무 적용 사례를 통해 개발자의 역할과 협업, 지속적인 학습의 중요성을 확인할 수 있다."
        if not line2.endswith('.'): line2 += '을 확인했다.'
        return f"{line1}\n{line2}"

    # 5. General Tech / How-to
    practical = [l for l in all_lines if any(x in l for x in ['방법', '설정', '기능', '사용', '작성', '구현', '원리', '제공', '필요'])]
    line1 = f"{clean_title}의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다."
    if practical:
        specific = practical[0]
        if len(practical) > 1 and len(specific) < 30:
            specific = practical[1]
        line2 = specific
        if not line2.endswith('.'): line2 += '을 적용할 수 있다.'
    else:
        line2 = "핵심 설정과 구현 코드를 단계별로 파악하여 상황에 맞게 유연하게 활용할 수 있다."

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

def process_all():
    posts = glob.glob('source/_posts/*.md')
    print(f"Processing {len(posts)} posts...")
    updated = 0
    for p in posts:
        filename = os.path.basename(p)
        with open(p, 'r', encoding='utf-8', errors='ignore') as f:
            raw = f.read()

        parts = raw.split('---', 2)
        if len(parts) < 3: continue
        front = parts[1]
        body = parts[2]

        m_title = re.search(r'^title:\s*["\']?(.*?)["\']?$', front, re.M)
        title = m_title.group(1).strip() if m_title else filename.replace('.md', '')

        body_cleaned = re.sub(r'<div class="notification is-tldr">[\s\S]*?</div>\s*', '', body).strip()
        body_cleaned = re.sub(r'<!-- more -->\s*', '', body_cleaned).strip()

        tldr_text = generate_tldr(filename, title, body_cleaned)
        tldr_block = format_tldr_block(tldr_text)

        new_post = f"---{front}---\n\n{tldr_block}\n\n<!-- more -->\n\n{body_cleaned}\n"
        with open(p, 'w', encoding='utf-8') as f:
            f.write(new_post)
        updated += 1

    print(f"All {updated} posts updated in user's style successfully.")

if __name__ == '__main__':
    process_all()
