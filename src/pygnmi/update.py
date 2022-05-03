import os
import json
from pprint import pprint as pp

from pygnmi.client import gNMIclient

ARISTA_HOST = os.getenv("ARISTA_HOST", "198.51.100.105")
ARISTA_PORT = os.getenv("ARISTA_PORT", "6030")
ARISTA_USERNAME = os.getenv("ARISTA_USERNAME", "arista")
ARISTA_PASSWORD = os.getenv("ARISTA_PASSWORD", "arista")

host = (ARISTA_HOST, ARISTA_PORT)

print("GET RPC, interface Ethernet1 config, before the update")

paths = ["openconfig:/interfaces/interface[name=Ethernet1]/config"]

with gNMIclient(
    target=host, username=ARISTA_USERNAME, password=ARISTA_PASSWORD, insecure=True
) as gc:
    raw_data = gc.get(path=paths, encoding="json_ietf")
    print(json.dumps(raw_data, sort_keys=True, indent=2))

print("\nSET RPC, update, interface Ethernet1")

u = [
    (
        "openconfig:/interfaces/interface[name=Ethernet1]",
        {"config": {"name": "Ethernet1", "enabled": True, "description": "Test"}},
    )
]

with gNMIclient(
    target=host, username=ARISTA_USERNAME, password=ARISTA_PASSWORD, insecure=True
) as gc:
    result = gc.set(update=u)
    print(result)

print("\nGET RPC, interface Ethernet1 config, after the update")

paths = ["openconfig:/interfaces/interface[name=Ethernet1]/config"]

with gNMIclient(
    target=host, username=ARISTA_PASSWORD, password=ARISTA_PASSWORD, insecure=True
) as gc:
    raw_data = gc.get(path=paths, encoding="json_ietf")
    print(json.dumps(raw_data, sort_keys=True, indent=2))
