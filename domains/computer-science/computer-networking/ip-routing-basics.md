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

## Questions

```yaml
- question: "A router receives a packet destined for 10.5.3.7. Its routing table has three matching entries: 10.0.0.0/8, 10.5.0.0/16, and 10.5.3.0/24. Which entry does the router use?"
  type: multiple-choice
  options:
    - "10.0.0.0/8, because it is the broadest match and ensures the packet reaches the right general network"
    - "10.5.0.0/16, as the middle-specificity entry provides a balanced forwarding decision"
    - "10.5.3.0/24, because it is the longest (most specific) prefix that matches the destination"
    - "The router floods the packet on all interfaces since multiple entries match simultaneously"
  answer: 2
  explanation: "IP routing uses longest-prefix match: the entry with the most bits in the prefix that still matches the destination wins. All three entries match 10.5.3.7, but the /24 has 24 matching prefix bits versus /16 with 16 and /8 with 8. The router always uses the most specific matching entry. This rule is what makes Internet routing scalable — routers aggregate millions of addresses into short-prefix entries and only maintain longer, more specific entries where finer-grained routing is needed."

- question: "A packet is traveling from New York to Tokyo across the Internet, passing through a router in Los Angeles. What does the LA router know about the complete path to Tokyo?"
  type: multiple-choice
  options:
    - "It has a full routing map showing all 10–15 hops to Tokyo, which it uses to select the optimal complete path"
    - "It knows only the best next hop toward Tokyo — which neighboring router to forward the packet to — and nothing about the path beyond that"
    - "It broadcasts the packet to all connected neighbors and lets them compete to determine the next hop"
    - "It must first query Tokyo to establish the full path before forwarding any packets"
  answer: 1
  explanation: "IP routing is hop-by-hop: each router makes an independent, local decision based solely on its own routing table, forwarding to the single best next hop without knowing or storing any information about the complete path. The LA router has no global map; it simply consults its table, finds the best next-hop for the Tokyo-bound destination prefix, and forwards. That router repeats the process, and so on. This stateless, local decision-making at each hop is what makes the Internet scalable — no router needs global knowledge."

- question: "A router's default route (0.0.0.0/0) is used only when no other routing table entry matches the destination, because it has the shortest possible prefix."
  type: true-false
  answer: true
  explanation: "The default route has a prefix length of zero, meaning it technically matches every IP address. But because longest-prefix match always prefers more specific entries, the default route is selected only when no other entry matches. This makes it a catch-all 'last resort' entry — traffic that doesn't match any specific prefix gets forwarded toward the default gateway (typically toward the broader Internet). Home routers typically have just one real routing entry: a default route pointing to the ISP's gateway."

- question: "Dynamic routing protocols like OSPF allow routers to compute and store the full end-to-end path to each destination network, which they then follow when forwarding packets."
  type: true-false
  answer: false
  explanation: "Dynamic routing protocols allow routers to exchange reachability information and build routing tables — mappings from destination prefixes to next-hop addresses — but not full end-to-end paths. When forwarding a packet, each router still makes a purely local, hop-by-hop decision: 'which of my neighbors is the best next hop for this destination prefix?' The complete Internet path is an emergent property of many independent per-hop decisions. No single router knows or stores the full path."

- question: "Why does the Internet use longest-prefix match routing rather than exact-IP-address matching, and what fundamental Internet design property does this enable?"
  type: short-answer
  answer: "Exact-address matching would require a routing table entry for every individual IP address — billions of entries per router, which is completely infeasible. Longest-prefix match allows a single routing entry to represent an entire address block (e.g., 192.168.0.0/16 covers 65,536 addresses). Routers can aggregate many specific addresses into summarizing prefixes, maintaining only more specific entries where finer-grained routing is needed. This hierarchical aggregation is what makes Internet routing scalable: backbone routers maintain routing tables with hundreds of thousands of prefixes, not billions of individual host addresses."
  explanation: "Students who think routing works like a phone book (one entry per host) haven't grasped the key insight. The IP address hierarchy combined with longest-prefix match is the architectural mechanism that makes the Internet scale — without it, the routing system would collapse under the weight of billions of individual entries."
```

## Explainer

From your knowledge of IPv4 addressing and subnetting with CIDR notation, you understand that IP addresses are structured hierarchically and that networks are identified by prefixes of varying length. **IP routing** is the mechanism that uses this hierarchical structure to forward packets across interconnected networks from source to destination. Every router along the path makes an independent forwarding decision based on its own local **routing table** — no single device knows or controls the entire path.

A **routing table** is essentially a lookup table mapping destination IP prefixes to **next-hop** addresses and **outgoing interfaces**. When a packet arrives at a router, the router examines the destination IP address in the packet header and searches its routing table for matching entries. The critical rule is **longest-prefix match**: if the destination 192.168.5.42 matches both 192.168.0.0/16 (a broad match) and 192.168.5.0/24 (a more specific match), the router uses the /24 entry because it has the longer prefix and therefore provides more specific routing information. This is what makes Internet routing scalable — routers do not need an entry for every individual IP address. They can aggregate millions of addresses into a single prefix and only maintain specific entries where finer-grained routing is needed.

The forwarding process at each router is purely local and **hop-by-hop**. A router does not compute or store the complete path to the destination. It simply determines the best next hop — the neighboring router (or the destination itself, if directly connected) — and forwards the packet to that neighbor. That neighbor then repeats the same process using its own routing table. The packet hops from router to router until it reaches a router that is directly connected to the destination's subnet. This is analogous to asking for driving directions at each intersection rather than planning the entire route upfront. Each router only needs to know the best direction to send traffic for each destination prefix.

Routing tables are populated through two mechanisms. **Static routes** are manually configured by network administrators and are appropriate for simple, stable topologies. **Dynamic routing protocols** (like OSPF, BGP, and RIP) allow routers to exchange information about which networks they can reach, automatically building and updating routing tables as the network topology changes. When a link fails, dynamic routing protocols detect the change and recalculate paths, enabling the network to route around the failure. A special entry called the **default route** (0.0.0.0/0) matches any destination that does not have a more specific match — it is the "if all else fails, send it this way" entry, typically pointing toward the broader Internet. Home routers usually have just one real routing entry: a default route pointing to the ISP's gateway.
