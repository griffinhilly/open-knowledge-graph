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
stage: advanced
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

## Explainer

You already know that problem solving involves searching through a **problem space** — a graph of states connected by operators — from an initial state toward a goal state. You also know from constraint satisfaction that many problems have constrained variables where certain combinations are forbidden, and that the structure of constraints (how many neighbors each variable has, how tightly it is constrained) dramatically affects how easy or hard a problem is to solve. These two ideas — problem space search and constraint topology — combine to explain why the *direction* of search matters enormously.

**Forward search** starts from the initial state and repeatedly applies operators to generate successor states, moving toward the goal. This is the natural strategy when you know where you are but the goal is distant or underspecified. Navigating a city to an address you've never visited: you know your starting location and can generate successor positions by driving, but the goal is a fixed target you move toward. **Backward search** starts from the goal state and applies operators in reverse, generating predecessor states that could lead to the goal. This is the natural strategy when the goal is tightly constrained but the initial approach is unclear. Geometric proof problems are a classic example: the theorem to be proved is known and fixed; the question is which lemmas and axioms would yield it. Starting from the goal and asking "what would I need to have proved to get here?" generates a much smaller search tree than starting from axioms and trying to derive the theorem blindly.

The efficiency argument depends on **branching factor** — how many successor states each state generates. If the goal state has fewer successors (when reversed into predecessors) than the initial state has forward successors, backward search visits fewer nodes and is faster. In your constraint-satisfaction prerequisite, you encountered the idea that highly constrained variables should be assigned first — the **fail-first heuristic**. The same principle applies here: if the goal is the most constrained end of the problem (few legal preceding states), backward search exploits that constraint to prune the search space early. In geometry proofs, a theorem has only a few ways it can be proved; axioms can be combined in essentially unlimited ways forward. The constraint topology argument generalizes: whenever one end of the problem space is more constrained than the other, search should start at the constrained end.

In practice, sophisticated problem solvers — and AI planning systems like GPS (General Problem Solver) — use **bidirectional search**, working from both ends simultaneously and stopping when the two frontiers meet in the middle. This can reduce search complexity from exponential in the full depth to exponential in *half* the depth — a dramatic improvement. The human analog is the expert's ability to quickly assess a problem and implicitly select a search direction, or to alternate between working forward from givens and backward from the goal as intermediate subgoals are identified. This strategic flexibility — choosing search direction based on problem structure rather than habit — is one of the hallmarks that distinguishes expert problem solvers from novices who always work forward by default.
