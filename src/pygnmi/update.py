from pygnmi.client import gNMIclient
from pprint import pprint as pp
import json

host = ('10.73.1.105', '6030')
username ='arista'
password ='arista'

print ('GET RPC, interface Ethernet1 config, before the update')

paths=['openconfig-interfaces:interfaces/interface[name=Ethernet1]/config']

with gNMIclient(target=host, username='arista', password='arista', insecure=True) as gc:
    raw_data = gc.get(path=paths, encoding='json_ietf')
    print(json.dumps(raw_data, sort_keys=True, indent=2))
    # print(raw_data['notification'][0]['update'][0]['val']['openconfig-interfaces:description'])

print ('\nSET RPC, update, interface Ethernet1')

u = [
        (
            "openconfig-interfaces:interfaces/interface[name=Ethernet1]",
            {
                "config": {
                    "name": "Ethernet1",
                    "enabled": True,
                    "description": "Test"
                }
            }
        )
   ]

with gNMIclient(target=host, username='arista', password='arista', insecure=True) as gc:
    result = gc.set(update=u)
    print(result)

print ('\nGET RPC, interface Ethernet1 config, after the update')

paths=['openconfig-interfaces:interfaces/interface[name=Ethernet1]/config']

with gNMIclient(target=host, username='arista', password='arista', insecure=True) as gc:
    raw_data = gc.get(path=paths, encoding='json_ietf')
    print(json.dumps(raw_data, sort_keys=True, indent=2))
    # print(raw_data['notification'][0]['update'][0]['val']['openconfig-interfaces:description'])
