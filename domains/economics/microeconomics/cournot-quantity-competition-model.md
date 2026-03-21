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
stage: formal-systems
status: draft
---

# Cournot Model: Quantity Competition and Nash Equilibrium

## Core Idea
In the Cournot model, each firm chooses its output quantity simultaneously to maximize profit given the quantities it expects rivals will produce. The Nash equilibrium occurs where each firm's quantity choice is optimal given rivals' quantities. With symmetric firms, equilibrium output lies between the monopoly level (lowest output and highest price) and the perfectly competitive level (highest output and lowest price). Increasing the number of firms pushes the equilibrium toward competition.

## Questions

```yaml
- question: "In a Cournot duopoly, if firm 2 unexpectedly increases its output, firm 1's best response is to:"
  type: multiple-choice
  options:
    - "Increase its own output to defend market share and prevent firm 2 from gaining"
    - "Keep its output unchanged because Cournot firms choose simultaneously and cannot react to rivals"
    - "Decrease its own output, because firm 2's expansion lowers market price, reducing the marginal revenue firm 1 receives"
    - "Exit the market, since higher total output drives price below both firms' marginal costs"
  answer: 2
  explanation: "The reaction function (best-response function) is downward-sloping: more output from firm 2 lowers the market price, which reduces the marginal revenue that firm 1 earns on each unit. To re-equate marginal revenue with marginal cost, firm 1 cuts back production. This is the key strategic insight of the Cournot model — firms' outputs are strategic substitutes. The Nash equilibrium is where both firms are simultaneously on their own reaction functions, with neither wanting to deviate given the other's choice."

- question: "A student claims that rational Cournot duopolists will collectively produce the monopoly output, since two intelligent firms can find the jointly optimal strategy. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — Cournot duopolists do produce the joint-profit-maximizing (monopoly) output at equilibrium"
    - "Each firm maximizes its own profit taking the rival's output as fixed, ignoring the negative price externality it imposes on its rival, so total Cournot output exceeds the monopoly level"
    - "Cournot firms overshoot the competitive output through aggressive price-cutting"
    - "The student is correct, but only if the two firms can communicate their output choices before the game is played"
  answer: 1
  explanation: "This is the core game-theoretic insight of the Cournot model. A monopolist internalizes the full price impact of its output — producing one more unit lowers the price it receives on all units. A Cournot duopolist only internalizes the price impact on its own output, not on its rival's. This 'missing internalization' means each firm produces more than its share of the monopoly output. Reaching the monopoly outcome would require explicit coordination (which is cartelization and illegal in most jurisdictions) — the Nash equilibrium without coordination produces strictly higher total output."

- question: "In the Cournot model, adding more identical firms to a market causes equilibrium price to fall and total output to rise, converging toward the perfectly competitive outcome as the number of firms approaches infinity."
  type: true-false
  answer: true
  explanation: "With n symmetric Cournot firms facing linear demand P = a − bQ and marginal cost c, each firm produces (a − c)/[(n+1)b] and total output is n(a − c)/[(n+1)b]. As n → ∞, total output approaches (a − c)/b and price approaches c — exactly the perfectly competitive outcome. The Cournot model is therefore a general framework: n = 1 gives monopoly, n = 2 gives duopoly, and n → ∞ gives perfect competition. Market structure continuously shapes the degree of market power."

- question: "Two Cournot-competing firms produce as much total output as a perfectly competitive market, because competition between just two firms is sufficient to eliminate market power entirely."
  type: true-false
  answer: false
  explanation: "This is the Bertrand paradox, not the Cournot result. In Cournot duopoly with symmetric linear demand P = a − bQ and marginal cost c, each firm produces (a−c)/3b and total output is 2(a−c)/3b — only two-thirds of the perfectly competitive output (a−c)/b. Price is (a+2c)/3, which is above marginal cost c. Each firm still has market power: it faces a downward-sloping residual demand curve and earns positive economic profit. Two Cournot firms are more competitive than a monopolist but remain well short of perfect competition."

- question: "Why does the Cournot Nash equilibrium produce more total output than a monopoly but less than perfect competition?"
  type: short-answer
  answer: "A monopolist internalizes the full price effect of its output: producing one more unit lowers price on all units, so the monopolist restricts output severely to keep price high. A Cournot firm only internalizes the price effect on its own output — it ignores the negative externality it imposes on its rival when it expands. This partial internalization leads each firm to produce more than its share of the monopoly output, pushing total output above the monopoly level. But Cournot firms are not price-takers: each still faces a downward-sloping residual demand and sets output where its own marginal revenue equals marginal cost. This market power causes them to produce less than perfectly competitive firms, who expand until price equals marginal cost."
  explanation: "The key phrase is 'negative externality on rivals': when firm 1 expands output, it lowers the price that firm 2 also receives, imposing a cost on firm 2. Firm 1 ignores this cost when maximizing its own profit. The monopolist (or a cartel) would internalize this externality by restricting joint output. The perfectly competitive firm ignores it in the other direction — it treats price as fixed regardless of its output. Cournot sits between these extremes because it partially internalizes: each firm accounts for its own price impact but not the impact on rivals."
```

## Explainer

You already understand Nash equilibrium from simultaneous-move games: each player's strategy is a best response to the others', and no one has a unilateral incentive to deviate. The Cournot model is the classic economic application of that idea. Instead of abstract strategies, each firm chooses an **output quantity**, and the market price emerges from those combined quantities through the inverse demand function. More total output means a lower price — that's the strategic tension. If you produce more, you drive down the price you and your rival both receive.

To find the Nash equilibrium, derive each firm's **best-response function** (also called a reaction function). Firm 1 asks: given how much firm 2 produces (q₂), what quantity q₁ maximizes my profit? Setting marginal revenue equal to marginal cost while treating q₂ as a constant gives a downward-sloping function: q₁* = f(q₂). More output from firm 2 lowers market price, which reduces the marginal revenue firm 1 receives — so firm 1's best response is to *reduce* its own quantity. The same logic applies symmetrically to firm 2. The Nash equilibrium is where the two reaction functions intersect: both best-response conditions are satisfied simultaneously, and neither firm wants to change.

With symmetric duopoly and linear demand P = a − bQ and constant marginal cost c, each firm produces (a − c)/(3b) at equilibrium, total output is 2(a − c)/(3b), and price is (a + 2c)/3. Compare these benchmarks: the monopolist would produce (a − c)/(2b) at price (a + c)/2; perfect competition yields (a − c)/b at price c. Cournot sits between them. This makes intuitive sense — each firm independently internalizes only its own profit, ignoring the negative externality it imposes on its rival by lowering the market price. That leads to more output than a joint monopolist would choose, but less output than competitive firms because each still has market power.

Adding more firms extends the pattern. With n symmetric Cournot firms, each produces (a − c)/((n+1)b) and total output is n(a − c)/((n+1)b). As n → ∞, total output approaches (a − c)/b and price approaches c — perfect competition. With n = 1 you recover monopoly. The Cournot model is therefore a general framework that spans from monopoly to competition as the number of competitors grows. This is why economists treat it as the canonical model of **imperfect competition**: it captures the logic that firms with market power overproduce relative to monopoly but underproduce relative to perfect competition, and it quantifies exactly how market structure shapes that outcome.
