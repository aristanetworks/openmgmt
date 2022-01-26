from oc_bgp import openconfig_bgp
import pyangbind.lib.pybindJSON as pybindJSON

oc = openconfig_bgp()

oc.bgp.global_.config.as_ = "65002"

oc.bgp.peer_groups.peer_group.add("XYZ")
oc.bgp.peer_groups.peer_group["XYZ"].config.peer_group_name = "XYZ"
oc.bgp.peer_groups.peer_group["XYZ"].config.peer_as = 65002

oc.bgp.neighbors.neighbor.add("192.0.2.154")
oc.bgp.neighbors.neighbor["192.0.2.154"].config.neighbor_address = "192.0.2.154"
oc.bgp.neighbors.neighbor["192.0.2.154"].config.peer_group = "XYZ"
oc.bgp.neighbors.neighbor["192.0.2.154"].config.enabled = True

oc.bgp.neighbors.neighbor.add("192.0.2.157")
oc.bgp.neighbors.neighbor["192.0.2.157"].config.neighbor_address = "192.0.2.157"
oc.bgp.neighbors.neighbor["192.0.2.157"].config.peer_group = "XYZ"
oc.bgp.neighbors.neighbor["192.0.2.157"].config.enabled = True

with open("../../docs/examples/pyangbind/demo.json", "w") as f:
    f.write(pybindJSON.dumps(oc.bgp, mode="ietf"))
