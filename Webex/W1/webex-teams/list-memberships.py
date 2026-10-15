import requests
access_token = 'ZGY4OWE3YzEtNDVkNC00NTJjLTlkOTQtMWI2ZDIxZjExNWE4ZDZjNzdhODItZTk2_P0A1_cce0a1f3-bf77-42c7-a45d-46ec83d996ea'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vOGY5NjhkNDAtOWVkMC0xMWYwLWIzMjktMDdkMDA4YjkyZmU3'
url = 'https://webexapis.com/v1/memberships'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id}
res = requests.get(url, headers=headers, params=params)
print(res.json())