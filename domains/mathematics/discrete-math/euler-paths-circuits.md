---
id: euler-paths-circuits
title: Eulerian Paths, Circuits, and Characterization
domain: mathematics
course: discrete-math
prerequisites:
- id: walks-paths-cycles
  type: hard
- id: degree-sequences-graphs
  type: soft
builds-toward:
- hamiltonian-paths-cycles
tags:
- graph-theory
- euler
stage: formal-systems
status: draft
---

# Eulerian Paths, Circuits, and Characterization

## Core Idea
An Eulerian path traverses every edge exactly once; an Eulerian circuit is a closed Eulerian path. A connected graph has an Eulerian circuit if and only if all vertices have even degree. It has an Eulerian path if and only if exactly 0 or 2 vertices have odd degree.

## How It's Best Learned
Draw small graphs and try to find Eulerian paths by hand. Check the degree condition before attempting.

## Common Misconceptions
- Confusing Eulerian paths with Hamiltonian paths (edges vs. vertices).
- Assuming all graphs have Eulerian paths.
- Misapplying the degree condition.

## Explainer

The concept of an **Eulerian path** was born from the famous Königsberg bridge problem: can you cross each of seven bridges exactly once and return to your starting point? Euler answered no in 1736 by noticing a structural reason — and in doing so, founded graph theory. From your prerequisite on walks, paths, and cycles, you know that a **walk** allows repeated vertices and edges, while a **path** does not repeat vertices. An Eulerian path is distinct: it may revisit *vertices* but must use each *edge* exactly once. This edge-traversal constraint is what makes the problem interesting.

The key insight is to think about what happens at each vertex as you pass through it. Every time you enter a vertex along one edge, you must leave it along a different edge. This uses up edges in pairs — one in, one out. A vertex that you merely pass through must therefore have **even degree** (its edges pair up perfectly). The only vertices allowed to have odd degree are the start and end of the path, where you leave without entering (start) or enter without leaving (end). This gives the complete characterization: a connected graph has an **Eulerian circuit** (a closed path returning to the start) if and only if every vertex has even degree. It has an **Eulerian path** (not necessarily closed) if and only if exactly two vertices have odd degree — those two are the forced start and end.

To see this in action, take the Königsberg graph: four land masses connected by seven bridges. Three of the four vertices have odd degree (5, 3, 3, and 3). That's more than two odd-degree vertices, so no Eulerian path exists at all. By contrast, consider a simple cycle (each vertex has degree 2, all even) — every edge can be traversed in circuit order. Now consider a path graph A–B–C–D: vertices A and D have degree 1 (odd), B and C have degree 2 (even). Exactly two odd-degree vertices means an Eulerian path exists from A to D.

The **degree sequence** you studied as a prerequisite becomes the decision tool here: you don't need to attempt traversal — just count odd-degree vertices. Zero means a circuit exists; two means a path exists from one odd-degree vertex to the other; anything else means neither exists. When an Eulerian circuit does exist, finding one algorithmically is efficient (Hierholzer's algorithm runs in linear time). A common confusion is with **Hamiltonian** paths and cycles, which visit every *vertex* exactly once instead of every edge — these have no known efficient characterization and are NP-complete in general. The Eulerian condition is clean and local; the Hamiltonian condition is global and hard.
