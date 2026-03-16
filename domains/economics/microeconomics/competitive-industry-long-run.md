---
id: competitive-industry-long-run
title: Competitive Industry Long-Run Equilibrium
domain: economics
course: microeconomics
prerequisites:
- id: firm-output-decision-competitive
  type: hard
- id: market-equilibrium
  type: hard
builds-toward:
- long-run-equilibrium-zero-profit
tags:
- producer theory
- competition
- industry equilibrium
stage: abstract-reasoning
status: draft
---

# Competitive Industry Long-Run Equilibrium

## Core Idea
Long-run competitive equilibrium requires zero economic profit (price equals minimum long-run average cost), free entry and exit until no firm earns above-normal returns, and all firms produce where P = MC. The industry supply is horizontal (perfectly elastic) at the minimum LAC if input prices remain constant (constant-cost industry), or upward-sloping if input prices rise with industry output (increasing-cost industry).

## Explainer

You already know from firm-output decision theory that a competitive firm maximizes profit by producing where P = MC, and you know from market equilibrium that price is determined by the intersection of supply and demand. Long-run equilibrium takes this logic one step further: it asks what happens *over time* when profit is positive or negative, and free entry and exit are allowed.

The key mechanism is the **entry and exit process**. Suppose the market price settles above minimum long-run average cost (LRAC). Every firm in the industry is earning positive economic profit — revenue exceeds the full opportunity cost of all resources. This profit signal attracts new firms. As new firms enter, the market supply curve shifts right, driving price down. Entry continues until price falls to the minimum of LRAC — the point where economic profit is exactly zero. The reverse happens when price falls below minimum LRAC: firms exit, supply shrinks, and price recovers. The long-run equilibrium is therefore a gravitational attractor: any deviation triggers entry or exit that restores P = minimum LRAC.

At this **zero-profit equilibrium**, three conditions hold simultaneously: P = MC (profit maximization), P = ATC (zero profit), and the firm is at the minimum point of its LRAC curve (productive efficiency). This is not a coincidence — the three conditions are forced to coincide by the entry/exit mechanism. The long-run supply curve of the *industry* reflects this. In a **constant-cost industry** (where input prices don't rise as the industry expands), every entering firm faces the same cost curves, so the industry's long-run supply curve is perfectly horizontal at the minimum LRAC. Demand can increase dramatically, and in the long run, the price returns to exactly the same level — more firms, same price.

In an **increasing-cost industry**, higher industry output bids up the prices of specialized inputs (skilled labor, land in a particular region). Each new firm enters at slightly higher cost, so the zero-profit equilibrium settles at a higher price than before. The long-run industry supply curve slopes upward — not because individual firms are less efficient, but because input prices rise with scale. This distinction matters for predicting how price responds to a permanent demand increase: flat industry supply means consumers bear none of the long-run cost increase; upward-sloping supply means they bear some.

"Zero economic profit" is often misread as a grim result for firms. It is not. Economic profit accounts for the opportunity cost of the owner's capital and time — if you earn zero economic profit, you are earning exactly the return you could have earned in your next-best alternative. The firm is viable and the owner is being fully compensated. It simply means there is no excess return to attract still more entry. Positive *accounting* profit is perfectly consistent with zero *economic* profit.

## Questions

```yaml
- question: "A competitive industry is in short-run equilibrium with firms earning positive economic profit. Trace the long-run adjustment."
  type: short-answer
  answer: "Positive profit attracts entry. New firms shift the industry supply curve right, pushing price down. Entry continues until price falls to the minimum of LRAC, at which point economic profit equals zero and entry stops."
  explanation: "The entry/exit mechanism is the engine of long-run adjustment. Notice that the short-run supply curve shifts during this process (more firms), but each individual firm moves along its own cost curves."

- question: "In long-run competitive equilibrium, which conditions hold simultaneously?"
  type: multiple-choice
  options:
    - "P = MC only"
    - "P = ATC only"
    - "P = MC = ATC = minimum LRAC"
    - "P = MC and P > ATC"
  answer: 2
  explanation: "All three coincide at the long-run equilibrium. P = MC is the profit-maximizing output rule. P = ATC is the zero-profit condition. The minimum of LRAC is where both can hold simultaneously — this is productive efficiency."

- question: "Why is the long-run supply curve of a constant-cost industry perfectly horizontal?"
  type: short-answer
  answer: "Because input prices don't change as the industry expands, every firm always faces the same cost curves. The zero-profit condition is always restored at the same minimum LRAC, regardless of how many firms enter. So price returns to the same level in the long run no matter how much demand increases."
  explanation: "The horizontal long-run supply is a consequence of constant input prices plus free entry — not a special assumption about technology. It implies that in the very long run, competitive markets supply any quantity consumers demand at the same price."
```
