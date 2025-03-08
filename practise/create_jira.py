# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://deepika9785.atlassian.net/rest/api/3/issue"
API_TOKEN="ATATT3xFfGF0Ju7WdFWNRlrXjyXn-SkCg05i6n39ZQ0q1BwMjDtlZ9wmuphdCYyRrDfd_m2gjoOS94Omh1hXyBkiB3pyqsODBX-DO_cEGPu-pcLel4OewugZaxvYSjU82WXz2ofk2B7FUL1aUBhRjCgYYdXsNjZPajEgnQXDYj4Anq29iwR-KTg=CF77014B"

auth = HTTPBasicAuth("deepika9785@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "TEST1"
    },
    "issuetype": {
      "id": "10004"
    },
    "summary": "First JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))