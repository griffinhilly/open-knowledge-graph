---
id: cournot-quantity-competition
title: Cournot Quantity Competition
domain: economics
course: advanced-microeconomics
prerequisites:
- id: oligopoly-and-strategic-behavior
  type: hard
- id: profit-maximization-microeconomics
  type: hard
- id: game-theory-basics-microeconomics
  type: hard
- id: constrained-optimization
  type: hard
- id: optimization-multivariable-basics
  type: hard
- id: critical-points-multivariable
  type: soft
builds-toward:
- stackelberg-sequential-moves
- collusion-cartel-stability
tags:
- industrial-organization
- oligopoly
- competition
stage: advanced
status: draft
---

# Cournot Quantity Competition

## Core Idea
Cournot competition models firms simultaneously choosing output quantities, with market price determined by aggregate demand. Each firm takes rivals' quantities as given (Cournot conjecture). Equilibrium occurs where each firm's quantity maximizes profit given others' output. Equilibrium output lies between monopoly and perfect competition levels; firms earn positive but below-monopoly profit.

## Explainer

From oligopoly theory, you know that a small number of firms must think strategically — each firm's profit depends on what competitors do. From game theory, you know that Nash equilibrium describes outcomes where no player can improve by unilaterally changing strategy. Cournot competition applies Nash equilibrium to the specific strategic problem of **quantity setting**: each firm chooses how much to produce, and the market price adjusts to clear total output through the demand curve.

The setup is concrete. Consider a duopoly (two firms) facing an inverse demand curve P = a − b(q₁ + q₂), where q₁ and q₂ are the quantities each firm produces. Each firm has constant marginal cost c. Firm 1 maximizes profit π₁ = (P − c)q₁ = (a − b(q₁ + q₂) − c)q₁ by choosing q₁, treating q₂ as fixed. Taking the first-order condition and solving gives Firm 1's **best response function**: q₁* = (a − c − bq₂) / 2b. This tells you exactly how much Firm 1 should produce for any given output level of Firm 2. Firm 2 has a symmetric best response. The **Cournot-Nash equilibrium** is where both best responses are simultaneously satisfied — graphically, where the two reaction curves intersect.

The result is illuminating: each firm produces (a − c) / 3b, total output is 2(a − c) / 3b, and the market price is (a + 2c) / 3. Compare this to the benchmarks. A monopolist would produce (a − c) / 2b — less total output and a higher price. Perfect competitors would produce until P = c, yielding total output (a − c) / b. The Cournot duopoly falls exactly between these extremes. Each firm earns positive economic profit, but less than a monopolist would, because competition drives output up and prices down. This "in-between" result is the defining feature of oligopoly — some market power, but constrained by rivalry.

The logic extends naturally to n firms. With n identical Cournot competitors, each produces (a − c) / (n + 1)b, and total output is n(a − c) / (n + 1)b. As n grows large, total output approaches the competitive level (a − c) / b and price approaches marginal cost. The Cournot model thus provides a smooth bridge between monopoly (n = 1) and perfect competition (n → ∞), with market power declining continuously in the number of firms. This is why the model is central to industrial organization — it gives precise predictions about how market structure (number of firms, cost differences) maps to market outcomes (prices, quantities, profits, welfare).

A subtlety worth noting: the Cournot conjecture — that each firm treats rivals' quantities as fixed — is a modeling assumption, not a claim about how firms literally think. It is justified as the Nash equilibrium of the simultaneous quantity-setting game. The alternative where firms set *prices* (Bertrand competition) yields starkly different results: with identical products, even two firms drive price to marginal cost. This contrast between Cournot and Bertrand outcomes highlights that the nature of the strategic variable — quantity versus price — fundamentally shapes competitive outcomes, a theme you will revisit when studying Stackelberg leadership and collusion.
