---
id: rip-routing-information-protocol
title: 'RIP: Routing Information Protocol'
domain: computer-science
course: computer-networking
prerequisites:
- id: distance-vector-routing-protocols
  type: hard
- id: routing-algorithms-overview
  type: hard
builds-toward:
- eigrp-enhanced-distance-vector-routing
- routing-convergence-flap-damping
tags:
- routing
- distance-vector
- igp
- dynamic-routing
stage: advanced
status: draft
---

# RIP: Routing Information Protocol

## Core Idea
RIP (Routing Information Protocol) is a distance-vector interior gateway protocol using hop count as the metric, with a maximum of 15 hops (limiting scalability). RIPv1 sends classful updates via broadcast; RIPv2 supports CIDR and multicast updates. Routers exchange routing tables periodically, implementing the Bellman-Ford algorithm with slow convergence and high overhead.

## How It's Best Learned
Deploy RIPv2 in a GNS3 lab and observe periodic updates (30-second intervals). Cause a topology change and measure convergence time. Monitor update traffic with Wireshark to understand message structure and timers.

## Common Misconceptions
RIP converges very slowly due to counting to infinity; split-horizon and poison reverse partially mitigate this. Hop count is a poor metric, favoring paths through many low-capacity links over fewer high-capacity ones. RIP is rarely used in production; OSPF and BGP are preferred.
