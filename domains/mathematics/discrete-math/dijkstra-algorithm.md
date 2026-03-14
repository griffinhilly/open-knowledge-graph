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
