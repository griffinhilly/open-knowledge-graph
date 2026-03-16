---
id: mpls-multiprotocol-label-switching
title: 'MPLS: Multiprotocol Label Switching'
domain: computer-science
course: computer-networking
prerequisites:
- id: routing-table-concepts
  type: hard
- id: routing-algorithms-overview
  type: hard
builds-toward:
- segment-routing-architecture-sr
- vpn-virtual-private-networks
tags:
- routing
- mpls
- label-switching
- traffic-engineering
stage: advanced
status: draft
---

# MPLS: Multiprotocol Label Switching

## Core Idea
MPLS (Multiprotocol Label Switching) inserts labels between the IP and link-layer headers, enabling fast forwarding based on simple label lookups rather than longest-prefix IP matching. Label Distribution Protocol (LDP) and RSVP-TE distribute labels and establish label-switched paths (LSPs). MPLS enables Traffic Engineering (TE) and VPN services (MPLS-TE, L3VPN).

## How It's Best Learned
Deploy LDP-based MPLS on Cisco or open-source routers (Quagga, FRRouting). Observe label distribution and LSP establishment. Configure MPLS-TE with explicit paths and bandwidth constraints. Monitor label stacks using tcpdump.

## Common Misconceptions
MPLS is not a replacement for IP routing; it runs alongside it. Label lookups are O(1) but still require table lookups; MPLS does not eliminate routing overhead. MPLS labels are local to each link; different labels represent the same path on different hops.

## Explainer

From your study of routing tables and routing algorithms, you know that traditional IP forwarding works by examining the destination address in each packet's header and performing a **longest-prefix match** against the routing table. This works well, but longest-prefix matching is computationally expensive — a router might need to compare the destination against hundreds of thousands of prefixes. **MPLS** (Multiprotocol Label Switching) offers an alternative forwarding mechanism: instead of inspecting the IP header at every hop, routers attach a short, fixed-length **label** to each packet at the network's edge, and interior routers forward packets by simply looking up that label in a small, flat table. Label lookup is a direct index operation — far faster than longest-prefix matching.

The MPLS label is inserted between the link-layer header (e.g., Ethernet) and the IP header, in a position sometimes called the **shim header**. It is only 4 bytes: a 20-bit label value, a 3-bit traffic class field, a 1-bit bottom-of-stack flag, and an 8-bit TTL. When a packet enters an MPLS network, the first MPLS-capable router (the **ingress label edge router**, or ingress LER) examines the IP destination, consults its label forwarding table, and pushes an appropriate label onto the packet. Interior routers (**label switch routers**, or LSRs) never look at the IP header — they read the label, look it up in their label forwarding table, **swap** it for a new outgoing label, and forward the packet out the appropriate interface. At the far end, the **egress LER** pops the label and delivers the packet as a normal IP datagram.

A critical detail is that labels have **local significance** — they are meaningful only on the link between two adjacent routers. Router A might use label 42 to mean "this packet is headed for the 10.0.0.0/8 prefix," but when it forwards the packet to router B, it swaps label 42 for label 17, which is what router B expects. This is why it is called label *switching*: each hop swaps the incoming label for an outgoing one. **Label Distribution Protocol (LDP)** or **RSVP-TE** handles the negotiation, with adjacent routers agreeing on which labels to use for which destinations. The sequence of labels from ingress to egress defines a **Label Switched Path (LSP)** — a predetermined route through the network.

The real power of MPLS lies in **traffic engineering** and **VPN services**. Because LSPs are explicitly established paths, network operators can steer traffic away from congested links, distribute load across parallel paths, and guarantee bandwidth — something that traditional shortest-path IP routing cannot do. MPLS also enables **Layer 3 VPNs** (L3VPN), where a service provider uses label stacking (multiple labels on one packet) to keep different customers' traffic separated on shared infrastructure. The outer label routes the packet through the provider's backbone, while the inner label identifies the customer's VPN. This made MPLS the backbone technology for enterprise WAN services for over two decades, and while newer approaches like segment routing are evolving the paradigm, MPLS remains widely deployed.
