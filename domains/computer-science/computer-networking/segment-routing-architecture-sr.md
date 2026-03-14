---
id: segment-routing-architecture-sr
title: Segment Routing and Source Routing
domain: computer-science
course: computer-networking
prerequisites:
- id: routing-algorithms-overview
  type: hard
- id: bgp-border-gateway-protocol
  type: hard
builds-toward:
- mpls-multiprotocol-label-switching
- network-standards-and-ietf
tags:
- routing
- segment-routing
- source-routing
- traffic-engineering
stage: advanced
status: draft
---

# Segment Routing and Source Routing

## Core Idea
Segment Routing (SR) simplifies traffic engineering by encoding the path as a list of segment identifiers (SIDs) in packet headers. Rather than relying on per-flow state in routers, SR pushes routing decisions to the ingress node. Segment routing can run over MPLS (SR-MPLS) or IPv6 (SRv6), with segment identifiers mapping to prefixes, adjacencies, or functions.

## How It's Best Learned
Deploy segment routing on open-source implementations (FRRouting) or network simulators. Configure SIDs for prefixes and adjacencies. Test traffic engineering policies using segment lists. Compare convergence time and state management vs. MPLS-TE.

## Common Misconceptions
Segment routing does not replace OSPF/BGP; it augments them with a label distribution mechanism. SIDs are not addresses; they are indices into forwarding tables. Segment routing requires all routers to understand SID semantics for correct forwarding.
