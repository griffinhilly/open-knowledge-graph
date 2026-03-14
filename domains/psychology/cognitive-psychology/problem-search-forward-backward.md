---
id: problem-search-forward-backward
title: Forward and Backward Search Strategies in Problem Solving
domain: psychology
course: cognitive-psychology
prerequisites:
- id: problem-representation-and-search
  type: hard
- id: constraint-satisfaction-problems
  type: hard
builds-toward:
- problem-solving-strategies
tags:
- problem-solving
- search
- strategy
- constraints
stage: formal-systems
status: draft
---

# Forward and Backward Search Strategies in Problem Solving

## Core Idea
Problem solving can proceed forward from the initial state toward the goal (forward search) or backward from the goal toward initial state (backward search). The efficiency of each strategy depends on the structure of the problem space: when the goal state is more constrained (fewer successor states) than the initial state, backward search is more efficient because it explores fewer nodes. Skilled problem solvers choose search direction based on implicit analysis of problem structure and constraint topology, reducing search space and enabling efficient solution finding.

## How It's Best Learned
Present well-defined problems (like the Tower of Hanoi or logic puzzles) and measure solution times and path efficiency under conditions that vary which search direction is optimal. Show how expert problem solvers implicitly choose the efficient search direction.

## Common Misconceptions
- Assuming forward search is always intuitive and necessary; backward search from goals can be far more efficient.
- Overlooking that search direction choice depends on problem structure, not problem type; the same type of problem might require different strategies depending on constraint topology.
