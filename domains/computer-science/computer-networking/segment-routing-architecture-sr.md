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

## Explainer

Traditional IP routing works hop-by-hop: each router independently examines the destination address and consults its own routing table to decide where to forward the packet. From your study of routing algorithms and BGP, you know this model works well for basic reachability — packets find a path to their destination. But it gives the network operator very little control over *which* path traffic takes. If you want to steer certain flows through a specific sequence of routers (for traffic engineering, policy compliance, or avoiding congested links), hop-by-hop routing alone cannot do it. **Segment Routing (SR)** solves this by letting the source node encode the entire forwarding path directly into the packet header.

The core abstraction is the **segment**, identified by a **Segment Identifier (SID)**. A segment represents an instruction — "forward to node X," "use the link between A and B," or "apply function F." There are two main types: **prefix SIDs** identify a destination node (like a global address), while **adjacency SIDs** identify a specific link between two neighboring routers. The source constructs an ordered list of SIDs — called a **segment list** — and pushes it onto the packet. Each router along the path reads the active SID, performs the corresponding action, pops that SID from the list, and forwards the packet onward. The result is source-routed traffic engineering without any per-flow state stored in intermediate routers.

This statelessness is Segment Routing's most important advantage over older traffic engineering approaches like RSVP-TE in MPLS networks. With RSVP-TE, every router along a traffic-engineered path must maintain signaling state for every tunnel — a significant operational burden that scales poorly. Segment Routing eliminates this entirely: intermediate routers just need to know how to process SIDs, which are distributed through extensions to protocols you already know (IS-IS or OSPF for interior routing, BGP for inter-domain). The intelligence lives at the network edge, where a controller or ingress router computes paths and encodes them as segment lists.

Segment Routing runs in two flavors: **SR-MPLS** uses MPLS label stacks to carry SIDs (each SID is simply an MPLS label), making it deployable on existing MPLS infrastructure with software upgrades. **SRv6** encodes SIDs as IPv6 addresses in a Segment Routing Header extension, leveraging IPv6's native extensibility and enabling richer programmability — a SID can encode not just a destination but a network function to apply. Both approaches achieve the same goal of source-directed forwarding, but SRv6 trades some header overhead for greater flexibility and a unified IPv6 data plane.
