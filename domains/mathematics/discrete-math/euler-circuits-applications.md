---
id: euler-circuits-applications
title: Euler Paths, Euler Circuits, and Applications
domain: mathematics
course: discrete-math
prerequisites:
- id: euler-paths-circuits
  type: hard
builds-toward:
- hamiltonian-cycles-discrete
tags:
- Euler-path
- Euler-circuit
- degree
- Chinese-postman
stage: formal-systems
status: draft
---

# Euler Paths, Euler Circuits, and Applications

## Core Idea
An Euler path visits every edge exactly once; an Euler circuit closes back to its start. A connected graph has an Euler circuit iff all vertices have even degree; an Euler path exists iff exactly 0 or 2 vertices have odd degree. The Chinese postman problem seeks a shortest walk covering all edges.

## How It's Best Learned
Check degree conditions to determine Euler path/circuit existence before searching. Construct Euler circuits using Hierholzer's algorithm. Apply to street traversal (postman, parade routes) and circuit design.

## Common Misconceptions
Euler paths traverse edges, not vertices. A graph can have many Euler paths/circuits if the conditions hold. The bridge-crossing puzzle (Königsberg) famously has no Euler circuit.

## Explainer

The historical starting point is the Königsberg bridge problem: seven bridges crossed the branches of the Pregel River, and citizens wondered whether they could walk through the city crossing each bridge exactly once and return to their starting point. Euler proved it was impossible in 1736 — and in doing so, invented graph theory. His insight was to model the landmasses as vertices and the bridges as edges, then ask a purely structural question about the graph.

The answer hinges entirely on **vertex degree**. When you enter a vertex through an edge, you must leave through a different edge — so each visit to a vertex uses up two edges (one in, one out). This means an **Euler circuit** (a closed walk covering every edge exactly once) can only exist if every vertex has even degree: no vertex can be "stuck" with an edge entering that has no matching exit. Conversely, an **Euler path** (which may start and end at different vertices) can tolerate exactly two odd-degree vertices — the start (which you leave first) and the end (which you enter last). The Königsberg graph has four odd-degree vertices, so neither an Euler path nor an Euler circuit exists.

These are if-and-only-if conditions, not just necessary ones. If a connected graph has all even degrees, an Euler circuit is guaranteed to exist, and **Hierholzer's algorithm** constructs one efficiently: start anywhere, follow edges (avoiding bridges when possible) until you return to the start, then splice in detours through any unvisited edges. The algorithm runs in O(E) time. The conditions you learned in the prerequisite topic (Euler paths/circuits) are applied here: first check degrees to determine existence, then construct if possible.

Real-world applications make the abstraction concrete. The **Chinese postman problem** asks a mail carrier to traverse every street at least once and return to the starting point with minimum total distance. In graph terms: if the graph already has an Euler circuit, the carrier just follows it. If some vertices have odd degree, the carrier must repeat certain edges — the optimal solution adds repeated edges to pair up odd-degree vertices at minimum cost, effectively restoring the all-even-degree condition. Similar problems arise in circuit board testing (probing every connector), DNA fragment assembly, and route planning for autonomous vehicles.
