---
id: union-find
title: Union-Find (Disjoint Set Union)
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: arrays-and-lists
  type: hard
- id: amortized-analysis
  type: soft
- id: time-space-complexity
  type: soft
- id: equivalence-relations
  type: soft
- id: depth-first-search
  type: soft
tags:
- union-find
- disjoint-sets
- DSU
- connectivity
stage: formal-systems
status: validated
---
# Union-Find (Disjoint Set Union)

## Core Idea
Union-Find (Disjoint Set Union, DSU) tracks a collection of elements partitioned into disjoint sets, supporting union (merge two sets) and find (identify a set's representative). With two optimizations — union by rank and path compression — both operations run in nearly O(1) amortized time, formally O(α(n)) where α is the inverse Ackermann function, an astronomically slowly growing function. Union-Find is used to detect cycles in undirected graphs and is the core component of Kruskal's minimum spanning tree algorithm.

## How It's Best Learned
Implement union-find with a plain parent array first, then add union by rank, then path compression. Measure how the effective tree height changes with each optimization on large inputs.

## Common Misconceptions
- Path compression restructures the tree during find operations, but this does not affect correctness — only future query speed.
- The near-O(1) amortized bound requires BOTH union by rank AND path compression; either optimization alone gives a weaker guarantee.

## Explainer

Imagine you're at a party where people keep forming groups. Initially everyone stands alone. Periodically, two people decide their groups should merge. At any moment, someone might ask: "Are Alice and Bob in the same group?" **Union-Find** is the data structure that answers this question efficiently, even as groups keep merging — and it does so in nearly constant time per operation.

The core representation is surprisingly simple: an array `parent[]` where `parent[i]` points to i's parent in a tree. Each group forms a tree, and the root of that tree is the group's **representative**. To find which group an element belongs to, you follow parent pointers until you reach a root (an element that is its own parent). To merge two groups, you find their roots and make one point to the other. This is where your knowledge of arrays comes in — the entire structure is just an integer array, with indices representing elements and values representing parent links.

The naive version has a problem: trees can become long chains. If you always attach the second root under the first, a sequence of unions can produce a tree of depth n, making find operations O(n). **Union by rank** fixes this by always attaching the shorter tree under the taller one, keeping tree heights logarithmic. But the real magic is **path compression**: every time you call find and walk up to the root, you redirect every node along the path to point directly at the root. Future finds on those nodes become O(1). The combination of both optimizations yields an amortized cost of O(α(n)) per operation, where α is the **inverse Ackermann function** — a function that grows so slowly it's effectively constant for any input size you'll ever encounter (α(n) ≤ 4 for n up to roughly 10^80).

Union-Find's most important application is in graph algorithms. To detect whether adding an edge creates a **cycle** in an undirected graph, check whether the two endpoints are already in the same set — if they are, connecting them would form a cycle. This is exactly what **Kruskal's algorithm** does when building a minimum spanning tree: sort edges by weight, then greedily add each edge unless it would create a cycle (i.e., unless find returns the same representative for both endpoints). With Union-Find powering the cycle check, Kruskal's runs in O(E log E) time, dominated by the initial sort. The Union-Find operations themselves contribute essentially O(E) total work — nearly free.
