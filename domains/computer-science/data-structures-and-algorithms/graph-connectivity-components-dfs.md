---
id: graph-connectivity-components-dfs
title: 'Graph Connectivity: Finding Connected Components'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: depth-first-search
  type: hard
- id: graph-adjacency-representation-analysis
  type: hard
builds-toward:
- strongly-connected-components-algorithms
- articulation-points-cut-vertices
tags:
- graphs
- connectivity
- components
- dfs
stage: formal-systems
status: draft
---

# Graph Connectivity: Finding Connected Components

## Core Idea
A connected component is a maximal set of vertices reachable from each other. DFS or BFS starting from an unvisited vertex marks all vertices in its component. Running this repeatedly identifies all components in O(V+E) time.

## How It's Best Learned
Implement DFS-based component finding. Verify on graphs with known component structure. Use components to solve applications like detecting if a graph is connected or merging two graphs safely.

## Common Misconceptions
- Confusing connected components (undirected) with strongly connected components (directed).
- Thinking component finding requires special algorithms; it's a straightforward DFS/BFS application.
- Not recognizing components are useful for partitioning large graphs and understanding structure.
