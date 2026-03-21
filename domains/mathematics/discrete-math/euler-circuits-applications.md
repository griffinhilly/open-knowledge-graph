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

## Questions

```yaml
- question: "A connected road network has every intersection at even degree except two: the library and the post office. What can be concluded about Euler paths and circuits in this network?"
  type: multiple-choice
  options:
    - "An Euler circuit exists starting and ending at any intersection."
    - "An Euler path exists from the library to the post office, but no Euler circuit exists."
    - "An Euler path exists between any two odd-degree vertices, not just the library and post office."
    - "Neither an Euler path nor an Euler circuit exists because there are vertices with odd degree."
  answer: 1
  explanation: "Exactly two odd-degree vertices is the precise condition for an Euler path — and the path must start at one odd-degree vertex and end at the other. Since the two odd-degree vertices are the library and post office, an Euler path connects them. No Euler circuit exists because a circuit requires *all* even-degree vertices. Option D is wrong because odd-degree vertices don't prevent an Euler path — they just determine its endpoints."

- question: "In the Chinese postman problem, a mail carrier must traverse every street at least once and return to the start. The route graph has four vertices with odd degree. Why must the carrier repeat some streets?"
  type: multiple-choice
  options:
    - "Postal regulations require redundancy on high-traffic routes."
    - "Odd-degree vertices make a closed walk that covers all edges exactly once impossible; repeating selected edges converts odd-degree vertices to even, restoring the Euler circuit condition."
    - "The carrier prefers to avoid backtracking, so skipping streets is unavoidable."
    - "Eulerian conditions apply only to directed graphs, not street networks."
  answer: 1
  explanation: "An Euler circuit exists only when all vertices have even degree. With four odd-degree vertices, no closed walk can cover all edges exactly once. The solution is to add repeated traversals of certain edges to pair up odd-degree vertices — making their effective degree even. The optimal solution minimizes total repeated distance, which is a minimum-weight perfect matching on the odd-degree vertices. Without any repetition, an Euler circuit simply cannot exist."

- question: "If a connected graph has exactly two vertices with odd degree, an Euler path must start at one of those odd-degree vertices and end at the other."
  type: true-false
  answer: true
  explanation: "This is exact. An Euler path requires visiting every edge exactly once without backtracking to the start. A vertex 'uses up' two edges per internal visit (one in, one out), so it needs even degree to be traversable without getting stuck. The two odd-degree vertices must be endpoints: one is left first (degree contributes one unmatched outgoing edge) and one is arrived at last (one unmatched incoming edge). Starting or ending at any other vertex would violate the degree parity."

- question: "The Königsberg bridge problem has no Euler circuit because the graph is disconnected."
  type: true-false
  answer: false
  explanation: "The Königsberg graph is connected — all landmasses are reachable from each other via bridges. The reason no Euler circuit (or even Euler path) exists is that the graph has *four* odd-degree vertices. An Euler circuit requires all even-degree vertices; an Euler path allows exactly two. With four odd-degree vertices, neither condition is met. Euler's 1736 proof identified degree parity — not connectivity — as the decisive structural property."

- question: "Why does satisfying the degree-parity condition guarantee the existence of an Euler circuit in a connected graph, rather than merely being a necessary condition for it?"
  type: short-answer
  answer: "The degree condition is both necessary and sufficient. If every vertex has even degree in a connected graph, Hierholzer's algorithm can always construct an Euler circuit: start anywhere, follow any available edge, and continue until returning to the start. Because every vertex has even degree, you can never get trapped at an intermediate vertex — every entry into a vertex has a corresponding exit. If unvisited edges remain, splice in a new subcircuit starting from the nearest vertex with unvisited edges. The algorithm terminates with all edges visited exactly once."
  explanation: "The key is that even degree prevents 'getting stuck': since each visit to a vertex uses one edge in and one edge out, a vertex with even degree always has a way out whenever you enter it. The only exception is the starting vertex, which you exit first and return to last — but that's exactly the definition of a circuit. The sufficiency proof is constructive, which is why we know the condition isn't just necessary — it actively enables the construction."
```

## Explainer

The historical starting point is the Königsberg bridge problem: seven bridges crossed the branches of the Pregel River, and citizens wondered whether they could walk through the city crossing each bridge exactly once and return to their starting point. Euler proved it was impossible in 1736 — and in doing so, invented graph theory. His insight was to model the landmasses as vertices and the bridges as edges, then ask a purely structural question about the graph.

The answer hinges entirely on **vertex degree**. When you enter a vertex through an edge, you must leave through a different edge — so each visit to a vertex uses up two edges (one in, one out). This means an **Euler circuit** (a closed walk covering every edge exactly once) can only exist if every vertex has even degree: no vertex can be "stuck" with an edge entering that has no matching exit. Conversely, an **Euler path** (which may start and end at different vertices) can tolerate exactly two odd-degree vertices — the start (which you leave first) and the end (which you enter last). The Königsberg graph has four odd-degree vertices, so neither an Euler path nor an Euler circuit exists.

These are if-and-only-if conditions, not just necessary ones. If a connected graph has all even degrees, an Euler circuit is guaranteed to exist, and **Hierholzer's algorithm** constructs one efficiently: start anywhere, follow edges (avoiding bridges when possible) until you return to the start, then splice in detours through any unvisited edges. The algorithm runs in O(E) time. The conditions you learned in the prerequisite topic (Euler paths/circuits) are applied here: first check degrees to determine existence, then construct if possible.

Real-world applications make the abstraction concrete. The **Chinese postman problem** asks a mail carrier to traverse every street at least once and return to the starting point with minimum total distance. In graph terms: if the graph already has an Euler circuit, the carrier just follows it. If some vertices have odd degree, the carrier must repeat certain edges — the optimal solution adds repeated edges to pair up odd-degree vertices at minimum cost, effectively restoring the all-even-degree condition. Similar problems arise in circuit board testing (probing every connector), DNA fragment assembly, and route planning for autonomous vehicles.
