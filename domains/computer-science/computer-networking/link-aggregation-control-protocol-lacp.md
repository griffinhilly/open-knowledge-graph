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
status: draft
---

# Link Aggregation Control Protocol (LACP)

## Core Idea
Link Aggregation Control Protocol (LACP, 802.3ad) enables multiple physical links to be bundled into a single logical link, increasing bandwidth and providing redundancy. LACP dynamically negotiates which links are active and handles failures by rebalancing traffic. Load balancing algorithms distribute frames based on source/destination MAC, IP addresses, or port numbers.

## How It's Best Learned
Configure LACP bonds on Linux (bonding driver) or switches. Observe LACP frame exchanges (PDUs) using tcpdump. Simulate link failures and measure failover time. Test different load-balancing algorithms and observe traffic distribution.

## Common Misconceptions
LACP requires both sides of the link to support it; one-sided aggregation (static LAG) is also common. LACP does not guarantee load balancing per flow; it distributes flows heuristically. Aggregation does not provide redundancy if all links share a common failure point.

## Explainer

From your study of Ethernet and switching, you know that a single Ethernet link between two switches has a fixed bandwidth — 1 Gbps, 10 Gbps, or whatever the physical medium supports. If you need more bandwidth between two switches, you could upgrade to a faster link, but that requires new hardware. **Link aggregation** offers an alternative: bundle multiple existing physical links into a single **logical link** (called a LAG, port channel, or bond) that appears to the rest of the network as one connection with the combined bandwidth. Four 1 Gbps links aggregated together provide up to 4 Gbps of aggregate throughput.

**LACP** (Link Aggregation Control Protocol, defined in IEEE 802.3ad) is the standard protocol for dynamically negotiating and maintaining these bundles. Without LACP, you could statically configure aggregation on both sides, but static configuration is fragile: if one side is misconfigured or a cable is plugged into the wrong port, traffic may be silently dropped or looped. LACP solves this by having the two sides exchange **LACPDUs** (LACP Data Units) — small control frames sent every second (or every 30 seconds in slow mode) that announce each port's identity, system priority, and aggregation key. Both sides use this information to agree on which ports belong to the aggregation group, automatically detecting mismatches and excluding incompatible ports. If a link fails, LACP detects the loss of LACPDUs within seconds and removes that link from the bundle, redistributing traffic across the surviving links.

You might wonder how traffic is distributed across the bundled links. The switch uses a **hashing algorithm** that takes some combination of source and destination MAC addresses, IP addresses, or TCP/UDP port numbers and maps each flow to a specific link in the bundle. The key word is *flow*: all packets belonging to the same conversation (same source-destination pair) always travel over the same physical link, preserving packet ordering. This means link aggregation does not speed up any single flow — a single TCP connection still maxes out at the speed of one physical link. The throughput benefit comes from having *many* flows that distribute across all the links. If traffic is dominated by one large flow, most of the bundle's bandwidth goes unused.

The relationship to **Spanning Tree Protocol (STP)** is worth understanding. STP's job is to prevent loops by blocking redundant links — but link aggregation creates what looks like a redundant path. The key distinction is that STP sees the LAG as a single logical link, not multiple parallel links, so it does not block any of the member ports. This is one of the main reasons link aggregation is preferred over simply adding parallel links: it provides both extra bandwidth and redundancy without triggering STP's loop-prevention blocking. If one physical link in the bundle fails, the logical link remains up (at reduced bandwidth) and no STP reconvergence is needed — traffic simply redistributes across the remaining member links within seconds.
