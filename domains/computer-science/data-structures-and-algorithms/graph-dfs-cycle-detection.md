---
id: graph-dfs-cycle-detection
title: Depth-First Search and Cycle Detection
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: depth-first-search
  type: hard
- id: stacks-data-structure
  type: soft
- id: adjacency-list-representation
  type: soft
tags:
- dfs
- cycle-detection
- graph-traversal
- recursive
- back-edges
stage: formal-systems
status: draft
---

# Depth-First Search and Cycle Detection

## Core Idea
DFS explores a graph by going as deep as possible before backtracking, typically implemented recursively. It detects cycles via back edges: an edge to an ancestor in the DFS tree indicates a cycle. DFS also computes connected components, topological order, and strongly connected components in O(V + E) time.

## How It's Best Learned
Trace DFS by hand, noting pre- and post-visit times. Implement both recursively and iteratively (stack-based). Understand the three edge types (tree, forward, back, cross) and which indicate cycles. Use DFS for cycle detection and topological sorting.

## Common Misconceptions
- DFS must be recursive (iterative with a stack works equally well). - Back edges always exist if a cycle exists (yes in undirected graphs; in directed graphs, back edges specifically indicate cycles).
