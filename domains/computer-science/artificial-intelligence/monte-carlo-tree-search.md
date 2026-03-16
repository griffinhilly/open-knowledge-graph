---
id: monte-carlo-tree-search
title: Monte Carlo Tree Search
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: algorithm-design-basics
  type: hard
- id: probability
  type: soft
- id: expected-value
  type: soft
tags:
- search
- monte-carlo
- games
- sampling
stage: advanced
status: draft
---

# Monte Carlo Tree Search

## Core Idea
MCTS builds a game tree incrementally through random simulations. Each iteration selects nodes using UCB, expands children, runs random playouts, and backpropagates results. It excels in large branching-factor games where evaluation functions are unavailable, balancing exploration and exploitation.

## Explainer

Traditional game-tree search algorithms like minimax require an evaluation function that can score any board position — but for games like Go, with a branching factor in the hundreds and positions that resist simple heuristic scoring, no good evaluation function exists. **Monte Carlo Tree Search** sidesteps this problem entirely: instead of evaluating a position, it plays out random games from that position and uses the win/loss statistics as a stand-in for evaluation. If you simulate a thousand random games from a position and win 700 of them, that position is probably strong — no domain-specific heuristic needed.

Each MCTS iteration follows four steps. **Selection** walks down the existing tree from the root, at each node choosing the child that maximizes the **Upper Confidence Bound (UCB1)** formula: the child's average reward plus an exploration bonus that grows when the child has been visited less often. This is the same exploration-exploitation tradeoff you know from probability and expected value — UCB ensures you do not just exploit the currently best-looking move but also explore uncertain alternatives that might turn out better. **Expansion** adds a new child node when selection reaches a leaf. **Simulation** (or rollout) plays the game to completion from that new node using a random or lightly guided policy. **Backpropagation** sends the result — win or loss — back up the tree, updating the visit counts and reward totals at every ancestor node.

The elegance of MCTS is that it is **anytime**: you can stop after ten iterations or ten million, and at any point the most-visited child of the root is your best move. With more iterations, the tree grows deeper and wider around the most promising lines of play, automatically allocating search effort where it matters most. Early iterations explore broadly; later iterations concentrate on refining the best candidates. The UCB formula guarantees that every move gets tried eventually, but clearly bad moves are quickly abandoned in favor of more promising branches.

MCTS achieved its most famous success in computer Go, where it broke through decades of stagnation in AI game-playing. When combined with neural network evaluation (as in AlphaGo), the random rollout phase is replaced by a learned value network, and the selection phase is guided by a learned policy network — but the four-phase structure remains the same. Even in its pure form without neural networks, MCTS performs remarkably well in domains with large state spaces, imperfect information, or no obvious evaluation heuristic, from game AI to planning under uncertainty.
