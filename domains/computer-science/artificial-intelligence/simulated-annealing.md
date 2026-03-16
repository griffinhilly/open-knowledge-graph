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

## Explainer

From local search optimization, you know the fundamental problem: hill climbing finds a local optimum but gets stuck there, unable to reach a potentially better solution elsewhere in the search space. Imagine you are hiking in fog and can only feel the slope beneath your feet. Hill climbing always walks uphill, so you reach the nearest peak — but it might be a small hill when a mountain is just across the valley. Simulated annealing solves this by occasionally allowing downhill steps, especially early in the search, giving the algorithm a chance to escape local optima and explore the broader landscape.

The key mechanism is the **acceptance probability**. When simulated annealing considers a neighboring solution, it always accepts improvements (moves to a better solution). But when the neighbor is *worse*, it accepts the move with probability exp(−ΔE / T), where ΔE is how much worse the neighbor is and T is the current **temperature**. This formula comes from statistical mechanics — it models how atoms in a heated metal occasionally jump to higher-energy configurations. At high temperature, exp(−ΔE / T) is close to 1, so almost any move is accepted, and the algorithm wanders freely through the search space. As temperature decreases, the probability of accepting worse moves drops, and the algorithm increasingly behaves like pure hill climbing, settling into a good solution.

The **cooling schedule** controls how temperature decreases over time and is the most important design choice. A common schedule is geometric cooling: T_new = α · T_old, where α is typically between 0.9 and 0.999. Fast cooling (low α, or few iterations) behaves almost like hill climbing — you barely explore before settling. Slow cooling (high α, or many iterations) gives the algorithm time to escape traps but takes longer to converge. The theoretical guarantee is striking: with an infinitely slow cooling schedule (specifically, T(t) ≥ C / log(t)), simulated annealing converges to the global optimum with probability 1. In practice, you never cool this slowly, so you trade guaranteed optimality for a good-enough solution in reasonable time.

Simulated annealing shines on combinatorial optimization problems where the search space is too large for exhaustive search and too rugged for gradient-based methods. Classic applications include the traveling salesman problem, circuit layout, and scheduling. The algorithm requires only three things: a way to represent solutions, a way to generate neighboring solutions, and a way to evaluate solution quality. It needs no gradient, no differentiability, and no assumptions about the structure of the search space. The tradeoff is that tuning the cooling schedule, initial temperature, and neighborhood structure requires experimentation — there is no single recipe that works for all problems.
