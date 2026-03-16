---
id: depth-first-search-graphs
title: Depth-First Search (DFS)
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-theory-intro
  type: hard
- id: big-o-notation
  type: soft
builds-toward:
- topological-sorting
- strongly-connected-components
- cycle-detection-directed-graphs
tags:
- graph-algorithms
- traversal
- dfs
stage: formal-systems
status: draft
---

# Depth-First Search (DFS)

## Core Idea
Depth-first search systematically explores a graph by going as deep as possible before backtracking. Starting from a source vertex, DFS visits adjacent unvisited vertices recursively, generating a DFS tree. It runs in O(V+E) time and is fundamental to many graph algorithms.

## How It's Best Learned
Trace DFS by hand on small graphs, maintaining a stack of vertices to visit. Observe how DFS discovers edges as tree edges, back edges, and cross edges in directed graphs.

## Common Misconceptions
- Confusing the DFS tree with the original graph structure. - Assuming DFS always finds the shortest path, which is true only for unweighted graphs in BFS.

## Explainer

Think of DFS as exploring a maze using the rule "always go as deep as you can before turning back." You enter a corridor, keep walking forward into new corridors, and only backtrack when you hit a dead end — then you return to the last junction you hadn't fully explored. This explore-deep-first strategy is exactly what DFS implements on a graph. Starting from a source vertex, DFS visits an unvisited neighbor, then immediately recurses into *that* vertex's neighbors before returning. The call stack (or an explicit stack data structure) remembers where to backtrack.

From your prerequisite knowledge of graph theory, you know that a graph G = (V, E) consists of vertices and edges. DFS systematically marks each vertex as **discovered** when first visited and **finished** when all its neighbors have been explored. The edges DFS traverses form a **DFS tree** — a spanning substructure rooted at the source. Not all edges of the original graph end up in this tree, and classifying the non-tree edges is one of DFS's most powerful features. In a directed graph, an edge (u, v) is a **back edge** if v is an ancestor of u in the DFS tree (meaning there's a cycle), a **forward edge** if v is a descendant but not a child, or a **cross edge** otherwise.

The runtime of O(V + E) follows naturally from the structure: each vertex is discovered and finished exactly once (contributing O(V)), and each edge is examined exactly once when DFS processes the vertex it leaves from (contributing O(E)). If you've seen Big-O notation, this is as good as it gets for graph traversal — you can't process a graph without at least touching every vertex and edge.

The real power of DFS lies in what the discovery and finish times reveal. If you record a **timestamp** when each vertex is discovered and when it's finished, these intervals nest cleanly: if v is a descendant of u in the DFS tree, then u's discovery time < v's discovery time < v's finish time < u's finish time. This **parenthesis structure** is the engine behind topological sorting (process vertices in reverse finish order), cycle detection (a back edge exists if and only if a cycle exists), and finding strongly connected components. DFS is not just a traversal — it is a framework that, with small instrumentation changes, solves an entire family of graph problems.
