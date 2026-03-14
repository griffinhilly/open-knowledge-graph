---
id: bellman-ford-distance-vector-routing
title: Bellman-Ford Algorithm and Distance-Vector Routing
domain: computer-science
course: computer-networking
prerequisites:
- id: routing-algorithms-overview
  type: hard
- id: bellman-ford-algorithm
  type: hard
tags:
- bellman-ford
- distance-vector
- rip
- distributed-algorithm
stage: advanced
status: draft
---

# Bellman-Ford Algorithm and Distance-Vector Routing

## Core Idea
The Bellman-Ford algorithm is the basis for distance-vector routing protocols (e.g., RIP) where routers share their distance vectors (hop counts or costs) with direct neighbors. Each router updates its routing table based on neighbors' announcements, converging to shortest paths in a distributed manner, though more slowly than link-state protocols.
