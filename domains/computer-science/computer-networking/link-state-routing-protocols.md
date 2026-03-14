---
id: link-state-routing-protocols
title: Link-State Routing Protocols
domain: computer-science
course: computer-networking
prerequisites:
- id: routing-algorithms-overview
  type: hard
- id: dijkstras-shortest-path-routing
  type: hard
builds-toward:
- ospf-open-shortest-path-first
tags:
- link-state
- ls-routing
- dijkstra
- flooding
stage: advanced
status: draft
---

# Link-State Routing Protocols

## Core Idea
Link-state routing protocols have each router flood information about its directly connected links to all other routers, allowing each router to independently compute shortest paths using Dijkstra's algorithm. OSPF is the most deployed link-state protocol; it converges faster than distance-vector approaches and avoids count-to-infinity problems but requires more memory and CPU.
