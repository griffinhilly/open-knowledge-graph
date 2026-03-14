---
id: floyd-warshall-all-pairs-shortest-path
title: Floyd-Warshall Algorithm for All-Pairs Shortest Paths
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: dynamic-programming-intro
  type: hard
- id: dijkstras-algorithm
  type: soft
tags:
- shortest-path
- all-pairs
- dynamic-programming
- negative-weights
- transitive-closure
stage: formal-systems
status: draft
---

# Floyd-Warshall Algorithm for All-Pairs Shortest Paths

## Core Idea
Floyd-Warshall computes shortest paths between all pairs of vertices in O(V³) time and O(V²) space using dynamic programming. It iterates through intermediate vertices k, updating distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j]). Unlike Dijkstra, it handles negative-weight edges (but not negative cycles) and is simple to implement.

## How It's Best Learned
Trace the algorithm on a small graph, layer-by-layer through intermediate vertices k. Understand the recurrence relation and why the triple-nested loop works. Detect negative cycles by checking the diagonal. Compare to running Dijkstra V times.

## Common Misconceptions
- Floyd-Warshall is always optimal (O(V³) is high; Dijkstra from all sources can be faster for sparse graphs). - It handles negative cycles (it detects them but doesn't fix them; shortest paths are undefined in their presence).
