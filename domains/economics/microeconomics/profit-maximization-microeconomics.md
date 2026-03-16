---
id: profit-maximization-microeconomics
title: Profit Maximization
domain: economics
course: microeconomics
prerequisites:
- id: short-run-costs
  type: hard
- id: marginal-utility-and-consumer-choice
  type: soft
- id: derivative-as-slope-of-tangent
  type: soft
- id: optimization-problems
  type: soft
- id: first-derivative-test
  type: soft
- id: second-derivative-test
  type: soft
- id: long-run-costs-economies-of-scale
  type: soft
builds-toward:
- perfect-competition
- monopoly-microeconomics
- shutdown-and-breakeven
tags:
- profit maximization
- MR=MC
- economic profit
- marginal revenue
stage: abstract-reasoning
status: validated
---
# Profit Maximization

## Core Idea
A profit-maximizing firm produces the quantity where marginal revenue (MR) equals marginal cost (MC), provided price exceeds average variable cost. Profit equals total revenue minus total cost; economic profit differs from accounting profit by subtracting implicit (opportunity) costs. MR = MC is the universal profit-maximization condition across all market structures, though MR differs by structure: for a price-taker, MR = P; for a monopolist, MR < P. The second-order condition requires MC to be rising at the optimum.

## How It's Best Learned
First demonstrate MR = MC numerically using a table of revenues and costs, then graphically, then using calculus. Compare economic and accounting profit explicitly using a numerical example with implicit costs.

## Common Misconceptions
- Students confuse maximizing revenue (MR = 0) with maximizing profit (MR = MC).
- Zero economic profit does not mean the firm should exit — it means all resources including the owner's opportunity costs are being compensated.

## Questions

```yaml
- question: "A firm currently produces 100 units, where marginal revenue is $20 and marginal cost is $15. What should it do to maximize profit?"
  type: multiple-choice
  options: ["Reduce output, since costs are rising", "Hold output steady, since MR > MC already means it is profitable", "Increase output, since each additional unit adds more revenue than cost", "Set output where marginal revenue equals zero"]
  answer: 2
  explanation: "When MR > MC, producing one more unit adds more to revenue than to cost, so profit increases. The firm should expand until MR = MC. Option 3 (MR = 0) maximizes total revenue, not profit — a common confusion. Stopping at the current output leaves money on the table."

- question: "A firm earning zero economic profit is failing to cover its costs and should consider shutting down."
  type: true-false
  answer: false
  explanation: "Zero economic profit means total revenue exactly covers all costs including implicit (opportunity) costs — the owner's forgone salary, the return on capital that could have been invested elsewhere. The firm's accounting profit is actually positive. A zero-economic-profit firm is doing exactly as well as its next-best alternative, so there is no reason to exit."

- question: "Explain why a firm that sets output to maximize total revenue is not necessarily maximizing profit."
  type: short-answer
  answer: "Revenue is maximized where MR = 0 (the last unit adds nothing to revenue). But profit = revenue - cost, so profit is maximized where MR = MC. As long as MC > 0, the firm sacrifices more in costs than it gains in revenue by pushing output to MR = 0. The only case where revenue-maximizing and profit-maximizing coincide is if MC = 0."
  explanation: "This misconception arises from ignoring costs. A firm could sell more units and earn more revenue while its costs rise even faster, shrinking profit. The MR = MC rule balances the marginal gain against the marginal cost, identifying the true optimum."
```

## Explainer

Profit is total revenue minus total cost — but maximizing it is not as simple as making revenue as large as possible or cost as small as possible. The key insight is marginal analysis: at any given output level, ask whether producing one more unit would add more to revenue or more to cost. If the answer is revenue (MR > MC), produce more. If the answer is cost (MC > MR), produce less. At the quantity where MR = MC, no further adjustment improves profit — you have found the optimum.

This MR = MC rule applies universally across all market structures, but what marginal revenue looks like varies. For a perfectly competitive firm that takes the market price as given, every unit sells at the same price P, so MR = P. For a monopolist who must lower price to sell more, MR < P because the price cut applies to all previous units. Despite this difference, the logic of comparing marginal revenue to marginal cost remains identical.

A critical distinction that trips up many students is economic profit versus accounting profit. Accounting profit subtracts only explicit costs — wages paid, inputs purchased, rent written on an invoice. Economic profit also subtracts implicit costs: the value of what the owner's time, capital, and resources could have earned in their best alternative use. A bakery owner who earns $80,000 revenue, pays $60,000 in explicit costs, but could have earned $30,000 working for someone else has an accounting profit of $20,000 but an economic profit of −$10,000. The business is actually destroying value relative to the alternative.

This is why zero economic profit is not a crisis. It means the firm is earning exactly the competitive return — all resources, including the owner's opportunity cost, are being fully compensated. In a competitive market, zero long-run economic profit is the normal equilibrium outcome. Firms enter when economic profit is positive (attracting competition) and exit when it is negative (resources leave for better uses). The market settles at zero economic profit, which is efficient, not dismal.

One technical condition often glossed over: the second-order condition. The MR = MC intersection identifies a profit maximum only if MC is rising at that point (or equivalently, if the profit function is concave there). If MC is falling, you may be at a profit minimum instead. For most standard cost curves with the typical U-shaped average cost structure, this condition holds at the relevant output levels, but it is worth verifying when working with unusual cost functions.
