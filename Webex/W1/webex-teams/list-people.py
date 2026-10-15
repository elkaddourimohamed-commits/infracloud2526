import requests
import json

access_token = 'ZGY4OWE3YzEtNDVkNC00NTJjLTlkOTQtMWI2ZDIxZjExNWE4ZDZjNzdhODItZTk2_P0A1_cce0a1f3-bf77-42c7-a45d-46ec83d996ea'
person_id = 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS8wY2I4Nzk1Ny0zYmRkLTRhMzMtYjU3NS01MzhlNDk2ZTI1NGI'
url = 'https://webexapis.com/v1/people/{}'.format(person_id)
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))