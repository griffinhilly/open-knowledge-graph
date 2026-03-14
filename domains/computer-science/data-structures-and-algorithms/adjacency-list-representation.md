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
