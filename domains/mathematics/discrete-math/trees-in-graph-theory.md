---
id: trees-in-graph-theory
title: Trees and Spanning Trees
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-connectivity
  type: hard
- id: mathematical-induction
  type: hard
builds-toward:
- minimum-spanning-trees
tags:
- trees
- spanning-trees
- acyclic
- graph-theory
- cayley
stage: formal-systems
status: validated
---

# Trees and Spanning Trees

## Core Idea
A tree is a connected acyclic graph. A tree on n vertices has exactly n−1 edges, and there is a unique path between any two vertices — these properties are all equivalent characterizations. A spanning tree of a connected graph G is a subgraph that is a tree and includes every vertex of G. Cayley's formula states there are n^(n−2) distinct labeled trees on n vertices. Trees are among the most important structures in mathematics and computer science, appearing in parse trees, hierarchical data, and network design.

## How It's Best Learned
Verify the n−1 edges characterization on small examples, then prove it by induction: adding the nth vertex with one edge maintains the tree. Show the equivalence of the three characterizations. Build spanning trees manually by removing edges from cycles in small connected graphs.

## Common Misconceptions
- Confusing (unrooted) trees with rooted trees — a tree is just a graph; a root is an additional designation.
- Thinking a connected graph has a unique spanning tree — most graphs have exponentially many.
- Not recognizing that removing any single edge from a tree disconnects it.

## Explainer

A **tree** is a connected graph with no cycles. You know from graph connectivity that "connected" means there is a path between every pair of vertices. "Acyclic" means no path ever loops back on itself. These two constraints together produce a surprisingly rigid structure: a tree on n vertices has *exactly* n−1 edges, and there is a *unique* path between every pair of vertices. These are not three separate facts — they are equivalent characterizations of the same thing. Any two of the three properties (connected, acyclic, n−1 edges) imply the third.

The n−1 edges property is cleanest to see by induction, which you know from your prerequisites. Base case: a single vertex (n = 1) has 0 = 1−1 edges. For the inductive step, any tree on n vertices has at least one leaf — a vertex of degree 1 (this is provable: if every vertex had degree ≥ 2, you could keep walking without revisiting and eventually cycle, contradicting acyclicity). Remove the leaf and its single edge. The remaining graph is still connected and acyclic — a tree on n−1 vertices with n−2 edges by induction. Restore the leaf: n vertices, n−1 edges. The unique-path property follows from connectivity and acyclicity: if two paths existed between the same pair of vertices, their union would contain a cycle.

A **spanning tree** of a connected graph G is a subgraph that includes every vertex of G and is itself a tree. Think of G as a road network with redundant connections. A spanning tree keeps just enough roads to get between any two cities — exactly one route between each pair. Every connected graph has at least one spanning tree; you can build one by starting with all edges and removing edges one at a time from any cycle. Spanning trees are fundamental to network design: minimum spanning trees (your next topic) find the cheapest such structure.

**Cayley's formula** states that the number of distinct labeled trees on n vertices is n^(n−2). For n = 4, that's 4² = 16 distinct trees — you can verify this by hand. This result is deceptively simple to state but non-trivial to prove. The Prüfer sequence provides an elegant bijective proof: every labeled tree on n vertices corresponds to a unique sequence of n−2 integers, each between 1 and n. This establishes a one-to-one correspondence between labeled trees and sequences, so there are exactly n^(n−2) of each. The formula is a reminder that even in the tightly constrained world of trees, the count can explode rapidly with n.
