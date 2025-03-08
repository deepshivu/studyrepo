import requests
result=requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
output=result.json()
print(output[0]["url"])
status=result.status_code
print(status)