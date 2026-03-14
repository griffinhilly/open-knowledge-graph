---
id: network-address-translation
title: Network Address Translation (NAT)
domain: computer-science
course: computer-networking
prerequisites:
- id: ipv4-addressing
  type: hard
- id: ip-routing-basics
  type: hard
builds-toward:
- firewall-architecture-and-rules
tags:
- nat
- address-translation
- private-addressing
- port-forwarding
stage: advanced
status: draft
---

# Network Address Translation (NAT)

## Core Idea
NAT translates IP addresses in packet headers as they cross a boundary, allowing multiple devices with private addresses to share a single public address. NAT rewrites source addresses in outgoing packets and destination addresses in incoming replies, maintaining a translation table. While NAT was designed as a workaround for IPv4 address scarcity, it also provides a basic security benefit by hiding internal network structure.
