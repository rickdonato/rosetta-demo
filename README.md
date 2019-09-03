THIS 100% DRAFT/WIP .......

## About
Repo containing scripts, commands, and general notes around the testing and demo`ing of NTC-Rosetta + Yangify.

## Workflow
1. Create yang models (if required) - `yang_create.py`
2. Create candiate yang model (changes required)
3. Create native configuration for nos required - `yang_merge.py`
```
# ./yang_merge.py -n ios -r data/yang/current.yang -c data/yang/candidate.yang
interface FastEthernet1.2
   description Description removed
   exit
!
interface FastEthernet4
   switchport trunk allowed vlan 10,20,30,40
   exit
!
no vlan 20
vlan 200
   name dev
   no shutdown
   exit
!
```


## Links
* https://ntc-rosetta.readthedocs.io
* https://yangify.readthedocs.io
