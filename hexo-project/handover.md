# [Handover] GitHub 블로그(sowon-dev.github.io) 구조 및 UI/UX 개편 인수인계서

- **작성일**: 2026-10-12
- **블로그 플랫폼**: Hexo
- **테마**: [Icarus](https://github.com/ppoffice/hexo-theme-icarus)
- **도메인**: `https://sowon-dev.github.io/`

---

## 1. 개요 및 배경

기존 블로그는 게시글별로 세부 기술 스택이 개별 카테고리로 생성되어 카테고리 목록이 과도하게 길어지고, 사이드바에 월별 아카이브 위젯이 무한 스크롤을 유발하여 글 읽기 집중도와 검색 편의성이 떨어지는 문제가 있었습니다. 또한 기본 브랜치(`master`) 관리 및 안전성 이슈를 개선하고자 다음 개편 작업을 진행/계획했습니다.

---

## 2. 브랜치 및 저장소 관리

### 2.1 Public / Private 정책 및 Hexo 보안 특성
- **정책**: 무료 GitHub 플랜을 유지하는 한 저장소는 **Public** 상태를 유지해야 `https://sowon-dev.github.io`로 정상 호스팅됩니다.
- **보안 아키텍처 특성**:
  - **DB 및 백엔드(WAS) 부재**: 데이터베이스나 실시간 서버 사이드 런타임이 없어 SQL Injection, 서버 쉘 탈취, 관리자 로그인 무차별 대입(Brute-force) 공격이 원천적으로 불가능합니다.
  - **GitHub 글로벌 인프라**: DDoS 방어 및 SSL/HTTPS 암호화 통신이 GitHub 인프라 레벨에서 자동 제공됩니다.
- **운영 시 필수 보안 주의사항**:
  1. **실제 자격증명(Credentials) 커밋 주의**:
     - 실습 및 트러블슈팅 글 작성 시 실수로 개인/회사용 AWS Key, GitHub Token, DB 접속 비밀번호, 사내 IP 등을 마크다운에 적지 않도록 주의합니다.
     - 테스트 데이터는 반드시 가상 데이터(`test@example.com`, `010-0000-0000`)를 사용합니다.
  2. **개인 연락처/민감정보 노출 방지**:
     - 공개 프로필 설정 시 개인 이메일(`sowonkim177@gmail.com`)이나 개인 전화번호가 실수로 노출되지 않도록 테마 설정을 관리합니다.
  3. **검증되지 않은 외부 스크립트 지양**:
     - 카운터, 위젯, 광고 스크립트 추가 시 공식 테마 지원(Icarus) 또는 신뢰할 수 있는 CDN/오픈소스만 사용하여 잠재적 XSS(크로스 사이트 스크립팅)를 예방합니다.


### 2.2 기본 브랜치 변경 (`master` ➔ `main`) [완료됨 ✅]
- **진행 현황**: GitHub 웹 콘솔에서 `main` 브랜치로 전환 및 default 지정 완료됨.
- **배포 설정(deploy) 유의사항**:
  - 향후 `hexo deploy` 시 구 버전의 `master` 브랜치가 아니라 **`main` 브랜치**로 푸시되도록 루트 `_config.yml`의 배포 설정을 지정합니다:
    ```yaml
    deploy:
      type: git
      repo: https://github.com/sowon-dev/sowon-dev.github.io.git
      branch: main
    ```


### 2.3 URL(Permalink) 불변 원칙 (포트폴리오 링크 깨짐 방지)
- **원칙**: 외부 이력서 및 포트폴리오에 기입된 기존 글 URL(`https://sowon-dev.github.io/:year/:month/:day/:title/`)은 1글자도 변경되지 않아야 합니다.
- **보장 방안**:
  - 기존 블로그의 URL 규칙은 카테고리(`:category`)를 포함하지 않는 `:year/:month/:day/:title/` 형식입니다.
  - 따라서 카테고리를 대분류로 통폐합하더라도 글 주소에는 아무런 영향이 없습니다.
  - 루트 `_config.yml`의 퍼머링크 설정을 기존과 100% 동일하게 유지합니다:
    ```yaml
    permalink: :year/:month/:day/:title/
    permalink_defaults:
    ```

---

## 3. 카테고리 & 태그 체계 개편


### 3.1 분류 가이드라인
수십 개로 나뉘어 있던 카테고리를 **3~4개 대분류**로 통폐합하고, 세부 기술 키워드는 **태그(Tags)**로 분리합니다.

| 분류 | 대분류 카테고리 (`categories`) | 태그로 전환할 키워드 (`tags`) |
| :--- | :--- | :--- |
| **백엔드** | `Backend` | `Java`, `Spring`, `Spring Boot`, `.NET`, `API`, `SMTP` 등 |
| **프론트/모바일** | `Frontend` | `JavaScript`, `CSS`, `Android`, `Vue`, `React` 등 |
| **데이터/인프라** | `Database` | `Oracle`, `SQL`, `Query`, `Git`, `Hexo`, `Server` 등 |
| **기록/회고** | `Reflections` | `회고`, `TIL`, `자격증`, `스터디`, `커리어` 등 |

### 3.2 포스트 Front-matter 작성 규칙
```yaml
---
title: "[Oracle] GROUP BY 쿼리 분석"
date: 2026-10-12 10:00:00
categories:
  - Database       # 반드시 대분류 1개 지정
tags:
  - Oracle         # 세부 기술 키워드는 태그에 다중 지정
  - SQL
  - Optimization
top: true          # (선택) 메인 홈 화면 최상단 추천글 핀 고정
---
```

### 3.3 HTML ➔ Markdown 변환 시 글 구조(Structure) 자동 개선 규칙
원문의 텍스트 내용은 100% 온전하게 보존하면서, 가독성과 모바일 친화도, AI 인용성을 극대화하기 위해 글의 틀(구조)을 다음과 같이 개선하여 생성합니다:
1. **도입부 `[!NOTE]` 핵심 요약 블록 자동 삽입**:
   - 본문 상단에 GitHub Flavored Markdown Callout 문법으로 주제와 카테고리를 한눈에 볼 수 있는 요약 카드를 삽입하여 독자 및 AI 크롤러의 가독성을 극대화합니다.
2. **코드 블록 순도 복원 (Clean Code Block)**:
   - 복잡한 HTML 라인 번호 태그(`gutter`)를 정돈하고, 순수한 마크다운 코드 블록(```java, ```javascript 등)으로 변환하여 언어별 문법 강조를 정확하게 살립니다.
3. **불필요한 과도한 공백 정돈 (모바일 최적화)**:
   - 레거시 에디터에서 발생한 연속 `<br><br><br>` 빈 줄을 적절한 마크다운 문단 간격(빈 줄 1개)으로 정돈하여 모바일 화면에서의 스크롤 피로도를 줄입니다.

---

## 4. Icarus 테마 UI/UX 및 레이아웃 개선

### 4.0 코드 블록 다크 테마(어두운 배경) 유지
- **스타일**: 기존에 사용하던 가독성 높은 다크 배경 테마(`hybrid` 또는 `tomorrow-night`)를 유지합니다.
- **설정 파일**: `_config.icarus.yml`
```yaml
article:
  highlight:
    theme: hybrid    # 어두운 배경 + syntax highlight + 코드 복사(clipboard) 지원
```

### 4.0.1 홈 화면 추천글(Top/Pinned Post) 고정 (로딩 지연 방지)
- **성능 고려**: 외부 통계 API(Busuanzi 등)를 호출하여 실시간으로 정렬하면 메인 페이지 접속 시 3~5초의 로딩 딜레이가 발생하므로, 정적 빌드 방식인 `top: true` 핀 기능을 사용합니다.
- **사용법**: 반응이 좋았던 대표 글이나 자랑하고 싶은 핵심 프로젝트 글의 마크다운 머리말에 `top: true` (또는 숫자 순위)를 부여하여 메인 홈 상단에 카드로 바로 노출합니다.


### 4.1 사이드바 2단 간소화 (아카이브 위젯 제거)
- **목적**: 긴 월별 아카이브 스크롤을 사이드바에서 제거하여 본문 글 가독성 확보.
- **설정 파일**: `_config.icarus.yml` (또는 `themes/icarus/_config.yml`)

```yaml
widgets:
  - type: profile
    position: left
  - type: categories     # 대분류 적용 시 3~4줄로 슬림하게 표시
    position: left
  - type: recent_posts
    position: left
  # - type: archives     # 주석 처리 또는 삭제하여 사이드바 스크롤 제거
  #   position: left
```

> **참고**: 아카이브 목록은 상단 GNB(`navbar.menu`)의 `Archives: /archives/`를 통해 전용 페이지로 탐색할 수 있습니다.

### 4.2 Local Search (Insight Search) 활성화
- **목적**: 방문자가 원하는 키워드를 실시간 모달 팝업으로 빠르게 검색.

#### Step 1: 플러그인 설치 (로컬 터미널)
```bash
npm install hexo-generator-search --save
```

#### Step 2: 루트 `_config.yml` 설정
```yaml
search:
  path: search.xml
  field: post
  content: true
  format: html
```

#### Step 3: `_config.icarus.yml` 테마 설정
```yaml
search:
  type: insight
```

### 4.3 프로필 위젯 실시간 방문/조회 통계 (Busuanzi) 활성화
- **목적**: 프로필 카드 하단 및 개별 포스트에 실시간 방문자 수(PV/UV)와 조회수 통계 배지 표시.
- **설정 파일**: `_config.icarus.yml`

```yaml
# 실시간 방문자 통계 (Busuanzi)
busuanzi: true
```

### 4.4 AI 검색엔진 최적화 (AI SEO & AEO: sitemap.xml, llms.txt)
AI 모델(ChatGPT, Perplexity, Claude, Cue: 등) 및 검색엔진 크롤러가 블로그 글을 신뢰도 높은 출처로 즉시 인용할 수 있도록 메타 규격을 구성합니다.

#### 1) 사이트맵 플러그인 설정 (Google & Search Engine)
```bash
npm install hexo-generator-sitemap --save
```
루트 `_config.yml`:
```yaml
sitemap:
  path: sitemap.xml
```

#### 2) `llms.txt` 표준 스펙 제공 (AI 봇 친화적 메타데이터)
`source/llms.txt` 파일을 생성하여 AI 모델이 블로그 주제와 구조를 한눈에 읽을 수 있도록 제공합니다.
```markdown
# sowon-dev Tech Blog
> 백엔드(Java, Spring), 프론트엔드, 데이터베이스 트러블슈팅 및 실무 의사결정을 기록하는 기술 블로그

- Author: sowon-dev
- Website: https://sowon-dev.github.io/
- Categories: Backend, Frontend, Database, Reflections
- Sitemap: https://sowon-dev.github.io/sitemap.xml
```


---

## 5. 빌드 및 배포 절차

### 5.1 배포 전 자동 보안 검사 (민감정보 유출 원천 차단)
배포 시 실수로 API 키, 비밀번호, 개인 이메일(`sowonkim177@gmail.com`)이 업로드되는 것을 방지하기 위해 **배포 직전 보안 검사 스크립트(`check_security.py`)가 선행 실행**되도록 구성합니다.

`package.json`:
```json
{
  "scripts": {
    "check-security": "python check_security.py",
    "deploy": "python check_security.py && hexo clean && hexo deploy"
  }
}
```

### 5.2 빌드 및 배포 순서
```bash
# 1. 로컬 서버 실행 후 글 미리보기 확인 (http://localhost:4000)
hexo server

# 2. 보안 자동 검사 후 안전하게 GitHub 배포
npm run deploy
# (또는 수동: python check_security.py && hexo clean && hexo deploy)
```
- **동작**: `check_security.py`가 새 글들을 검사하여 민감정보가 발견되면 **즉시 배포를 중단(Exit 1)**하고 에러를 발생시킵니다. 이상이 없을 때만 `hexo deploy`가 실행됩니다.


---

## 6. 향후 신규 글 작성 워크플로우

1. **새 글 생성**:
   ```bash
   hexo new post "포스트-제목"
   # source/_posts/포스트-제목.md 자동 생성
   ```
2. **Front-matter 및 본문 작성**:
   - `categories`: 4대 대분류(`Backend`, `Frontend`, `Database`, `Reflections`) 중 1개 지정
   - `tags`: 세부 기술 스택 다중 지정

3. **로컬 확인 및 배포**:
   - `hexo server`로 확인 ➔ `hexo deploy`로 배포

---

## 7. [부록] AI 시대 블로그 PR(포트폴리오) 활용 전략 가이드

AI가 문법 설명과 공식 문서 요약을 순식간에 생성하는 환경에서는 **'단순 지식 정리형 블로그' 대신 '엔지니어의 맥락과 의사결정을 증명하는 블로그'**가 가장 강력한 PR 무기가 됩니다.

### 7.1 '지식 나열' 대신 '문제 해결 맥락(Context)과 의사결정' 기록
AI가 대체할 수 없는 것은 실제 프로덕션 환경에서의 고민과 트레이드오프입니다.
- **Bad**: `Java Stream API 사용법 정리`
- **Good**: `대용량 엑셀 다운로드 중 OOM 발생: 단순 반복문 대신 Stream과 Chunk 단위 처리를 선택하며 겪은 트러블슈팅과 성능 비교`
- **추천 글 구조 (3단계)**:
  1. **문제 상황**: 발생한 장애/요구사항 및 제약조건
  2. **대안 비교**: 방식 A vs 방식 B의 장단점 및 B를 선택한 이유
  3. **결과 및 수치**: 처리 속도 개선율(%), 메모리 절감 수치 등

### 7.2 AI 도구 활용 경험을 통한 엔지니어링 깊이 증명
- "Antigravity/GitHub Copilot을 활용한 리팩토링 중 발생한 엣지 케이스와 이를 사람의 도메인 지식으로 바로잡은 과정"
- "LLM 추천 쿼리가 실제 운영 DB(Oracle)에서 인덱스를 타지 못했던 원인과 실행 계획(Explain Plan) 튜닝기"
- ➔ *AI를 맹신하지 않고, 도구의 한계를 이해하고 통제할 수 있는 개발자임을 어필.*

### 7.3 이력서(Resume)의 '살아있는 각주(Footnote)'로 연계
- 이력서의 성과 줄 옆에 블로그 상세 링크 삽입:
  > *"레거시 배치 성능 40% 개선"*  
  > ↳ `[자세한 벤치마크 및 고민 과정: sowon-dev.github.io/...]`
- 면접관에게 기술 검증 신뢰도를 주고, 기술 면접의 주도권을 확보.

### 7.4 AI 검색(Perplexity, SearchGPT 등) 및 크롤러 친화적 작성 (AI SEO)
- **TL;DR (3줄 요약) 상단 배치**: 글 도입부에 핵심 결론을 3줄로 요약하여 독자 및 AI 크롤러의 인용 확률 증대
- **신뢰성 있는 환경 정보 명시**: Java/Spring/DB 버전 등 구체적 환경을 명시하여 AI가 최우선 인용 출처로 채택하도록 유도

