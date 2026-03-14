---
id: cycle-detection-directed-graphs
title: Cycle Detection in Directed Graphs
domain: mathematics
course: discrete-math
prerequisites:
- id: directed-graphs-and-digraphs
  type: hard
builds-toward:
- directed-acyclic-graphs
- strongly-connected-components
tags:
- directed-graphs
- cycles
- algorithms
stage: formal-systems
status: draft
---

# Cycle Detection in Directed Graphs

## Core Idea
Cycle detection determines whether a directed graph contains any cycles. Algorithms like DFS-based backtracking identify cycles by marking vertices as visited, visiting, and done. Detecting cycles is essential for deadlock detection, dependency validation, and proving acyclicity.
