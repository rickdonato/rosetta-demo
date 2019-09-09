from napalm import get_network_driver
import pprint 

driver_junos = get_network_driver('junos')
device_junos = driver_junos('172.29.133.2', 'admin', 'Juniper')
device_junos.open()
print("[*] JUNOS Driver Loaded")


print("[*] device_junos.load_merge_candidate()")
device_junos.load_merge_candidate(config='set vlans VLAN345 vlan-id 345')

print("[*] device_junos.compare_config()")
print(device_junos.compare_config())

print("[*] device_junos.commit_config()")
device_junos.commit_config()
