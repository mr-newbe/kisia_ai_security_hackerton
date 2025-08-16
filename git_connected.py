import requests
import re

def get_pypi_metadata(package_name):
    url = f"https://pypi.org/pypi/{package_name}/json"
    response = requests.get(url)
    if response.status_code != 200:
        return None

    data = response.json()
    info = data.get("info", {})
    requires_dist = info.get("requires_dist", [])
    home_page = info.get("home_page", "")
    project_urls = info.get("project_urls", {})

    # 깃허브 연동 여부 확인
    github_link = None
    for key, value in project_urls.items():
        if "github.com" in value.lower():
            github_link = value
            break
    if not github_link and "github.com" in home_page.lower():
        github_link = home_page

    # 의존성 패키지 추출
    dependencies = [re.split(r"[ ;]", dep)[0] for dep in requires_dist]

    return {
        "name": package_name,
        "github_link": github_link,
        "dependencies": dependencies
    }
"""
def get_pepy_downloads(package_name):
    url = f"https://pepy.tech/api/projects/{package_name}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    return {
        "total_downloads": data.get("total_downloads"),
        "downloads_last_30_days": data.get("downloads", {}).get("last_30_days")
    }
"""
# 예시 실행
package = "requests"
meta = get_pypi_metadata(package)
#downloads = get_pepy_downloads(package)

print("📦 PyPI Metadata:")
print(meta)
#print("\n📈 Download Stats:")
#print(downloads)
