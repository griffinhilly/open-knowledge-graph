---
id: eigrp-enhanced-distance-vector-routing
title: 'EIGRP: Enhanced Interior Gateway Routing Protocol'
domain: computer-science
course: computer-networking
prerequisites:
- id: distance-vector-routing-protocols
  type: hard
- id: routing-algorithms-overview
  type: hard
- id: rip-routing-information-protocol
  type: soft
builds-toward:
- routing-convergence-flap-damping
- bgp-border-gateway-protocol
tags:
- routing
- eigrp
- igp
- dynamic-routing
- cisco
stage: advanced
status: draft
---

# EIGRP: Enhanced Interior Gateway Routing Protocol

## Core Idea
EIGRP (Enhanced Interior Gateway Routing Protocol) is a Cisco proprietary distance-vector protocol that uses a composite metric of bandwidth, delay, reliability, and load. It converges faster than RIP using the Diffusing Update Algorithm (DUAL) and maintains backup routes (feasible successors). EIGRP sends incremental updates only when topology changes, reducing overhead significantly.

## How It's Best Learned
Deploy EIGRP on Cisco equipment or GNS3 with IOS images. Observe DUAL calculations and feasible successor selection. Cause link failures and measure convergence compared to RIP. Configure EIGRP for IPv6 (EIGRPv6) and compare protocol behavior.

## Common Misconceptions
EIGRP is not proprietary in modern versions; Cisco submitted it as an IETF draft but does not enforce patents. EIGRP does not send periodic updates like RIP; it sends triggered updates only. Feasible distance is not the same as advertised distance from the neighbor.
