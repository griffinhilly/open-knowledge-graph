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
