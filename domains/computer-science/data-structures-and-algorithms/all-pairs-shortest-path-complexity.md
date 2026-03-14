---
id: all-pairs-shortest-path-complexity
title: 'All-Pairs Shortest Paths: Floyd-Warshall Analysis'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: shortest-paths-all-pairs-floyd-warshall
  type: hard
tags:
- shortest-paths
- algorithms
- dynamic-programming
stage: formal-systems
status: draft
---

# All-Pairs Shortest Paths: Floyd-Warshall Analysis

## Core Idea
Floyd-Warshall solves all-pairs shortest paths in O(V³) time via dynamic programming. It works with negative weights and detects negative cycles. Although slower than running Dijkstra V times on sparse graphs, it's simpler and often preferred for small to medium-sized graphs.

## How It's Best Learned
Implement Floyd-Warshall and trace the DP recurrence D[k][i][j] = min(D[k-1][i][j], D[k-1][i][k] + D[k-1][k][j]). Compare performance and simplicity to running Bellman-Ford or Dijkstra multiple times.

## Common Misconceptions
- Assuming Floyd-Warshall is inefficient; O(V³) is acceptable for small graphs and offers elegance.
- Not recognizing the cache-friendly dense representation; it can beat sparse algorithms in practice.
- Forgetting that Floyd-Warshall extends naturally to detecting negative cycles and reconstructing paths.
