import requests

def get_metadata(package_name):
  url = f"https://pypi.org/pypi/{package_name}/json"
  response = requests.get(url)
  if response.status_code == 200:
    data  = response.json()
    info  = data.get("info",{})
    return {
      "name" : info.get("name"),
      "version" : info.get("version"),
      "license" : info.get("license"),
      "summary" : info.get("summary"),
      "requires_dist" : info.get("requires_dist"),
    }
  else:
    return None


print(get_metadata("requests"))