---
layout: default
title: "RESTCONF"
date: 2021-07-16 08:17:00 --0600
categories:
---

RESTCONF examples with EOS

## About RESTCONF

RESTCONF is defined in the [RFC 8040](https://datatracker.ietf.org/doc/html/rfc8040)

- The GET method is sent by the client to retrieve data for a resource.
- The HEAD method is sent by the client to retrieve just the header fields (which contain the metadata for a resource)
that would be returned for the comparable GET method, without the response message-body.
It is supported for all resources that support the GET method.
- The POST method is sent by the client to create a data resource.
- The PUT method is sent by the client to create or replace the target data resource.
- The DELETE method is used to delete the target resource.

## EOS configuration

Please refer to [this link](../../configuration/restconf.md)

## EOS Control plane ACL

The default RESTCONF port on Arista devices is TCP 6020.

We need to change the default control-plane ACL on EOS in order to allow TCP 6020 (or the configured RESTCONF TCP port).

Please refer to [this link](../../configuration/security.md)
