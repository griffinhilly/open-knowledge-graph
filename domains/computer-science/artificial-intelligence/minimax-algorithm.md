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

## Explainer

Consider a game like tic-tac-toe or chess where two players alternate turns, one trying to win and the other trying to prevent it. The **minimax algorithm** treats this as a tree search problem — a natural extension of the recursive thinking and algorithm design you already know. From any game state, you recursively enumerate all possible moves, then all responses to those moves, and so on until you reach terminal states (wins, losses, or draws) that can be scored.

The key insight is that the two players have **opposing objectives**. One player (call them Max) wants the highest possible score; the other (Min) wants the lowest. At each level of the game tree, the acting player picks the move that is best *for them*. A **Max node** returns the maximum value among its children, because Max will choose the most favorable outcome. A **Min node** returns the minimum, because Min will choose the outcome most damaging to Max. Values propagate upward from the leaves — the terminal scores — through alternating max and min layers until you reach the root, which tells Max the best score achievable against a perfectly rational opponent.

This is where the "zero-sum" assumption matters: whatever Max gains, Min loses. There is no cooperation, no mutual benefit — the game is purely adversarial. The algorithm assumes **optimal play from both sides**, which means it finds the strategy that guarantees the best worst-case outcome. In tic-tac-toe, minimax proves that perfect play by both sides always ends in a draw. In more complex games, it establishes the theoretical value of positions even if the full tree is too large to search exhaustively.

The practical challenge is that game trees grow exponentially. Chess has roughly 10^40 legal positions, making full minimax search impossible. This is why minimax is typically combined with **depth-limited search** and an **evaluation function** that estimates the value of non-terminal positions, along with pruning strategies like **alpha-beta pruning** that skip branches guaranteed to be irrelevant. But the foundational logic remains the same: alternate between maximizing and minimizing at each level, assume your opponent plays as well as possible, and choose the move that leads to the best guaranteed outcome. Understanding minimax gives you the conceptual backbone for all adversarial search algorithms in AI.
