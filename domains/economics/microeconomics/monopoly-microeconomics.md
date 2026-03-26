---
id: monopoly-microeconomics
title: Monopoly
domain: economics
course: microeconomics
prerequisites:
- id: profit-maximization-microeconomics
  type: hard
- id: price-elasticity-of-demand
  type: hard
- id: perfect-competition
  type: soft
- id: shutdown-and-breakeven
  type: soft
builds-toward:
- price-discrimination
- natural-monopoly
- monopolistic-competition
tags:
- monopoly
- market power
- MR < P
- deadweight loss
- markup
stage: formal-systems
status: validated
---
# Monopoly

## Core Idea
A monopolist is the sole seller in a market, facing a downward-sloping demand curve, and is therefore a price-maker. Marginal revenue is less than price (MR < P) because selling an additional unit requires lowering price on all units. The monopolist maximizes profit at MR = MC and then reads the price off the demand curve, producing less and charging more than the competitive equilibrium. This results in deadweight loss (foregone surplus from trades that would have been mutually beneficial). The Lerner Index (P − MC) / P measures the degree of monopoly power and equals 1/|PED|.

## How It's Best Learned
Derive MR algebraically from a linear demand curve, then solve the monopoly optimum both graphically and numerically. Compare the monopoly solution to the competitive one to quantify deadweight loss.

## Common Misconceptions
- A monopolist does not charge the highest possible price; it charges the *profit-maximizing* price, which depends on elasticity.
- Monopoly power is not binary: firms have varying degrees of market power, measured by the Lerner Index.

## Questions

```yaml
- question: "A monopolist faces demand P = 100 - Q and constant marginal cost MC = 20. What quantity maximizes profit?"
  type: multiple-choice
  options:
    - "Q = 80"
    - "Q = 40"
    - "Q = 20"
    - "Q = 60"
  answer: 1
  explanation: "For a linear demand P = 100 - Q, marginal revenue is MR = 100 - 2Q (same intercept, twice the slope). Setting MR = MC: 100 - 2Q = 20, so Q = 40. The price is P = 100 - 40 = 60. A common error is setting P = MC (the competitive rule), which gives Q = 80 — but that ignores that MR < P for a monopolist."

- question: "A profit-maximizing monopolist typically charges the highest price that any consumer is willing to pay."
  type: true-false
  answer: false
  explanation: "The monopolist charges the profit-maximizing price, not the maximum willingness-to-pay price. Charging too high reduces quantity sold so much that total revenue and profit fall. The optimal price trades off margin against volume, found by the MR = MC condition. Only a perfectly price-discriminating monopolist extracts maximum willingness to pay from every buyer."

- question: "Why is marginal revenue less than price for a monopolist, and what does this imply about monopoly output relative to the competitive outcome?"
  type: short-answer
  answer: "A monopolist faces a downward-sloping demand curve, so selling one more unit requires lowering price on all units already sold. MR = P - (price cut × existing quantity), which is always less than P. Since MR < P, setting MR = MC occurs at a lower quantity than the competitive P = MC condition. The monopolist produces less and charges more than would occur under competition, generating deadweight loss."
  explanation: "In perfect competition, each firm is a price taker — it can sell more without cutting its price, so MR = P. A monopolist cannot do this. The lost revenue on existing units (the price-reduction effect) makes each additional unit less profitable than its price suggests. This wedge between MR and P is the fundamental source of monopoly inefficiency."
```

## Explainer

You know that a competitive firm is a **price taker**: it sells as much as it wants at the market price, and its marginal revenue equals that price. A monopolist breaks this assumption entirely. As the sole seller, it faces the **entire downward-sloping market demand curve** — if it wants to sell more, it must lower its price. This single difference transforms everything about how profit maximization works.

The key insight is why **MR < P** for a monopolist. Suppose the current price is $60 and you sell 40 units. To sell a 41st unit, you must drop the price to, say, $59 — but that new price applies to all 41 units, not just the last one. You gain $59 from the new sale but lose $1 on each of the 40 existing sales. MR = $59 − $40 = $19, far below the $59 price. More generally, for a linear demand curve P = a − bQ, the marginal revenue is MR = a − 2bQ — same intercept, twice the slope downward. The monopolist's MR curve lies below the demand curve everywhere (except the first unit).

Given this, profit maximization still follows the MR = MC rule — produce until the revenue gained from the last unit equals its cost. But because MR < P, the monopolist stops at a lower quantity than the competitive outcome (where P = MC). Having found the profit-maximizing quantity, the monopolist reads the **price off the demand curve** (not off MR). This is the two-step monopoly solution: (1) find Q where MR = MC, (2) find P from the demand curve at that Q. The gap between price and marginal cost is where monopoly profit comes from — and where social harm originates.

That social harm takes the form of **deadweight loss**: transactions that would have been mutually beneficial (for consumers willing to pay above MC but below the monopoly price) never occur. Resources that could have been used productively are not. The **Lerner Index** (P − MC) / P = 1 / |PED| quantifies the markup as a fraction of price and connects it to demand elasticity — a monopolist with inelastic demand can charge a large markup; one facing elastic demand cannot. This explains why pharmaceutical companies (with patented drugs that have few substitutes) earn larger margins than, say, gasoline retailers.

A common misconception is that the monopolist charges "the highest possible price." In fact, raising price beyond the optimum reduces quantity so much that total profit falls — the lost sales more than offset the higher margin per unit. The monopolist is constrained by demand, not unconstrained. It is a price-maker, not a price-ignorer. Understanding this distinction prepares you for studying price discrimination, where a monopolist extracts more surplus by charging different prices to different buyers — and potentially eliminates deadweight loss in the extreme case of perfect price discrimination.
