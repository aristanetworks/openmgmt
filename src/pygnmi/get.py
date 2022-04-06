from pygnmi.client import gNMIclient, telemetryParser
import json

host = ("198.51.100.105", "6030")

paths = [
    "interfaces/interface[name=Ethernet1]/state/counters",
    "network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state",
]

with gNMIclient(target=host, username="arista", password="arista", insecure=True) as gc:
    raw_data = gc.get(path=paths, encoding="json_ietf")
    print(json.dumps(raw_data, sort_keys=True, indent=2))
