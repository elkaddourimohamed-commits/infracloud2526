import json
import csv

json_data = '''
{
  "interfaces": [
    {
      "name": "GigabitEthernet0/0",
      "ip": "192.168.1.1",
      "status": "up"
    },
    {
      "name": "GigabitEthernet0/1",
      "ip": "unassigned",
      "status": "down"
    }
  ]
}
'''

data = json.loads(json_data)

with open("interfaces.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Interface", "IP", "Status"])

    for iface in data["interfaces"]:
        writer.writerow([iface["name"], iface["ip"], iface["status"]])

print("CSV-bestand aangemaakt")
