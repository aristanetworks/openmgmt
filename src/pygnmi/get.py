import os
import json

from pygnmi.client import gNMIclient, telemetryParser

ARISTA_HOST = os.getenv("ARISTA_HOST", "198.51.100.105")
ARISTA_PORT = os.getenv("ARISTA_PORT", "6030")
ARISTA_USERNAME = os.getenv("ARISTA_USERNAME", "arista")
ARISTA_PASSWORD = os.getenv("ARISTA_PASSWORD", "arista")

host = (ARISTA_HOST, ARISTA_PORT)

paths = [
    "interfaces/interface[name=Ethernet1]/state/counters",
    "network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state",
]

with gNMIclient(
    target=host, username=ARISTA_USERNAME, password=ARISTA_PASSWORD, insecure=True
) as gc:
    raw_data = gc.get(path=paths, encoding="json_ietf")
    print(json.dumps(raw_data, sort_keys=True, indent=2))
