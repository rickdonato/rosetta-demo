config = """<configuration>
  <vlans>
    <vlan>
      <vlan-id>10</vlan-id>
      <name>prod</name>
      <disable delete="delete"/>
    </vlan>
    <vlan>
      <vlan-id>20</vlan-id>
      <name>dev</name>
      <disable/>
    </vlan>
  </vlans>
</configuration>"""

from napalm import get_network_driver
driver = get_network_driver('junos')
device = driver('172.29.133.2', 'admin', 'Juniper')
device.open()
device.load_merge_candidate(config=config)
print(device.compare_config())
device.commit_config()
