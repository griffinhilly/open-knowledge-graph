---
id: minimax-algorithm
title: Minimax Algorithm
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: algorithm-design-basics
  type: hard
- id: recursion-basics
  type: hard
- id: proof-by-cases
  type: soft
tags:
- adversarial-search
- games
- game-theory
stage: advanced
status: draft
---

# Minimax Algorithm

## Core Idea
Minimax is a recursive algorithm for two-player zero-sum games where one player maximizes utility and the other minimizes it. Values propagate from leaves: max nodes return the maximum child value, min nodes return the minimum. The algorithm assumes both players play optimally.

## Questions

```yaml
- question: "In a minimax tree, a Min node has three children with values −5, 3, and 0. What value does the Min node return?"
  type: multiple-choice
  options:
    - "3, because Max always wants the highest value"
    - "−5, because Min picks the child value lowest for Max"
    - "0, because the algorithm averages across children"
    - "−5 only if it is the leftmost child; otherwise the first child encountered"
  answer: 1
  explanation: "At a Min node, the minimizing player picks the move leading to the outcome worst for Max — so the node returns the minimum child value, −5. Returning the average or the maximum would contradict the assumption of optimal play: the minimizing player will never choose an outcome better for Max when a worse one is available."

- question: "A minimax search finds that Move A guarantees a score of +1.5 against a perfect opponent, while Move B leads to +3 if the opponent blunders but −2 if the opponent plays optimally. Which move does minimax recommend, and why?"
  type: multiple-choice
  options:
    - "Move B — it has higher upside and the algorithm should maximize expected value"
    - "Move A — it guarantees the better outcome against optimal play"
    - "Move B — minimax explores all branches and prefers the one with the highest leaf value"
    - "Move A — but only because Move B has a longer search depth"
  answer: 1
  explanation: "Minimax assumes the opponent plays optimally. Under that assumption, Move B leads to −2 (the opponent will find the refutation), while Move A guarantees +1.5. The algorithm recommends Move A because it maximizes the worst-case outcome. Move B's +3 upside is irrelevant — it is only reachable if the opponent makes a mistake, which the algorithm does not assume. This is the core meaning of 'minimax': maximize the minimum outcome."

- question: "The minimax algorithm finds the move that leads to the best possible outcome for the maximizing player."
  type: true-false
  answer: false
  explanation: "Minimax finds the best *guaranteed* outcome against a perfectly rational opponent — the move that maximizes the worst case. The 'best possible' outcome might be achievable only if the opponent blunders. Minimax explicitly assumes the opponent plays optimally and finds the strategy that is safe against that assumption. A player who optimizes for the best possible outcome (ignoring opponent rationality) is playing a different and riskier strategy."

- question: "In a zero-sum two-player game, the outcome that maximizes the score for the Max player is simultaneously the worst outcome for the Min player."
  type: true-false
  answer: true
  explanation: "This is the defining property of a zero-sum game: the players' utilities sum to a constant (often zero). Whatever Max gains, Min loses by exactly that amount. There is no outcome where both benefit, so the Max-optimal outcome and the Min-worst outcome are always the same state. This is precisely why the minimax logic works: choosing the highest value for Max is identical to choosing the worst value from Min's perspective."

- question: "Why does the minimax algorithm assume optimal play from both sides, and what would be the consequence of not making this assumption?"
  type: short-answer
  answer: "Assuming optimal play from both sides guarantees the best worst-case outcome — a strategy that is safe regardless of how well the opponent actually plays. If the algorithm assumed a weak opponent and chose moves that exploit expected blunders, it would be vulnerable to strong play: those same moves might be easily refuted, leading to worse outcomes than the 'safe' minimax choice. By preparing for the hardest possible opponent, minimax produces a strategy that degrades gracefully — it does no worse than expected against a perfect opponent and may do better against a weaker one."
  explanation: "This connects minimax to game theory's concept of a maximin strategy — the strategy that maximizes the minimum payoff. Real-world chess engines use minimax (with alpha-beta pruning) as a foundation precisely because preparation for optimal opposition is the correct competitive stance when the opponent's actual strength is unknown."
```

## Explainer

Consider a game like tic-tac-toe or chess where two players alternate turns, one trying to win and the other trying to prevent it. The **minimax algorithm** treats this as a tree search problem — a natural extension of the recursive thinking and algorithm design you already know. From any game state, you recursively enumerate all possible moves, then all responses to those moves, and so on until you reach terminal states (wins, losses, or draws) that can be scored.

The key insight is that the two players have **opposing objectives**. One player (call them Max) wants the highest possible score; the other (Min) wants the lowest. At each level of the game tree, the acting player picks the move that is best *for them*. A **Max node** returns the maximum value among its children, because Max will choose the most favorable outcome. A **Min node** returns the minimum, because Min will choose the outcome most damaging to Max. Values propagate upward from the leaves — the terminal scores — through alternating max and min layers until you reach the root, which tells Max the best score achievable against a perfectly rational opponent.

This is where the "zero-sum" assumption matters: whatever Max gains, Min loses. There is no cooperation, no mutual benefit — the game is purely adversarial. The algorithm assumes **optimal play from both sides**, which means it finds the strategy that guarantees the best worst-case outcome. In tic-tac-toe, minimax proves that perfect play by both sides always ends in a draw. In more complex games, it establishes the theoretical value of positions even if the full tree is too large to search exhaustively.

The practical challenge is that game trees grow exponentially. Chess has roughly 10^40 legal positions, making full minimax search impossible. This is why minimax is typically combined with **depth-limited search** and an **evaluation function** that estimates the value of non-terminal positions, along with pruning strategies like **alpha-beta pruning** that skip branches guaranteed to be irrelevant. But the foundational logic remains the same: alternate between maximizing and minimizing at each level, assume your opponent plays as well as possible, and choose the move that leads to the best guaranteed outcome. Understanding minimax gives you the conceptual backbone for all adversarial search algorithms in AI.
