# Modules
from pygnmi.client import gNMIclient
import json

# Variables
host = ('10.20.30.67', '6030')

# Body
if __name__ == '__main__':
    with gNMIclient(target=host, username='ansible', password='ansible', insecure=True) as gc:
         result = gc.get(path=['openconfig:interfaces'])
    print(json.dumps(result, indent=4))
