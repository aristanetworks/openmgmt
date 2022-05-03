# Modules
import os
import json

from pygnmi.client import gNMIclient

ARISTA_HOST = os.getenv("ARISTA_HOST", "198.51.100.105")
ARISTA_PORT = os.getenv("ARISTA_PORT", "6030")
ARISTA_USERNAME = os.getenv("ARISTA_USERNAME", "ansible")
ARISTA_PASSWORD = os.getenv("ARISTA_PASSWORD", "ansible")

host = (ARISTA_HOST, ARISTA_PORT)

# Body
if __name__ == "__main__":
    with gNMIclient(
        target=host, username=ARISTA_USERNAME, password=ARISTA_PASSWORD, insecure=True
    ) as gc:
        result = gc.get(path=["openconfig:interfaces"])
    print(json.dumps(result, indent=4))
