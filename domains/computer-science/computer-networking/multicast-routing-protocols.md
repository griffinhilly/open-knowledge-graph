---
id: multicast-routing-protocols
title: Multicast Routing Protocols
domain: computer-science
course: computer-networking
prerequisites:
- id: igmp-internet-group-management
  type: hard
- id: routing-algorithms-overview
  type: hard
tags:
- multicast
- pim
- routing
- group-communication
stage: advanced
status: draft
---

# Multicast Routing Protocols

## Core Idea
Multicast routing forwards packets from a sender to all members of a group using minimal spanning trees, avoiding unnecessary duplication. Protocol Independent Multicast (PIM) is a widely deployed multicast routing protocol that supports both source-specific and shared trees. Multicast is essential for bandwidth-efficient delivery of video, audio, and other one-to-many applications.

## Explainer

Imagine a university lecture being streamed to 500 students across campus. A naive approach would have the server send 500 identical copies of each video packet — one per student. This wastes enormous bandwidth because the same data travels over the same links many times. **Multicast routing** solves this by having routers duplicate packets only at branching points in the network, so each link carries at most one copy of any given packet. The result is a tree-shaped distribution path from sender to all receivers, using a fraction of the bandwidth that 500 individual streams would require.

The foundation of multicast routing is the concept of a **multicast distribution tree**. You already know from routing algorithms that routers build paths through a network; multicast extends this by building trees that branch toward groups of receivers rather than single destinations. There are two main tree types. A **source-specific tree** (or shortest-path tree) is rooted at the sender, with branches reaching every group member via the shortest path from that particular source. A **shared tree** uses a designated rendezvous point as the root, and all sources send to this common root, which then distributes down the shared branches. Source-specific trees are more efficient per-source but require more state in routers; shared trees use less state but may route packets along suboptimal paths.

**Protocol Independent Multicast (PIM)** is the dominant multicast routing protocol, and its name reveals its key design choice: it does not run its own unicast routing algorithm. Instead, PIM piggybacks on whatever unicast routing protocol is already deployed (OSPF, BGP, etc.) to determine the topology. PIM operates in two primary modes. **PIM Sparse Mode (PIM-SM)** assumes receivers are spread thinly across the network and uses explicit join messages — receivers must actively request to join a group, and traffic flows only where it has been requested. **PIM Dense Mode (PIM-DM)** assumes most routers want the traffic and floods it everywhere initially, then prunes branches where no receivers exist. Sparse mode is far more common in practice because most multicast groups have a small number of receivers relative to the total network size.

The lifecycle of a PIM-SM multicast session illustrates how these pieces fit together. When a host wants to receive a multicast group, it signals its local router using IGMP (your prerequisite). That router sends a PIM Join message toward the rendezvous point, and each router along the path installs forwarding state for that group. Initially, traffic flows through the shared tree via the rendezvous point. Once the receiver's router detects actual traffic, it can optionally switch to a source-specific tree by sending a Join directly toward the source, bypassing the rendezvous point for a shorter path. This two-phase approach balances the low setup cost of shared trees with the efficiency of source-specific trees once traffic is flowing.

Understanding multicast routing matters beyond video streaming. Financial market data feeds, software update distribution, and multiplayer gaming all benefit from multicast's bandwidth efficiency. The core insight is that multicast transforms a one-to-many communication problem from O(n) copies at the source into O(1) per link, with duplication happening only at the minimum number of branching points needed to reach all receivers.
