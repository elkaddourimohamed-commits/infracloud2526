from netmiko import ConnectHandler
from netmiko.ssh_exception import (
    NetmikoTimeoutException,
    NetmikoAuthenticationException
)

router = {
    "device_type": "cisco_ios",
    "host": "192.168.1.38",     # CSR1000v router
    "username": "cisco",          # juiste gebruiker
    "password": "cisco123!",      # juist wachtwoord
}

# Configuratiecommando’s (best practice: loopback)
config_commands = [
    "interface Loopback100",
    "description Configured by Netmiko (N2)",
    "ip address 10.100.100.1 255.255.255.255"
]

try:
    print("🔗 Verbinden met router via SSH...")
    connection = ConnectHandler(**router)

    print("⚙️ Configuratie toepassen...")
    output = connection.send_config_set(config_commands)
    print(output)

    connection.disconnect()
    print("✅ Configuratie succesvol toegepast en verbinding gesloten")

except NetmikoAuthenticationException:
    print("❌ Authenticatie mislukt (verkeerde gebruikersnaam of wachtwoord)")

except NetmikoTimeoutException:
    print("❌ Router niet bereikbaar via SSH")
