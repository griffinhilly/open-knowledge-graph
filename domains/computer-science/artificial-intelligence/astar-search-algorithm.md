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
