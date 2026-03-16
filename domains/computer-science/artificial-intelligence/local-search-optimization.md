---
id: local-search-optimization
title: Local Search Optimization
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: algorithm-design-basics
  type: hard
- id: greedy-algorithms
  type: soft
builds-toward:
- simulated-annealing
- genetic-algorithms
tags:
- optimization
- local-search
- hill-climbing
- metaheuristics
stage: advanced
status: draft
---

# Local Search Optimization

## Core Idea
Local search maintains a single current state and iteratively moves to neighboring states, useful for optimization problems where the path is irrelevant and only the goal state matters. Methods like hill climbing, simulated annealing, and tabu search balance exploration (escaping local optima) and exploitation (converging to good solutions). Local search trades completeness for efficiency, making it applicable to large combinatorial problems.

## How It's Best Learned
Implement hill climbing on a landscape with multiple local optima to understand the problem, then compare with simulated annealing to see how probabilistic moves help escape local optima.

## Explainer

From your work with greedy algorithms, you know the appeal of always taking the locally best option: it is fast, simple, and often surprisingly effective. **Local search optimization** takes this idea and applies it to problems where you do not care about the path to a solution — you only care about finding the best solution itself. Think of scheduling, circuit layout, or the traveling salesperson problem: nobody asks *how* you arrived at the route, only whether the route is short. Local search starts with some candidate solution, examines its "neighbors" (solutions reachable by a small change), and moves to a better one. Repeat until no neighbor improves the current state.

The simplest version is **hill climbing**: evaluate your current position, look at all neighbors, and step to the best one. It is the optimization equivalent of walking uphill in fog — you can feel the slope under your feet but cannot see the summit. The critical weakness is **local optima**: hilltops that are not the highest point in the landscape. Hill climbing will reach the top of whatever hill it starts on and stop, even if a much taller peak sits just across a valley. If you run hill climbing on a function with many bumps, the result depends heavily on where you start, and restarts with random initial states become essential.

The insight behind more sophisticated methods is that sometimes you must accept a *worse* move to eventually find a *better* solution. **Simulated annealing** borrows from metallurgy: at high "temperatures" early in the search, the algorithm frequently accepts downhill moves, allowing it to escape shallow local optima. As the temperature cools, it becomes increasingly greedy, settling into the best basin it has found. **Tabu search** takes a different approach: it maintains a memory of recently visited states and forbids returning to them, forcing the search to explore new territory even if that means temporarily moving to worse solutions. Both methods illustrate the fundamental tradeoff in optimization between **exploration** (searching broadly) and **exploitation** (refining what you have found so far).

Local search trades the guarantees of exhaustive methods — completeness, optimality — for the ability to handle problems far too large for systematic search. A brute-force search over all possible schedules for a university with thousands of courses is intractable, but local search can produce a good schedule in seconds by starting with a random assignment and iteratively swapping conflicting courses. The solutions are not provably optimal, but in practice they are often excellent, and the algorithms scale to problem sizes where no exact method is feasible.
