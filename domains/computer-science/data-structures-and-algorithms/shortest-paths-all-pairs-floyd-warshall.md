---
id: shortest-paths-all-pairs-floyd-warshall
title: 'All-Pairs Shortest Paths: Floyd-Warshall Algorithm'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: dijkstras-algorithm
  type: soft
- id: bellman-ford-algorithm
  type: soft
- id: divide-and-conquer-strategy
  type: soft
tags:
- shortest-path
- all-pairs
- dynamic-programming
stage: formal-systems
status: draft
---

# All-Pairs Shortest Paths: Floyd-Warshall Algorithm

## Core Idea
Floyd-Warshall solves all-pairs shortest paths in O(V³) time using dynamic programming: dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) for all k. It works on graphs with negative edges (but no negative cycles) and is simpler to code than running Dijkstra V times.
