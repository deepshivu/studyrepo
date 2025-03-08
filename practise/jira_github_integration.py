# http://docs.python-requests.org
#request module to make api calls
import requests
#import package and use HTTPBASICAUTH module
from requests.auth import HTTPBasicAuth
import json

url = "https://deepika9785.atlassian.net/rest/api/3/project"
API_TOKEN="ATATT3xFfGF0Ju7WdFWNRlrXjyXn-SkCg05i6n39ZQ0q1BwMjDtlZ9wmuphdCYyRrDfd_m2gjoOS94Omh1hXyBkiB3pyqsODBX-DO_cEGPu-pcLel4OewugZaxvYSjU82WXz2ofk2B7FUL1aUBhRjCgYYdXsNjZPajEgnQXDYj4Anq29iwR-KTg=CF77014B"

auth = HTTPBasicAuth("deepika9785@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
output=json.loads(response.text)
for i in range(len(output)):
  name=output[i]["name"]
  print(name)
