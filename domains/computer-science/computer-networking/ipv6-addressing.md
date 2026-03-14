---
id: ipv6-addressing
title: IPv6 Addressing and Autoconfiguration
domain: computer-science
course: computer-networking
prerequisites:
- id: ipv4-addressing
  type: hard
tags:
- ipv6
- addressing
- 128-bit
- next-generation
stage: advanced
status: draft
---

# IPv6 Addressing and Autoconfiguration

## Core Idea
IPv6 addresses are 128-bit identifiers designed to overcome IPv4 address exhaustion. They are written in hexadecimal with colons (e.g., 2001:db8::1) and include built-in support for address autoconfiguration (SLAAC), allowing hosts to generate globally unique addresses without DHCP.

## How It's Best Learned
Convert IPv6 addresses between full and compressed notation; use IPv6 simulation to test SLAAC and neighbor discovery.

## Common Misconceptions
- IPv6 adoption is near complete; IPv4 still dominates as of 2026.
- IPv6 addresses are all globally routable; link-local and unique-local addresses are not routable globally.
