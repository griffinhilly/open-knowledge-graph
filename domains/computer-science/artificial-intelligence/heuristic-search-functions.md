---
id: heuristic-search-functions
title: Heuristic Search Functions
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: astar-search-algorithm
  type: hard
- id: greedy-algorithms
  type: soft
builds-toward:
- local-search-optimization
- constraint-propagation
tags:
- search
- heuristics
- admissibility
- optimization
stage: advanced
status: draft
---

# Heuristic Search Functions

## Core Idea
Heuristic functions estimate the cost from a state to the goal without exploring the full search space, enabling guided search. Well-designed heuristics must be admissible (never overestimate) to guarantee optimal solutions, and consistent heuristics satisfy the triangle inequality to enable efficient pruning. The quality of the heuristic determines whether A* will terminate quickly or explore exponentially many states.

## How It's Best Learned
Study examples of admissible heuristics like Manhattan distance for grid puzzles and implement A* with different heuristics to observe how heuristic quality affects search performance.

## Common Misconceptions
A faster heuristic is always better (domination matters: h1 dominates h2 if h1(s) ≥ h2(s) for all s). Optimality requires admissibility, not just consistency.

## Explainer

From your study of A* search, you know that A* evaluates nodes using f(n) = g(n) + h(n), where g(n) is the cost so far and h(n) is the heuristic estimate of the remaining cost to the goal. The entire performance of A* — whether it finds the optimal solution quickly or degenerates into exhaustive search — hinges on the quality of h(n). A heuristic function is your way of injecting problem-specific knowledge into a general search algorithm, telling it which directions look promising without actually exploring them.

The most important property of a heuristic is **admissibility**: h(n) must never overestimate the true cost to reach the goal. If h always underestimates (or exactly equals) the true remaining cost, A* is guaranteed to find the optimal solution. Intuitively, an admissible heuristic is optimistic — it never makes a path look worse than it actually is, so A* will never dismiss the optimal path prematurely. The trivial heuristic h(n) = 0 is always admissible (it is maximally optimistic), but it gives A* no guidance, reducing it to Dijkstra's algorithm. The ideal heuristic would equal the true cost exactly — then A* would march straight to the goal without exploring a single unnecessary node. Real heuristics fall between these extremes.

Consider the 8-puzzle (sliding tiles). Two classic heuristics are **misplaced tiles** (count how many tiles are not in their goal position) and **Manhattan distance** (sum the number of horizontal and vertical moves each tile needs to reach its goal position). Both are admissible because neither can overestimate — a tile that is out of place needs at least one move, and the Manhattan distance of each tile is a lower bound on its actual moves because it ignores the constraint that other tiles block the way. Manhattan distance **dominates** misplaced tiles: for every state, Manhattan distance is greater than or equal to misplaced tiles. This domination is precisely what makes it the better heuristic. A dominating heuristic is closer to the true cost, so A* expands fewer nodes — it has tighter guidance about which paths to pursue.

A stronger property than admissibility is **consistency** (also called monotonicity): for every node n and successor n', the heuristic satisfies h(n) ≤ cost(n, n') + h(n'). This is the triangle inequality — the estimated cost from n to the goal should not exceed the cost of stepping to n' plus the estimate from n'. Consistent heuristics guarantee that when A* expands a node, it has already found the optimal path to that node, so nodes never need to be re-expanded. Every consistent heuristic is admissible, but not every admissible heuristic is consistent (though counterexamples are rare in practice). When designing heuristics, a powerful technique is **relaxation**: remove some constraints from the original problem, solve the easier version, and use its cost as h(n). Manhattan distance, for instance, is the exact solution to a relaxed 8-puzzle where tiles can pass through each other. This relaxation approach systematically generates admissible heuristics for any problem where you can formalize the constraints.
