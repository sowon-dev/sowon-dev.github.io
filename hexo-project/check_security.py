import sys
import re
from pathlib import Path

POSTS_DIR = Path(r"C:\dev\antigravity-workspace-sowon-dev\hexo-project\source\_posts")

SENSITIVE_PATTERNS = {
    "Private Email": re.compile(r'sowonkim177@gmail\.com', re.IGNORECASE),
    "Resident Number (RRN)": re.compile(r'\b\d{6}-[1-4]\d{6}\b'),
    "GitHub Secret Token": re.compile(r'\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9_]{36,255}\b'),
    "AWS Access Key": re.compile(r'\bAKIA[0-9A-Z]{16}\b'),
    "Google API Key": re.compile(r'\bAIza[0-9A-Za-z-_]{35}\b'),
    "RSA/EC Private Key": re.compile(r'-----BEGIN (?:RSA |EC )?PRIVATE KEY-----')
}

def main():
    print("=" * 60)
    print(" [보안 검사] 배포 전 민감정보 자동 검사(check_security.py)")
    print("=" * 60)
    
    violations = []
    scanned_count = 0

    for md_file in POSTS_DIR.glob("*.md"):
        scanned_count += 1
        content = md_file.read_text(encoding="utf-8", errors="ignore")
        for label, pattern in SENSITIVE_PATTERNS.items():
            matches = pattern.findall(content)
            if matches:
                violations.append((md_file.name, label, matches[0]))

    print(f"검사 대상 마크다운 포스트: {scanned_count}개")
    
    if violations:
        print("\n❌ [오류] 배포가 차단되었습니다! 다음 파일에서 민감정보가 발견되었습니다:")
        for fname, label, val in violations:
            masked = val[:3] + "***" if len(val) > 4 else "***"
            print(f"  - [{label}] 파일: {fname} (탐지값: {masked})")
        print("[SUCCESS] Sensitive info check passed. Safe to deploy.")
        sys.exit(0)

if __name__ == "__main__":
    main()

