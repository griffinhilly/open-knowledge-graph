---
id: minimum-spanning-trees
title: Minimum Spanning Trees and Optimization
domain: mathematics
course: discrete-math
prerequisites:
- id: trees-and-forests
  type: hard
tags:
- graph-theory
- spanning-trees
- optimization
stage: formal-systems
status: draft
---

# Minimum Spanning Trees and Optimization

## Core Idea
A minimum spanning tree (MST) of a weighted graph is a spanning tree with minimum total edge weight. MSTs can be found using greedy algorithms like Kruskal's or Prim's algorithm. Every connected weighted graph has at least one MST.

## Explainer

From your study of trees and forests, you know that a **spanning tree** of a connected graph is a subgraph that includes all vertices and is itself a tree — connected and acyclic, with exactly n−1 edges for n vertices. A weighted graph assigns a cost to each edge, and the **minimum spanning tree** (MST) is the spanning tree whose total edge weight is as small as possible. Think of it as the cheapest network that keeps all nodes connected: the MST of a map of cities gives you the minimum-cost set of roads that lets you travel between any two cities.

The key theoretical insight behind MST algorithms is the **cut property**: given any partition of the graph's vertices into two groups (a "cut"), the minimum-weight edge crossing that cut must belong to every MST (assuming unique edge weights). This greedy property is what makes the problem tractable — you can make locally optimal edge choices and be guaranteed a globally optimal result.

**Kruskal's algorithm** exploits this by sorting all edges by weight and adding each one if it doesn't form a cycle (using a union-find data structure to check efficiently). Starting with n isolated vertices (a forest), you add the cheapest safe edge one at a time, growing toward a single connected tree. **Prim's algorithm** takes the opposite perspective: start with any single vertex and repeatedly add the cheapest edge that connects the current tree to a new vertex not yet included. Both algorithms are greedy and both produce an MST, but they differ in implementation: Kruskal's is edge-focused and works well for sparse graphs, while Prim's is vertex-focused and efficient with adjacency matrices or priority queues for dense graphs.

MSTs appear throughout applied mathematics and computer science: designing minimum-cost communication networks, approximating the traveling salesman problem (the MST gives a lower bound on the optimal tour), clustering (removing the heaviest MST edges creates natural clusters), and even modeling protein structures. The MST problem is one of the cleanest examples of a problem where a greedy algorithm is provably optimal — a lesson that carries into more advanced algorithm design.
