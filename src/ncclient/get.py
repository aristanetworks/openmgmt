from ncclient import manager

eos = manager.connect(
    host="198.51.100.203",
    port="830",
    timeout=30,
    username="arista",
    password="arista",
    hostkey_verify=False,
)

# Get interface Ethernet 3 operational status
int_eth3_op_status = """
<interfaces>
    <interface>
        <name>
            Ethernet3
        </name>
        <state>
            <oper-status>
            </oper-status>
        </state>
    </interface>
</interfaces>
"""
get_int_eth3_op_status = eos.get(filter=("subtree", int_eth3_op_status))
print(get_int_eth3_op_status)

eos.close_session()
