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

## Questions

```yaml
- question: "500 hosts are receiving a multicast video stream. A link in the distribution tree connects a router to two downstream routers, each of which has receivers. How many copies of each packet travel over that link?"
  type: multiple-choice
  options:
    - "500 copies — one per receiver reachable through that link"
    - "Two copies — one per downstream router"
    - "One copy — the downstream router receiving it will duplicate the packet toward its own branches"
    - "Zero copies — multicast packets are never forwarded over internal links"
  answer: 2
  explanation: "This is the core efficiency of multicast: each link carries at most one copy of each packet. The router at the branching point receives one copy and replicates it only there — sending one copy down each outgoing branch. Traffic on the link equals one copy regardless of how many receivers sit downstream. If each receiver required its own stream, this single link would carry 500 copies (or however many receivers are downstream), wasting orders of magnitude more bandwidth."

- question: "A large enterprise WAN has thousands of routers but only 50 hosts subscribed to a particular multicast group. Which PIM mode is appropriate, and why?"
  type: multiple-choice
  options:
    - "PIM Dense Mode, because flooding reaches all 50 receivers immediately without requiring them to join explicitly"
    - "PIM Sparse Mode, because receivers are spread thinly and explicit join messages ensure traffic flows only to paths where receivers actually exist"
    - "PIM Dense Mode, because shared trees use less state than source-specific trees"
    - "Neither mode; multicast cannot function across a WAN"
  answer: 1
  explanation: "PIM-SM is designed for exactly this scenario. 'Sparse' refers to the density of receivers relative to the total network — 50 receivers among thousands of routers is very sparse. Explicit join messages propagate only toward receivers who request traffic, so the vast majority of routers never see the multicast traffic. PIM-DM would flood the entire network first and then prune, which wastes bandwidth proportional to network size. Option C mistakes the tree types — sparse mode can use both shared trees and source-specific trees."

- question: "In PIM Sparse Mode, a multicast session begins with traffic flowing via the rendezvous point, but can later switch to a source-specific tree once active traffic is detected."
  type: true-false
  answer: true
  explanation: "PIM-SM's two-phase design is intentional. The rendezvous point provides a common meeting place for sources and receivers with low setup cost, before anyone knows whether the stream will even be used. Once traffic flows and the receiver's router detects it, it can send a Join directly toward the source, cutting out the rendezvous point for a shorter, more efficient path. This balances setup simplicity against long-term efficiency."

- question: "PIM (Protocol Independent Multicast) runs its own separate routing algorithm to compute the network topology for building multicast distribution trees."
  type: true-false
  answer: false
  explanation: "The 'Protocol Independent' in PIM is a direct statement that it does NOT run its own routing algorithm. Instead, PIM consults whatever unicast routing table is already populated by OSPF, BGP, or another protocol, and uses those routes to determine the reverse-path toward the source. This is why PIM can be deployed on top of any unicast routing infrastructure without replacing it — a key design advantage."

- question: "Explain how multicast routing reduces bandwidth compared to individual unicast streams, and where packet duplication actually occurs."
  type: short-answer
  answer: "With unicast, the source sends N separate copies — one per receiver — so any link on the path to all receivers carries N copies. With multicast, the source sends one copy into the network, and routers replicate it only at branching points in the distribution tree where the tree forks toward different receivers. Each link carries at most one copy. Duplication happens only where necessary, at the router where two or more downstream branches diverge. The result is O(1) packets per link rather than O(N) at the source."
  explanation: "The bandwidth reduction is most dramatic when many receivers share a common upstream path. In the lecture-streaming example, a single campus backbone link carries one copy regardless of whether 5 or 5,000 students are watching. Without multicast, that link would carry 5,000 copies. The tree structure ensures minimum replication: each link and each router does only the work that is strictly necessary to reach its downstream receivers."
```

## Explainer

Imagine a university lecture being streamed to 500 students across campus. A naive approach would have the server send 500 identical copies of each video packet — one per student. This wastes enormous bandwidth because the same data travels over the same links many times. **Multicast routing** solves this by having routers duplicate packets only at branching points in the network, so each link carries at most one copy of any given packet. The result is a tree-shaped distribution path from sender to all receivers, using a fraction of the bandwidth that 500 individual streams would require.

The foundation of multicast routing is the concept of a **multicast distribution tree**. You already know from routing algorithms that routers build paths through a network; multicast extends this by building trees that branch toward groups of receivers rather than single destinations. There are two main tree types. A **source-specific tree** (or shortest-path tree) is rooted at the sender, with branches reaching every group member via the shortest path from that particular source. A **shared tree** uses a designated rendezvous point as the root, and all sources send to this common root, which then distributes down the shared branches. Source-specific trees are more efficient per-source but require more state in routers; shared trees use less state but may route packets along suboptimal paths.

**Protocol Independent Multicast (PIM)** is the dominant multicast routing protocol, and its name reveals its key design choice: it does not run its own unicast routing algorithm. Instead, PIM piggybacks on whatever unicast routing protocol is already deployed (OSPF, BGP, etc.) to determine the topology. PIM operates in two primary modes. **PIM Sparse Mode (PIM-SM)** assumes receivers are spread thinly across the network and uses explicit join messages — receivers must actively request to join a group, and traffic flows only where it has been requested. **PIM Dense Mode (PIM-DM)** assumes most routers want the traffic and floods it everywhere initially, then prunes branches where no receivers exist. Sparse mode is far more common in practice because most multicast groups have a small number of receivers relative to the total network size.

The lifecycle of a PIM-SM multicast session illustrates how these pieces fit together. When a host wants to receive a multicast group, it signals its local router using IGMP (your prerequisite). That router sends a PIM Join message toward the rendezvous point, and each router along the path installs forwarding state for that group. Initially, traffic flows through the shared tree via the rendezvous point. Once the receiver's router detects actual traffic, it can optionally switch to a source-specific tree by sending a Join directly toward the source, bypassing the rendezvous point for a shorter path. This two-phase approach balances the low setup cost of shared trees with the efficiency of source-specific trees once traffic is flowing.

Understanding multicast routing matters beyond video streaming. Financial market data feeds, software update distribution, and multiplayer gaming all benefit from multicast's bandwidth efficiency. The core insight is that multicast transforms a one-to-many communication problem from O(n) copies at the source into O(1) per link, with duplication happening only at the minimum number of branching points needed to reach all receivers.
