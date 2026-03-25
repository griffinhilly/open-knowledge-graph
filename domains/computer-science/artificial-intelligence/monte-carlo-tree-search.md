---
id: monte-carlo-tree-search
title: Monte Carlo Tree Search
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: algorithm-design-basics
  type: hard
- id: probability-axioms
  type: soft
- id: expected-value
  type: soft
tags:
- search
- monte-carlo
- games
- sampling
stage: advanced
status: validated
---

# Monte Carlo Tree Search

## Core Idea
MCTS builds a game tree incrementally through random simulations. Each iteration selects nodes using UCB, expands children, runs random playouts, and backpropagates results. It excels in large branching-factor games where evaluation functions are unavailable, balancing exploration and exploitation.

## Questions

```yaml
- question: "A student claims MCTS evaluates board positions using a heuristic function, just like minimax. What actually happens during the simulation (rollout) phase of MCTS?"
  type: multiple-choice
  options:
    - "MCTS calls a neural network to evaluate the position and assign a score"
    - "MCTS uses the same alpha-beta pruning as minimax but in a randomized order"
    - "MCTS plays the game out to completion using a random or lightly guided policy, then uses the win/loss result as the evaluation"
    - "MCTS applies a domain-specific heuristic to estimate the probability of winning from the position"
  answer: 2
  explanation: "The key innovation of MCTS is replacing the evaluation function with random playouts. Instead of needing a heuristic that scores a board position, MCTS simulates complete games from a position — randomly or with a simple policy — and uses the win/loss outcome directly. If you win 700 out of 1000 random games from a position, that position is estimated as strong. This is why MCTS works so well in Go and other domains where good evaluation functions do not exist: it requires no domain-specific scoring knowledge."

- question: "After running MCTS for a fixed time budget, how do you select which move to actually play?"
  type: multiple-choice
  options:
    - "Choose the child of the root with the highest UCB1 score, since that balances value and exploration"
    - "Choose the child of the root that was visited most often, as visit count reflects accumulated confidence"
    - "Choose the child of the root with the highest average reward, regardless of visit count"
    - "Choose a random child, weighted by each child's average reward"
  answer: 1
  explanation: "At decision time, you choose the most-visited child of the root — not the highest UCB1 score and not the highest average reward. The UCB1 formula is used during tree traversal to balance exploration and exploitation while building the tree. But at the end, visit count is the most reliable signal: a move that has been visited many times has had its average reward estimate refined by many simulations. A move with high average reward but few visits might be a statistical fluke. The most-visited child represents the algorithm's most confident recommendation."

- question: "MCTS requires that the game be played to a terminal state before any useful information is obtained, meaning it cannot return a move recommendation until the search is complete."
  type: true-false
  answer: false
  explanation: "MCTS is an 'anytime' algorithm — at any point during the search, the most-visited child of the root is a valid move recommendation. You can stop after 10 iterations or 10 million, and the algorithm will give you its best current estimate. This is a significant practical advantage: in time-constrained settings (like competitive game play), you run MCTS for the available time budget and then immediately use the current recommendation. The recommendation simply improves with more iterations."

- question: "The UCB1 formula in MCTS selects moves with high average reward but also adds an exploration bonus for moves that have been visited less often."
  type: true-false
  answer: true
  explanation: "UCB1 = (average reward) + C × √(ln(parent visits) / child visits). The first term exploits what is currently known — prefer moves that have won often. The second term explores — the bonus grows as a child is visited less relative to its parent, ensuring that underexplored moves are eventually tried. This mirrors the exploration-exploitation tradeoff from multi-armed bandit problems. Without the exploration bonus, MCTS would greedily concentrate on the first move that looks good and never discover better alternatives."

- question: "Explain how the UCB formula in MCTS prevents the algorithm from permanently ignoring a move that happened to lose in its first few simulations."
  type: short-answer
  answer: "The UCB1 formula includes an exploration bonus that grows as a node's visit count falls behind its siblings. When a move has been tried only a few times, the exploration term is large, making UCB1 artificially inflate its apparent value and forcing the algorithm to revisit it. Only after a move accumulates enough visits to give its average reward a statistically reliable estimate will the exploration bonus shrink relative to the exploitation term. This guarantees that every legal move is eventually explored, and clearly bad moves are only 'abandoned' gradually — they still get occasional visits, but far fewer than promising moves."
  explanation: "This is the core contribution of UCB to MCTS. Pure exploitation (always pick the highest average reward) gets stuck on local optima. Pure exploration (visit everything equally) wastes effort on clearly bad moves. UCB1 — adapted from the multi-armed bandit literature — is provably near-optimal for balancing these concerns, ensuring the total regret grows only logarithmically with the number of iterations."
```

## Explainer

Traditional game-tree search algorithms like minimax require an evaluation function that can score any board position — but for games like Go, with a branching factor in the hundreds and positions that resist simple heuristic scoring, no good evaluation function exists. **Monte Carlo Tree Search** sidesteps this problem entirely: instead of evaluating a position, it plays out random games from that position and uses the win/loss statistics as a stand-in for evaluation. If you simulate a thousand random games from a position and win 700 of them, that position is probably strong — no domain-specific heuristic needed.

Each MCTS iteration follows four steps. **Selection** walks down the existing tree from the root, at each node choosing the child that maximizes the **Upper Confidence Bound (UCB1)** formula: the child's average reward plus an exploration bonus that grows when the child has been visited less often. This is the same exploration-exploitation tradeoff you know from probability and expected value — UCB ensures you do not just exploit the currently best-looking move but also explore uncertain alternatives that might turn out better. **Expansion** adds a new child node when selection reaches a leaf. **Simulation** (or rollout) plays the game to completion from that new node using a random or lightly guided policy. **Backpropagation** sends the result — win or loss — back up the tree, updating the visit counts and reward totals at every ancestor node.

The elegance of MCTS is that it is **anytime**: you can stop after ten iterations or ten million, and at any point the most-visited child of the root is your best move. With more iterations, the tree grows deeper and wider around the most promising lines of play, automatically allocating search effort where it matters most. Early iterations explore broadly; later iterations concentrate on refining the best candidates. The UCB formula guarantees that every move gets tried eventually, but clearly bad moves are quickly abandoned in favor of more promising branches.

MCTS achieved its most famous success in computer Go, where it broke through decades of stagnation in AI game-playing. When combined with neural network evaluation (as in AlphaGo), the random rollout phase is replaced by a learned value network, and the selection phase is guided by a learned policy network — but the four-phase structure remains the same. Even in its pure form without neural networks, MCTS performs remarkably well in domains with large state spaces, imperfect information, or no obvious evaluation heuristic, from game AI to planning under uncertainty.
