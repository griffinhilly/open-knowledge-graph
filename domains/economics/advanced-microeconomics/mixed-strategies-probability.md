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
stage: expert
status: validated
---

# Mixed Strategies and Probabilistic Play

## Core Idea
A mixed strategy is a probability distribution over pure strategies. Players may use mixed strategies when payoff matrices make any pure strategy exploitable by opponents. Mixed strategy equilibrium exists under standard conditions even when pure strategy equilibrium does not. Indifference conditions ensure players are willing to randomize: expected payoffs from strategies in the support must be equal.

## Questions

```yaml
- question: "In a mixed strategy Nash equilibrium of Matching Pennies, Player 1 plays Heads 50% of the time. What happens if Player 1 deviates to playing Heads 70% of the time?"
  type: multiple-choice
  options:
    - "Nothing — Player 1 is still mixing, so it remains an equilibrium"
    - "Player 2 will exploit the predictability by best-responding with a pure strategy, breaking the equilibrium"
    - "Player 1's expected payoff increases because Heads is now favored"
    - "Player 2 must also adjust to maintain equal mixing probabilities"
  answer: 1
  explanation: "In a mixed strategy Nash equilibrium, each player's mixing probabilities are chosen specifically to make the other player indifferent between their strategies. If Player 1 plays Heads 70%, Player 2 can now identify which pure strategy gives a higher expected payoff and will deviate to it — breaking the equilibrium. The 50/50 split is the unique profile where Player 2 has no profitable deviation, precisely because 50/50 leaves Player 2 indifferent."

- question: "In a mixed strategy Nash equilibrium, what determines Player 1's equilibrium mixing probabilities?"
  type: multiple-choice
  options:
    - "Player 1's own payoffs — Player 1 mixes in the proportions that maximize their expected payoff"
    - "Player 2's payoffs — Player 1's mix must make Player 2 indifferent between their strategies"
    - "The total number of strategies available to both players"
    - "Player 1's risk aversion — more risk-averse players mix closer to 50/50"
  answer: 1
  explanation: "This is the counterintuitive core of mixed strategy equilibrium: your mixing probabilities are determined by the OTHER player's payoff structure, not your own. Player 1 must choose probabilities that equate Player 2's expected payoffs across the strategies in Player 2's support — because if Player 2 strictly preferred one strategy, Player 2 would not be willing to mix. Player 1's own mixing probabilities are pinned down by Player 2's indifference condition."

- question: "In a mixed strategy Nash equilibrium, each player randomizes in order to maximize their own expected payoff."
  type: true-false
  answer: false
  explanation: "Players do not mix to maximize their own payoff — in fact, in a mixed strategy NE, a player is INDIFFERENT between all strategies in their support (they all yield the same expected payoff). The purpose of mixing is to prevent opponents from exploiting predictability. A player randomizes to make opponents indifferent, which sustains the equilibrium. If a player were mixing to maximize their own payoff, they would play a pure strategy (the best-responding pure strategy)."

- question: "Nash's theorem guarantees that every finite strategic-form game has at least one Nash equilibrium."
  type: true-false
  answer: true
  explanation: "Nash's theorem (proved using Kakutani's fixed-point theorem) states that every finite game — finitely many players, each with finitely many pure strategies — has at least one Nash equilibrium, possibly in mixed strategies. This is why mixed strategies matter: they ensure the equilibrium concept is never vacuous. Games like Matching Pennies have no pure strategy NE but always have a mixed strategy NE, so the solution concept remains well-defined."

- question: "Why does predictability undermine equilibrium in games like Matching Pennies, and why does mixing solve this problem?"
  type: short-answer
  answer: "In Matching Pennies, any deterministic pure strategy is exploitable: if Player 1 always plays Heads, Player 2 best-responds by always playing Tails, but then Player 1 wants to switch to Tails, and so on — there is no stable resting point. Mixing solves this by making Player 1 genuinely unpredictable: if Player 1 plays Heads with probability 1/2, Player 2 cannot improve by changing strategy because both Heads and Tails yield the same expected payoff. Unpredictability removes the opponent's ability to exploit any systematic pattern."
  explanation: "This captures the strategic logic of randomization: it is not about literally flipping a coin for its own sake, but about creating genuine uncertainty that neutralizes the opponent's ability to best-respond. The equilibrium mixing probabilities are exactly those that accomplish this — making the other player indifferent — and no other probabilities can sustain equilibrium."
```

## Explainer

From strategic form games, you know how to represent players, strategies, and payoffs in a matrix. From Nash equilibrium, you know that an equilibrium is a strategy profile where no player can improve by unilaterally deviating. But some games have no Nash equilibrium in **pure strategies** — deterministic choices where each player picks one action with certainty. Matching Pennies is the classic example: Player 1 wants to match (both Heads or both Tails), Player 2 wants to mismatch. For any pure strategy pair, one player wants to switch. The solution is to allow **mixed strategies**, where players randomize over their available actions according to specific probabilities.

The key insight is *why* the specific probabilities emerge. In a mixed strategy Nash equilibrium, each player's randomization must make the *other* player **indifferent** between the strategies in their mix. If Player 1 plays Heads with probability p, then Player 2's expected payoff from choosing Heads must equal their expected payoff from choosing Tails — otherwise Player 2 would prefer one pure strategy and would not be willing to randomize. This indifference condition pins down p. In Matching Pennies with symmetric payoffs, the equilibrium requires each player to play Heads with probability 1/2. If Player 1 deviated to, say, 60% Heads, Player 2 would exploit this by playing Tails more often, breaking the equilibrium.

Working through the mechanics: suppose Player 1 mixes between strategies A and B with probabilities (p, 1−p), and Player 2 mixes between X and Y with probabilities (q, 1−q). For Player 1 to willingly randomize, it must be that EU₁(A) = EU₁(B), where expected utilities are computed using Player 2's mixing probabilities q. This equation in q determines Player 2's equilibrium mix. Symmetrically, Player 1's mixing probability p is determined by Player 2's indifference condition. Notice the counterintuitive implication: your own mixing probabilities are determined by the *other* player's payoffs, not yours. You randomize not to maximize your own payoff directly but to prevent your opponent from exploiting a predictable pattern.

The existence result is powerful: **Nash's theorem** guarantees that every finite game (finitely many players, finitely many strategies each) has at least one Nash equilibrium, possibly in mixed strategies. This is why mixed strategies matter theoretically — they ensure the equilibrium concept is not vacuous. Without them, many important games would have no solution at all. The theorem relies on fixed-point mathematics (Kakutani or Brouwer), but the economic intuition is straightforward: if pure strategies cycle (each best response triggers a counter-response), mixing breaks the cycle by making players genuinely unpredictable.

Mixed strategies have practical interpretations beyond literal coin-flipping. In many applications, the mixture represents a **population distribution** — not one player randomizing, but a population of players each choosing a pure strategy, with the proportions matching the equilibrium probabilities. In penalty kicks in soccer, goalkeepers and kickers do not flip coins, but over many kicks the observed frequencies closely match mixed strategy predictions. In auditing and enforcement, the "randomization" interpretation is literal: tax authorities randomize audits to keep taxpayers uncertain. The mixed strategy framework provides the right model whenever predictability would be exploited and unpredictability is strategically valuable.
