---
id: dijkstra-algorithm
title: Dijkstra's Shortest Path Algorithm
domain: mathematics
course: discrete-math
prerequisites:
- id: shortest-paths-unweighted-graphs
  type: hard
- id: big-o-notation
  type: soft
tags:
- shortest-paths
- algorithms
- weighted-graphs
stage: formal-systems
status: draft
---

# Dijkstra's Shortest Path Algorithm

## Core Idea
Dijkstra's algorithm finds the shortest path in a weighted graph with non-negative edge weights using a greedy approach: always extend the shortest known path. Using a priority queue, it runs in O((V+E) log V) time and is widely applied in GPS navigation and routing.

## Explainer

You already know how to find shortest paths in an unweighted graph using BFS — explore layer by layer, and the first time you reach a node is guaranteed to be the shortest. But BFS only works because every edge has the same "cost" (1). Once edges have different weights, a path with more hops might actually be cheaper than a path with fewer. Dijkstra's algorithm solves this generalization by replacing BFS's queue with a **priority queue** (min-heap), always processing whichever unvisited node currently has the smallest known total distance from the source.

The algorithm maintains a table of "best known distances" to every node, all initialized to infinity except the source node which starts at 0. Each round, you pull out the node with the smallest distance, then examine all its neighbors. For each neighbor, you compute the candidate distance: (distance to current node) + (edge weight to neighbor). If this candidate is better than what's already recorded for that neighbor, you update the table — this is called **relaxing an edge**. Repeat until all nodes are settled. The insight behind correctness is the greedy guarantee: once a node is pulled from the priority queue, its recorded distance is final. This works because all edge weights are non-negative — no future path through other nodes can be shorter, since distances can only increase as you add more edges.

Consider a simple road network where you want to drive from city A to city D. Direct path A→D costs 10. Alternatively, A→B costs 2, B→C costs 3, C→D costs 4 — a total of 9. BFS would find A→D first (one hop) and call it optimal. Dijkstra correctly discovers the three-hop path is cheaper. It does this by settling A first, then B (distance 2), then C (distance 5), then D via C (distance 9), only then seeing that the direct A→D edge gives distance 10, which is worse.

The non-negative weight requirement is not a minor technicality — it's load-bearing. If negative edges existed, settling a node would no longer be final: a later path going through a negative edge could undercut an already-settled distance. For graphs with negative weights, the **Bellman-Ford algorithm** handles this correctly (at higher cost: O(VE)). The O((V+E) log V) complexity of Dijkstra comes from performing up to E edge relaxations, each of which requires a priority queue update costing O(log V). This efficiency makes it practical for real-world networks with millions of nodes, which is why it underlies GPS routing, internet packet forwarding (OSPF), and shortest-path queries in maps.
