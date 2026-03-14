---
id: dhcp-dynamic-host-configuration
title: DHCP (Dynamic Host Configuration Protocol)
domain: computer-science
course: computer-networking
prerequisites:
- id: ipv4-addressing
  type: hard
builds-toward:
- network-management-and-monitoring
tags:
- dhcp
- address-assignment
- dynamic-configuration
- leasing
stage: advanced
status: draft
---

# DHCP (Dynamic Host Configuration Protocol)

## Core Idea
DHCP automatically assigns IP addresses and network configuration to clients from a pool of addresses managed by a server. Clients request a lease for a specific duration and must renew it to maintain their address; leases expiring return addresses to the pool. DHCP eliminates manual configuration errors and simplifies network management, especially in environments with mobile or frequently-changing devices.
