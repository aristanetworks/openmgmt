---
layout: page
title: "golang"
date: 2021-03-19 08:17:00 --0600
categories:
---

## Overview

The following example uses the
[goarista](https://pkg.go.dev/github.com/aristanetworks/goarista) go module for
gNMI to interact with a device. Within this very simplistic getting started
example main.go will simply perform a get method to the device for all paths.

```shell
go run main.go
```

## Truncated output

```javascript
{
  "openconfig-acl:acl": {
    "state": {
      "counter-capability": "AGGREGATE_ONLY"
    }
  },
  "arista-exp-eos:arista": {
    "eos": {
      "arista-exp-eos-igmpsnooping:bridging": {
        "igmpsnooping": {
          "config": {}
        }
      },
      "arista-exp-eos-mlag:mlag": {
        "config": {
          "dual-primary-action": "action-none",
```
