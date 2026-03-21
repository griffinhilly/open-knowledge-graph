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

## Questions

```yaml
- question: "The maximizing player has already found a move guaranteeing a score of at least 7 (alpha = 7). While evaluating a different branch, it discovers the minimizing player can force a score of 5 from that branch. What should alpha-beta pruning do?"
  type: multiple-choice
  options:
    - "Continue exploring remaining children of this branch to find the exact minimax value"
    - "Prune the remaining children of this branch — the maximizer would never choose it over the guaranteed score of 7"
    - "Update alpha to 5 and continue, since 5 is now the new best guaranteed outcome"
    - "Update beta to 7, indicating the maximizer has a better option available"
  answer: 1
  explanation: "This is the core alpha-beta cutoff condition. The maximizer already has an option guaranteeing 7; this new branch lets the minimizer force 5, which is worse for the maximizer. No matter how good the remaining children of this branch might be, the minimizer would choose the 5-option or worse — so the maximizer would never prefer this branch over its guaranteed 7. Pruning the remaining children saves computation without changing the result. Option C is wrong — alpha represents a floor for the maximizer and should only increase, not decrease."

- question: "In the best case, alpha-beta pruning reduces the effective branching factor of a minimax search from b to approximately:"
  type: multiple-choice
  options:
    - "b/2 — half the branches are pruned on average"
    - "b^(2/3) — a two-thirds reduction in branching factor"
    - "√b — allowing the search to reach twice the depth in the same time"
    - "log(b) — a logarithmic reduction corresponding to the tree depth"
  answer: 2
  explanation: "In the best case — when moves are examined in perfect order from best to worst — alpha-beta pruning reduces the effective branching factor to approximately √b. This means the algorithm can search to roughly twice the depth in the same time compared to plain minimax. For chess with branching factor ~35, this means reaching depth 10 instead of 5 with the same node budget. Achieving this best case requires optimal move ordering, which is why practical engines invest heavily in heuristics to examine the most promising moves first."

- question: "Alpha-beta pruning always produces the same final move decision as plain minimax, regardless of how moves are ordered."
  type: true-false
  answer: true
  explanation: "This is the key correctness guarantee of alpha-beta pruning. It is purely a computational optimization — it prunes branches that are provably irrelevant because no value from those subtrees could change the maximizer's or minimizer's decision. The cutoff condition (alpha ≥ beta) guarantees that any pruned subtree cannot contain a better option than what is already established. The final move decision is identical to what plain minimax would return; if it ever differed, that would indicate a bug."

- question: "Alpha-beta pruning changes the move that minimax would select, which is why game-playing engines prefer it over plain minimax."
  type: true-false
  answer: false
  explanation: "This is a fundamental misconception. Alpha-beta pruning produces exactly the same optimal move as plain minimax — it does not change the result at all. Its advantage is purely computational: it reaches the same answer while examining far fewer nodes, allowing deeper searches within the same time budget. Deeper searches produce stronger play, which is why engines prefer alpha-beta. But the algorithm is not finding a different or better move than minimax would find at the same depth — it is finding the exact same move, faster."

- question: "Why does move ordering dramatically affect alpha-beta pruning efficiency, and how do practical game engines exploit this without changing the underlying algorithm?"
  type: short-answer
  answer: "Alpha-beta cutoffs occur when the current node's value is provably outside the range that could matter (when alpha ≥ beta). If the best moves are examined first, alpha and beta bounds tighten quickly, enabling cutoffs early and often — large subtrees get pruned. If moves are examined worst-first, bounds tighten slowly, cutoffs are rare, and performance degrades to plain minimax. Practical engines improve move ordering through iterative deepening (using results from shallower searches to order moves in deeper ones), killer move heuristics (trying moves that caused cutoffs at sibling nodes), and history tables (tracking which moves have historically been effective). All of these remain within the alpha-beta framework — they only rearrange which children are examined first."
  explanation: "The insight that the same algorithm's performance varies dramatically with input ordering is a general lesson in algorithm design. Alpha-beta is an extreme case: best-case and worst-case performance differ by a factor of b (the branching factor), depending entirely on move ordering. This is why move ordering is as important as the pruning algorithm itself in practical implementations."
```

## Explainer

You already know minimax: at each node in a game tree, the maximizing player picks the child with the highest value, and the minimizing player picks the child with the lowest value. The problem is that minimax explores every single leaf node, and game trees grow exponentially — a game with branching factor b and depth d has b^d leaf nodes. For chess, with an average branching factor around 35 and searches to depth 10+, evaluating every leaf is computationally prohibitive. Alpha-beta pruning makes minimax practical by proving that large portions of the tree cannot possibly affect the outcome, so they can be skipped entirely.

The intuition is straightforward. Imagine you are the maximizing player evaluating your moves. You have already found a move that guarantees you a score of at least 7 (this is your **alpha** value — the best you can guarantee so far). Now you start evaluating another move, and you discover that if you play it, the minimizer can force a score of 5. There is no reason to keep looking at this branch — you already have a better option. Symmetrically, the minimizer maintains a **beta** value representing the best (lowest) score they can guarantee. Whenever alpha ≥ beta at any node, a **cutoff** occurs: the remaining children of that node are pruned because they cannot influence the final decision. The key insight is that this pruning never changes the result — it simply avoids computing values that are provably irrelevant.

The efficiency of alpha-beta pruning depends critically on **move ordering**. In the best case, when moves happen to be examined in order from best to worst, alpha-beta reduces the effective branching factor from b to approximately √b, meaning you can search twice as deep in the same time. In the worst case (moves examined worst-first), no pruning occurs and you get the same cost as plain minimax. This is why practical game engines invest heavily in heuristic move ordering: techniques like examining captures before quiet moves in chess, using results from shallower searches (iterative deepening), or maintaining a "killer move" table that remembers which moves caused cutoffs at sibling nodes. None of these change the algorithm — they just arrange the work so that good moves are examined first, maximizing the number of branches that can be pruned.

Alpha-beta pruning is the foundation upon which modern game-playing AI is built. Even in the era of neural network evaluation (as in AlphaZero), the underlying search still uses alpha-beta variants like principal variation search or the closely related Monte Carlo tree search with value bounds. Understanding alpha-beta also builds intuition for a general principle in AI search: you do not need to explore every possibility if you can establish bounds that prove some possibilities are dominated by others. This same reasoning appears in branch-and-bound optimization, A* search, and constraint propagation.
