import requests
import json

access_token = 'ZGY4OWE3YzEtNDVkNC00NTJjLTlkOTQtMWI2ZDIxZjExNWE4ZDZjNzdhODItZTk2_P0A1_cce0a1f3-bf77-42c7-a45d-46ec83d996ea'
url = 'https://webexapis.com/v1/people/me'
headers = {'Authorization': 'Bearer {}'.format(access_token)}
res = requests.get(url, headers=headers)

print(json.dumps(res.json(), indent=4))