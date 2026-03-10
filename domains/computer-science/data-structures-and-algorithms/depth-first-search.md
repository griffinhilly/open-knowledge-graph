---
id: depth-first-search
title: Depth-First Search (DFS)
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: recursion-basics
  type: hard
- id: graph-representation
  type: hard
- id: stacks-data-structure
  type: soft
- id: graph-theory-intro
  type: soft
builds-toward:
- topological-sort
- union-find
tags:
- DFS
- graph-traversal
- recursion
- cycle-detection
- connected-components
stage: formal-systems
status: draft
---

# Depth-First Search (DFS)

## Core Idea
Depth-first search (DFS) explores a graph by going as deep as possible along each branch before backtracking. It can be implemented recursively or iteratively with an explicit stack, and runs in O(V + E) time. DFS is the foundation for cycle detection, topological sorting, strongly connected components (Tarjan's and Kosaraju's algorithms), and solving maze-like problems. Tracking discovery and finish times during DFS produces edge classifications: tree edges, back edges (cycles), forward edges, and cross edges.

## How It's Best Learned
Implement recursive DFS tracking discovery and finish timestamps. Then implement the iterative stack version and verify equivalent results. Use DFS to detect cycles in both directed and undirected graphs as a practical exercise.

## Common Misconceptions
- DFS does not find shortest paths; BFS does.
- In an undirected graph, encountering an already-visited node that is not your direct parent indicates a cycle. In directed graphs, only a back edge (reaching an ancestor in the current DFS path) indicates a cycle.
