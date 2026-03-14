---
id: path-mtu-discovery-pmtud
title: Path MTU Discovery and Handling MTU Issues
domain: computer-science
course: computer-networking
prerequisites:
- id: ip-fragmentation-reassembly
  type: hard
- id: icmp-internet-control-message-protocol
  type: hard
builds-toward:
- tcp-flow-control-and-congestion-control
- network-management-and-monitoring
tags:
- network-layer
- mtu
- path-discovery
- icmp
stage: advanced
status: draft
---

# Path MTU Discovery and Handling MTU Issues

## Core Idea
Path MTU Discovery (PMTUD) determines the smallest MTU along a path to avoid fragmentation. The source sends packets with the DF (Do Not Fragment) flag set; routers responding with ICMP Fragmentation Needed messages indicate the bottleneck MTU. Hosts adjust MSS (Maximum Segment Size) accordingly, improving performance.

## How It's Best Learned
Trace PMTUD across networks with varying MTUs using ping with DF flag and large sizes. Observe ICMP Fragmentation Needed messages. Simulate broken PMTUD (blocked ICMP) and observe performance degradation. Monitor MSS negotiation in TCP handshakes.

## Common Misconceptions
PMTUD requires ICMP Fragmentation Needed messages; blocking ICMP breaks PMTUD. MTU-related issues cause subtle failures; packets succeed on some hops but fail downstream. Black-hole routers (drop ICMP) cause connection timeouts, not immediate failures.
