---
id: cycle-detection-directed-undirected
title: Cycle Detection in Directed and Undirected Graphs
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: depth-first-search
  type: hard
builds-toward:
- topological-sort
tags:
- graphs
- cycles
- dfs
stage: formal-systems
status: draft
---

# Cycle Detection in Directed and Undirected Graphs

## Core Idea
In undirected graphs, a back edge (to a visited neighbor other than the parent) signals a cycle. In directed graphs, back edges are those to ancestors in the DFS tree. Both detections run in O(V+E) during DFS. Cycle detection is essential for dependency resolution and deadlock detection.

## How It's Best Learned
Implement DFS with three vertex states (white, gray, black). Use gray edges as back edges. Trace on examples with and without cycles. Apply to topological sorting and deadlock detection.

## Common Misconceptions
- Treating directed and undirected cycle detection identically; the algorithms differ significantly.
- Not handling self-loops and parallel edges correctly.
- Assuming cycle detection requires storing all edges; DFS detects them during traversal.
