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
status: validated
---
# Segment Routing and Source Routing

## Core Idea
Segment Routing (SR) simplifies traffic engineering by encoding the path as a list of segment identifiers (SIDs) in packet headers. Rather than relying on per-flow state in routers, SR pushes routing decisions to the ingress node. Segment routing can run over MPLS (SR-MPLS) or IPv6 (SRv6), with segment identifiers mapping to prefixes, adjacencies, or functions.

## How It's Best Learned
Deploy segment routing on open-source implementations (FRRouting) or network simulators. Configure SIDs for prefixes and adjacencies. Test traffic engineering policies using segment lists. Compare convergence time and state management vs. MPLS-TE.

## Common Misconceptions
Segment routing does not replace OSPF/BGP; it augments them with a label distribution mechanism. SIDs are not addresses; they are indices into forwarding tables. Segment routing requires all routers to understand SID semantics for correct forwarding.

## Questions

```yaml
- question: "A network operator wants to force a specific traffic flow through a particular physical link between routers A and B, even though normal shortest-path routing would avoid it. Which Segment Routing SID type is appropriate, and why?"
  type: multiple-choice
  options:
    - "A prefix SID for router B — this directs traffic toward B via any path"
    - "An adjacency SID for the A-B link — this explicitly identifies the specific link to traverse"
    - "A new BGP route announcement redirecting traffic to B"
    - "An OSPF cost adjustment to make the A-B link the shortest path"
  answer: 1
  explanation: "Prefix SIDs identify a destination node and let the network choose the path — they do not guarantee which specific link is used. Adjacency SIDs identify a specific directed link between two neighboring routers, so including an adjacency SID in a segment list forces traffic to traverse exactly that link. This is the precise traffic engineering use case for SR: encode the desired path as a sequence of adjacency (and prefix) SIDs so the ingress node dictates the route end-to-end."

- question: "What is Segment Routing's most significant operational advantage over RSVP-TE for traffic engineering in MPLS networks?"
  type: multiple-choice
  options:
    - "Segment Routing supports IPv6 while RSVP-TE is IPv4-only"
    - "Segment Routing eliminates per-flow state in intermediate routers; intermediate nodes only need to know how to process SIDs"
    - "Segment Routing computes shorter paths than RSVP-TE by leveraging global topology knowledge"
    - "Segment Routing requires no changes to existing routing protocols"
  answer: 1
  explanation: "With RSVP-TE, every router along a traffic-engineered path must maintain signaling state for every tunnel — state that must be refreshed, is vulnerable to failures, and grows proportionally with the number of traffic-engineered flows. Segment Routing eliminates this entirely: intermediate routers just process SIDs locally and forward; all path intelligence lives at the ingress node (or a controller). This statelessness vastly improves scalability and reduces the operational burden of traffic engineering."

- question: "In a Segment Routing network, each intermediate router along the segment list path must maintain per-flow state to correctly forward packets."
  type: true-false
  answer: false
  explanation: "This is the key distinction between SR and older traffic engineering approaches. Intermediate routers in an SR network are stateless — they simply read the active SID, perform the corresponding action (forward to a node or via a specific link), pop that SID, and forward the packet. No per-flow state is stored or maintained. All path information is carried in the packet's segment list itself, which was encoded by the ingress node. This is what makes SR scalable to large numbers of traffic-engineered flows."

- question: "SR-MPLS can be deployed on existing MPLS infrastructure with software upgrades because Segment IDs are carried as standard MPLS labels."
  type: true-false
  answer: true
  explanation: "SR-MPLS maps each SID to an MPLS label value in the label stack, using the existing MPLS data plane without hardware changes. The segment list becomes a stack of MPLS labels — each SID is just a label, and the MPLS forwarding mechanism (push, swap, pop) already handles label stacks. This backward compatibility is a key deployment advantage: operators can adopt segment routing incrementally, adding SR capabilities via software upgrades to existing MPLS routers rather than replacing hardware."

- question: "Explain why the statelessness of intermediate routers in Segment Routing matters operationally, particularly compared to RSVP-TE."
  type: short-answer
  answer: "In RSVP-TE, every router along a traffic-engineered path must store and maintain signaling state for every active tunnel — this state must be refreshed periodically, consumes memory, requires complex failure recovery, and grows with the number of engineered flows. In large networks with thousands of traffic-engineered tunnels, this becomes a significant operational burden. Segment Routing moves all path intelligence to the ingress node: the path is encoded in the packet's segment list, and intermediate routers simply execute SID instructions without storing anything per-flow. This means adding new traffic-engineered paths requires no coordination with or state changes in intermediate routers — only the ingress changes."
  explanation: "The practical consequence is dramatic scalability improvement: the number of traffic-engineered flows is limited only by the ingress node's compute capacity, not by memory across hundreds of intermediate routers. It also simplifies failure recovery, since there is no distributed state to synchronize when links or nodes fail."
```

## Explainer

Traditional IP routing works hop-by-hop: each router independently examines the destination address and consults its own routing table to decide where to forward the packet. From your study of routing algorithms and BGP, you know this model works well for basic reachability — packets find a path to their destination. But it gives the network operator very little control over *which* path traffic takes. If you want to steer certain flows through a specific sequence of routers (for traffic engineering, policy compliance, or avoiding congested links), hop-by-hop routing alone cannot do it. **Segment Routing (SR)** solves this by letting the source node encode the entire forwarding path directly into the packet header.

The core abstraction is the **segment**, identified by a **Segment Identifier (SID)**. A segment represents an instruction — "forward to node X," "use the link between A and B," or "apply function F." There are two main types: **prefix SIDs** identify a destination node (like a global address), while **adjacency SIDs** identify a specific link between two neighboring routers. The source constructs an ordered list of SIDs — called a **segment list** — and pushes it onto the packet. Each router along the path reads the active SID, performs the corresponding action, pops that SID from the list, and forwards the packet onward. The result is source-routed traffic engineering without any per-flow state stored in intermediate routers.

This statelessness is Segment Routing's most important advantage over older traffic engineering approaches like RSVP-TE in MPLS networks. With RSVP-TE, every router along a traffic-engineered path must maintain signaling state for every tunnel — a significant operational burden that scales poorly. Segment Routing eliminates this entirely: intermediate routers just need to know how to process SIDs, which are distributed through extensions to protocols you already know (IS-IS or OSPF for interior routing, BGP for inter-domain). The intelligence lives at the network edge, where a controller or ingress router computes paths and encodes them as segment lists.

Segment Routing runs in two flavors: **SR-MPLS** uses MPLS label stacks to carry SIDs (each SID is simply an MPLS label), making it deployable on existing MPLS infrastructure with software upgrades. **SRv6** encodes SIDs as IPv6 addresses in a Segment Routing Header extension, leveraging IPv6's native extensibility and enabling richer programmability — a SID can encode not just a destination but a network function to apply. Both approaches achieve the same goal of source-directed forwarding, but SRv6 trades some header overhead for greater flexibility and a unified IPv6 data plane.
