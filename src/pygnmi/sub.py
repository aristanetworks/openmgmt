from pygnmi.client import gNMIclient, telemetryParser

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

host = ("198.51.100.105", "6030")

with gNMIclient(target=host, username="arista", password="arista", insecure=True) as gc:
    telemetry_stream = gc.subscribe(subscribe=subscribe)
    for telemetry_entry in telemetry_stream:
        print(telemetryParser(telemetry_entry))
