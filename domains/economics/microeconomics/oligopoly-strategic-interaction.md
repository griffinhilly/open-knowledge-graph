---
id: oligopoly-strategic-interaction
title: Oligopoly and Strategic Firm Interaction
domain: economics
course: microeconomics
prerequisites:
- id: oligopoly-and-strategic-behavior
  type: hard
builds-toward:
- cournot-vs-bertrand-equilibrium
tags:
- market structure
- oligopoly
- strategy
stage: formal-systems
status: validated
---

# Oligopoly and Strategic Firm Interaction

## Core Idea
Oligopolies involve few firms where each firm's profit depends on rivals' actions, creating strategic interdependence. Cournot firms choose quantities best-responding to each other's output; Bertrand firms choose prices. Both yield equilibrium between perfect competition and monopoly, with outcomes depending on number of firms, substitutability, and cost structure. Collusion to set monopoly price is unstable due to incentive to undercut.

## Questions

```yaml
- question: "Two identical firms each have a constant marginal cost of $10. They compete by simultaneously setting prices (Bertrand competition). According to the Bertrand model, what is the equilibrium price?"
  type: multiple-choice
  options:
    - "Between $10 and the monopoly price — duopolists split the market and both earn positive profit"
    - "The monopoly price — each firm recognizes their mutual dependence and coordinates implicitly"
    - "$10 (marginal cost) — either firm would undercut any price above $10 to capture the entire market"
    - "Just above $10 — firms always retain a small markup to cover fixed costs"
  answer: 2
  explanation: "This is the Bertrand paradox: with identical products and equal costs, any price above $10 is unstable. If one firm charges $11, the other can charge $10.99, capture the whole market, and earn positive profit. The first firm then undercuts to $10.98, and so on — this undercutting continues until price equals marginal cost, where neither firm can profitably undercut further. The result is the perfectly competitive outcome with only two firms. Option A describes the Cournot outcome, not Bertrand. The paradox reveals that the competitive variable matters as much as the number of firms."

- question: "In the Cournot model, the Nash equilibrium quantity pair is found where:"
  type: multiple-choice
  options:
    - "Both firms set the monopoly quantity and split the profits"
    - "Each firm's best-response function is satisfied simultaneously — neither firm can increase its profit by changing its output alone"
    - "Total industry output equals the perfectly competitive output level"
    - "Each firm earns zero economic profit, as in perfect competition"
  answer: 1
  explanation: "A Nash equilibrium requires that each player is best-responding to what the others are doing. In Cournot, each firm's best-response function gives the profit-maximizing output given the rival's quantity. The equilibrium is the intersection of both best-response curves — a quantity pair where each firm is simultaneously optimizing. Option A is the collusive outcome. Option C describes perfect competition, which requires many firms or Bertrand competition. Option D is the Bertrand outcome, not Cournot."

- question: "Collusion between oligopolists is inherently unstable because each individual firm has an incentive to undercut the agreed price and capture a larger market share."
  type: true-false
  answer: true
  explanation: "Even if firms successfully agree to set the monopoly price, each individual firm's profit-maximizing response is to shade its price slightly below the agreed level, capturing the entire market rather than sharing it. This is the prisoner's dilemma structure of cartels: collectively, firms prefer the collusive outcome; individually, each prefers to defect. Without binding enforcement mechanisms, this logic unravels collusion. It explains why cartels require explicit coordination, monitoring, and punishment threats to sustain."

- question: "The Cournot and Bertrand models always predict the same market price because they both analyze oligopoly with the same number of firms and the same cost structure."
  type: true-false
  answer: false
  explanation: "The models can produce dramatically different predictions despite identical market structure. The Bertrand model with two identical firms predicts price equals marginal cost — the competitive outcome. The Cournot model with two identical firms predicts a price above marginal cost but below the monopoly price. The key difference is the strategic variable: quantity competition (Cournot) generates market power even with few firms; price competition (Bertrand) eliminates it. Market structure alone does not determine outcome — the competitive variable is equally important."

- question: "Why does the Bertrand model predict a competitive outcome with only two firms, and what does this reveal about the relationship between market structure and market outcome in oligopoly?"
  type: short-answer
  answer: "In Bertrand competition, firms can capture the entire market by undercutting a rival's price by any amount. This creates a race to the bottom: any price above marginal cost invites undercutting, so the only stable equilibrium is price equals marginal cost — identical to perfect competition. The implication is that market structure (number of firms) alone does not determine how competitive a market is. The competitive variable — whether firms compete on price or quantity — is equally important. Two price-competing firms can produce the same outcome as an infinite number of competitive firms."
  explanation: "The Bertrand paradox challenges the intuition that 'fewer firms means more market power.' Real oligopolies avoid the Bertrand trap through product differentiation (making direct price comparison harder), capacity constraints (firms cannot actually serve the whole market at a lower price), or repeated interaction (the threat of future price wars disciplines current pricing). These departures from the basic Bertrand model explain why duopolies like Coke and Pepsi maintain prices well above marginal cost."
```

## Explainer

In monopoly, a single firm sets prices without concern for rivals. In perfect competition, no firm is large enough to affect price. **Oligopoly** sits in between: a small number of firms, each large enough that its decisions directly affect the others. This creates **strategic interdependence** — the defining feature. Your profit depends not just on your own choices, but on what competitors decide. This is why the game theory framework from your prerequisite is the natural language for oligopoly analysis.

The **Cournot model** has firms compete on quantity. Each firm chooses how much output to produce, taking rivals' quantities as given. The **best-response function** tells each firm: "If my rival produces q₂, my profit-maximizing output is q₁ = f(q₂)." Both firms have such a function. The Nash equilibrium is where the two best-response curves intersect — a quantity pair where each firm is simultaneously best-responding to the other. No firm can profitably deviate. The Cournot equilibrium price lands above marginal cost (unlike perfect competition) but below the monopoly price.

The **Bertrand model** competes on price instead. The logic seems similar, but the result is dramatically different: when firms sell identical products with equal costs, Bertrand competition drives prices all the way to marginal cost — the perfectly competitive outcome — even with just two firms. This **Bertrand paradox** shows that the competitive variable matters enormously. Real oligopolies avoid this pressure through product differentiation, capacity constraints, or repeated interaction that creates implicit threat of punishment.

Collusion offers a third path. If firms jointly set the monopoly price, they split monopoly profits — better for both than Cournot. But collusion is inherently unstable: each firm has an individual incentive to undercut the agreed price slightly and capture extra market share. This is the prisoner's dilemma of industrial organization. The instability explains why cartels require enforcement mechanisms to hold together, and why antitrust authorities target them. The formal Cournot vs. Bertrand analysis you're building toward makes these intuitions precise and quantitative.
