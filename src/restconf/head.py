import requests
from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings()

USER = 'arista'
PASS = 'arista'
headers = {'Accept': 'application/yang-data+json'}

api_call = "https://10.73.1.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet1/state"
result = requests.head(api_call, auth=HTTPBasicAuth(USER, PASS), headers=headers, verify=False)

print("url is %s" % (result.url))
print("status_code is %s" % (result.status_code))
print("response headers are %s" % (result.headers))
print("content is %s" % (result.content))


