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
stage: expert
status: validated
---

# Extensive Form Games and Subgame Perfect Equilibrium

## Core Idea
Extensive form represents games as game trees with nodes and branches. Subgame perfect equilibrium (SPE) requires Nash equilibrium play in every subgame, eliminating non-credible threats. SPE is found by backward induction: optimize at the last decision node, then work backward. SPE is more restrictive than Nash equilibrium in strategic form, as converting to extensive form may eliminate non-credible equilibria.

## Questions

```yaml
- question: "In an entry game, the incumbent threatens to start a price war (at net loss to itself) if a rival enters. The rival stays out, and no player wants to deviate — making it a Nash equilibrium. Why does subgame perfect equilibrium reject this outcome?"
  type: multiple-choice
  options:
    - "Nash equilibrium is not defined for sequential games, so the analysis is invalid"
    - "The rival's strategy of 'stay out' is not a best response given the incumbent's threat"
    - "If entry actually occurred, the incumbent would prefer to accommodate rather than fight — the threat to fight is not credible at that decision node"
    - "The game tree has too many subgames for the equilibrium to be tractable"
  answer: 2
  explanation: "Nash equilibrium only checks that each player's overall strategy is a best response to others' overall strategies — it does not verify that the strategy remains optimal at every decision point within the game. The incumbent's threat to fight deters entry and looks fine from a global perspective, but when we examine the subgame starting *after* entry occurs, fighting is suboptimal for the incumbent (accommodation gives higher payoffs). The threat is non-credible: a rational incumbent would not actually execute it. SPE eliminates this by requiring Nash equilibrium play in every subgame, including the post-entry subgame — and in that subgame, accommodation is the only Nash equilibrium."

- question: "A game has Player 1 moving first, then Player 2, then Player 1 again. To find the subgame perfect equilibrium using backward induction, you should:"
  type: multiple-choice
  options:
    - "Start at Player 1's first move and determine the best action given predictions about all future play"
    - "Start at Player 1's final move, optimize there, then move to Player 2's decision given that, then optimize Player 1's first move given both"
    - "Find all Nash equilibria in the strategic form matrix and then apply a tie-breaking rule"
    - "Solve simultaneously for all three moves using a system of best-response equations"
  answer: 1
  explanation: "Backward induction starts at the end of the game tree — the final decision nodes — and works backward toward the root. At Player 1's last move, there are no future choices to worry about, so the optimal action is straightforward. Given Player 1 will take that action, Player 2's optimal choice at the preceding node can be determined. Given both of those, Player 1's optimal first move can be determined. Each step uses known future choices as given, ensuring credibility at every node. Starting from the first node and reasoning forward would require predicting future play without having solved for it — backward induction avoids this circularity."

- question: "Every subgame perfect equilibrium is a Nash equilibrium, but not every Nash equilibrium is subgame perfect."
  type: true-false
  answer: true
  explanation: "SPE is a refinement of Nash equilibrium — it adds the requirement that strategies must form a Nash equilibrium in every subgame, not just the overall game. Since the overall game is itself a subgame, any SPE satisfies the Nash equilibrium condition for the whole game. But Nash equilibria can be sustained by non-credible threats — strategies that are optimal globally but suboptimal at some information sets — which SPE rules out. The set of SPEs is always a subset of the set of Nash equilibria, and the subset can be strictly smaller."

- question: "Backward induction finds the subgame perfect equilibrium by starting at the first move in the game tree and optimizing forward, predicting each subsequent player's response."
  type: true-false
  answer: false
  explanation: "Backward induction works from the *last* decision nodes in the game tree backward to the first, not forward from the first. The technique starts at the terminal nodes and determines optimal play at the final decision points, then moves one step earlier, then earlier still, until the root is reached. Working forward from the first move would require anticipating future choices without having solved for them, introducing circular reasoning. The backward direction ensures that at each step, the future play is already fully determined — making each optimization self-contained and credible."

- question: "What makes a threat 'non-credible' in a sequential game, and how does subgame perfect equilibrium eliminate such threats?"
  type: short-answer
  answer: "A threat is non-credible if, at the decision node where the threatening player would actually have to act on it, executing the threat is suboptimal — they would prefer a different action if actually called upon to move. Non-credible threats can sustain Nash equilibria because Nash only checks global best responses, not point-by-point optimality. SPE eliminates non-credible threats by requiring Nash equilibrium play in every subgame: if at any decision node a threatened action would not be optimal, SPE rules out any strategy that includes that action. Backward induction implements this: at each node, the player optimizes given what will actually happen downstream, which is already determined — so only credible actions survive."
  explanation: "The classic example is the incumbent's threat to start a price war. In the global strategic form, 'threaten to fight' can look rational if it deters entry. But in the subgame beginning after entry occurs, fighting is suboptimal — so a backward-induction player will not make that threat. Any equilibrium requiring a player to take a suboptimal action at some reachable node is not subgame perfect. This is what makes SPE the standard equilibrium concept for sequential games: it rules out equilibria sustained only by threats that the threatening player would never actually carry out."
```

## Explainer

In strategic-form games, you represented interactions as a matrix of payoffs where players choose simultaneously. But many real strategic situations are sequential: one player moves first, the other observes the move, then responds. A **game tree** captures this timing explicitly. Each node represents a point where a specific player must make a decision, branches represent the available actions, and terminal nodes list the payoffs for all players. The tree structure encodes who moves when, what they know at the time, and what outcomes result from each combination of choices.

The key insight that motivates subgame perfection is that ordinary Nash equilibrium allows players to make **non-credible threats** — strategies they would never actually follow through on if called upon to act. Consider a simple entry game: an incumbent threatens to start a price war if a rival enters the market. In the strategic form, "enter, and the incumbent fights" can be a Nash equilibrium if the incumbent's threat deters entry. But look at the game tree: if entry actually happens, fighting is costly for the incumbent too. The incumbent would rationally accommodate rather than fight. The threat to fight is not credible because, at the decision node where the incumbent must act, fighting is suboptimal. Nash equilibrium does not catch this problem because it only checks that each player's overall strategy is a best response — it does not verify that the strategy remains optimal at every decision point within the game.

**Subgame perfect equilibrium** fixes this by requiring that strategies form a Nash equilibrium not just in the overall game, but in every **subgame** — every portion of the game tree that could stand alone as a well-defined game. The method for finding SPE is **backward induction**: start at the final decision nodes, determine each player's optimal choice there, then move one step earlier in the tree and optimize given that you now know what will happen downstream. Continue working backward to the root of the tree. At every step, players are choosing optimally given what will actually happen later, not what someone threatens will happen. This guarantees credibility at every decision point.

Backward induction is simple to execute in finite games of perfect information (where every player observes all previous moves). In the entry game, you start at the incumbent's node: accommodate beats fight, so the incumbent will accommodate. Moving backward, the entrant knows this, so entry is profitable, and the entrant enters. The unique SPE is (enter, accommodate) — the price war threat is pruned away. In more complex games with multiple stages, backward induction can produce strikingly different predictions than Nash equilibrium analysis of the strategic form. This refinement is foundational for analyzing sequential bargaining, Stackelberg competition, and any setting where the order of moves and the credibility of commitments determine the outcome.
