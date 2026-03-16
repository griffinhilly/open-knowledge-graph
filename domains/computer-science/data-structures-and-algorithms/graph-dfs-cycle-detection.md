---
id: graph-dfs-cycle-detection
title: Depth-First Search and Cycle Detection
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: depth-first-search
  type: hard
- id: stacks-data-structure
  type: soft
- id: adjacency-list-representation
  type: soft
tags:
- dfs
- cycle-detection
- graph-traversal
- recursive
- back-edges
stage: formal-systems
status: draft
---

# Depth-First Search and Cycle Detection

## Core Idea
DFS explores a graph by going as deep as possible before backtracking, typically implemented recursively. It detects cycles via back edges: an edge to an ancestor in the DFS tree indicates a cycle. DFS also computes connected components, topological order, and strongly connected components in O(V + E) time.

## How It's Best Learned
Trace DFS by hand, noting pre- and post-visit times. Implement both recursively and iteratively (stack-based). Understand the three edge types (tree, forward, back, cross) and which indicate cycles. Use DFS for cycle detection and topological sorting.

## Common Misconceptions
- DFS must be recursive (iterative with a stack works equally well). - Back edges always exist if a cycle exists (yes in undirected graphs; in directed graphs, back edges specifically indicate cycles).

## Explainer

You already understand depth-first search as a traversal strategy: pick a starting vertex, explore as far as possible along one branch, then backtrack and try the next. During this traversal, DFS implicitly classifies every edge in the graph. **Tree edges** are the edges DFS follows to discover new vertices — they form the DFS tree (or forest). The remaining edges connect vertices that are already discovered, and their classification reveals the graph's structure. The most important category for cycle detection is the **back edge**: an edge from a vertex to one of its ancestors in the DFS tree.

Why do back edges indicate cycles? A back edge from vertex `v` to ancestor `u` means there is a path from `u` down through the DFS tree to `v` (the tree edges), and also a direct edge from `v` back to `u` (the back edge). Together, these form a cycle: `u → ... → v → u`. Conversely, if a cycle exists, DFS must encounter a back edge — when it first reaches the cycle, it will traverse tree edges around most of the cycle until it finds an edge leading back to an already-visited ancestor. So the rule is simple: **a graph contains a cycle if and only if DFS encounters a back edge**.

For **undirected graphs**, implementation is straightforward. Maintain a visited set and track each vertex's parent in the DFS tree. When you examine a neighbor of the current vertex, if it is already visited and it is not the parent, you have found a back edge — and therefore a cycle. The parent check is necessary because in an undirected graph, the edge you just traversed from parent to child also exists from child to parent; without the check, you would falsely detect a "cycle" on every edge.

For **directed graphs**, the situation is more subtle because edges are classified into four types: tree, back, forward (to a descendant), and cross (to a vertex in a different subtree). Only back edges indicate cycles — a forward or cross edge does not create one. To detect back edges in a directed graph, you need to distinguish between vertices that are **currently on the recursion stack** (ancestors of the current vertex) and vertices that are merely visited (fully processed and off the stack). Use a three-color scheme: white (unvisited), gray (in progress — on the stack), and black (finished). If DFS encounters an edge to a gray vertex, that is a back edge and a cycle exists. An edge to a black vertex is a cross or forward edge and is harmless. This gray/black distinction is also the foundation for **topological sorting**: if DFS completes without finding any back edges, the graph is a DAG (directed acyclic graph), and the reverse of the finish order gives a valid topological ordering.
