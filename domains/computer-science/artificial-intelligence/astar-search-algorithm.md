---
id: astar-search-algorithm
title: A* Search Algorithm
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: breadth-first-search
  type: hard
- id: dijkstras-algorithm
  type: hard
tags:
- search
- graphs
- pathfinding
- heuristics
stage: advanced
status: draft
---

# A* Search Algorithm

## Core Idea
A* combines actual path cost with heuristic estimates of remaining cost to find optimal paths efficiently. It uses f(n) = g(n) + h(n), where g(n) is the cost to reach node n and h(n) estimates cost to goal. A* is complete and optimal when h(n) is admissible.

## Explainer

You already know two graph search algorithms that A* builds on directly. **Breadth-first search** (BFS) explores nodes in order of their depth from the start — it finds the shortest path in terms of number of edges, but it ignores edge weights entirely. **Dijkstra's algorithm** fixes this by always expanding the node with the lowest accumulated cost g(n) — it finds the truly cheapest path, but it explores outward uniformly in all directions, wasting effort on paths heading away from the goal. A* combines the best of both worlds by adding a **heuristic function** h(n) that estimates how far node n is from the goal, directing the search toward promising areas of the graph.

The evaluation function **f(n) = g(n) + h(n)** is what makes A* work. Here g(n) is the actual cost of the cheapest known path from the start to node n (just like Dijkstra's), and h(n) is your best guess of the remaining cost from n to the goal. A* maintains a priority queue ordered by f(n) and always expands the node with the smallest f value. Think of it as answering the question: "Which unexplored node is on the most promising total path?" If h(n) = 0 for all nodes, A* degenerates into Dijkstra's algorithm. If g(n) = 0, it becomes a pure greedy best-first search that chases the heuristic without accounting for cost already spent.

The key property that guarantees A* finds the optimal path is **admissibility**: the heuristic must never overestimate the true cost to the goal. For pathfinding on a map, the straight-line (Euclidean) distance is admissible because you can never get somewhere faster than a straight line. Manhattan distance is admissible on a grid where you can only move in four directions. When h(n) is admissible, A* will never prematurely commit to a suboptimal path — it may explore a node with a slightly higher g(n) if the heuristic suggests the total path through it could still be cheaper. A stronger property, **consistency** (or monotonicity), requires that h(n) ≤ cost(n, n') + h(n') for every edge. Consistent heuristics guarantee that once A* expands a node, it has already found the optimal path to that node, eliminating the need to re-open closed nodes.

The practical performance of A* depends almost entirely on the quality of the heuristic. A tighter (closer to true cost) but still admissible heuristic prunes more of the search space, making A* dramatically faster. In the best case, a perfect heuristic leads A* straight to the goal along the optimal path with no wasted exploration. In the worst case (h = 0 everywhere), it examines every node Dijkstra's would. This is why designing good heuristics is the central challenge when applying A* — the algorithm itself is simple, but its effectiveness is only as good as the heuristic guiding it. A* is used extensively in game AI for pathfinding, in robotics for motion planning, and in any domain where you need optimal paths through weighted graphs and have domain knowledge to estimate remaining costs.
