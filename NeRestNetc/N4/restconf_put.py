import json
import requests
requests.packages.urllib3.disable_warnings()

api_url = "https://192.168.1.38/restconf/data/ietf-interfaces:interfaces"
headers = {
    "Accept": "application/yang-data+json",
    "Content-type": "application/yang-data+json"
}
basicauth = ("cisco", "cisco123!")

yangConfig = {
    "ietf-interfaces:interface": {
        "name": "Loopback6",
        "description": "My second RESTCONF loopback",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": { "address": [ {"ip": "10.3.1.1","netmask": "255.255.255.0"} ] },
        "ietf-ip:ipv6": {}
    }
}

resp = requests.post(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)

if 200 <= resp.status_code <= 299:
    print("STATUS OK: {}".format(resp.status_code))
else:
    print('Error. Status Code: {} \nError message: {}'.format(resp.status_code, resp.text))
