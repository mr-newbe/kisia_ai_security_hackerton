import requests
import whois
from datetime import datetime

def get_pypi_maintainer_email(package_name):
    """PyPI에서 패키지 관리자의 이메일 도메인 추출"""
    url = f"https://pypi.org/pypi/{package_name}/json"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    info = response.json().get("info", {})
    email = info.get("author_email") or info.get("maintainer_email")
    return email

def get_latest_release_date(package_name):
    """PyPI에서 최신 릴리스 날짜 추출"""
    url = f"https://pypi.org/pypi/{package_name}/json"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    releases = response.json().get("releases", {})
    versions = sorted(releases.keys(), reverse=True)
    for version in versions:
        files = releases[version]
        if files:
            upload_time = files[0].get("upload_time_iso_8601")
            if upload_time:
                return datetime.fromisoformat(upload_time.replace("Z", "+00:00"))
    return None

def check_domain_re_registration(email, release_date):
    """WHOIS 정보를 기반으로 이메일 도메인이 릴리스 이후에 재등록되었는지 확인"""
    if not email or "@" not in email:
        return None
    domain = email.split("@")[1]
    try:
        domain_info = whois.whois(domain)
        creation_date = domain_info.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        # 시간대 통일: release_date를 naive로 변환
        release_date_naive = release_date.replace(tzinfo=None)

        if creation_date and release_date_naive and creation_date > release_date_naive:
            return True  # 릴리스 이후 도메인이 재등록됨
        return False
    except Exception as e:
        print(f"WHOIS 조회 실패: {e}")
        return None

def analyze_domain_reuse(package_name):
    email = get_pypi_maintainer_email(package_name)
    release_date = get_latest_release_date(package_name)
    print(release_date)
    re_registered = check_domain_re_registration(email, release_date)
    return {
        "package": package_name,
        "maintainer_email": email,
        "latest_release_date": release_date.isoformat() if release_date else None,
        "domain_re_registered": re_registered
    }

# 예시 실행
result = analyze_domain_reuse("requests")
print(result)
