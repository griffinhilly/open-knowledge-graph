---
id: route-aggregation-supernetting
title: Route Aggregation and Supernetting
domain: computer-science
course: computer-networking
prerequisites:
- id: subnetting-and-cidr-notation
  type: hard
builds-toward:
- bgp-border-gateway-protocol
tags:
- aggregation
- supernetting
- cidr
- routing-scalability
stage: advanced
status: validated
---

# Route Aggregation and Supernetting

## Core Idea
Route aggregation combines multiple routing table entries with consecutive CIDR blocks into a single entry with a shorter prefix, reducing routing table size. For example, 192.168.0.0/24 and 192.168.1.0/24 can be aggregated as 192.168.0.0/23. Aggregation is essential for scaling the Internet; without it, routing tables would contain billions of entries.

## Questions

```yaml
- question: "An ISP wants to aggregate four customer networks into a single route advertisement. The customers hold: 172.16.4.0/24, 172.16.5.0/24, 172.16.6.0/24, and 172.16.7.0/24. Which prefix correctly summarizes all four networks?"
  type: multiple-choice
  options:
    - "172.16.0.0/22 — a /22 starting at the class B base address"
    - "172.16.4.0/22 — a /22 starting at the first network address"
    - "172.16.4.0/21 — a /21 covering eight /24 networks"
    - "172.16.0.0/16 — the full class B block containing all four networks"
  answer: 1
  explanation: "172.16.4.0 in binary has third-octet 00000100; 172.16.7.0 has 00000111. The first 22 bits are identical across all four networks (the leading bits 000001 are constant in the third octet; only the last two bits vary from 00 to 11). So the aggregate is 172.16.4.0/22. Option A (172.16.0.0/22) covers 172.16.0.0–172.16.3.0, not the target networks. Option C (/21 from 172.16.4.0) is not /21-aligned — a valid /21 from 172.16.0.0 covers 172.16.0.0–172.16.7.0, eight networks including ones not belonging to this ISP. Option D is technically inclusive but far too broad."

- question: "A network operator aggregates routes for 10.0.0.0/24 through 10.0.7.0/24 into a single advertisement of 10.0.0.0/21. One subnet, 10.0.5.0/24, is later decommissioned and becomes unreachable. The operator continues advertising the aggregate. What is the likely result?"
  type: multiple-choice
  options:
    - "Routers automatically detect the unreachable subnet and stop forwarding traffic to it"
    - "Traffic destined for addresses in 10.0.5.0/24 is attracted by the aggregate route and then dropped, creating a routing black hole"
    - "The aggregate becomes invalid and is withdrawn by BGP automatically"
    - "Traffic to 10.0.5.0/24 is rerouted through alternative paths within the aggregate"
  answer: 1
  explanation: "This is the routing black hole problem. The aggregate 10.0.0.0/21 promises reachability for all 2048 addresses in that block. External routers forward traffic to the originating AS based on this advertisement. But inside the AS, 10.0.5.0/24 no longer exists — there is no specific route, and the traffic is dropped. The aggregate attracts the traffic but cannot deliver it. Solutions include withdrawing the aggregate, advertising a more-specific null route for the decommissioned prefix, or never advertising an aggregate without a specific backing route for every covered subnet."

- question: "Route aggregation reduces routing table size, which decreases the memory and lookup time required by routers handling Internet-scale traffic."
  type: true-false
  answer: true
  explanation: "True. This is the primary motivation for aggregation. Without it, each individual network would require a separate routing table entry — the global Internet routing table would contain billions of entries (one per customer network). Aggregation allows ISPs to advertise summary routes covering hundreds or thousands of customer networks in a single entry. The global BGP table currently holds over a million entries even with aggressive aggregation; without it, routing infrastructure would be untenable. Reduced table size also speeds up longest-prefix-match lookups, reducing forwarding latency."

- question: "Any two numerically adjacent /24 networks (e.g., 10.0.1.0/24 and 10.0.2.0/24) can always be aggregated into a single /23 prefix."
  type: true-false
  answer: false
  explanation: "False — adjacency is necessary but not sufficient; alignment is also required. A valid /23 must start on a /23 boundary (an address where bit 23 is 0 in the third octet). 10.0.0.0/24 and 10.0.1.0/24 are properly aligned and aggregate to 10.0.0.0/23. But 10.0.1.0/24 and 10.0.2.0/24 cannot form a valid /23 together: no single /23 covers exactly these two; any /23 covering 10.0.1.0 would cover 10.0.0.0, while any /23 covering 10.0.2.0 would cover 10.0.3.0. Alignment ensures the aggregate is a well-defined CIDR block."

- question: "Why does route aggregation require that component networks be both contiguous and properly aligned on a CIDR boundary, rather than simply contiguous?"
  type: short-answer
  answer: "A CIDR prefix describes a power-of-two block starting at an address divisible by its block size. Contiguity alone is insufficient because an arbitrary sequence of networks may not start on a valid CIDR boundary. For example, 10.0.1.0/24 and 10.0.2.0/24 are contiguous, but no valid /23 covers exactly these two — a /23 at 10.0.0.0 also includes 10.0.0.0/24, and a /23 at 10.0.2.0 also includes 10.0.3.0/24. Alignment ensures the aggregate prefix describes exactly the intended block without accidentally advertising reachability for addresses outside the aggregated range."
  explanation: "CIDR prefixes have a mathematical structure: a /n prefix covers a block of 2^(32-n) addresses starting at an address divisible by 2^(32-n). This power-of-two alignment means aggregation only works cleanly when networks were originally allocated from contiguous, aligned blocks — which is why IP address planning matters so much. ISPs that allocate from aligned blocks can aggregate cleanly; fragmented allocations resist aggregation and contribute to routing table bloat, which is a real and growing problem for Internet infrastructure."
```

## Explainer

From your work with subnetting and CIDR notation, you know that IP addresses are divided into a network prefix and a host portion, and that the prefix length determines the size of the address block. Subnetting splits a larger block into smaller ones by extending the prefix — moving the boundary rightward. **Route aggregation** (also called **supernetting**) is the reverse operation: it combines multiple smaller, contiguous blocks into a single larger block by shortening the prefix — moving the boundary leftward.

Consider a concrete example. An organization has been assigned four /24 networks: 10.1.0.0/24, 10.1.1.0/24, 10.1.2.0/24, and 10.1.3.0/24. Without aggregation, the upstream router must maintain four separate routing table entries. But look at the binary representations of the third octet: 00, 01, 10, 11. The first 22 bits of all four addresses are identical (10.1.0.0 through 10.1.3.255). So the upstream router can advertise a single route: 10.1.0.0/22. Any packet destined for any address in that range gets forwarded the same way. Four entries collapse into one.

The mathematical requirement is that aggregation only works cleanly when the blocks are **contiguous and aligned**. You cannot aggregate 10.1.1.0/24 and 10.1.3.0/24 into a single prefix because 10.1.2.0/24 sits between them — a shorter prefix covering both would also cover 10.1.0.0/24 and 10.1.2.0/24, potentially attracting traffic not meant for your network. This is why careful IP address planning matters: organizations that allocate addresses from contiguous CIDR blocks can aggregate cleanly, while fragmented allocations resist aggregation and bloat the global routing table.

The stakes are real. The global Internet routing table (carried by BGP between autonomous systems) currently holds over a million entries. Every router in the default-free zone must store and search this table for every packet. Without aggregation, the table would be orders of magnitude larger — one entry per individual network instead of one per aggregated block. ISPs perform aggregation hierarchically: customer routes are aggregated at the edge, regional routes are aggregated at the backbone, and the result is a routing table that remains manageable despite the Internet's explosive growth. The tradeoff is that overly aggressive aggregation can create **routing black holes** — if part of an aggregated block is actually unreachable, the aggregate route still attracts traffic to it, which then gets dropped. Operators must balance aggregation's scalability benefits against the precision of more specific routes.
