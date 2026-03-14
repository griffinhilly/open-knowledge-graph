---
id: dhcp-relay-snooping-security
title: DHCP Relay Agents and DHCP Snooping Security
domain: computer-science
course: computer-networking
prerequisites:
- id: dhcp-dynamic-host-configuration
  type: hard
- id: network-security-fundamentals
  type: hard
builds-toward:
- network-security-fundamentals
- network-management-and-monitoring
tags:
- security
- dhcp
- snooping
- link-layer
stage: advanced
status: draft
---

# DHCP Relay Agents and DHCP Snooping Security

## Core Idea
DHCP relay agents forward DHCP broadcasts across subnets to centralized DHCP servers, adding the giaddr field to requests. DHCP snooping, a switch-level security mechanism, learns the binding between MAC addresses, IP addresses, and ports by listening to DHCP messages. It prevents rogue DHCP servers and prevents clients from receiving addresses from untrusted sources.

## How It's Best Learned
Configure a DHCP relay agent on a router and observe giaddr insertion. Set up DHCP snooping on a switch and observe binding database. Attempt to set up a rogue DHCP server and confirm snooping blocks it. Monitor DHCP starvation attacks.

## Common Misconceptions
DHCP relay is not the same as a DHCP server; it forwards requests to a server elsewhere. DHCP snooping does not prevent DHCP requests from reaching trusted DHCP servers. Port security and DHCP snooping are complementary, not redundant.
