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
status: draft
---

# Route Aggregation and Supernetting

## Core Idea
Route aggregation combines multiple routing table entries with consecutive CIDR blocks into a single entry with a shorter prefix, reducing routing table size. For example, 192.168.0.0/24 and 192.168.1.0/24 can be aggregated as 192.168.0.0/23. Aggregation is essential for scaling the Internet; without it, routing tables would contain billions of entries.

## Explainer

From your work with subnetting and CIDR notation, you know that IP addresses are divided into a network prefix and a host portion, and that the prefix length determines the size of the address block. Subnetting splits a larger block into smaller ones by extending the prefix — moving the boundary rightward. **Route aggregation** (also called **supernetting**) is the reverse operation: it combines multiple smaller, contiguous blocks into a single larger block by shortening the prefix — moving the boundary leftward.

Consider a concrete example. An organization has been assigned four /24 networks: 10.1.0.0/24, 10.1.1.0/24, 10.1.2.0/24, and 10.1.3.0/24. Without aggregation, the upstream router must maintain four separate routing table entries. But look at the binary representations of the third octet: 00, 01, 10, 11. The first 22 bits of all four addresses are identical (10.1.0.0 through 10.1.3.255). So the upstream router can advertise a single route: 10.1.0.0/22. Any packet destined for any address in that range gets forwarded the same way. Four entries collapse into one.

The mathematical requirement is that aggregation only works cleanly when the blocks are **contiguous and aligned**. You cannot aggregate 10.1.1.0/24 and 10.1.3.0/24 into a single prefix because 10.1.2.0/24 sits between them — a shorter prefix covering both would also cover 10.1.0.0/24 and 10.1.2.0/24, potentially attracting traffic not meant for your network. This is why careful IP address planning matters: organizations that allocate addresses from contiguous CIDR blocks can aggregate cleanly, while fragmented allocations resist aggregation and bloat the global routing table.

The stakes are real. The global Internet routing table (carried by BGP between autonomous systems) currently holds over a million entries. Every router in the default-free zone must store and search this table for every packet. Without aggregation, the table would be orders of magnitude larger — one entry per individual network instead of one per aggregated block. ISPs perform aggregation hierarchically: customer routes are aggregated at the edge, regional routes are aggregated at the backbone, and the result is a routing table that remains manageable despite the Internet's explosive growth. The tradeoff is that overly aggressive aggregation can create **routing black holes** — if part of an aggregated block is actually unreachable, the aggregate route still attracts traffic to it, which then gets dropped. Operators must balance aggregation's scalability benefits against the precision of more specific routes.
