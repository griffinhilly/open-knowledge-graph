---
id: traveling-salesman-problem
title: Traveling Salesman Problem (TSP)
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness-formal
  type: hard
- id: graph-theory-fundamentals
  type: soft
builds-toward:
- knapsack-problem-variations
- approximation-algorithms
tags:
- optimization
- np-hard
- routing
stage: advanced
status: draft
---

# Traveling Salesman Problem (TSP)

## Core Idea
The traveling salesman problem asks for the shortest route visiting all cities exactly once and returning home. The decision version (is there a tour of length ≤ k?) is NP-complete. TSP exemplifies an optimization problem whose hardness motivates approximation algorithms: while finding the optimal tour is hard, finding a tour within a constant factor of optimal is tractable for some variants.
