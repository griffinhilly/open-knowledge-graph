---
id: dijkstras-algorithm
title: 'Dijkstra''s Algorithm'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: heaps-and-priority-queues
  type: hard
- id: breadth-first-search
  type: hard
- id: graph-representation
  type: hard
- id: graph-theory-intro
  type: soft
- id: greedy-algorithms
  type: soft
builds-toward:
- bellman-ford-algorithm
tags:
- shortest-path
- Dijkstra
- weighted-graph
- greedy
stage: formal-systems
status: validated
---
# Dijkstra's Algorithm

## Core Idea
Dijkstra's algorithm finds the shortest path from a source vertex to all other vertices in a weighted graph with non-negative edge weights. It uses a greedy strategy with a priority queue: always extend the shortest known tentative path first. With a binary heap, the algorithm runs in O((V + E) log V). The algorithm maintains a distance array and relaxes edges by updating distances when a shorter path is discovered. It is the workhorse of navigation systems, network routing, and game AI pathfinding.

## How It's Best Learned
Implement Dijkstra's using Python's heapq module. Trace through a small weighted graph manually, tracking the priority queue state and distance table at each step. Add path reconstruction using a previous-node array.

## Common Misconceptions
- Dijkstra's fails with negative edge weights; use Bellman-Ford instead.
- The algorithm is greedy and correct because non-negative weights guarantee that once a node's shortest distance is finalized it cannot later be improved.
- With a Fibonacci heap the complexity improves to O(V log V + E), but binary heaps are used in practice due to simpler implementation.
