---
id: ospf-open-shortest-path-first
title: 'OSPF: Open Shortest Path First'
domain: computer-science
course: computer-networking
prerequisites:
- id: dijkstras-shortest-path-routing
  type: hard
builds-toward:
- bgp-border-gateway-protocol
tags:
- ospf
- link-state
- igp
- interior-gateway-protocol
stage: advanced
status: draft
---

# OSPF: Open Shortest Path First

## Core Idea
OSPF is a widely-used interior gateway protocol (IGP) that routers within an autonomous system use to exchange topology information and compute shortest paths. OSPF organizes networks into areas to reduce overhead, supports equal-cost multipath routing, and converges quickly to topology changes.
