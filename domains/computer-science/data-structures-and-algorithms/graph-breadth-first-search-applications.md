---
id: graph-breadth-first-search-applications
title: 'Breadth-First Search: Implementation and Applications'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: graph-adjacency-list-matrix-representations
  type: hard
- id: breadth-first-search
  type: soft
builds-toward:
- dijkstras-algorithm
tags:
- bfs
- search
- graph-algorithm
stage: formal-systems
status: draft
---

# Breadth-First Search: Implementation and Applications

## Core Idea
BFS explores a graph level-by-level via a queue, visiting all distance-k neighbors before distance-(k+1). It finds shortest paths in unweighted graphs, connected components, and bipartiteness. Both run in O(V + E) time.
