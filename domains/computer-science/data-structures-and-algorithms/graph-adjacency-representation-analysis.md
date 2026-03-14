---
id: graph-adjacency-representation-analysis
title: 'Graph Representations: Adjacency List and Matrix'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: graph-theory-intro
  type: soft
builds-toward:
- breadth-first-search
- depth-first-search
tags:
- graphs
- representation
- implementation
stage: formal-systems
status: draft
---

# Graph Representations: Adjacency List and Matrix

## Core Idea
Graphs are represented as adjacency lists (O(V+E) space, O(degree) to traverse neighbors) or adjacency matrices (O(V²) space, O(1) edge lookup). Choice depends on graph density: sparse graphs favor lists, dense graphs favor matrices. Weighted edges naturally extend both.

## How It's Best Learned
Implement both representations for the same graph. Measure space and time for edge lookup, neighbor traversal, and insertion. Run BFS/DFS on both and observe differences in memory and cache behavior.

## Common Misconceptions
- Assuming one representation is universally better; the choice depends on V, E, and query patterns.
- Thinking adjacency lists are always efficient; with poor hash functions or linked lists, traversal can be slow.
- Not accounting for the cost of dynamic graph modifications (edge insertion/deletion).
