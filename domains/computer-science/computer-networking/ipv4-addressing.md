---
id: ipv4-addressing
title: IPv4 Addressing and Address Classes
domain: computer-science
course: computer-networking
prerequisites:
- id: tcp-ip-model
  type: hard
builds-toward:
- ipv6-addressing
- subnetting-and-cidr-notation
- ip-routing-basics
tags:
- ipv4
- addressing
- classes
- layer-3
stage: advanced
status: draft
---

# IPv4 Addressing and Address Classes

## Core Idea
IPv4 addresses are 32-bit identifiers for hosts on the Internet, typically written in dotted-decimal notation (e.g., 192.168.1.1). Classful addressing (now obsolete) divided addresses into Classes A–E; modern networking uses Classless Inter-Domain Routing (CIDR) for more flexible address allocation.

## How It's Best Learned
Convert IPv4 addresses between decimal and binary; practice identifying address classes and private address ranges (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16).

## Common Misconceptions
- All IP addresses are globally routable; private addresses (RFC 1918) are only routable within private networks.
- IPv4 address space is infinite; address exhaustion is real and motivated the transition to IPv6.
