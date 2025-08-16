import requests

def get_missing_metadata(package_name):
    """
    PyPI 패키지에서 누락된 메타데이터 항목을 분석합니다.
    주요 체크 항목: description 없음, version 0.0.0, author_email 없음
    """
    url = f"https://pypi.org/pypi/{package_name}/json"
    response = requests.get(url)
    if response.status_code != 200:
        return {"error": "패키지를 찾을 수 없습니다."}

    info = response.json().get("info", {})
    missing_fields = []

    # 1. 설명(description) 누락
    if not info.get("description") or len(info.get("description").strip()) == 0:
        missing_fields.append("description")

    # 2. 버전이 0.0.0
    if info.get("version") == "0.0.0":
        missing_fields.append("version")

    # 3. 메인테이너 이메일 누락
    if not info.get("author_email") and not info.get("maintainer_email"):
        missing_fields.append("email")

    # 4. 프로젝트 URL 없음
    if not info.get("project_url") and not info.get("home_page"):
        missing_fields.append("project_url")

    return {
        "package": package_name,
        "missing_metadata": missing_fields,
        "is_suspicious": len(missing_fields) > 0
    }

# 예시 실행
result = get_missing_metadata("requests")
print(result)
