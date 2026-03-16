---
id: graph-representation-methods
title: 'Graph Representation: Adjacency Lists, Matrices, and Edge Lists'
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-theory-fundamentals
  type: hard
builds-toward:
- graph-isomorphism-equivalence
tags:
- graph-theory
- representation
stage: formal-systems
status: draft
---

# Graph Representation: Adjacency Lists, Matrices, and Edge Lists

## Core Idea
Graphs can be represented as adjacency matrices (n×n where entry (i,j) is the edge weight), adjacency lists (list of neighbors for each vertex), or edge lists (list of all edges). Each representation has different time and space tradeoffs depending on graph density and algorithm requirements.

## Explainer

From graph theory fundamentals, you know a graph is an abstract object: a set of vertices and a set of edges between them. But to actually *compute* with a graph — run an algorithm, store it in memory, search it — you need to encode that abstract structure in concrete form. The choice of representation shapes what operations are fast, how much memory you use, and which algorithms become natural to implement.

The **adjacency matrix** represents a graph as an n×n grid where row i, column j holds the weight of the edge from vertex i to vertex j (or 1 if unweighted, 0 if no edge). This makes one question instant: "Is there an edge between vertex i and vertex j?" — just look up the cell in O(1). But it costs O(n²) space regardless of how many edges actually exist. For a sparse graph with only a handful of edges per vertex, this wastes enormous space storing zeros. For a dense graph where nearly every pair of vertices is connected, the matrix is a natural fit.

The **adjacency list** stores, for each vertex, a list of its neighbors (and optionally edge weights). A graph with n vertices and m edges uses O(n + m) space — proportional only to what actually exists. Iterating over all edges from a given vertex is fast (just walk its list), which makes adjacency lists ideal for algorithms like BFS, DFS, and Dijkstra's that repeatedly ask "what are this vertex's neighbors?" The tradeoff is that checking whether a specific edge (u, v) exists requires scanning u's neighbor list, taking O(degree(u)) time in the worst case rather than O(1).

The **edge list** is the simplest representation: just an unordered collection of (u, v, weight) triples. It uses O(m) space and is easy to iterate over all edges, making it natural for algorithms that process every edge once — like Kruskal's minimum spanning tree algorithm. However, it is slow for neighbor lookups or checking edge existence. The right choice depends on the algorithm: Dijkstra's wants adjacency lists; Floyd-Warshall wants a matrix; Kruskal's wants an edge list. In practice, understanding all three and knowing when to convert between them is as important as knowing the representations themselves.
