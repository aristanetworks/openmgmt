import requests
from requests.auth import HTTPBasicAuth
import json

requests.packages.urllib3.disable_warnings()

USER = "arista"
PASS = "arista"
headers = {
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json",
}

api_call = "https://198.51.100.105:6020/restconf/data/ietf-interfaces:interfaces/interface=Loopback100"

# check if int lo100 exists
print("get int lo100")
result_get = requests.get(
    api_call, auth=HTTPBasicAuth(USER, PASS), headers=headers, verify=False
)
print("status_code is %s" % (result_get.status_code))

if result_get.status_code == 200:
    print("content is %s" % (result_get.json()))
    # delete int lo100
    print("deleting int lo100")
    result_delete = requests.delete(
        api_call, auth=HTTPBasicAuth(USER, PASS), headers=headers, verify=False
    )
    print("status_code is %s" % (result_delete.status_code))
