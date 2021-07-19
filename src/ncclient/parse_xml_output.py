from ncclient import manager
eos=manager.connect(host="10.73.1.105", port="830", timeout=30, username="arista", password="arista", hostkey_verify=False)

# Get interface state and configuration data
Interface_Ethernet3='''
    <interfaces>
        <interface>
            <name>Ethernet3</name>
        </interface>
    </interfaces>
'''
get_interface_ethernet3 = eos.get(filter=("subtree", Interface_Ethernet3))

# Parse the XML output

ns = {None: 'http://openconfig.net/yang/interfaces'}

operStatus = get_interface_ethernet3.data.find(".//interfaces/interface/state/oper-status", namespaces=ns)
print(operStatus.text)

eos.close_session()