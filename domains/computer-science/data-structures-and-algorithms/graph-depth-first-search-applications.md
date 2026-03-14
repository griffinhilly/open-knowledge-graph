---
id: graph-depth-first-search-applications
title: 'Depth-First Search: Implementation and Applications'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: graph-adjacency-list-matrix-representations
  type: hard
- id: depth-first-search
  type: soft
builds-toward:
- topological-sort
- strongly-connected-components-algorithms
tags:
- dfs
- search
- graph-algorithm
stage: formal-systems
status: draft
---

# Depth-First Search: Implementation and Applications

## Core Idea
DFS explores a graph deeply via recursion or an explicit stack, visiting unvisited neighbors. It finds connected components, detects cycles, computes finish times (for topological sort), and identifies strongly connected components.
