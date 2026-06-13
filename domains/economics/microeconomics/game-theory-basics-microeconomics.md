---
id: game-theory-basics-microeconomics
title: Game Theory Basics
domain: economics
course: microeconomics
prerequisites:
- id: scarcity-and-opportunity-cost
  type: hard
- id: oligopoly-and-strategic-behavior
  type: soft
- id: expected-value
  type: soft
builds-toward:
- nash-equilibrium-microeconomics
tags:
- game theory
- normal form
- payoff matrix
- dominant strategy
- prisoners dilemma
stage: formal-systems
status: validated
---

# Game Theory Basics

## Core Idea
Game theory studies strategic interactions where each player's payoff depends on the choices of all players. A game in normal form specifies players, strategies, and payoffs in a matrix. A dominant strategy is one that is optimal regardless of what the opponent does. The Prisoner's Dilemma is the canonical example where individual dominant strategies lead to a mutually inferior outcome, illustrating why coordination problems and market failures arise even among rational agents.

## How It's Best Learned
Work through the Prisoner's Dilemma payoff matrix by hand, identifying dominant strategies before defining Nash equilibrium. Then apply the framework to advertising decisions, pricing, and arms-race scenarios.

## Common Misconceptions
- Rational play does not guarantee a good outcome — the Prisoner's Dilemma demonstrates that individually rational strategies can be collectively irrational.
- A dominant strategy equilibrium is a special case; most games do not have dominant strategies, requiring Nash equilibrium analysis.

## Questions

```yaml
- question: "In the Prisoner's Dilemma, both players have defect as a dominant strategy. What happens when both players follow their dominant strategies?"
  type: multiple-choice
  options: ["Both players achieve the best possible joint outcome", "Both players get their individually best possible payoff", "One player benefits at the other's expense", "Both players end up worse off than if they had both cooperated"]
  answer: 3
  explanation: "This is the defining tragedy of the Prisoner's Dilemma: mutual defection (the dominant strategy outcome) is worse for both players than mutual cooperation would have been. It is not the worst absolute outcome (being the sole cooperator is worse), but it is worse than the cooperative outcome — illustrating how individually rational choices can be collectively self-defeating."

- question: "If both players in a game act rationally and choose their dominant strategies, they are expected to reach the best possible collective outcome."
  type: true-false
  answer: false
  explanation: "The Prisoner's Dilemma is a direct counterexample. Both players rationally choose to defect (their dominant strategy), yet the result is mutual defection — worse for both than mutual cooperation. Rational individual play can produce collective irrationality. This is one of the central insights of game theory and the foundation for understanding market failures, public goods problems, and arms races."

- question: "Why is a 'dominant strategy' stronger than merely 'the best response to a specific opponent action'?"
  type: short-answer
  answer: "A dominant strategy is optimal regardless of what the opponent does — it beats or ties every other strategy no matter the opponent's choice. A best response depends on the opponent's action and may differ across scenarios."
  explanation: "The key word is 'regardless.' A strategy that is best only when the opponent plays X is a conditional best response, not a dominant strategy. A dominant strategy must outperform (or at least match) every other strategy for every possible opponent action, making it robust to uncertainty. When one exists, rational players choose it without needing to predict the opponent at all."
```

## Explainer

Game theory studies decision-making in strategic interactions — situations where your payoff depends not just on your own choice but on the choices of others. This distinguishes it from the optimization problems you've seen elsewhere in microeconomics, where you simply maximize utility or profit given fixed prices and constraints. In strategic situations, your best action depends on what others do, and their best action depends on what you do. Game theory provides the tools to analyze this mutual dependence precisely.

Every game in normal form has three elements: players, strategies, and payoffs. A payoff matrix displays this information visually. Each row is a strategy for player 1, each column is a strategy for player 2, and each cell shows what both players earn for that combination of choices. Reading the matrix is itself a skill — by convention, the row player's payoff is listed first. Before solving any game, spend a moment mapping out what each cell means in terms of the actual situation being modeled.

A dominant strategy is one that is optimal regardless of what the opponent does. To identify it: compare each strategy of player 1 across all columns. If one row always gives a payoff at least as high as every other row, that row dominates. When a dominant strategy exists, a rational player should always choose it — no prediction about the opponent is needed. This makes dominant-strategy reasoning especially robust. Most games, however, do not have dominant strategies for all players, which is why Nash equilibrium (a concept you'll study next) is the more general solution concept.

The Prisoner's Dilemma is the most important example in introductory game theory precisely because it exposes the limits of individual rationality. Each player has a dominant strategy — defect. Both play it. But the result (mutual defection) is worse for both than if they had cooperated. The core insight: individual rationality does not guarantee collective optimality. You've already seen this idea in the context of market failures and public goods: the rational choice for each individual (free-ride, pollute, defect) undermines the outcome for everyone. The Prisoner's Dilemma gives that intuition mathematical precision.

This framework applies far beyond stylized examples. Firms deciding whether to advertise, countries choosing military spending levels, and commuters choosing routes all face Prisoner's Dilemma-style structures. In each case, the temptation to defect is individually rational but collectively costly. Understanding this structure tells you when regulation, contracts, or repeated interaction might enable better outcomes — because when the game is played repeatedly, the calculus changes and cooperation can become self-sustaining. That extension is where the analysis gets richer.
