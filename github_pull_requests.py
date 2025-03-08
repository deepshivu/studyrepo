import requests
output=requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
result=output.json()
print(output.status_code)
for element in range(len(result)):
    print(result[element]["user"]["id"])
set_example={"ram","tim","john","tim"}
set_list=list(set_example)
print(set_list[0])
