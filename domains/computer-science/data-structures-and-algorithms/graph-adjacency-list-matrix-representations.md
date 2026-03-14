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
