---
id: adjacency-list-representation
title: Adjacency List Graph Representation
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: arrays-and-indexed-collections
  type: hard
- id: linked-lists
  type: soft
- id: graph-theory-intro
  type: soft
builds-toward:
- breadth-first-search
- depth-first-search
- graph-bfs-unweighted-shortest-path
tags:
- graphs
- adjacency-list
- representation
- sparse
- memory-efficient
stage: formal-systems
status: draft
---

# Adjacency List Graph Representation

## Core Idea
An adjacency list represents a graph as an array of lists, where each vertex has a list of adjacent vertices. This representation is space-efficient for sparse graphs (E ≪ V²), using O(V + E) space. It is ideal for DFS, BFS, and most graph algorithms, as neighbor iteration is naturally efficient.

## How It's Best Learned
Build adjacency lists by hand for directed and undirected graphs. Implement neighbor iteration. Compare space usage to adjacency matrix for sparse vs. dense graphs. Trace BFS and DFS using adjacency list representation.

## Common Misconceptions
- Adjacency list is always better than adjacency matrix (adjacency matrix is faster for dense graphs and edge-existence queries). - Adjacency lists require linked lists (vectors of vectors work better in practice for cache locality).

## Explainer

You already know that a graph consists of vertices and edges, and that arrays let you store collections with indexed access. An **adjacency list** combines these ideas: for each vertex in the graph, you maintain a list of the vertices it connects to. If vertex 0 has edges to vertices 1, 3, and 4, then the entry at index 0 holds the list [1, 3, 4]. The entire graph is stored as an array of these per-vertex lists — conceptually, an array of arrays.

Consider a social network with 1,000 users where each person has about 150 friends. An adjacency matrix would allocate a 1,000 × 1,000 grid — one million entries — even though only about 150,000 of them (counting both directions) represent actual friendships. The adjacency list stores only the edges that exist: 1,000 lists averaging 150 entries each, totaling roughly 150,000 entries. This is the O(V + E) space guarantee — you pay for the number of vertices (the array of lists) plus the number of edges (the entries within those lists). For **sparse graphs** where E is much less than V², this is dramatically more efficient than the O(V²) matrix.

The adjacency list's real strength shows up when you need to iterate over a vertex's neighbors — the most common operation in graph algorithms. In BFS, you visit every neighbor of the current vertex. In DFS, you explore neighbors recursively. With an adjacency list, iterating over the neighbors of vertex v takes O(degree(v)) time — you simply walk through v's list. With an adjacency matrix, the same operation requires scanning an entire row of V entries, most of which may be zero. For sparse graphs, this difference is the gap between a practical algorithm and an impractical one.

The tradeoff appears when you need to answer "does edge (u, v) exist?" With an adjacency matrix, this is a single O(1) array lookup. With a basic adjacency list, you must search through u's neighbor list, which takes O(degree(u)) time. For algorithms that frequently check edge existence (like certain dense-graph optimizations), the matrix wins. In practice, most graph algorithms — shortest paths, connected components, topological sort — spend their time iterating over neighbors rather than checking individual edges, which is why adjacency lists are the default choice. Implementation-wise, despite the name "list," using a dynamic array (vector) for each vertex's neighbors gives better cache performance than linked list nodes scattered across memory.
