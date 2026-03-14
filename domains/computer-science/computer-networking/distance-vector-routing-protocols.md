---
id: distance-vector-routing-protocols
title: Distance-Vector Routing Protocols
domain: computer-science
course: computer-networking
prerequisites:
- id: routing-algorithms-overview
  type: hard
- id: bellman-ford-distance-vector-routing
  type: hard
builds-toward:
- bgp-border-gateway-protocol
tags:
- distance-vector
- dv-routing
- bellman-ford
- rip
stage: advanced
status: draft
---

# Distance-Vector Routing Protocols

## Core Idea
Distance-vector routing protocols compute shortest paths based on a simple metric by having each router advertise its distances to all destinations and update based on neighbors' advertisements. RIP is a classic distance-vector protocol that uses hop count as its metric. Distance-vector protocols converge slowly and suffer from count-to-infinity problems, but remain simple to implement.
