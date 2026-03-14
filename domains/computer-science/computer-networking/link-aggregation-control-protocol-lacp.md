---
id: link-aggregation-control-protocol-lacp
title: Link Aggregation Control Protocol (LACP)
domain: computer-science
course: computer-networking
prerequisites:
- id: ethernet-protocol
  type: hard
- id: switching-basics
  type: hard
- id: spanning-tree-protocol-stp
  type: soft
builds-toward:
- network-topologies
- qos-quality-of-service
tags:
- link-layer
- aggregation
- lacp
- port-channeling
stage: advanced
status: draft
---

# Link Aggregation Control Protocol (LACP)

## Core Idea
Link Aggregation Control Protocol (LACP, 802.3ad) enables multiple physical links to be bundled into a single logical link, increasing bandwidth and providing redundancy. LACP dynamically negotiates which links are active and handles failures by rebalancing traffic. Load balancing algorithms distribute frames based on source/destination MAC, IP addresses, or port numbers.

## How It's Best Learned
Configure LACP bonds on Linux (bonding driver) or switches. Observe LACP frame exchanges (PDUs) using tcpdump. Simulate link failures and measure failover time. Test different load-balancing algorithms and observe traffic distribution.

## Common Misconceptions
LACP requires both sides of the link to support it; one-sided aggregation (static LAG) is also common. LACP does not guarantee load balancing per flow; it distributes flows heuristically. Aggregation does not provide redundancy if all links share a common failure point.
