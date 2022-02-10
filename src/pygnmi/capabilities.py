from pygnmi.client import gNMIclient
from pprint import pprint as pp
import json

host = ("198.51.100.105", "6030")
username = "arista"
password = "arista"

with gNMIclient(target=host, username=username, password=password, insecure=True) as gc:
    result = gc.capabilities()
    pp(result)
