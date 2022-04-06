from pygnmi.client import gNMIclient
from pprint import pprint as pp

host = ("198.51.100.105", "6030")
username = "arista"
password = "arista"

d = [
    "openconfig-interfaces:interfaces/interface[name=Ethernet1]/config/description",
]
with gNMIclient(target=host, username="arista", password="arista", insecure=True) as gc:
    result = gc.set(delete=d)
    print(result)
