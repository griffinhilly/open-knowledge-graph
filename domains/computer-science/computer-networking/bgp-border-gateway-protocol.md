---
id: bgp-border-gateway-protocol
title: 'BGP: Border Gateway Protocol'
domain: computer-science
course: computer-networking
prerequisites:
- id: ospf-open-shortest-path-first
  type: soft
tags:
- bgp
- egp
- exterior-gateway-protocol
- autonomous-system
- path-vector
stage: advanced
status: draft
---

# BGP: Border Gateway Protocol

## Core Idea
BGP is the exterior gateway protocol used to route traffic between autonomous systems (AS) on the Internet. Unlike OSPF, BGP uses path-vector routing where routers announce the full AS path to each destination, allowing policies (e.g., business relationships, traffic engineering) to influence route selection, not just hop count.
