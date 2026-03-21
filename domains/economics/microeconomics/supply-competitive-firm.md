---
id: supply-competitive-firm
title: Individual Firm Supply Curve in Competition
domain: economics
course: microeconomics
prerequisites:
- id: shutdown-condition-firm-loss
  type: hard
builds-toward:
- equilibrium-perfect-competition
tags:
- supply-curve
- firm-supply
- marginal-cost
- competitive-firm
stage: formal-systems
status: draft
---

# Individual Firm Supply Curve in Competition

## Core Idea
In a competitive market, the firm's supply curve is its marginal cost curve above the average variable cost (AVC). At any price, the firm produces the quantity where P = MC, as long as P ≥ AVC; if P < AVC, the firm shuts down and produces nothing. This relationship between price and profit-maximizing quantity is the individual firm's supply curve.

## How It's Best Learned
Derive the firm's supply curve by finding the MR = MC quantity for several different prices. Observe how the supply curve shifts when costs change (reflecting technological improvement or input price increases).

## Common Misconceptions
- Assuming firms always follow their supply curve—they do so only when profit-maximizing and facing competitive prices they cannot influence.

## Questions

```yaml
- question: "A competitive firm's input costs rise, shifting both its marginal cost and average variable cost curves upward. What happens to the firm's supply curve?"
  type: multiple-choice
  options:
    - "It shifts rightward — lower profit motivates the firm to produce more to remain viable"
    - "It shifts leftward — at every price, the firm is now willing to supply less"
    - "It does not shift — supply curves only shift when the market price changes"
    - "Only the shutdown point changes; the firm produces the same quantity at prices above AVC"
  answer: 1
  explanation: "The firm's supply curve is its MC curve above AVC minimum. When input costs rise, MC shifts upward — for any given price P, the P = MC condition is satisfied at a lower quantity, so the firm supplies less at every price. The supply curve shifts leftward (a decrease in supply). This is a direct consequence of supply being derived from the cost structure: any change in marginal cost shifts supply in the same direction."

- question: "A competitive firm's rent (a fixed cost) increases significantly. How does this affect its short-run supply curve?"
  type: multiple-choice
  options:
    - "The supply curve shifts leftward — higher costs always reduce supply"
    - "The supply curve shifts rightward — the firm must produce more to cover the higher cost"
    - "The supply curve does not shift — fixed costs do not affect marginal cost"
    - "The firm shuts down immediately since fixed costs now make production unprofitable"
  answer: 2
  explanation: "This is the most common misconception. Fixed costs (rent, licensing fees, equipment already purchased) do not affect marginal cost — they do not change with output. Since the supply curve is the MC curve above AVC, and neither MC nor AVC is changed by a fixed cost increase, the supply curve doesn't move. Fixed costs affect average total cost and the long-run exit decision, but not the short-run quantity decision at any given price."

- question: "A competitive firm's supply curve is the portion of its marginal cost curve that lies above the average variable cost curve minimum, because below that price the firm shuts down rather than produce."
  type: true-false
  answer: true
  explanation: "This is the precise definition of the individual firm's supply curve. The shutdown rule says a firm produces zero when P < AVC_min — it loses less by covering only fixed costs than by also losing money on each unit produced. For any price above AVC_min, the profit-maximizing output is found at P = MC (an upward-sloping portion of MC), so the supply curve traces the MC curve from the shutdown point upward."

- question: "A technological improvement that reduces marginal cost shifts the firm's supply curve leftward, because lower costs reduce the firm's incentive to produce."
  type: true-false
  answer: false
  explanation: "Lower marginal cost shifts supply rightward, not leftward. When MC falls, the P = MC condition is satisfied at a higher quantity for every price — the firm is willing and able to supply more at any given price. Intuitively, cheaper production means more units can be profitably produced. The supply curve is the MC curve, so moving the MC curve down/rightward moves the supply curve rightward (an increase in supply)."

- question: "Explain why the competitive firm's supply curve is derived from its marginal cost curve, and why a change in fixed costs does not shift it."
  type: short-answer
  answer: "A price-taking firm maximizes profit by producing where P = MC: the price received for one more unit exactly equals the cost of producing it. Sweeping P from zero upward maps out successively higher quantities along the upward-sloping MC curve (due to diminishing returns), giving the supply curve as the set of (P, q*) pairs that satisfy the profit-maximizing condition. Fixed costs are excluded from this logic because marginal cost is the derivative of variable cost with respect to quantity — fixed costs, by definition, don't change with output and therefore contribute nothing to MC. A fixed cost change shifts average total cost but leaves MC and AVC unchanged, so neither the P = MC quantity nor the shutdown threshold is affected. The supply curve stays put."
  explanation: "This derivation matters because it shows that supply is not an assumption — it is a consequence of rational profit-maximizing behavior under price-taking competition. It also means supply shifts only when the firm's cost of producing one more unit changes, which occurs with input price changes, technology changes, or anything else that moves the MC curve."
```

## Explainer

You already know the shutdown condition: a competitive firm shuts down and produces nothing when the market price falls below average variable cost. The **individual firm supply curve** is what you get when you trace how the firm's optimal quantity responds to *every* possible price. The result turns out to be something you've already computed — the marginal cost curve — but only the portion that matters for production decisions.

Here's the logic step by step. A competitive firm is a price-taker: it sees a market price P it cannot influence. Its profit is maximized by choosing output q where marginal cost equals that price: **P = MC**. This condition gives the output level that adds the most to revenue (an extra unit sells for P) while just breaking even on the cost of producing it (MC). If P > MC, producing one more unit adds more revenue than cost — expand. If P < MC, the last unit costs more than it earns — contract. Equilibrium is exactly at P = MC.

Now imagine sweeping P from $0 upward. Below average variable cost, the firm shuts down and produces zero (from your shutdown condition — covering variable costs is the minimum test for staying open). At exactly AVC minimum, the firm is indifferent between producing a small amount or nothing; this is the **shutdown point**. Above AVC minimum, the firm follows its MC curve: as P rises, the MC = P condition is satisfied at higher and higher quantities, because MC is upward sloping (due to diminishing returns). The supply curve is therefore the MC curve above the AVC minimum — a direct read-off of the firm's cost structure.

This means anything that shifts the cost curves shifts the supply curve. A technological improvement that lowers MC shifts supply rightward: for every price, the firm is now willing to produce more. Higher input prices shift MC upward, reducing supply. A fixed cost change (like a permit fee) shifts average cost but not marginal cost — so it affects the shutdown decision in the long run but not the shape of the supply curve in the short run. Understanding supply as "MC above AVC" gives you a direct connection between a firm's internal cost structure and its external market behavior. The supply curve is not an assumption — it is a derivation from profit-maximizing behavior under price-taking competition.
