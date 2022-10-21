---
layout: default
title: "Device Models"
date: 2021-03-02 12:17:00 --0600
---

## Overview

What are YANG models and why should I care?

Models are structured representations of network elements and their associated configured and operational state.

YANG (Yet Another Next Generation - [RFC6020](https://datatracker.ietf.org/doc/html/rfc6020)) is a data modeling
language. YANG is used to describe the configured and operational state of network elements. This allows for the
consistent and structured representation of device and protocol attributes. The model definition typically includes the
low level data types used to represent operational attributes as well as constraints that should be enforced in
configuration.

These modeled representations provide a consistent mechanism for device configuration as well as validating the device
state through streaming telemetry or other device interrogation methods. These modeled device representations can also
be transformed into data structures that can be used by configuration systems to dynamically control device
configuration or state.

YANG has been adopted as the official modeling language of the IETF and the OpenConfig group.

## IETF models

The for the past few years the IETF has been providing models for previously standardized technologies as well as
protocols and technologies which are under active standardization. These models are commonly used with complementary
IETF standardized network management protocols (for example, NETCONF and RESTCONF) and have been selectively incorporated
into other modeling initiatives.

## OpenConfig models

[OpenConfig](https://www.openconfig.net) is an operator led group defining models for network devices. Their models
have been widely adopted by a number of vendors including Arista and an ecosystem of open source tooling has emerged to
utilize these models for telemetry and configuration applications.

In addition to defining device and protocol models the OpenConfig group has defined complementary network management
protocols which leverage these models for telemetry (gNMI), configuration (gNMI), operational activities (gNOI) and
RIB manipulation (gRIBI).  Though it bears noting that OpenConfig models can also be used with NETCONF and RESTCONF
protocols as well.

Details regarding the OpenConfig model support within Arista's EOS software can be found online.

## Vendor-Specific Models

While standard models provide a wide range of feature coverage there is commonly a need to model vendor-specific device
or feature operation. Examples of this may include device specific behaviors (hardware configuration details) or
pre-standard functionality that is deployed in operator networks that needs to be managed using the same tooling.

Vendors may opt to define all new models which are published independently. Alternately, vendors may choose to leverage
an existing standardized model and add vendor-specific elements to the standard models these are known as model
augments. These augments are commonly published to allow integration into operator tooling.

Arista publishes augments associated with a given EOS release on [GitHub](https://github.com/aristanetworks/yang).

## References / Resources

- [YANG RFC](https://tools.ietf.org/html/rfc6020)
- [Repository of OpenConfig YANG models](https://github.com/openconfig/public)
- [Arista Networks YANG Repository](https://github.com/aristanetworks/yang)
