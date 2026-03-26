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
status: validated
---

# Routing Table Concepts

## Core Idea
A routing table maps destination addresses to outgoing interfaces and next-hop addresses. Routers use longest-prefix matching to find the most specific route for each packet destination. Efficient routing table lookup requires data structures like tries or hash tables to handle millions of routes at line-rate speeds.

## Questions

```yaml
- question: "A router has two entries: 10.0.0.0/8 (metric 5, via Router A) and 10.10.0.0/16 (metric 100, via Router B). A packet arrives for destination 10.10.5.3. Which route does the router use?"
  type: multiple-choice
  options:
    - "10.0.0.0/8 via Router A, because it has a lower metric (5 < 100)"
    - "10.10.0.0/16 via Router B, because it is the longest matching prefix"
    - "Both routes are used — the router load-balances across both"
    - "The default route, since neither entry is an exact match for 10.10.5.3"
  answer: 1
  explanation: "Longest-prefix match always takes priority over metric comparison. Both entries match 10.10.5.3 (/8 covers all 10.x.x.x, /16 covers 10.10.x.x), but the /16 is more specific. The router selects the longest prefix regardless of metric — metrics only matter when comparing routes of the same prefix length from different sources. Option A is the classic misconception: students often apply metrics as the primary decision criterion, but prefix length takes absolute priority."

- question: "What is the role of the default route (0.0.0.0/0) in a routing table?"
  type: multiple-choice
  options:
    - "It routes traffic to the local subnet when no other match exists"
    - "It matches all destination addresses and is selected only when no more specific route exists"
    - "It overrides all other routes because 0.0.0.0/0 has the highest administrative priority"
    - "It is only used for multicast traffic and does not affect unicast routing decisions"
  answer: 1
  explanation: "0.0.0.0/0 has the shortest possible prefix (zero bits must match), so it matches every possible destination address. But because longest-prefix match always selects the most specific entry, the default route loses to any more specific entry and is only used as a last resort when no other match exists. This is the opposite of how students often imagine it: longer (more specific) prefixes always win, so the very shortest prefix always loses in competition."

- question: "A router generally selects the route with the lowest metric when multiple entries match a destination address."
  type: true-false
  answer: false
  explanation: "False — the primary selection criterion is prefix length (specificity), not metric. The router first applies longest-prefix match: among all entries whose network address and mask match the destination, it selects the one with the most bits matching. Metrics are only consulted to break ties among routes with equal prefix lengths from different sources. A route with a higher metric but a longer prefix will always win over a shorter-prefix route with a lower metric."

- question: "Directly connected routes are automatically added to a routing table when a router interface is configured with an IP address."
  type: true-false
  answer: true
  explanation: "True. When a router interface is assigned an IP address (e.g., 192.168.1.1/24), the router automatically creates a routing table entry for the directly connected network (192.168.1.0/24) via that interface. These entries require no static configuration or routing protocol — the router simply knows its own subnets. This is why directly connected routes have the lowest administrative distance: the router has direct, first-hand knowledge of their reachability."

- question: "Explain why longest-prefix match is used in routing tables rather than simply selecting the first matching entry or the route with the best metric."
  type: short-answer
  answer: "Longest-prefix match ensures the most specific available route is used, corresponding to the most precise knowledge about where traffic should go. A broad route like 10.0.0.0/8 might be a general fallback, while 10.10.0.0/16 represents more specific information about a particular subnet — perhaps a direct path. Selecting the 'first match' would make routing dependent on entry insertion order, which is arbitrary. Selecting by metric alone would ignore the critical distinction between specific and general routes, potentially misrouting traffic to a less accurate path even when a better-targeted route exists."
  explanation: "The routing table encodes knowledge at multiple levels of specificity. A /24 entry represents more specific knowledge than a /8 entry — knowledge about a particular subnet rather than a broad address block. Longest-prefix match operationalizes the principle that more specific knowledge should take precedence. This allows general summary routes (aggregates) to coexist with specific subnet routes in the same table, enabling scalable hierarchical routing architecture."
```

## Explainer

From IP routing basics, you know that routers forward packets hop by hop toward their destinations. The routing table is the data structure that makes each forwarding decision possible — it is essentially the router's map of the network. Each entry in the table says: "To reach this destination network, send the packet out this interface to this next-hop address." When a packet arrives, the router extracts the destination IP address from the header and consults the table to decide where to send it next.

A routing table entry typically contains several fields: the **destination network** (expressed as a prefix like 192.168.1.0/24), the **next-hop address** (the IP of the neighboring router that gets the packet closer to its destination), the **outgoing interface** (which physical or logical port to use), a **metric** (a cost value used to compare routes), and the **route source** (how the router learned this route — directly connected, statically configured, or via a routing protocol). Routes learned from different sources carry different levels of trust, expressed as **administrative distance** — a directly connected network is more trustworthy than a route learned from an external routing protocol, so it takes priority if both claim to reach the same destination.

The key algorithm that makes routing tables work is **longest-prefix match**. When a router looks up destination 192.168.1.50, it might find two matching entries: 192.168.0.0/16 (a broad route covering the entire 192.168.x.x range) and 192.168.1.0/24 (a more specific route covering just the 192.168.1.x subnet). The router always chooses the longest prefix — the /24 in this case — because a more specific route represents more precise knowledge about where that traffic should go. This is analogous to mailing a letter: if you know both "somewhere in New York State" and "123 Main Street, Buffalo, NY," you use the more specific address. The **default route** (0.0.0.0/0) is the shortest possible prefix and matches everything — it is the route of last resort when no more specific entry exists.

Routing tables are populated through three mechanisms. **Directly connected routes** are added automatically when an interface is configured with an IP address. **Static routes** are manually configured by an administrator — useful for simple networks or specific policy overrides. **Dynamic routes** are learned from routing protocols like OSPF or BGP, which exchange reachability information with neighboring routers and automatically update the table as network topology changes. In a large network, the routing table may contain hundreds of thousands of entries, and the router must perform a lookup for every single packet at line rate — potentially millions of lookups per second. This is why efficient data structures like **tries** (prefix trees) are used in hardware, allowing the longest-prefix match to complete in a fixed number of memory accesses regardless of table size.
