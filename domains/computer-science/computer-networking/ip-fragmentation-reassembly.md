---
id: ip-fragmentation-reassembly
title: IP Fragmentation and Reassembly
domain: computer-science
course: computer-networking
prerequisites:
- id: ipv4-addressing
  type: hard
- id: osi-model-layers
  type: hard
builds-toward:
- path-mtu-discovery-pmtud
- icmp-internet-control-message-protocol
tags:
- network-layer
- ip
- fragmentation
- mtu
stage: advanced
status: draft
---

# IP Fragmentation and Reassembly

## Core Idea
IP fragmentation occurs when a datagram exceeds the Maximum Transmission Unit (MTU) of a network link, splitting it into smaller fragments. Each fragment carries the original IP header plus an offset and a flag indicating more fragments. The destination host reassembles fragments, and loss of any fragment causes the entire datagram to be discarded.

## How It's Best Learned
Use ping with large packet sizes (-s flag) to trigger fragmentation across different network links. Observe fragment reassembly timeouts by dropping fragments in a controlled lab. Compare IPv4 fragmentation with IPv6's approach (no fragmentation at routers).

## Common Misconceptions
Routers fragment packets in IPv4, not TCP; TCP must use MSS negotiation to avoid fragmentation. IPv6 does not fragment at routers; the source must discover MTU via ICMPv6. Fragmentation is not efficient; modern networks prefer to avoid it via MTU discovery.
