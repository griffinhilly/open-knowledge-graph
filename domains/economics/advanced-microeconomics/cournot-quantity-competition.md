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
stage: expert
status: validated
---

# Cournot Quantity Competition

## Core Idea
Cournot competition models firms simultaneously choosing output quantities, with market price determined by aggregate demand. Each firm takes rivals' quantities as given (Cournot conjecture). Equilibrium occurs where each firm's quantity maximizes profit given others' output. Equilibrium output lies between monopoly and perfect competition levels; firms earn positive but below-monopoly profit.

## Questions

```yaml
- question: "In a symmetric Cournot duopoly, a third identical firm enters the market. How does this entry affect total industry output and market price?"
  type: multiple-choice
  options:
    - "Total output falls and price rises, because each firm now receives only one-third of the market"
    - "Total output rises and price falls, as competition increases each firm's equilibrium output relative to duopoly levels"
    - "Total output and price are unchanged, because each firm simply reduces its individual quantity by one-third"
    - "The market immediately becomes perfectly competitive since three competing firms are sufficient"
  answer: 1
  explanation: "With n Cournot competitors, each firm produces (a−c)/[(n+1)b] and total output is n(a−c)/[(n+1)b]. Going from n=2 (duopoly) to n=3 (triopoly): each firm produces less individually, but total output rises from 2(a−c)/3b to 3(a−c)/4b, and price falls. The entry of each additional competitor shifts best-response functions and moves equilibrium closer to the competitive outcome. The market does NOT immediately become perfectly competitive — that requires n→∞. Cournot firms retain market power (price > marginal cost) at any finite n."

- question: "Firm 1's Cournot best response function is q₁* = (a − c − bq₂) / 2b. If Firm 2 increases its output q₂, what should Firm 1 do, and why?"
  type: multiple-choice
  options:
    - "Increase output to match Firm 2 and defend its market share"
    - "Maintain output because the Cournot conjecture assumes each firm ignores rivals' moves"
    - "Decrease output, because higher total supply lowers market price, making additional units less profitable for Firm 1"
    - "Exit the market, since Firm 2 now produces more and has a competitive advantage"
  answer: 2
  explanation: "The best response function shows that q₁* decreases as q₂ increases — the reaction curves are downward sloping. The intuition: if Firm 2 expands output, total supply rises and market price falls (P = a − b(q₁+q₂)). At the lower price, Firm 1's marginal revenue from additional units is lower, so it optimally pulls back. This is the strategic substitutes relationship — each firm's output is a decreasing best response to rivals' output. Note the Cournot conjecture means Firm 1 *treats* q₂ as fixed when solving, but in equilibrium both firms simultaneously choose quantities consistent with each other's best responses."

- question: "In the Cournot model, the Nash equilibrium occurs where firms cooperatively maximize joint industry profit by restricting output below the non-cooperative level."
  type: true-false
  answer: false
  explanation: "The Cournot-Nash equilibrium is explicitly non-cooperative: each firm independently maximizes its own profit taking rivals' quantities as given. The result is total output ABOVE the monopoly (joint-profit-maximizing) level, with price below the monopoly price. Joint profit maximization would require firms to collectively restrict output to the monopoly quantity — this is a collusive outcome, not the Cournot equilibrium. In fact, the Cournot equilibrium can be understood as the outcome where neither firm can profitably deviate *unilaterally*; this is a distinct and weaker condition than maximizing joint profits."

- question: "As the number of identical Cournot competitors in a market increases without bound, the equilibrium price converges to marginal cost and each firm's profit converges to zero."
  type: true-false
  answer: true
  explanation: "With n Cournot firms, equilibrium price is P* = c + (a−c)/(n+1). As n→∞, the term (a−c)/(n+1)→0, so P*→c (marginal cost). Each firm's output (a−c)/[(n+1)b] → 0, and profit → 0. This smooth convergence is one of the Cournot model's most important properties: it provides a continuous bridge between monopoly (n=1, maximum market power) and perfect competition (n→∞, zero profit). Real markets with 5–10 firms sit somewhere along this continuum, and the Cournot model gives precise predictions about where."

- question: "Explain why the 'Cournot conjecture' — that each firm treats its rivals' quantities as fixed — is a modeling assumption rather than a literal description of how firms think, and why the Cournot-Nash equilibrium is still a useful prediction despite this unrealistic assumption."
  type: short-answer
  answer: "The Cournot conjecture says each firm maximizes profit assuming its rivals' current output levels will not change in response to its own decision. Real firms do react to each other, often dynamically over time. The conjecture is a simplifying assumption that allows clean mathematical analysis of simultaneous quantity-setting. Despite this, the Cournot-Nash equilibrium is a useful prediction because it is the unique fixed point of best-response dynamics: if firms are repeatedly adjusting quantities, the only stable resting point — where neither firm wants to change — is the Cournot equilibrium. Additionally, Nash equilibrium is justified by rational reasoning: if each firm correctly anticipates that its rival is also playing its best response, neither has an incentive to deviate. The equilibrium concept captures strategic stability without requiring firms to literally 'hold beliefs constant.'"
  explanation: "This connects Cournot to the broader Nash equilibrium framework: the Cournot conjecture is a modeling device to set up the best-response problem, but the Nash equilibrium concept validates the outcome on game-theoretic grounds. The contrast with Bertrand competition (where firms set prices) is instructive — the strategic variable fundamentally changes the equilibrium: Bertrand duopoly with homogeneous goods drives price to marginal cost, while Cournot duopoly does not."
```

## Explainer

From oligopoly theory, you know that a small number of firms must think strategically — each firm's profit depends on what competitors do. From game theory, you know that Nash equilibrium describes outcomes where no player can improve by unilaterally changing strategy. Cournot competition applies Nash equilibrium to the specific strategic problem of **quantity setting**: each firm chooses how much to produce, and the market price adjusts to clear total output through the demand curve.

The setup is concrete. Consider a duopoly (two firms) facing an inverse demand curve P = a − b(q₁ + q₂), where q₁ and q₂ are the quantities each firm produces. Each firm has constant marginal cost c. Firm 1 maximizes profit π₁ = (P − c)q₁ = (a − b(q₁ + q₂) − c)q₁ by choosing q₁, treating q₂ as fixed. Taking the first-order condition and solving gives Firm 1's **best response function**: q₁* = (a − c − bq₂) / 2b. This tells you exactly how much Firm 1 should produce for any given output level of Firm 2. Firm 2 has a symmetric best response. The **Cournot-Nash equilibrium** is where both best responses are simultaneously satisfied — graphically, where the two reaction curves intersect.

The result is illuminating: each firm produces (a − c) / 3b, total output is 2(a − c) / 3b, and the market price is (a + 2c) / 3. Compare this to the benchmarks. A monopolist would produce (a − c) / 2b — less total output and a higher price. Perfect competitors would produce until P = c, yielding total output (a − c) / b. The Cournot duopoly falls exactly between these extremes. Each firm earns positive economic profit, but less than a monopolist would, because competition drives output up and prices down. This "in-between" result is the defining feature of oligopoly — some market power, but constrained by rivalry.

The logic extends naturally to n firms. With n identical Cournot competitors, each produces (a − c) / (n + 1)b, and total output is n(a − c) / (n + 1)b. As n grows large, total output approaches the competitive level (a − c) / b and price approaches marginal cost. The Cournot model thus provides a smooth bridge between monopoly (n = 1) and perfect competition (n → ∞), with market power declining continuously in the number of firms. This is why the model is central to industrial organization — it gives precise predictions about how market structure (number of firms, cost differences) maps to market outcomes (prices, quantities, profits, welfare).

A subtlety worth noting: the Cournot conjecture — that each firm treats rivals' quantities as fixed — is a modeling assumption, not a claim about how firms literally think. It is justified as the Nash equilibrium of the simultaneous quantity-setting game. The alternative where firms set *prices* (Bertrand competition) yields starkly different results: with identical products, even two firms drive price to marginal cost. This contrast between Cournot and Bertrand outcomes highlights that the nature of the strategic variable — quantity versus price — fundamentally shapes competitive outcomes, a theme you will revisit when studying Stackelberg leadership and collusion.
