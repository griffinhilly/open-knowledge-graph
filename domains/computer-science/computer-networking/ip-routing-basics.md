---
id: ip-routing-basics
title: IP Routing and Forwarding
domain: computer-science
course: computer-networking
prerequisites:
- id: ipv4-addressing
  type: hard
- id: subnetting-and-cidr-notation
  type: hard
builds-toward:
- routing-algorithms-overview
tags:
- routing
- forwarding
- routing-table
- hop
stage: advanced
status: draft
---

# IP Routing and Forwarding

## Core Idea
IP routing is the process by which routers forward packets toward their destination based on routing tables that map destination IP prefixes to outgoing interfaces and next-hop addresses. Routers use longest-prefix-match lookup to select the most specific matching route, enabling hierarchical routing and Internet scalability.

## How It's Best Learned
Examine routing tables using `route -n` (Linux) or `route print` (Windows); trace packet routes with `traceroute` to visualize multi-hop paths.

## Common Misconceptions
- Routers look up the exact destination IP; they match the longest matching prefix.
- Routers know the full path to the destination; they only forward to the next hop.

## Explainer

From your knowledge of IPv4 addressing and subnetting with CIDR notation, you understand that IP addresses are structured hierarchically and that networks are identified by prefixes of varying length. **IP routing** is the mechanism that uses this hierarchical structure to forward packets across interconnected networks from source to destination. Every router along the path makes an independent forwarding decision based on its own local **routing table** — no single device knows or controls the entire path.

A **routing table** is essentially a lookup table mapping destination IP prefixes to **next-hop** addresses and **outgoing interfaces**. When a packet arrives at a router, the router examines the destination IP address in the packet header and searches its routing table for matching entries. The critical rule is **longest-prefix match**: if the destination 192.168.5.42 matches both 192.168.0.0/16 (a broad match) and 192.168.5.0/24 (a more specific match), the router uses the /24 entry because it has the longer prefix and therefore provides more specific routing information. This is what makes Internet routing scalable — routers do not need an entry for every individual IP address. They can aggregate millions of addresses into a single prefix and only maintain specific entries where finer-grained routing is needed.

The forwarding process at each router is purely local and **hop-by-hop**. A router does not compute or store the complete path to the destination. It simply determines the best next hop — the neighboring router (or the destination itself, if directly connected) — and forwards the packet to that neighbor. That neighbor then repeats the same process using its own routing table. The packet hops from router to router until it reaches a router that is directly connected to the destination's subnet. This is analogous to asking for driving directions at each intersection rather than planning the entire route upfront. Each router only needs to know the best direction to send traffic for each destination prefix.

Routing tables are populated through two mechanisms. **Static routes** are manually configured by network administrators and are appropriate for simple, stable topologies. **Dynamic routing protocols** (like OSPF, BGP, and RIP) allow routers to exchange information about which networks they can reach, automatically building and updating routing tables as the network topology changes. When a link fails, dynamic routing protocols detect the change and recalculate paths, enabling the network to route around the failure. A special entry called the **default route** (0.0.0.0/0) matches any destination that does not have a more specific match — it is the "if all else fails, send it this way" entry, typically pointing toward the broader Internet. Home routers usually have just one real routing entry: a default route pointing to the ISP's gateway.
