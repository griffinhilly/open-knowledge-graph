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
status: draft
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
