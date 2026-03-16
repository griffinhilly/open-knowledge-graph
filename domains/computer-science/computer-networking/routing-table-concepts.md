---
id: routing-table-concepts
title: Routing Table Concepts
domain: computer-science
course: computer-networking
prerequisites:
- id: ip-routing-basics
  type: hard
builds-toward:
- distance-vector-routing-protocols
- link-state-routing-protocols
tags:
- routing-table
- route-lookup
- next-hop
- longest-prefix-match
stage: advanced
status: draft
---

# Routing Table Concepts

## Core Idea
A routing table maps destination addresses to outgoing interfaces and next-hop addresses. Routers use longest-prefix matching to find the most specific route for each packet destination. Efficient routing table lookup requires data structures like tries or hash tables to handle millions of routes at line-rate speeds.

## Explainer

From IP routing basics, you know that routers forward packets hop by hop toward their destinations. The routing table is the data structure that makes each forwarding decision possible — it is essentially the router's map of the network. Each entry in the table says: "To reach this destination network, send the packet out this interface to this next-hop address." When a packet arrives, the router extracts the destination IP address from the header and consults the table to decide where to send it next.

A routing table entry typically contains several fields: the **destination network** (expressed as a prefix like 192.168.1.0/24), the **next-hop address** (the IP of the neighboring router that gets the packet closer to its destination), the **outgoing interface** (which physical or logical port to use), a **metric** (a cost value used to compare routes), and the **route source** (how the router learned this route — directly connected, statically configured, or via a routing protocol). Routes learned from different sources carry different levels of trust, expressed as **administrative distance** — a directly connected network is more trustworthy than a route learned from an external routing protocol, so it takes priority if both claim to reach the same destination.

The key algorithm that makes routing tables work is **longest-prefix match**. When a router looks up destination 192.168.1.50, it might find two matching entries: 192.168.0.0/16 (a broad route covering the entire 192.168.x.x range) and 192.168.1.0/24 (a more specific route covering just the 192.168.1.x subnet). The router always chooses the longest prefix — the /24 in this case — because a more specific route represents more precise knowledge about where that traffic should go. This is analogous to mailing a letter: if you know both "somewhere in New York State" and "123 Main Street, Buffalo, NY," you use the more specific address. The **default route** (0.0.0.0/0) is the shortest possible prefix and matches everything — it is the route of last resort when no more specific entry exists.

Routing tables are populated through three mechanisms. **Directly connected routes** are added automatically when an interface is configured with an IP address. **Static routes** are manually configured by an administrator — useful for simple networks or specific policy overrides. **Dynamic routes** are learned from routing protocols like OSPF or BGP, which exchange reachability information with neighboring routers and automatically update the table as network topology changes. In a large network, the routing table may contain hundreds of thousands of entries, and the router must perform a lookup for every single packet at line rate — potentially millions of lookups per second. This is why efficient data structures like **tries** (prefix trees) are used in hardware, allowing the longest-prefix match to complete in a fixed number of memory accesses regardless of table size.
