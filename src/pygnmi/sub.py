import os

from pygnmi.client import gNMIclient, telemetryParser

ARISTA_HOST = os.getenv("ARISTA_HOST", "198.51.100.105")
ARISTA_PORT = os.getenv("ARISTA_PORT", "6030")
ARISTA_USERNAME = os.getenv("ARISTA_USERNAME", "arista")
ARISTA_PASSWORD = os.getenv("ARISTA_PASSWORD", "arista")

host = (ARISTA_HOST, ARISTA_PORT)

subscribe = {
    "subscription": [
        {
            "path": "interfaces/interface[name=Ethernet1]/state/counters",
            "mode": "sample",
            "sample_interval": 10000000000,
        },
        {
            "path": "network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state",
            "mode": "sample",
            "sample_interval": 10000000000,
        },
    ],
    "mode": "stream",
    "encoding": "json",
}

with gNMIclient(
    target=host, username=ARISTA_USERNAME, password=ARISTA_PASSWORD, insecure=True
) as gc:
    telemetry_stream = gc.subscribe(subscribe=subscribe)
    for telemetry_entry in telemetry_stream:
        print(telemetryParser(telemetry_entry))
