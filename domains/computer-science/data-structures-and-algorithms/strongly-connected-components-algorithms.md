---
id: strongly-connected-components-algorithms
title: 'Strongly Connected Components: Kosaraju and Tarjan Algorithms'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: graph-depth-first-search-applications
  type: hard
- id: topological-sort
  type: soft
tags:
- scc
- kosaraju
- tarjan
- graph-algorithm
stage: formal-systems
status: draft
---

# Strongly Connected Components: Kosaraju and Tarjan Algorithms

## Core Idea
A strongly connected component (SCC) is a maximal subgraph where every vertex reaches every other vertex. Kosaraju's algorithm: DFS forward, DFS backward on transpose in reverse finish order. Tarjan's: single DFS with a stack, outputs SCCs on the fly. Both run in O(V + E).
