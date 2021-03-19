---
layout: page
title: "Ansible playbook example demo"
date: 2021-03-018 12:17:00 --0600
categories:
---

- [Ansible collections for](#overview)
- [Edit the inventory file](#Edit the inventory file to match your environment)
- [Ansible collection for grpc](#gNMI Collection)
- [Run the playbook](#Run the playbook)


## overview

In this ansible collection we show how to use ansible to find all the available modules within a Arista EOS device using the [capabilities method within gNMI.](https://github.com/openconfig/reference/blob/master/rpc/gnmi/gnmi-specification.md#32-capability-discovery)

##Edit the inventory file to match your environment 

```text
[leaf]
127.0.0.1 ansible_user=admin ansible_password=admin

[all:vars]
ansible_user=admin
ansible_password=admin
ansible_become_pass=admin
ansible_python_interpreter=/usr/bin/python3
ansible_port=6030
ansible_connection=nokia.grpc.gnmi
ansible_gnmi_encoding=JSON
```


##gNMI collection

```text
ansible-galaxy collection install nokia.openconfig
```

#Run the playbook

```text
ansible-playbook -i inventory capabilities.yaml
```

###output of playbook

```text
ok: [10.20.30.67] => {
    "msg": {
        "gNMIVersion": "0.7.0",
        "supportedEncodings": [
            "JSON",
            "JSON_IETF",
            "ASCII"
        ],
        "supportedModels": [
            {
                "name": "arista-exp-eos-multicast",
                "organization": "Arista Networks <http://arista.com/>"
            },
            {
                "name": "arista-exp-eos-evpn",
                "organization": "Arista Networks, Inc."
            },
```