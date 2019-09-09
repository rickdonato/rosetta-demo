from napalm import get_network_driver
import pprint

print("[*] JUNOS Driver Loaded")
driver_junos = get_network_driver('junos')
device_junos = driver_junos('172.29.133.2', 'admin', 'Juniper')
device_junos.open()

print("[*] IOS Driver Loaded")
driver_ios = get_network_driver('ios')
device_ios = driver_ios('172.29.133.3', 'cisco', 'cisco')
device_ios.open()

input("Press Enter to continue...")

print("\n[*] Get Facts")
pprint.pprint(device_junos.get_facts())
input("Press Enter to continue...")
pprint.pprint(device_ios.get_facts())
input("Press Enter to continue...")

print("\n[*] Get Interfaces")
pprint.pprint(device_junos.get_interfaces_ip())
input("Press Enter to continue...")
pprint.pprint(device_ios.get_interfaces_ip())
input("Press Enter to continue...")

print("\n[*] Get Config")
pprint.pprint(device_junos.get_config())
input("Press Enter to continue...")
pprint.pprint(device_ios.get_config())
input("Press Enter to continue...")
