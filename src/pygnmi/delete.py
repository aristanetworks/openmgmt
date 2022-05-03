import os
import json
from pprint import pprint as pp

from pygnmi.client import gNMIclient

ARISTA_HOST = os.getenv("ARISTA_HOST", "198.51.100.105")
ARISTA_PORT = os.getenv("ARISTA_PORT", "6030")
ARISTA_USERNAME = os.getenv("ARISTA_USERNAME", "arista")
ARISTA_PASSWORD = os.getenv("ARISTA_PASSWORD", "arista")

host = (ARISTA_HOST, ARISTA_PORT)

d = [
    "openconfig-interfaces:interfaces/interface[name=Ethernet1]/config/description",
]
with gNMIclient(
    target=host, username=ARISTA_USERNAME, password=ARISTA_PASSWORD, insecure=True
) as gc:
    result = gc.set(delete=d)
    print(result)
