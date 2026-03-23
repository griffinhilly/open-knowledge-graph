---
id: nash-refinements-and-trembling-hand
title: 'Nash Refinements: Trembling Hand Perfection'
domain: economics
course: advanced-microeconomics
prerequisites:
- id: strategic-form-games
  type: hard
- id: mixed-strategy-equilibrium
  type: soft
builds-toward:
- bayesian-games-and-incomplete-information
tags:
- game-theory
- equilibrium-selection
stage: expert
status: validated
---

# Nash Refinements: Trembling Hand Perfection

## Core Idea
Trembling hand perfection refines Nash equilibrium by requiring robustness to small mistakes: an equilibrium is perfect if it is a limit of equilibria in perturbed games where players make small errors. This eliminates equilibria dependent on implausibly irrational off-path beliefs. An equilibrium is perfect if no player has an incentive to deviate even when others may occasionally make mistakes.

## Questions

```yaml
- question: "Firm A has two strategies: Fight and Accommodate. Fighting is costly — if Firm B enters, Firm A's best response is to Accommodate. A Nash equilibrium has Firm B staying out, sustained by the belief that Firm A will always Fight. Is this equilibrium trembling hand perfect?"
  type: multiple-choice
  options:
    - "Yes — Firm B has no incentive to enter given the threat, so the equilibrium is self-sustaining"
    - "No — if there is a small chance Firm A trembles into Accommodating, Firm B's best response is to enter, so the equilibrium is not robust to small mistakes"
    - "Yes — trembling hand perfection only applies to simultaneous-move games, not entry deterrence"
    - "No — but only because Firm B is using a weakly dominated strategy"
  answer: 1
  explanation: "This is the classic case that trembling hand perfection was designed to eliminate. The threat to Fight is not credible: if Firm A actually faces entry, its best response is Accommodate. The Nash equilibrium survives only because Firm B believes the threat with certainty. But when Firm A trembles — plays Fight with probability only (1-ε) — Firm B's best response may shift to Enter. Because the equilibrium depends on a threat that would never be executed, it fails the perfection test."

- question: "Player A has a weakly dominated strategy W — another strategy D does at least as well against every opponent action and strictly better against some. A Nash equilibrium requires Player A to play W. What does trembling hand perfection say about this equilibrium?"
  type: multiple-choice
  options:
    - "The equilibrium is still trembling hand perfect if no player gains by deviating at the equilibrium profile"
    - "The equilibrium fails to be trembling hand perfect because when opponents tremble into every action with positive probability, W earns strictly less than D"
    - "The equilibrium is trembling hand perfect only if W and D yield the same payoff in expectation over the tremble distribution"
    - "The equilibrium is trembling hand perfect because Nash equilibria are by definition robust to small perturbations"
  answer: 1
  explanation: "In a perturbed game where opponents mix over all actions with small probability ε, there is positive probability on the actions where D strictly outperforms W. This means D yields a strictly higher expected payoff than W — Player A abandons W in the perturbed game. The Nash equilibrium requiring W therefore cannot be the limit of best responses as ε→0, so it is not trembling hand perfect. The key insight: weakly dominated strategies cannot survive the tremble test."

- question: "Trembling hand perfection requires that each player's strategy remains a best response even when every opponent plays a completely mixed strategy assigning positive probability to every available action."
  type: true-false
  answer: true
  explanation: "This is precisely the definition. The 'tremble' is modeled as each player mistakenly playing each action with some small but positive probability ε > 0. An equilibrium is trembling hand perfect if it is the limit of Nash equilibria in these perturbed games as ε → 0. This rules out equilibria that unravel when opponents might, even with tiny probability, take actions that were previously assumed to be off the equilibrium path."

- question: "Every Nash equilibrium in a finite game is trembling hand perfect, because Nash equilibria are defined as strategy profiles where no player can benefit by deviating."
  type: true-false
  answer: false
  explanation: "Nash equilibrium only requires that no player benefits from deviating *given the other players' exact equilibrium strategies*. It says nothing about robustness when opponents might make small mistakes. In particular, Nash equilibria sustained by weakly dominated strategies fail the perfection test: when opponents tremble, the weakly dominated strategy earns strictly less than its dominator, so the player deviates. Trembling hand perfection is strictly stronger than Nash equilibrium."

- question: "Why can't a weakly dominated strategy be part of a trembling hand perfect equilibrium, and what does this tell us about which strategic threats or commitments are 'credible'?"
  type: short-answer
  answer: "In any perturbed game where opponents play each action with positive probability ε, there is positive weight on the actions against which the dominating strategy strictly outperforms the dominated one. So the dominated strategy earns strictly less in expectation — the player will deviate to the dominator. As ε → 0, this means no equilibrium requiring the dominated strategy can arise as a limit of perturbed best responses. For credibility: an equilibrium sustained by a threat to play a weakly dominated strategy (e.g., 'I will fight entry even though accommodation is better') is not credible because, if the opponent ever plays with any positive probability, the threat-maker would not follow through. Trembling hand perfection formalizes the idea that only threats a player would actually carry out under small perturbations count as credible commitments."
  explanation: "The deeper point is that trembling hand perfection imposes a consistency requirement: equilibrium strategies must be best responses not just at the exact equilibrium point but throughout a neighborhood of it. This is why it eliminates the weakly dominated strategy problem and why it connects naturally to subgame perfect equilibrium (which eliminates non-credible threats in extensive-form games by a related backward-induction logic)."
```

## Explainer

From your study of strategic form games and Nash equilibrium, you know that a Nash equilibrium is a profile of strategies where no player can profitably deviate, given the others' strategies. The problem is that many games have multiple Nash equilibria, and some of them rely on threats or beliefs that seem unreasonable. **Trembling hand perfection**, introduced by Reinhard Selten, is a refinement that eliminates these implausible equilibria by asking: would this equilibrium survive if players occasionally made small mistakes?

Consider a simple coordination game. Suppose two firms must choose whether to enter a market. One Nash equilibrium has Firm A entering and Firm B staying out, sustained by Firm B's belief that Firm A will always enter. But what if there is a tiny chance — a "tremble" — that Firm A accidentally stays out? If Firm B's strategy is only optimal because it assumes Firm A never trembles, then the equilibrium is fragile. **Trembling hand perfection** requires that each player's strategy remains a best response even when every other player plays a **completely mixed strategy** — one that assigns small but positive probability to every available action. The equilibrium must be the limit of best responses as these tremble probabilities shrink to zero.

Formally, a Nash equilibrium is **trembling hand perfect** if there exists a sequence of completely mixed strategy profiles (where every action gets played with positive probability) converging to the equilibrium, such that each player's equilibrium strategy is a best response to every profile in the sequence. This rules out equilibria sustained by **weakly dominated strategies**. If a strategy is weakly dominated — meaning there exists another strategy that does at least as well against every opponent action and strictly better against some — then it cannot survive the tremble test. When opponents might tremble into any action with positive probability, the dominated strategy will underperform, and the player will abandon it.

The intuition is fundamentally about robustness: a credible equilibrium should not fall apart because of infinitesimal noise. In real strategic interactions — bargaining, auctions, market entry — players are not perfectly rational automatons. They make occasional errors, face computational limits, or experiment with off-equilibrium actions. Trembling hand perfection captures the idea that a good prediction about behavior should be robust to these small perturbations. If an equilibrium only works in a world of perfect rationality and zero mistakes, it is a poor prediction of actual play. This concept connects forward to Bayesian games, where incomplete information introduces a different kind of uncertainty about opponents' behavior, and the same spirit of robustness continues to drive equilibrium refinement.
