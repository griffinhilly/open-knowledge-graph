---
id: route-aggregation-supernetting
title: Route Aggregation and Supernetting
domain: computer-science
course: computer-networking
prerequisites:
- id: subnetting-and-cidr-notation
  type: hard
builds-toward:
- bgp-border-gateway-protocol
tags:
- aggregation
- supernetting
- cidr
- routing-scalability
stage: advanced
status: draft
---

# Route Aggregation and Supernetting

## Core Idea
Route aggregation combines multiple routing table entries with consecutive CIDR blocks into a single entry with a shorter prefix, reducing routing table size. For example, 192.168.0.0/24 and 192.168.1.0/24 can be aggregated as 192.168.0.0/23. Aggregation is essential for scaling the Internet; without it, routing tables would contain billions of entries.
