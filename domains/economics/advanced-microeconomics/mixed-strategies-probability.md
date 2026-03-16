---
id: mixed-strategies-probability
title: Mixed Strategies and Probabilistic Play
domain: economics
course: advanced-microeconomics
prerequisites:
- id: strategic-form-game-theory
  type: hard
- id: nash-equilibrium-microeconomics
  type: hard
tags:
- game-theory
- randomization
stage: advanced
status: draft
---

# Mixed Strategies and Probabilistic Play

## Core Idea
A mixed strategy is a probability distribution over pure strategies. Players may use mixed strategies when payoff matrices make any pure strategy exploitable by opponents. Mixed strategy equilibrium exists under standard conditions even when pure strategy equilibrium does not. Indifference conditions ensure players are willing to randomize: expected payoffs from strategies in the support must be equal.

## Explainer

From strategic form games, you know how to represent players, strategies, and payoffs in a matrix. From Nash equilibrium, you know that an equilibrium is a strategy profile where no player can improve by unilaterally deviating. But some games have no Nash equilibrium in **pure strategies** — deterministic choices where each player picks one action with certainty. Matching Pennies is the classic example: Player 1 wants to match (both Heads or both Tails), Player 2 wants to mismatch. For any pure strategy pair, one player wants to switch. The solution is to allow **mixed strategies**, where players randomize over their available actions according to specific probabilities.

The key insight is *why* the specific probabilities emerge. In a mixed strategy Nash equilibrium, each player's randomization must make the *other* player **indifferent** between the strategies in their mix. If Player 1 plays Heads with probability p, then Player 2's expected payoff from choosing Heads must equal their expected payoff from choosing Tails — otherwise Player 2 would prefer one pure strategy and would not be willing to randomize. This indifference condition pins down p. In Matching Pennies with symmetric payoffs, the equilibrium requires each player to play Heads with probability 1/2. If Player 1 deviated to, say, 60% Heads, Player 2 would exploit this by playing Tails more often, breaking the equilibrium.

Working through the mechanics: suppose Player 1 mixes between strategies A and B with probabilities (p, 1−p), and Player 2 mixes between X and Y with probabilities (q, 1−q). For Player 1 to willingly randomize, it must be that EU₁(A) = EU₁(B), where expected utilities are computed using Player 2's mixing probabilities q. This equation in q determines Player 2's equilibrium mix. Symmetrically, Player 1's mixing probability p is determined by Player 2's indifference condition. Notice the counterintuitive implication: your own mixing probabilities are determined by the *other* player's payoffs, not yours. You randomize not to maximize your own payoff directly but to prevent your opponent from exploiting a predictable pattern.

The existence result is powerful: **Nash's theorem** guarantees that every finite game (finitely many players, finitely many strategies each) has at least one Nash equilibrium, possibly in mixed strategies. This is why mixed strategies matter theoretically — they ensure the equilibrium concept is not vacuous. Without them, many important games would have no solution at all. The theorem relies on fixed-point mathematics (Kakutani or Brouwer), but the economic intuition is straightforward: if pure strategies cycle (each best response triggers a counter-response), mixing breaks the cycle by making players genuinely unpredictable.

Mixed strategies have practical interpretations beyond literal coin-flipping. In many applications, the mixture represents a **population distribution** — not one player randomizing, but a population of players each choosing a pure strategy, with the proportions matching the equilibrium probabilities. In penalty kicks in soccer, goalkeepers and kickers do not flip coins, but over many kicks the observed frequencies closely match mixed strategy predictions. In auditing and enforcement, the "randomization" interpretation is literal: tax authorities randomize audits to keep taxpayers uncertain. The mixed strategy framework provides the right model whenever predictability would be exploited and unpredictability is strategically valuable.
