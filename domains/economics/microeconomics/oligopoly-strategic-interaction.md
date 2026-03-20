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
status: draft
---

# Oligopoly and Strategic Firm Interaction

## Core Idea
Oligopolies involve few firms where each firm's profit depends on rivals' actions, creating strategic interdependence. Cournot firms choose quantities best-responding to each other's output; Bertrand firms choose prices. Both yield equilibrium between perfect competition and monopoly, with outcomes depending on number of firms, substitutability, and cost structure. Collusion to set monopoly price is unstable due to incentive to undercut.

## Explainer

In monopoly, a single firm sets prices without concern for rivals. In perfect competition, no firm is large enough to affect price. **Oligopoly** sits in between: a small number of firms, each large enough that its decisions directly affect the others. This creates **strategic interdependence** — the defining feature. Your profit depends not just on your own choices, but on what competitors decide. This is why the game theory framework from your prerequisite is the natural language for oligopoly analysis.

The **Cournot model** has firms compete on quantity. Each firm chooses how much output to produce, taking rivals' quantities as given. The **best-response function** tells each firm: "If my rival produces q₂, my profit-maximizing output is q₁ = f(q₂)." Both firms have such a function. The Nash equilibrium is where the two best-response curves intersect — a quantity pair where each firm is simultaneously best-responding to the other. No firm can profitably deviate. The Cournot equilibrium price lands above marginal cost (unlike perfect competition) but below the monopoly price.

The **Bertrand model** competes on price instead. The logic seems similar, but the result is dramatically different: when firms sell identical products with equal costs, Bertrand competition drives prices all the way to marginal cost — the perfectly competitive outcome — even with just two firms. This **Bertrand paradox** shows that the competitive variable matters enormously. Real oligopolies avoid this pressure through product differentiation, capacity constraints, or repeated interaction that creates implicit threat of punishment.

Collusion offers a third path. If firms jointly set the monopoly price, they split monopoly profits — better for both than Cournot. But collusion is inherently unstable: each firm has an individual incentive to undercut the agreed price slightly and capture extra market share. This is the prisoner's dilemma of industrial organization. The instability explains why cartels require enforcement mechanisms to hold together, and why antitrust authorities target them. The formal Cournot vs. Bertrand analysis you're building toward makes these intuitions precise and quantitative.
