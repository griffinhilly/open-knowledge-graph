---
id: nash-equilibrium-microeconomics
title: Nash Equilibrium
domain: economics
course: microeconomics
prerequisites:
- id: game-theory-basics-microeconomics
  type: hard
- id: optimization-multivariable-basics
  type: soft
builds-toward:
- externalities-and-market-failure
tags:
- Nash equilibrium
- best response
- mixed strategy
- no regret
stage: abstract-reasoning
status: validated
---
# Nash Equilibrium

## Core Idea
A Nash equilibrium is a strategy profile where no player can improve their payoff by unilaterally changing their strategy, given what everyone else is doing. It generalizes dominant strategy equilibrium and applies to a much broader class of games. Nash equilibria can be in pure strategies (deterministic choices) or mixed strategies (probability distributions over strategies). Nash's theorem guarantees that every finite game has at least one Nash equilibrium in mixed strategies. Nash equilibrium is the central solution concept in non-cooperative game theory.

## How It's Best Learned
Find Nash equilibria by underlining best responses in payoff matrices — cells where both players have underlined payoffs are Nash equilibria. Practice with coordination games, Battle of the Sexes, and Chicken to see that games can have zero, one, or multiple Nash equilibria.

## Common Misconceptions
- A Nash equilibrium is not necessarily a dominant strategy equilibrium; dominant strategy equilibrium is a stronger condition.
- Multiple Nash equilibria create a coordination problem that Nash equilibrium analysis alone cannot resolve — it predicts *possible* outcomes, not which one will occur.

## Questions

```yaml
- question: "In a 2-player game, which of the following correctly describes a Nash equilibrium?"
  type: multiple-choice
  options:
    - "Both players are using dominant strategies"
    - "No player can increase their payoff by unilaterally changing their strategy"
    - "The sum of all players' payoffs is maximized"
    - "Both players achieve their single best possible payoff simultaneously"
  answer: 1
  explanation: "A Nash equilibrium requires only that no player has a profitable unilateral deviation — each player's strategy is a best response to the other's. Option A is too strong (dominant strategy equilibrium implies Nash, but not vice versa). Option C is the definition of Pareto efficiency, not Nash equilibrium. Option D is also too strong — Nash equilibria can occur at payoff combinations far from each player's maximum."

- question: "Every Nash equilibrium is also a dominant strategy equilibrium."
  type: true-false
  answer: false
  explanation: "Dominant strategy equilibrium is a strictly stronger concept. A strategy dominates when it is best regardless of what others do. A Nash strategy is only required to be best given what others actually do. Many games (like Coordination and Battle of the Sexes) have Nash equilibria but no dominant strategies at all."

- question: "Why might a finite game have no pure strategy Nash equilibrium, and what does Nash's theorem say about this?"
  type: short-answer
  answer: "In some games (like Matching Pennies), for every pure strategy profile some player prefers to deviate, so best responses cycle with no stable fixed point. Nash's theorem guarantees that every finite game has at least one Nash equilibrium when players are allowed to use mixed strategies — probability distributions over their pure strategies."
  explanation: "The core insight is that mixed strategies expand the strategy space. By randomizing, a player can make opponents indifferent between their choices, breaking the cycle of deviation. The proof uses Kakutani's fixed-point theorem applied to the best-response correspondence over the compact, convex set of mixed strategy profiles."
```

## Explainer

You already know from game theory basics that strategic interaction means your best move depends on what others do. Nash equilibrium formalizes the natural stopping point of this reasoning: a strategy profile where every player is already doing the best they can, given what everyone else is doing. No one has an incentive to deviate unilaterally.

The cleanest way to find Nash equilibria in a payoff matrix is the best-response underline method. For each column (Player 2's strategy), find Player 1's best response and underline their payoff. For each row (Player 1's strategy), find Player 2's best response and underline their payoff. Any cell where both payoffs are underlined is a Nash equilibrium — both players are simultaneously best-responding.

It is important to distinguish Nash equilibrium from stronger solution concepts you may encounter. In a dominant strategy equilibrium, each player's strategy is best regardless of what others do — Nash equilibrium only requires best-response *to what others are actually doing*. This means every dominant strategy equilibrium is also a Nash equilibrium, but not vice versa. The Prisoner's Dilemma has a dominant strategy equilibrium; the Coordination Game has Nash equilibria but no dominant strategies.

Games can have zero, one, or many pure strategy Nash equilibria. When there are multiple equilibria, Nash equilibrium analysis alone cannot predict which one players will reach — this is the coordination problem. In Matching Pennies, there is no pure strategy Nash equilibrium at all: whatever one player does, the other wants to switch. Nash's theorem rescues predictive power by guaranteeing that every finite game has at least one Nash equilibrium in mixed strategies (probability distributions over pure strategies). A mixed equilibrium typically involves each player randomizing in a way that makes opponents indifferent between their pure strategy options.

Nash equilibrium captures a form of rational consistency, not optimality. Players at a Nash equilibrium may all be doing quite poorly — the Prisoner's Dilemma is a famous example where the Nash equilibrium is worse for both players than the cooperative outcome. Understanding Nash equilibrium as a stability concept (no one wants to deviate) rather than an optimality concept (everyone is doing well) is the key to applying it correctly.
