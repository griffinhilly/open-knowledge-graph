---
id: simulated-annealing
title: Simulated Annealing
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: local-search-optimization
  type: hard
- id: stochastic-gradient-descent
  type: soft
tags:
- optimization
- metaheuristic
- probability
- annealing
stage: advanced
status: draft
---

# Simulated Annealing

## Core Idea
Simulated annealing probabilistically accepts worse solutions early in search (high temperature) to escape local optima, then gradually accepts only improvements (low temperature) to converge. The cooling schedule determines the algorithm's behavior: fast cooling risks getting stuck in local optima, while slow cooling wastes iterations. The algorithm is theoretically guaranteed to find the global optimum with a sufficiently slow cooling schedule.

## How It's Best Learned
Implement simulated annealing with different cooling schedules (linear, exponential, adaptive) and visualize how each affects solution quality over iterations.

## Common Misconceptions
Simulated annealing always finds the global optimum (it requires infinitely slow cooling). Temperature should always decrease (adaptive schedules may increase temperature if improvement stalls).
