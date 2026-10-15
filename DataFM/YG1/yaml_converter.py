import yaml

yaml_data = """
interfaces:
  - name: GigabitEthernet0/0
    ip: 192.168.1.1
    description: Uplink naar router
  - name: GigabitEthernet0/1
    ip: 192.168.2.1
    description: LAN verbinding
"""
data = yaml.safe_load(yaml_data)
print(data)

import json
###Naar json
#json_data = json.dumps(data, indent=2)
#print(json_data)


###naar csv
import csv

with open('interfaces.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'ip', 'description']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for interface in data['interfaces']:
        writer.writerow(interface)
