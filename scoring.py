metadata = {
    "github_link": None,
    "dependencies": ["reqests", "idna"],
    "domain_re_registered": True,
    "description": "TODO: write description"
}


def calculate_malicious_score(metadata):
    score = 0

    # 1. 깃허브 연동 여부
    github_link = metadata.get("github_link")
    if not github_link or "github.com" not in github_link:
        score += 2
    elif "404" in github_link or "deleted" in github_link:
        score += 1

    # 2. 의존성 패키지 검사
    suspicious_deps = ["reqests", "beautifulsup4", "urllib3x"]
    dependencies = metadata.get("dependencies", [])
    for dep in dependencies:
        if dep.lower() in suspicious_deps:
            score += 3
            break
        elif len(dep) <= 3 or dep.isdigit():
            score += 1

    # 3. 이메일 도메인 재등록 여부
    if metadata.get("domain_re_registered") is True:
        score += 3

    # 4. 설명 누락
    description = metadata.get("description", "")
    if not description or "TODO" in description or "This is a Python package" in description:
        score += 2

    return min(score, 10)


score = calculate_malicious_score(metadata)
print(f"🚨 악성 탐지 점수: {score}/10")
