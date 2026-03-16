---
id: graph-adjacency-list-matrix-representations
title: 'Graph Representations: Adjacency List vs. Adjacency Matrix'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: arrays-and-indexed-collections
  type: hard
- id: linked-lists
  type: hard
builds-toward:
- graph-depth-first-search-applications
- graph-breadth-first-search-applications
tags:
- graph
- representation
- adjacency
stage: formal-systems
status: draft
---

# Graph Representations: Adjacency List vs. Adjacency Matrix

## Core Idea
Adjacency lists use O(V + E) space, fast for sparse graphs; adjacency matrices use O(V²) space, fast for edge lookups. Dense graphs (E ≈ V²) favor matrices; sparse graphs (E ≪ V²) favor lists. Representation choice affects algorithm complexity.

## Explainer

A graph is an abstract concept — vertices connected by edges — but to write algorithms that operate on graphs, you need a concrete data structure in memory. The two foundational choices are the **adjacency matrix** and the **adjacency list**, and the right choice depends on the shape of your graph and the operations your algorithm needs. Both build directly on arrays and linked lists, the data structures you already know.

An **adjacency matrix** is a V × V two-dimensional array where entry matrix[i][j] is 1 (or the edge weight) if there is an edge from vertex i to vertex j, and 0 otherwise. The appeal is simplicity and speed for one specific operation: checking whether an edge exists between two vertices is a single O(1) array lookup. For an undirected graph, the matrix is symmetric (matrix[i][j] = matrix[j][i]), which means half the storage is redundant. The cost is space: regardless of how many edges exist, you always allocate V² entries. A graph with 10,000 vertices requires a 100-million-entry matrix even if it has only 20,000 edges.

An **adjacency list** takes the opposite approach. You maintain an array of V lists (or dynamic arrays), one per vertex. The list at index i contains only the vertices that i actually connects to. If vertex i has 3 neighbors, its list has 3 entries — not V entries. Total space is O(V + E): V for the array of lists, and E for all the neighbor entries combined (2E for undirected graphs, since each edge appears in two lists). For sparse graphs — and most real-world graphs are sparse — this savings is enormous. The tradeoff is that checking "does edge (u, v) exist?" requires scanning u's neighbor list, which takes O(degree(u)) instead of O(1).

The choice between representations cascades through algorithm performance. BFS and DFS visit every vertex and examine every edge once — with an adjacency list, this takes O(V + E), but with a matrix, examining all edges requires scanning every row completely for O(V²) regardless of sparsity. For sparse graphs, O(V + E) can be vastly smaller. Conversely, algorithms that need constant-time edge lookups or that operate on dense graphs (where E approaches V²) lose nothing with a matrix and gain simpler code. Weighted graphs work naturally with both: the matrix stores weights instead of 1s, and each list entry becomes a (neighbor, weight) pair. In practice, adjacency lists are the default starting point, and you switch to a matrix only when your graph is dense or your algorithm's bottleneck is edge-existence queries.
