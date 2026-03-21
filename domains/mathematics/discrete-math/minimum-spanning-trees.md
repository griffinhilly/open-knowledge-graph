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

## Questions

```yaml
- question: "A network engineer connects 5 cities by always adding the cheapest remaining cable that does not create a loop. She never considers the global structure. Yet this greedy strategy is guaranteed to find the optimal network. What property makes this provably correct?"
  type: multiple-choice
  options:
    - "The MST is unique when all edge weights are distinct, so any consistent rule finds it."
    - "The cut property: the minimum-weight edge crossing any partition of vertices must belong to every MST."
    - "Greedy algorithms always produce optimal results for graph problems."
    - "Trees have exactly n−1 edges, so any set of n−1 acyclic edges forms a valid MST."
  answer: 1
  explanation: "The cut property is the key theoretical underpinning: given any partition of the graph's vertices into two groups, the minimum-weight edge crossing that cut belongs to every MST (assuming distinct weights). This means each greedy choice — 'take the cheapest edge that does not form a cycle' — adds an edge that must be in the MST regardless of future choices. Without this property, locally cheap choices could force globally expensive ones. Option D is wrong: n−1 arbitrary acyclic edges can fail to span the graph, and spanning n−1 edges that are individually cheap may not minimize total weight."

- question: "What is the key difference in approach between Kruskal's algorithm and Prim's algorithm?"
  type: multiple-choice
  options:
    - "Kruskal's guarantees an MST; Prim's only finds a locally optimal spanning tree."
    - "Kruskal's processes all edges globally in sorted order; Prim's grows a single tree vertex by vertex from a starting node."
    - "Kruskal's works only on undirected graphs; Prim's works on directed graphs."
    - "Kruskal's uses a priority queue for edge selection; Prim's uses union-find for cycle detection."
  answer: 1
  explanation: "Both algorithms are correct and both produce MSTs. Kruskal's is edge-focused: sort all edges by weight, then greedily add each if it connects two previously disconnected components (using union-find to detect cycles). Prim's is vertex-focused: grow a single tree from a starting vertex by repeatedly adding the cheapest edge connecting the current tree to any unincluded vertex. Option D reverses the data structures — Prim's typically uses a priority queue to find the minimum adjacent edge efficiently, while Kruskal's uses union-find for cycle detection."

- question: "If a connected weighted graph has all distinct edge weights, it has exactly one minimum spanning tree."
  type: true-false
  answer: true
  explanation: "With all distinct edge weights, the cut property uniquely determines each MST edge: for any cut, there is exactly one minimum-weight crossing edge, so every MST must include it. Both Kruskal's and Prim's will make identical edge choices and converge on the same unique MST. If two edges tie in weight, different algorithms might choose either, potentially producing different (but equally valid) MSTs. Distinctness eliminates all ties and forces uniqueness."

- question: "Kruskal's algorithm finds the MST by starting with the complete graph and repeatedly removing the most expensive edge that does not disconnect the graph."
  type: true-false
  answer: false
  explanation: "This describes a valid but different method (reverse-delete). Kruskal's actually starts with all vertices isolated (no edges) and adds edges in increasing weight order, skipping any that would form a cycle. The approach grows from an empty forest toward a connected tree. The key operation is cycle detection via union-find when adding edges, not connectivity checking when removing them. Both methods produce the same MST, but Kruskal's is additive, not subtractive."

- question: "Why does the cut property guarantee that a greedy edge-selection strategy produces a globally optimal spanning tree rather than just a locally cheap one?"
  type: short-answer
  answer: "The cut property states that for any partition of vertices into two groups, the minimum-weight edge crossing that cut must belong to every MST. This means each greedy choice to include the cheapest safe edge is not just locally convenient — it is logically required by global optimality. Any spanning tree that excludes this edge would have to include a heavier crossing edge instead, making it non-minimal. Because this reasoning applies at every step, each greedy decision is permanently correct, and the accumulated choices must form the globally optimal MST."
  explanation: "This is what distinguishes MST from problems where greedy fails (like the 0/1 knapsack). The cut property creates a 'safe' choice at every stage — not just a heuristic. The underlying reason is that spanning trees form a matroid, a combinatorial structure where the greedy algorithm is always exactly optimal. The cut property is the matroid exchange property expressed in graph-theoretic terms."
```

## Explainer

From your study of trees and forests, you know that a **spanning tree** of a connected graph is a subgraph that includes all vertices and is itself a tree — connected and acyclic, with exactly n−1 edges for n vertices. A weighted graph assigns a cost to each edge, and the **minimum spanning tree** (MST) is the spanning tree whose total edge weight is as small as possible. Think of it as the cheapest network that keeps all nodes connected: the MST of a map of cities gives you the minimum-cost set of roads that lets you travel between any two cities.

The key theoretical insight behind MST algorithms is the **cut property**: given any partition of the graph's vertices into two groups (a "cut"), the minimum-weight edge crossing that cut must belong to every MST (assuming unique edge weights). This greedy property is what makes the problem tractable — you can make locally optimal edge choices and be guaranteed a globally optimal result.

**Kruskal's algorithm** exploits this by sorting all edges by weight and adding each one if it doesn't form a cycle (using a union-find data structure to check efficiently). Starting with n isolated vertices (a forest), you add the cheapest safe edge one at a time, growing toward a single connected tree. **Prim's algorithm** takes the opposite perspective: start with any single vertex and repeatedly add the cheapest edge that connects the current tree to a new vertex not yet included. Both algorithms are greedy and both produce an MST, but they differ in implementation: Kruskal's is edge-focused and works well for sparse graphs, while Prim's is vertex-focused and efficient with adjacency matrices or priority queues for dense graphs.

MSTs appear throughout applied mathematics and computer science: designing minimum-cost communication networks, approximating the traveling salesman problem (the MST gives a lower bound on the optimal tour), clustering (removing the heaviest MST edges creates natural clusters), and even modeling protein structures. The MST problem is one of the cleanest examples of a problem where a greedy algorithm is provably optimal — a lesson that carries into more advanced algorithm design.
