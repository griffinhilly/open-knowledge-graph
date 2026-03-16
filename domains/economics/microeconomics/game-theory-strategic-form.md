---
id: game-theory-strategic-form
title: Game Theory and Strategic Form Analysis
domain: economics
course: microeconomics
prerequisites:
- id: game-theory-basics-microeconomics
  type: hard
- id: nash-equilibrium-microeconomics
  type: hard
builds-toward:
- bayesian-games-strategy
tags:
- game theory
- strategy
- equilibrium
stage: abstract-reasoning
status: draft
---

# Game Theory and Strategic Form Analysis

## Core Idea
Strategic form represents simultaneous-move games as payoff matrices. Nash equilibrium occurs when each player's strategy is optimal given others' strategies (no unilateral improvement incentive). Pure strategy equilibrium is a cell where neither player wants to deviate; mixed strategy involves randomizing. Multiple equilibria, no equilibrium, or unique solutions can arise depending on payoff structure. Dominated strategies can be iteratively eliminated.

## Explainer

The **strategic form** (also called **normal form**) is the simplest mathematical structure for representing a game. You list all players, all the strategies available to each player, and the payoffs each player receives for every combination of strategy choices. For two players, this becomes a matrix: rows are Player 1's strategies, columns are Player 2's strategies, and each cell contains the payoff pair (Row's payoff, Column's payoff). The beauty of this representation is that it strips away timing and sequential structure — it captures pure strategic interaction when players choose simultaneously without seeing each other's move.

Your prerequisite on Nash equilibrium gives you the central solution concept. A **Nash equilibrium** (NE) is a strategy profile — one strategy choice per player — where no player can improve their payoff by unilaterally switching to a different strategy, given what the other player is doing. In matrix form, you find a NE by checking each cell: would Player 1 want to switch rows given Column is fixed? Would Player 2 want to switch columns given Row is fixed? If neither wants to deviate, you have a Nash equilibrium. A **pure strategy NE** is a specific cell that satisfies this condition. Some games have no pure strategy NE; many have one; some have multiple.

When no pure strategy NE exists, players may play **mixed strategies** — probability distributions over their pure strategies. In a mixed NE, each player randomizes in a way that makes the other player indifferent between their available strategies. The classic example is Rock-Paper-Scissors: if your opponent plays each option with probability 1/3, you have no incentive to favor any single strategy, and the same logic applies in reverse. Mixed strategies expand the set of equilibria and ensure that finite games always have at least one (Nash's theorem).

A powerful analytical tool is **iterated elimination of dominated strategies (IESDS)**. A strategy is **strictly dominated** if there exists another strategy that gives a strictly higher payoff no matter what the opponent does. Rational players never play strictly dominated strategies — and rational players know their opponents are rational, so strategies dominated only after one round of elimination can also be removed. IESDS repeatedly removes dominated strategies until no more can be eliminated. If this process yields a unique outcome, that outcome is the uniquely rationalizable and Nash equilibrium solution. If it doesn't fully resolve the game, you still narrow the strategy space before applying Nash equilibrium analysis. The combination of matrix reasoning, Nash equilibrium, and dominance arguments is the complete toolkit for analyzing any simultaneous-move strategic interaction.
