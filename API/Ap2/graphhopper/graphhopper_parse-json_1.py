import requests
import urllib.parse

geocode_url= "https://graphhopper.com/api/1/geocode?"
route_url= "https://graphhopper.com/api/1/route?"
loc1= "Rome, Italy"
loc2= "Baltimore, Maryland"
key= "6511290f-697d-40b0-a1f1-ce7473046067"

url= geocode_url + urllib.parse.urlencode({"q":loc1, "limit":"1", "key":key})

replydata= requests.get(url)
json_data= replydata.json()
json_status= replydata.status_code
print(json_data)

