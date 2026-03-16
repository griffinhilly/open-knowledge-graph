---
id: alpha-beta-pruning
title: Alpha-Beta Pruning
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: minimax-algorithm
  type: hard
tags:
- search-optimization
- adversarial-search
- pruning
stage: advanced
status: draft
---

# Alpha-Beta Pruning

## Core Idea
Alpha-beta pruning optimizes minimax by eliminating branches that provably cannot affect the final decision. Alpha represents the best score max can guarantee; beta represents the best score min can guarantee. When alpha >= beta, the branch can be pruned without changing results.

## How It's Best Learned
Trace minimax and alpha-beta on identical game trees, highlighting pruned branches and comparing node counts.

## Common Misconceptions
Alpha-beta does not change minimax results, only reduces computation. Move ordering dramatically affects pruning efficiency without requiring algorithmic changes.

## Explainer

You already know minimax: at each node in a game tree, the maximizing player picks the child with the highest value, and the minimizing player picks the child with the lowest value. The problem is that minimax explores every single leaf node, and game trees grow exponentially — a game with branching factor b and depth d has b^d leaf nodes. For chess, with an average branching factor around 35 and searches to depth 10+, evaluating every leaf is computationally prohibitive. Alpha-beta pruning makes minimax practical by proving that large portions of the tree cannot possibly affect the outcome, so they can be skipped entirely.

The intuition is straightforward. Imagine you are the maximizing player evaluating your moves. You have already found a move that guarantees you a score of at least 7 (this is your **alpha** value — the best you can guarantee so far). Now you start evaluating another move, and you discover that if you play it, the minimizer can force a score of 5. There is no reason to keep looking at this branch — you already have a better option. Symmetrically, the minimizer maintains a **beta** value representing the best (lowest) score they can guarantee. Whenever alpha ≥ beta at any node, a **cutoff** occurs: the remaining children of that node are pruned because they cannot influence the final decision. The key insight is that this pruning never changes the result — it simply avoids computing values that are provably irrelevant.

The efficiency of alpha-beta pruning depends critically on **move ordering**. In the best case, when moves happen to be examined in order from best to worst, alpha-beta reduces the effective branching factor from b to approximately √b, meaning you can search twice as deep in the same time. In the worst case (moves examined worst-first), no pruning occurs and you get the same cost as plain minimax. This is why practical game engines invest heavily in heuristic move ordering: techniques like examining captures before quiet moves in chess, using results from shallower searches (iterative deepening), or maintaining a "killer move" table that remembers which moves caused cutoffs at sibling nodes. None of these change the algorithm — they just arrange the work so that good moves are examined first, maximizing the number of branches that can be pruned.

Alpha-beta pruning is the foundation upon which modern game-playing AI is built. Even in the era of neural network evaluation (as in AlphaZero), the underlying search still uses alpha-beta variants like principal variation search or the closely related Monte Carlo tree search with value bounds. Understanding alpha-beta also builds intuition for a general principle in AI search: you do not need to explore every possibility if you can establish bounds that prove some possibilities are dominated by others. This same reasoning appears in branch-and-bound optimization, A* search, and constraint propagation.
