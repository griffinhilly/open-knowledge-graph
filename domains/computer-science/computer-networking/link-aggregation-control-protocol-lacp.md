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
status: validated
---

# Link Aggregation Control Protocol (LACP)

## Core Idea
Link Aggregation Control Protocol (LACP, 802.3ad) enables multiple physical links to be bundled into a single logical link, increasing bandwidth and providing redundancy. LACP dynamically negotiates which links are active and handles failures by rebalancing traffic. Load balancing algorithms distribute frames based on source/destination MAC, IP addresses, or port numbers.

## How It's Best Learned
Configure LACP bonds on Linux (bonding driver) or switches. Observe LACP frame exchanges (PDUs) using tcpdump. Simulate link failures and measure failover time. Test different load-balancing algorithms and observe traffic distribution.

## Common Misconceptions
LACP requires both sides of the link to support it; one-sided aggregation (static LAG) is also common. LACP does not guarantee load balancing per flow; it distributes flows heuristically. Aggregation does not provide redundancy if all links share a common failure point.

## Questions

```yaml
- question: "A server is connected to a switch via a 4-link LACP bond (4 × 1 Gbps). An administrator starts a single large file transfer from the server to a client. What maximum throughput can this transfer achieve?"
  type: multiple-choice
  options:
    - "4 Gbps — all four physical links combine their bandwidth for any single transfer"
    - "2 Gbps — LACP automatically splits large flows across two links for load balancing"
    - "1 Gbps — the hashing algorithm maps a single flow to one physical link, and that link's speed is the ceiling"
    - "Variable, up to 4 Gbps — LACP dynamically routes individual packets across all links in round-robin fashion"
  answer: 2
  explanation: "LACP's hashing algorithm maps each flow (defined by its source/destination address pair or port numbers) to a specific physical link and keeps all packets of that flow on the same link to preserve ordering. A single TCP connection is a single flow — it maps to exactly one physical link and cannot exceed that link's bandwidth. The 4 Gbps aggregate capacity is realized only when many simultaneous flows from different source-destination pairs spread across all four links. This is the most important practical limitation of link aggregation."

- question: "A network engineer connects two switches with two parallel cables (no LACP configured) hoping to double bandwidth. What most likely happens?"
  type: multiple-choice
  options:
    - "Bandwidth doubles as the switches automatically distribute traffic across both cables"
    - "Spanning Tree Protocol detects a loop and blocks one of the parallel links, restoring single-link bandwidth"
    - "Both links remain active in an active-standby configuration: one carries traffic, the other waits for failover"
    - "The second link is used only for broadcast traffic, reducing congestion on the primary link"
  answer: 1
  explanation: "Without link aggregation, STP sees two parallel paths between the same two switches as a bridging loop. To prevent broadcast storms, STP blocks all but one path. This is exactly the problem LACP solves: the entire aggregated bundle appears to STP as a single logical link, so STP does not block any member ports. The engineer would need to configure LACP on both switches to gain bandwidth and redundancy without STP blocking."

- question: "LACP requires both sides of the link to be configured for it; connecting an LACP-configured port to a switch that only supports static LAG will not form a functional aggregation."
  type: true-false
  answer: true
  explanation: "LACP works by exchanging LACPDUs between both sides to dynamically negotiate which ports join the aggregation group. If one side does not speak LACP, the negotiation fails and no LAG is formed. Static LAG (manually configured port channel without LACP) is a separate mechanism that does not require LACP support from the peer, but it lacks LACP's ability to automatically detect misconfigurations, link failures, and incompatible ports."

- question: "When one physical link in an LACP bundle fails, the logical link (as seen by the rest of the network) goes down until STP reconverges and selects a new path."
  type: true-false
  answer: false
  explanation: "This is the key resilience advantage of LACP over simple parallel links. When one member link fails, LACP detects the loss of LACPDUs within seconds and removes that link from the bundle, redistributing traffic across the surviving member links. The logical LAG interface stays up (at reduced bandwidth). No STP reconvergence is needed because STP still sees one logical link — it has not gone down. This is faster and less disruptive than STP-based failover."

- question: "Explain why adding a 4-link LACP bond does not guarantee a 4x speedup for a single client downloading a large file from a server."
  type: short-answer
  answer: "LACP distributes flows across member links using a hash of source and destination addresses (or port numbers). All packets belonging to the same flow — same source IP, destination IP, and port combination — always travel over the same physical link to preserve packet ordering. A single file download is a single TCP flow, so it is hashed to one link and limited to that link's bandwidth. The 4x aggregate bandwidth is only realized when many different flows (from different clients or connections) hash to different links simultaneously."
  explanation: "This surprises many engineers. The mental model of 'four pipes = four times the water' is wrong for individual flows. The correct mental model is 'four separate lanes for four separate cars — one car still only uses one lane.' To saturate a 4-link bond, you need four or more concurrent flows with different address/port hashes. A single client downloading a single file will see at most 1 Gbps no matter how many links are in the bond."
```

## Explainer

From your study of Ethernet and switching, you know that a single Ethernet link between two switches has a fixed bandwidth — 1 Gbps, 10 Gbps, or whatever the physical medium supports. If you need more bandwidth between two switches, you could upgrade to a faster link, but that requires new hardware. **Link aggregation** offers an alternative: bundle multiple existing physical links into a single **logical link** (called a LAG, port channel, or bond) that appears to the rest of the network as one connection with the combined bandwidth. Four 1 Gbps links aggregated together provide up to 4 Gbps of aggregate throughput.

**LACP** (Link Aggregation Control Protocol, defined in IEEE 802.3ad) is the standard protocol for dynamically negotiating and maintaining these bundles. Without LACP, you could statically configure aggregation on both sides, but static configuration is fragile: if one side is misconfigured or a cable is plugged into the wrong port, traffic may be silently dropped or looped. LACP solves this by having the two sides exchange **LACPDUs** (LACP Data Units) — small control frames sent every second (or every 30 seconds in slow mode) that announce each port's identity, system priority, and aggregation key. Both sides use this information to agree on which ports belong to the aggregation group, automatically detecting mismatches and excluding incompatible ports. If a link fails, LACP detects the loss of LACPDUs within seconds and removes that link from the bundle, redistributing traffic across the surviving links.

You might wonder how traffic is distributed across the bundled links. The switch uses a **hashing algorithm** that takes some combination of source and destination MAC addresses, IP addresses, or TCP/UDP port numbers and maps each flow to a specific link in the bundle. The key word is *flow*: all packets belonging to the same conversation (same source-destination pair) always travel over the same physical link, preserving packet ordering. This means link aggregation does not speed up any single flow — a single TCP connection still maxes out at the speed of one physical link. The throughput benefit comes from having *many* flows that distribute across all the links. If traffic is dominated by one large flow, most of the bundle's bandwidth goes unused.

The relationship to **Spanning Tree Protocol (STP)** is worth understanding. STP's job is to prevent loops by blocking redundant links — but link aggregation creates what looks like a redundant path. The key distinction is that STP sees the LAG as a single logical link, not multiple parallel links, so it does not block any of the member ports. This is one of the main reasons link aggregation is preferred over simply adding parallel links: it provides both extra bandwidth and redundancy without triggering STP's loop-prevention blocking. If one physical link in the bundle fails, the logical link remains up (at reduced bandwidth) and no STP reconvergence is needed — traffic simply redistributes across the remaining member links within seconds.
