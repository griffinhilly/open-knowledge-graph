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
status: validated
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

## Questions

```yaml
- question: "A city planner wants to design a snow plow route that covers every road exactly once and returns to the starting depot. What must be true of the graph representing the street network?"
  type: multiple-choice
  options:
    - "The graph must be a tree with no cycles"
    - "Every vertex must have degree at least 2"
    - "Exactly two vertices must have odd degree"
    - "Every vertex must have even degree"
  answer: 3
  explanation: "A route that traverses every edge exactly once and returns to the start is an Eulerian circuit, which exists if and only if every vertex has even degree. The reasoning: every time you enter an intersection on one road, you must leave on a different road, using edges in pairs. Only if all edges pair up perfectly (even degree everywhere) can you return to the start without getting stuck. Option C describes the condition for an Eulerian path (not a circuit) — it would allow a route with different start and end points."

- question: "A connected graph has 8 vertices with degrees 4, 3, 2, 3, 2, 4, 2, 3. Does this graph have an Eulerian circuit, an Eulerian path, or neither?"
  type: multiple-choice
  options:
    - "Eulerian circuit, since the graph is connected and most vertices have even degree"
    - "Eulerian path from one odd-degree vertex to another"
    - "Neither — it has more than two vertices of odd degree"
    - "Eulerian path, since the sum of all degrees is even"
  answer: 2
  explanation: "Counting odd-degree vertices: 3 (odd), 3 (odd), 3 (odd) — three odd-degree vertices. The degree condition requires exactly 0 odd-degree vertices for a circuit or exactly 2 for a path. Three odd-degree vertices satisfies neither condition, so no Eulerian path or circuit exists. Option A commits the common error of assuming connectivity is sufficient. Option D is a red herring: the sum of degrees is always even (by the handshake lemma), but that tells you nothing about the Eulerian condition."

- question: "An Eulerian path visits nearly every vertex exactly once, while an Eulerian circuit also returns to the starting vertex."
  type: true-false
  answer: false
  explanation: "This confuses Eulerian paths with Hamiltonian paths. An Eulerian path traverses every EDGE exactly once — it may revisit vertices freely. A Hamiltonian path visits every VERTEX exactly once. The distinction is crucial: Eulerian conditions are easy to check (count odd-degree vertices) and can be solved efficiently, while Hamiltonian conditions are NP-complete in general."

- question: "If a connected graph has exactly two vertices of odd degree, those two vertices must be the endpoints (start and finish) of any Eulerian path in that graph."
  type: true-false
  answer: true
  explanation: "The logic is necessary: every vertex that is merely passed through uses its edges in pairs (one in, one out), requiring even degree. The start vertex contributes one extra edge leaving without entering, and the end vertex contributes one extra edge entering without leaving — both must have odd degree. With exactly two odd-degree vertices, these are forced to be the start and end, with no choice in the matter."

- question: "Why does a vertex in the middle of an Eulerian path require even degree, while the starting and ending vertices are allowed to have odd degree?"
  type: short-answer
  answer: "A vertex in the middle of the path is entered and exited repeatedly — each entry uses one edge and each exit uses another, so edges are consumed in enter/exit pairs. This requires the vertex to have even degree. The starting vertex is left initially without being entered first (one edge used before any pairing begins), and the ending vertex is entered last without being exited (one edge used after pairing ends). Each contributes exactly one 'unpaired' edge, giving both odd degree."
  explanation: "This degree-parity argument is the key insight of Eulerian characterization. The condition is not just a fact to memorize — it follows directly from the enter/exit pairing logic at each vertex. Understanding this argument also explains why the condition is both necessary and sufficient, and why exactly 0 or 2 odd-degree vertices are the only possibilities that permit an Eulerian traversal."
```

## Explainer

The concept of an **Eulerian path** was born from the famous Königsberg bridge problem: can you cross each of seven bridges exactly once and return to your starting point? Euler answered no in 1736 by noticing a structural reason — and in doing so, founded graph theory. From your prerequisite on walks, paths, and cycles, you know that a **walk** allows repeated vertices and edges, while a **path** does not repeat vertices. An Eulerian path is distinct: it may revisit *vertices* but must use each *edge* exactly once. This edge-traversal constraint is what makes the problem interesting.

The key insight is to think about what happens at each vertex as you pass through it. Every time you enter a vertex along one edge, you must leave it along a different edge. This uses up edges in pairs — one in, one out. A vertex that you merely pass through must therefore have **even degree** (its edges pair up perfectly). The only vertices allowed to have odd degree are the start and end of the path, where you leave without entering (start) or enter without leaving (end). This gives the complete characterization: a connected graph has an **Eulerian circuit** (a closed path returning to the start) if and only if every vertex has even degree. It has an **Eulerian path** (not necessarily closed) if and only if exactly two vertices have odd degree — those two are the forced start and end.

To see this in action, take the Königsberg graph: four land masses connected by seven bridges. Three of the four vertices have odd degree (5, 3, 3, and 3). That's more than two odd-degree vertices, so no Eulerian path exists at all. By contrast, consider a simple cycle (each vertex has degree 2, all even) — every edge can be traversed in circuit order. Now consider a path graph A–B–C–D: vertices A and D have degree 1 (odd), B and C have degree 2 (even). Exactly two odd-degree vertices means an Eulerian path exists from A to D.

The **degree sequence** you studied as a prerequisite becomes the decision tool here: you don't need to attempt traversal — just count odd-degree vertices. Zero means a circuit exists; two means a path exists from one odd-degree vertex to the other; anything else means neither exists. When an Eulerian circuit does exist, finding one algorithmically is efficient (Hierholzer's algorithm runs in linear time). A common confusion is with **Hamiltonian** paths and cycles, which visit every *vertex* exactly once instead of every edge — these have no known efficient characterization and are NP-complete in general. The Eulerian condition is clean and local; the Hamiltonian condition is global and hard.
