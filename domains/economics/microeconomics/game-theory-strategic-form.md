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
stage: advanced
status: validated
---

# Game Theory and Strategic Form Analysis

## Core Idea
Strategic form represents simultaneous-move games as payoff matrices. Nash equilibrium occurs when each player's strategy is optimal given others' strategies (no unilateral improvement incentive). Pure strategy equilibrium is a cell where neither player wants to deviate; mixed strategy involves randomizing. Multiple equilibria, no equilibrium, or unique solutions can arise depending on payoff structure. Dominated strategies can be iteratively eliminated.

## Questions

```yaml
- question: "Two firms simultaneously choose whether to advertise (A) or not advertise (N). If both advertise: both earn 2. If neither advertises: both earn 4. If one advertises and the other doesn't: the advertiser earns 5, the non-advertiser earns 1. What is the Nash equilibrium, and what does it reveal about the relationship between equilibrium and jointly optimal outcomes?"
  type: multiple-choice
  options:
    - "Neither firm advertises, because that gives the best combined payoff and rational firms coordinate on joint optimality"
    - "Both firms advertise, even though both would be better off if neither advertised — advertising is a dominant strategy regardless of what the other firm does"
    - "One firm advertises and one doesn't, splitting the asymmetric payoffs"
    - "There is no Nash equilibrium because both firms have an incentive to deviate from any outcome"
  answer: 1
  explanation: "This is a Prisoner's Dilemma structure. Advertising strictly dominates non-advertising for each firm: if the rival advertises, you earn 2 by advertising vs. 1 by not; if the rival doesn't advertise, you earn 5 by advertising vs. 4 by not. So advertising is always better regardless of what the other firm does. Both firms reason this way and both advertise — earning 2 each — even though mutual non-advertising would give 4 each. Nash equilibrium is defined by unilateral best response, not joint optimality. The equilibrium is individually rational but collectively suboptimal, which is the hallmark of coordination failures."

- question: "In a payoff matrix, a strategy is strictly dominated if some other strategy yields a strictly higher payoff no matter what the opponent does. Which statement about iterated elimination of dominated strategies (IESDS) is correct?"
  type: multiple-choice
  options:
    - "IESDS should only remove strategies that are dominated in the original game, not strategies that become dominated after earlier rounds of elimination"
    - "Strictly dominated strategies should never be played; moreover, rational players know their opponents won't play dominated strategies either, so strategies that become dominated after one round of elimination can also be removed"
    - "IESDS applies only when the game has a unique Nash equilibrium; with multiple equilibria it cannot be used"
    - "Dominated strategies can still appear in mixed strategy Nash equilibria, so they should not be eliminated before computing mixed equilibria"
  answer: 1
  explanation: "IESDS relies on common knowledge of rationality: rational Player 1 won't play dominated strategies; rational Player 2 knows this and can therefore treat those strategies as eliminated, potentially making previously non-dominated strategies now dominated; and so on. Each round of elimination uses the fact that players are not just rational but know their opponents are rational. Strictly dominated strategies never appear in any Nash equilibrium — pure or mixed — so their elimination is safe. The order of elimination doesn't change the final result for strict dominance."

- question: "In a Nash equilibrium, each player is choosing the strategy that maximizes the total payoff to all players combined."
  type: true-false
  answer: false
  explanation: "Nash equilibrium requires each player to maximize their *own* payoff given what others are doing — not the group payoff. The Prisoner's Dilemma is the clearest counterexample: the Nash equilibrium (both defect) is individually rational but leaves both players worse off than the cooperative outcome (both cooperate). A Nash equilibrium is a fixed point of individual best responses, not a solution to a social welfare maximization problem. Confusing these two concepts leads to incorrect predictions about strategic behavior."

- question: "In a finite game, if no pure strategy Nash equilibrium exists, then no Nash equilibrium of any kind exists."
  type: true-false
  answer: false
  explanation: "Nash's theorem guarantees that every finite game (finite players, finite strategy sets) has at least one Nash equilibrium, possibly in mixed strategies. When players randomize over their strategies, the mixed strategy Nash equilibrium requires each player to be indifferent between the strategies they mix over — their randomization makes the opponent indifferent. Rock-Paper-Scissors has no pure strategy equilibrium but has a unique mixed strategy equilibrium (each strategy played with probability 1/3). The existence theorem means the search for equilibrium never comes up empty in finite games."

- question: "Explain why Nash equilibrium does not necessarily produce the outcome that is best for all players combined. What structural feature of the strategic situation causes this gap?"
  type: short-answer
  answer: "Nash equilibrium is defined by individual best responses: each player maximizes their own payoff given what others do. There is no mechanism in this definition that coordinates players toward outcomes good for the group. The structural cause is externalities — when one player's choice affects another player's payoff, individual optimization ignores the cost or benefit imposed on others. In the Prisoner's Dilemma, each player's dominant strategy imposes a negative externality on the other; both act on it and land in an outcome worse for both. The equilibrium is stable (no one wants to deviate alone) but not efficient (a different outcome could make both better off). This gap between individual rationality and collective optimality is one of game theory's deepest insights."
  explanation: "The key concepts are best response and externalities. Nash equilibrium solves a fixed-point problem about unilateral deviations — it says nothing about coordinated improvements. When individual incentives diverge from social incentives (negative externalities, coordination failures, public goods), equilibria are typically inefficient. Understanding this structure explains a wide range of real-world phenomena from environmental economics to arms races."
```

## Explainer

The **strategic form** (also called **normal form**) is the simplest mathematical structure for representing a game. You list all players, all the strategies available to each player, and the payoffs each player receives for every combination of strategy choices. For two players, this becomes a matrix: rows are Player 1's strategies, columns are Player 2's strategies, and each cell contains the payoff pair (Row's payoff, Column's payoff). The beauty of this representation is that it strips away timing and sequential structure — it captures pure strategic interaction when players choose simultaneously without seeing each other's move.

Your prerequisite on Nash equilibrium gives you the central solution concept. A **Nash equilibrium** (NE) is a strategy profile — one strategy choice per player — where no player can improve their payoff by unilaterally switching to a different strategy, given what the other player is doing. In matrix form, you find a NE by checking each cell: would Player 1 want to switch rows given Column is fixed? Would Player 2 want to switch columns given Row is fixed? If neither wants to deviate, you have a Nash equilibrium. A **pure strategy NE** is a specific cell that satisfies this condition. Some games have no pure strategy NE; many have one; some have multiple.

When no pure strategy NE exists, players may play **mixed strategies** — probability distributions over their pure strategies. In a mixed NE, each player randomizes in a way that makes the other player indifferent between their available strategies. The classic example is Rock-Paper-Scissors: if your opponent plays each option with probability 1/3, you have no incentive to favor any single strategy, and the same logic applies in reverse. Mixed strategies expand the set of equilibria and ensure that finite games always have at least one (Nash's theorem).

A powerful analytical tool is **iterated elimination of dominated strategies (IESDS)**. A strategy is **strictly dominated** if there exists another strategy that gives a strictly higher payoff no matter what the opponent does. Rational players never play strictly dominated strategies — and rational players know their opponents are rational, so strategies dominated only after one round of elimination can also be removed. IESDS repeatedly removes dominated strategies until no more can be eliminated. If this process yields a unique outcome, that outcome is the uniquely rationalizable and Nash equilibrium solution. If it doesn't fully resolve the game, you still narrow the strategy space before applying Nash equilibrium analysis. The combination of matrix reasoning, Nash equilibrium, and dominance arguments is the complete toolkit for analyzing any simultaneous-move strategic interaction.
