---
id: cournot-quantity-competition-model
title: 'Cournot Model: Quantity Competition and Nash Equilibrium'
domain: economics
course: microeconomics
prerequisites:
- id: oligopoly-strategic-interdependence
  type: hard
- id: nash-equilibrium-simultaneous-move-games
  type: hard
tags:
- cournot-model
- quantity-competition
- nash-equilibrium
- oligopoly
stage: abstract-reasoning
status: draft
---

# Cournot Model: Quantity Competition and Nash Equilibrium

## Core Idea
In the Cournot model, each firm chooses its output quantity simultaneously to maximize profit given the quantities it expects rivals will produce. The Nash equilibrium occurs where each firm's quantity choice is optimal given rivals' quantities. With symmetric firms, equilibrium output lies between the monopoly level (lowest output and highest price) and the perfectly competitive level (highest output and lowest price). Increasing the number of firms pushes the equilibrium toward competition.

## Explainer

You already understand Nash equilibrium from simultaneous-move games: each player's strategy is a best response to the others', and no one has a unilateral incentive to deviate. The Cournot model is the classic economic application of that idea. Instead of abstract strategies, each firm chooses an **output quantity**, and the market price emerges from those combined quantities through the inverse demand function. More total output means a lower price — that's the strategic tension. If you produce more, you drive down the price you and your rival both receive.

To find the Nash equilibrium, derive each firm's **best-response function** (also called a reaction function). Firm 1 asks: given how much firm 2 produces (q₂), what quantity q₁ maximizes my profit? Setting marginal revenue equal to marginal cost while treating q₂ as a constant gives a downward-sloping function: q₁* = f(q₂). More output from firm 2 lowers market price, which reduces the marginal revenue firm 1 receives — so firm 1's best response is to *reduce* its own quantity. The same logic applies symmetrically to firm 2. The Nash equilibrium is where the two reaction functions intersect: both best-response conditions are satisfied simultaneously, and neither firm wants to change.

With symmetric duopoly and linear demand P = a − bQ and constant marginal cost c, each firm produces (a − c)/(3b) at equilibrium, total output is 2(a − c)/(3b), and price is (a + 2c)/3. Compare these benchmarks: the monopolist would produce (a − c)/(2b) at price (a + c)/2; perfect competition yields (a − c)/b at price c. Cournot sits between them. This makes intuitive sense — each firm independently internalizes only its own profit, ignoring the negative externality it imposes on its rival by lowering the market price. That leads to more output than a joint monopolist would choose, but less output than competitive firms because each still has market power.

Adding more firms extends the pattern. With n symmetric Cournot firms, each produces (a − c)/((n+1)b) and total output is n(a − c)/((n+1)b). As n → ∞, total output approaches (a − c)/b and price approaches c — perfect competition. With n = 1 you recover monopoly. The Cournot model is therefore a general framework that spans from monopoly to competition as the number of competitors grows. This is why economists treat it as the canonical model of **imperfect competition**: it captures the logic that firms with market power overproduce relative to monopoly but underproduce relative to perfect competition, and it quantifies exactly how market structure shapes that outcome.
