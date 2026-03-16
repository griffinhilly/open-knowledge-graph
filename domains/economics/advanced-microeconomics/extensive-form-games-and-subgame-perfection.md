---
id: extensive-form-games-and-subgame-perfection
title: Extensive Form Games and Subgame Perfect Equilibrium
domain: economics
course: advanced-microeconomics
prerequisites:
- id: strategic-form-games
  type: hard
builds-toward:
- stackelberg-competition
tags:
- game-theory
- sequential-play
stage: advanced
status: draft
---

# Extensive Form Games and Subgame Perfect Equilibrium

## Core Idea
Extensive form represents games as game trees with nodes and branches. Subgame perfect equilibrium (SPE) requires Nash equilibrium play in every subgame, eliminating non-credible threats. SPE is found by backward induction: optimize at the last decision node, then work backward. SPE is more restrictive than Nash equilibrium in strategic form, as converting to extensive form may eliminate non-credible equilibria.

## Explainer

In strategic-form games, you represented interactions as a matrix of payoffs where players choose simultaneously. But many real strategic situations are sequential: one player moves first, the other observes the move, then responds. A **game tree** captures this timing explicitly. Each node represents a point where a specific player must make a decision, branches represent the available actions, and terminal nodes list the payoffs for all players. The tree structure encodes who moves when, what they know at the time, and what outcomes result from each combination of choices.

The key insight that motivates subgame perfection is that ordinary Nash equilibrium allows players to make **non-credible threats** — strategies they would never actually follow through on if called upon to act. Consider a simple entry game: an incumbent threatens to start a price war if a rival enters the market. In the strategic form, "enter, and the incumbent fights" can be a Nash equilibrium if the incumbent's threat deters entry. But look at the game tree: if entry actually happens, fighting is costly for the incumbent too. The incumbent would rationally accommodate rather than fight. The threat to fight is not credible because, at the decision node where the incumbent must act, fighting is suboptimal. Nash equilibrium does not catch this problem because it only checks that each player's overall strategy is a best response — it does not verify that the strategy remains optimal at every decision point within the game.

**Subgame perfect equilibrium** fixes this by requiring that strategies form a Nash equilibrium not just in the overall game, but in every **subgame** — every portion of the game tree that could stand alone as a well-defined game. The method for finding SPE is **backward induction**: start at the final decision nodes, determine each player's optimal choice there, then move one step earlier in the tree and optimize given that you now know what will happen downstream. Continue working backward to the root of the tree. At every step, players are choosing optimally given what will actually happen later, not what someone threatens will happen. This guarantees credibility at every decision point.

Backward induction is simple to execute in finite games of perfect information (where every player observes all previous moves). In the entry game, you start at the incumbent's node: accommodate beats fight, so the incumbent will accommodate. Moving backward, the entrant knows this, so entry is profitable, and the entrant enters. The unique SPE is (enter, accommodate) — the price war threat is pruned away. In more complex games with multiple stages, backward induction can produce strikingly different predictions than Nash equilibrium analysis of the strategic form. This refinement is foundational for analyzing sequential bargaining, Stackelberg competition, and any setting where the order of moves and the credibility of commitments determine the outcome.
