# print client capabilities 

from ncclient import manager

eos=manager.connect(host="10.83.28.203", port="830", timeout=30, username="arista", password="arista", hostkey_verify=False)

for item in eos.client_capabilities: 
    print (item)

eos.close_session()


