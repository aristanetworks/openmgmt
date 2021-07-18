import requests
from requests.auth import HTTPBasicAuth
import json
from pprint import pprint as pp

requests.packages.urllib3.disable_warnings()

USER = 'arista'
PASS = 'arista'
headers = {'Accept': 'application/yang-data+json'}

api_call = "https://10.73.1.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet1/state"

result = requests.get(api_call, auth=HTTPBasicAuth(USER, PASS), headers=headers, verify=False)
pp(result.json())