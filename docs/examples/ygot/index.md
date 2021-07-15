---
layout: default
title: "ygot"
date: 2021-07-15 13:10:00 --0600
categories:
---

## Overview

![#ygot](images/ygot.png?raw=true)

[ygot](https://github.com/openconfig/ygot) is a collection of Go utilities that can generate Go structures based off of yang modules.  In the demo we are going to generate go code based off of the [openconfig-system model](https://github.com/openconfig/public/blob/master/release/models/system/.openconfig-system.yang) using ygot.

## The demo will do the following.

- Leverage necessary yang files for openconfig-system to create a hostname.
- The hostname will be printed out and stored within the system.json file.
- Using the [Arista gNMI binary](https://github.com/aristanetworks/goarista/tree/master/cmd/gnmi) we will configure a device to use the ceos1 hostname.

## clone this repo 
```
git clone https://github.com/aristanetworks/openmgmt && cd openmgmt/src/ygot
```

## Install ygot on your system 
```
go get github.com/openconfig/ygot
```

## Check to see if all of the current yang files are accurate
```
tree -f yang/
```
<details><summary> Reveal output</summary>
<p>

```javascript

├── yang/openconfig-aaa-radius.yang
├── yang/openconfig-aaa-tacacs.yang
├── yang/openconfig-aaa-types.yang
├── yang/openconfig-aaa.yang
├── yang/openconfig-alarms.yang
├── yang/openconfig-alarm-types.yang
├── yang/openconfig-extensions.yang
├── yang/openconfig-inet-types.yang
├── yang/openconfig-license.yang
├── yang/openconfig-messages.yang
├── yang/openconfig-platform-types.yang
├── yang/openconfig-platform.yang
├── yang/openconfig-procmon.yang
├── yang/openconfig-system-logging.yang
├── yang/openconfig-system-management.yang
├── yang/openconfig-system-terminal.yang
├── yang/openconfig-system.yang
├── yang/openconfig-types.yang
└── yang/openconfig-yang-types.yang
```

</p>
</details>

## run ygot 
```
go run $GOPATH/src/github.com/openconfig/ygot/generator/generator.go -path=yang -output_file=pkg/oc.go -package_name=oc -generate_fakeroot -fakeroot_name=device -compress_paths=true  yang/openconfig-system.yang
```

## Check the contents of pkg/oc.go 
```
pkg
└── oc.go
```

oc.go is the necessary go import / package for openconfig-system.  Looking at the Device struct within pkg/oc.go

```go
type Device struct {
	Component	map[string]*Component	`path:"components/component" module:"openconfig-platform"`
	Messages	*Messages	`path:"messages" module:"openconfig-messages"`
	System	*System	`path:"system" module:"openconfig-system"`
}
```

Then looking at the System struct we can see the Hostname field.

```go
type System struct {
	Hostname	*string	`path:"config/hostname" module:"openconfig-system"`
}
```

We need to simply fill in the Hostname field and pass it through the [EmitJSON function](https://pkg.go.dev/github.com/openconfig/ygot/ygot#EmitJSON) so we can render this model with the correct information which can be sounf in main.go. 

### Run the go code.

```
go run main.go 
```

<details><summary> Reveal output</summary>
<p>

```javascript
This is the output
{
  "openconfig-system:system": {
    "config": {
      "hostname": "ceos1"
    }
  }
}
Adding to config/hostname.json
```

</p>
</details>

The output is also within config/hostname.json which looks the same as the printed version. 

## Change the hostname on a device
```
gnmi -addr deviceip:6030 -username admin -password admin update '/' config/hostname.json
```
The device should now have the "ceos1" hostname.