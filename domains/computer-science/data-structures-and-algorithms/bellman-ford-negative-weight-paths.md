---
id: bellman-ford-negative-weight-paths
title: 'Bellman-Ford Algorithm: Shortest Paths with Negative Weights'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: dijkstras-algorithm
  type: hard
tags:
- shortest-paths
- algorithms
- negative-weights
stage: formal-systems
status: draft
---

# Bellman-Ford Algorithm: Shortest Paths with Negative Weights

## Core Idea
Bellman-Ford finds single-source shortest paths even with negative edge weights, running in O(VE) time. It relaxes all edges V-1 times; a Vth pass detecting a decreased distance indicates a negative cycle. Unlike Dijkstra, it cannot handle negative cycles gracefully but works on a broader class of graphs.

## How It's Best Learned
Implement Bellman-Ford and contrast with Dijkstra on graphs with negative weights. Observe the relaxation process and how the Vth pass detects negative cycles. Apply to currency arbitrage and difference constraints.

## Common Misconceptions
- Thinking Bellman-Ford is always slower; on sparse graphs with few edges, it can be faster than Dijkstra with binary heaps.
- Assuming negative weights are rare; they appear in many practical problems (e.g., cost/benefit models).
- Not detecting negative cycles; failing to do so yields incorrect shortest paths.
