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
stage: advanced
status: draft
---

# Nash Refinements: Trembling Hand Perfection

## Core Idea
Trembling hand perfection refines Nash equilibrium by requiring robustness to small mistakes: an equilibrium is perfect if it is a limit of equilibria in perturbed games where players make small errors. This eliminates equilibria dependent on implausibly irrational off-path beliefs. An equilibrium is perfect if no player has an incentive to deviate even when others may occasionally make mistakes.

## Explainer

From your study of strategic form games and Nash equilibrium, you know that a Nash equilibrium is a profile of strategies where no player can profitably deviate, given the others' strategies. The problem is that many games have multiple Nash equilibria, and some of them rely on threats or beliefs that seem unreasonable. **Trembling hand perfection**, introduced by Reinhard Selten, is a refinement that eliminates these implausible equilibria by asking: would this equilibrium survive if players occasionally made small mistakes?

Consider a simple coordination game. Suppose two firms must choose whether to enter a market. One Nash equilibrium has Firm A entering and Firm B staying out, sustained by Firm B's belief that Firm A will always enter. But what if there is a tiny chance — a "tremble" — that Firm A accidentally stays out? If Firm B's strategy is only optimal because it assumes Firm A never trembles, then the equilibrium is fragile. **Trembling hand perfection** requires that each player's strategy remains a best response even when every other player plays a **completely mixed strategy** — one that assigns small but positive probability to every available action. The equilibrium must be the limit of best responses as these tremble probabilities shrink to zero.

Formally, a Nash equilibrium is **trembling hand perfect** if there exists a sequence of completely mixed strategy profiles (where every action gets played with positive probability) converging to the equilibrium, such that each player's equilibrium strategy is a best response to every profile in the sequence. This rules out equilibria sustained by **weakly dominated strategies**. If a strategy is weakly dominated — meaning there exists another strategy that does at least as well against every opponent action and strictly better against some — then it cannot survive the tremble test. When opponents might tremble into any action with positive probability, the dominated strategy will underperform, and the player will abandon it.

The intuition is fundamentally about robustness: a credible equilibrium should not fall apart because of infinitesimal noise. In real strategic interactions — bargaining, auctions, market entry — players are not perfectly rational automatons. They make occasional errors, face computational limits, or experiment with off-equilibrium actions. Trembling hand perfection captures the idea that a good prediction about behavior should be robust to these small perturbations. If an equilibrium only works in a world of perfect rationality and zero mistakes, it is a poor prediction of actual play. This concept connects forward to Bayesian games, where incomplete information introduces a different kind of uncertainty about opponents' behavior, and the same spirit of robustness continues to drive equilibrium refinement.
