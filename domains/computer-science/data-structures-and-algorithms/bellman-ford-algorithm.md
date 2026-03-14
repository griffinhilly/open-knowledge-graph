---
id: bellman-ford-algorithm
title: Bellman-Ford Algorithm
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: graph-representation
  type: hard
- id: dijkstras-algorithm
  type: soft
- id: breadth-first-search
  type: soft
- id: graph-theory-intro
  type: soft
tags:
- shortest-path
- Bellman-Ford
- negative-weights
- negative-cycles
stage: formal-systems
status: validated
---

# Bellman-Ford Algorithm

## Core Idea
The Bellman-Ford algorithm finds shortest paths from a single source in a weighted graph, correctly handling negative edge weights. It relaxes all edges V−1 times; after these iterations, all shortest paths (assuming no negative cycles) are found. A V-th relaxation pass detects negative cycles: if any distance still decreases, a negative cycle is reachable from the source. Bellman-Ford runs in O(VE) time, slower than Dijkstra's but applicable to a broader class of graphs.

## How It's Best Learned
Implement Bellman-Ford on a graph with negative edge weights where Dijkstra's would fail. Trace through each round of edge relaxations to see how distances converge. Test negative cycle detection by introducing a cycle with negative total weight.

## Common Misconceptions
- Bellman-Ford handles negative weights correctly; it only fails on negative-weight cycles, where shortest paths are undefined.
- The V−1 bound on iterations comes from the fact that any shortest path without cycles visits at most V−1 edges.
