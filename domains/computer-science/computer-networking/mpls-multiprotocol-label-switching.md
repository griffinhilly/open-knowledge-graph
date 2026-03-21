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

## Questions

```yaml
- question: "Router A uses label 42 to forward a packet toward its destination. When it forwards the packet to router B, router B receives the packet with label 17. What happened to label 42?"
  type: multiple-choice
  options:
    - "Label 42 was corrupted in transit and router B corrected it to 17"
    - "Router A swapped label 42 for label 17 before forwarding, because labels have only local significance on each link"
    - "Router B relabeled the packet because it disagrees with router A's classification"
    - "The original label 42 is preserved inside the packet; label 17 is a new outer label added to a stack"
  answer: 1
  explanation: "MPLS labels have local significance — a label is meaningful only on the specific link between two adjacent routers. Router A and router B negotiate (via LDP or RSVP-TE) which label router B expects for traffic going to a given destination. Router A swaps its incoming label (42) for the outgoing label that router B expects (17) before forwarding. This per-hop label swap is the defining operation of a label switch router (LSR) and is what makes MPLS a label-switching technology, not a label-tunneling one."

- question: "A network engineer claims that MPLS replaces IP routing in the network core. Why is this statement incorrect?"
  type: multiple-choice
  options:
    - "MPLS does replace IP routing, but only for traffic that has been classified and labeled at the ingress router"
    - "MPLS replaces IP routing in the core but still requires IP at the edges where packets enter and leave"
    - "MPLS runs alongside IP routing — it uses IP routing to establish label-switched paths, and label forwarding operates on top of that infrastructure"
    - "MPLS is being phased out, so the statement is only incorrect because MPLS no longer operates in real networks"
  answer: 2
  explanation: "MPLS does not replace IP routing — it depends on it. The Label Distribution Protocol (LDP) and RSVP-TE that distribute labels and establish Label Switched Paths use IP routing to communicate between routers. The ingress LER uses the IP routing table to decide which LSP to assign a packet to. MPLS provides an alternative forwarding mechanism inside the network, but the IP routing infrastructure remains essential for path establishment and label management. Interior LSRs skip the per-packet IP lookup, but IP routing underlies the entire system."

- question: "In an MPLS network, interior label switch routers (LSRs) must examine the IP header of every packet to determine where to forward it."
  type: true-false
  answer: false
  explanation: "This is the key forwarding advantage of MPLS. Interior LSRs read only the MPLS label — a 20-bit value — and look it up in a flat label forwarding table. This is a direct index operation, far faster than longest-prefix IP matching against potentially hundreds of thousands of routes. Only the ingress LER (at the network edge) examines the IP header to assign the initial label. Once inside the MPLS network, IP-level forwarding is bypassed entirely until the egress LER pops the label and delivers the packet as a normal IP datagram."

- question: "MPLS can carry traffic from multiple different Layer 3 protocols (IPv4, IPv6, and others) because label forwarding does not depend on the contents of the encapsulated header."
  type: true-false
  answer: true
  explanation: "The 'Multiprotocol' in MPLS is meaningful: because interior LSRs forward based on the label alone and never inspect the Layer 3 payload, any Layer 3 protocol can be tunneled through the same MPLS infrastructure. An LSR does not need to understand IPv4, IPv6, or any other protocol in the payload — it simply reads the label, swaps it, and forwards. This protocol-agnosticism is one of the reasons MPLS became the backbone technology for carrier networks supporting diverse customer traffic types."

- question: "Why do MPLS labels have 'local significance only,' and what coordination mechanism makes this work across an entire network?"
  type: short-answer
  answer: "An MPLS label is an arbitrary number meaningful only on a single link between two adjacent routers — router A might use label 42 to mean 'traffic headed for destination X,' but router B uses label 17 for the same traffic on the next link. There is no global label namespace. This works because adjacent routers negotiate label bindings before traffic flows: protocols like LDP or RSVP-TE cause each router to advertise which label it expects to receive for each destination, and its upstream neighbor learns to swap its own label to match. The complete sequence of per-hop label assignments from ingress to egress defines a Label Switched Path (LSP)."
  explanation: "The local-significance design allows labels to be small (20-bit) without risk of global collision — each router independently manages its own label space. The per-hop swap operation is what makes MPLS a switching technology rather than a tunneling technology: rather than encapsulating the original packet in a fixed header stripped at the far end, each intermediate router actively rewrites the label. This also enables label stacking, where multiple labels are stacked to support VPN separation and traffic engineering simultaneously on shared infrastructure."
```

## Explainer

From your study of routing tables and routing algorithms, you know that traditional IP forwarding works by examining the destination address in each packet's header and performing a **longest-prefix match** against the routing table. This works well, but longest-prefix matching is computationally expensive — a router might need to compare the destination against hundreds of thousands of prefixes. **MPLS** (Multiprotocol Label Switching) offers an alternative forwarding mechanism: instead of inspecting the IP header at every hop, routers attach a short, fixed-length **label** to each packet at the network's edge, and interior routers forward packets by simply looking up that label in a small, flat table. Label lookup is a direct index operation — far faster than longest-prefix matching.

The MPLS label is inserted between the link-layer header (e.g., Ethernet) and the IP header, in a position sometimes called the **shim header**. It is only 4 bytes: a 20-bit label value, a 3-bit traffic class field, a 1-bit bottom-of-stack flag, and an 8-bit TTL. When a packet enters an MPLS network, the first MPLS-capable router (the **ingress label edge router**, or ingress LER) examines the IP destination, consults its label forwarding table, and pushes an appropriate label onto the packet. Interior routers (**label switch routers**, or LSRs) never look at the IP header — they read the label, look it up in their label forwarding table, **swap** it for a new outgoing label, and forward the packet out the appropriate interface. At the far end, the **egress LER** pops the label and delivers the packet as a normal IP datagram.

A critical detail is that labels have **local significance** — they are meaningful only on the link between two adjacent routers. Router A might use label 42 to mean "this packet is headed for the 10.0.0.0/8 prefix," but when it forwards the packet to router B, it swaps label 42 for label 17, which is what router B expects. This is why it is called label *switching*: each hop swaps the incoming label for an outgoing one. **Label Distribution Protocol (LDP)** or **RSVP-TE** handles the negotiation, with adjacent routers agreeing on which labels to use for which destinations. The sequence of labels from ingress to egress defines a **Label Switched Path (LSP)** — a predetermined route through the network.

The real power of MPLS lies in **traffic engineering** and **VPN services**. Because LSPs are explicitly established paths, network operators can steer traffic away from congested links, distribute load across parallel paths, and guarantee bandwidth — something that traditional shortest-path IP routing cannot do. MPLS also enables **Layer 3 VPNs** (L3VPN), where a service provider uses label stacking (multiple labels on one packet) to keep different customers' traffic separated on shared infrastructure. The outer label routes the packet through the provider's backbone, while the inner label identifies the customer's VPN. This made MPLS the backbone technology for enterprise WAN services for over two decades, and while newer approaches like segment routing are evolving the paradigm, MPLS remains widely deployed.
