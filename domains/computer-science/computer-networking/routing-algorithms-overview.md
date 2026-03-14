---
id: routing-algorithms-overview
title: Routing Algorithms and Protocols
domain: computer-science
course: computer-networking
prerequisites:
- id: ip-routing-basics
  type: hard
builds-toward:
- dijkstras-shortest-path-routing
- bellman-ford-distance-vector-routing
- ospf-open-shortest-path-first
tags:
- routing-algorithms
- protocols
- distance-vector
- link-state
stage: advanced
status: draft
---

# Routing Algorithms and Protocols

## Core Idea
Routing algorithms compute paths through a network to reach destination addresses. Distance-vector algorithms (e.g., RIP) share distances to known destinations with neighbors; link-state algorithms (e.g., OSPF) flood the entire network topology to all routers. Each approach has tradeoffs in convergence time, overhead, and scalability.

## How It's Best Learned
Simulate both distance-vector and link-state protocols in a network simulator; observe how each converges after topology changes.

## Common Misconceptions
- All routing algorithms find globally optimal paths; distributed algorithms converge to locally good paths.
- Distance-vector converges faster than link-state; link-state typically converges faster despite higher overhead.
