import requests
import hashlib
import json
from fuzzywuzzy import fuzz
from urllib.parse import quote

def get_pypi_metadata(package_name):
    url = f"https://pypi.org/pypi/{quote(package_name)}/json"
    print(url)
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    downloads = data.get("info", {}).get("downloads", {})
    urls = data.get("urls", [])
    print(f"package name {package_name} load complete")
    return {
        "name": data["info"]["name"],
        "version": data["info"]["version"],
        "summary": data["info"]["summary"],
        "downloads": downloads,
        "urls": urls
    }

def get_package_hash(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return hashlib.sha256(response.content).hexdigest()
    except:
        pass
    return None

def check_github_presence(package_name):
    search_url = f"https://api.github.com/search/repositories?q={quote(package_name)}+in:name"
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        items = response.json().get("items", [])
        return len(items) > 0
    return False

def check_typo_similarity(package_name, known_packages):
    scores = {pkg: fuzz.ratio(package_name, pkg) for pkg in known_packages}
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_scores[:3]  # Top 3 similar names


import requests

def get_pepy_downloads(package_name, api_key):
    """
    PePy.tech API를 사용하여 특정 Python 패키지의 총 다운로드 수를 반환합니다.
    
    Parameters:
        package_name (str): 조회할 PyPI 패키지 이름
        api_key (str): PePy API 키 (https://pepy.tech에서 발급 가능)
    
    Returns:
        int: 총 다운로드 수 (실패 시 -1 반환)
    """
    url = f"https://api.pepy.tech/api/v2/projects/{package_name}"
    headers = {
        "X-API-Key": api_key
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get("total_downloads", -1)
        else:
            print(f"API 요청 실패: {response.status_code}")
            return -1
    except Exception as e:
        print(f"오류 발생: {e}")
        return -1


def analyze_package(package_name, known_packages):
    metadata = get_pypi_metadata(package_name)
    if not metadata:
        return {"error": "Package not found on PyPI"}

    file_url = next((u["url"] for u in metadata["urls"] if u["packagetype"] == "sdist"), None)
    hash_value = get_package_hash(file_url) if file_url else None

    result = {
        "package_name": package_name,
        "pypi_found": True,
        "version": metadata["version"],
        "summary": metadata["summary"],
        "download_urls": [u["url"] for u in metadata["urls"]],
        "hash": hash_value,
        "github_exists": check_github_presence(package_name),
        "typo_similarity": check_typo_similarity(package_name, known_packages),
        "downloads": get_pepy_downloads(package_name,"0SRbc/jRFsHYxOShwIQ/N0jtrKf1syMW")
    }
    return result

# 예시 실행
known_packages = ["requests", "numpy", "pandas", "scikit-learn", "matplotlib"]
package_name = "requests"  # 일부러 오타
result = analyze_package(package_name, known_packages)

print(json.dumps(result, indent=2))
