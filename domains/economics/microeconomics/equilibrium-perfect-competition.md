---
id: equilibrium-perfect-competition
title: Market Equilibrium in Perfect Competition
domain: economics
course: microeconomics
prerequisites:
- id: supply-competitive-firm
  type: hard
- id: perfect-competition
  type: soft
- id: perfect-competition-firm-and-industry
  type: soft
builds-toward:
- zero-profit-long-run-entry
tags:
- market-equilibrium
- supply-demand
- perfect-competition
- price-taker
stage: formal-systems
status: validated
---
# Market Equilibrium in Perfect Competition

## Core Idea
In a perfectly competitive market, the equilibrium price is where the market supply curve (sum of all firm supply curves) intersects the market demand curve. At this price, quantity supplied equals quantity demanded. Individual firms are price-takers, accepting the equilibrium price as given. Competitive markets are efficient: equilibrium allocates resources to their highest-value uses (consumer and producer surplus are maximized).

## How It's Best Learned
Aggregate individual firm supply curves to derive the market supply curve. Find the intersection with market demand to determine equilibrium price and quantity. Analyze welfare by calculating consumer and producer surplus.

## Common Misconceptions
- Thinking competitive firms set prices—price-takers accept the market price.
- Assuming competitive equilibrium is optimal from the perspective of individual firms—equilibrium may involve losses that drive exit.

## Questions

```yaml
- question: "The equilibrium price in a perfectly competitive market is $10, but a particular firm's average total cost at its profit-maximizing output is $14. What will this firm do in the short run?"
  type: multiple-choice
  options:
    - "Raise its price to $14 to cover its costs"
    - "Lobby the government for a subsidy since it cannot survive at the market price"
    - "Continue producing as a price-taker, accepting the $10 price, and sustain a loss of $4 per unit"
    - "Increase output to spread fixed costs and reduce average total cost below $10"
  answer: 2
  explanation: "Competitive firms are price-takers — they cannot raise their price above the market equilibrium without losing all customers. In the short run, a firm producing where P = MC may still face losses if ATC exceeds price. It will continue operating as long as price covers average variable cost (since fixed costs are sunk), but it sustains an economic loss. This loss signals that resources should exit this industry — which drives the long-run adjustment toward zero economic profit. Option A is the key misconception: competitive firms do NOT set prices."

- question: "A competitive market is in equilibrium. At the equilibrium quantity, the last unit produced costs $20 to produce, and consumers value it at $20. What does this tell us about the efficiency of the outcome?"
  type: multiple-choice
  options:
    - "The market has failed, because the firm earns zero profit on the last unit"
    - "The allocation is inefficient, because surplus could increase by producing more"
    - "The allocation is allocatively efficient: the value of the last unit to consumers exactly equals the cost of producing it"
    - "The allocation is efficient only if all firms are earning positive economic profits"
  answer: 2
  explanation: "Allocative efficiency means output is carried to the point where marginal benefit (the demand curve) equals marginal cost (the supply curve). The equilibrium is where these intersect, so the last unit produced is worth exactly as much to consumers as it costs to produce. Producing less would leave unrealized gains (consumers willing to pay more than the cost); producing more would mean the last unit costs more to produce than buyers value it. Total surplus — consumer plus producer — is maximized at this point. Whether any individual firm earns a profit is separate from whether the aggregate allocation is efficient."

- question: "In a perfectly competitive market, individual firms have no influence over the equilibrium price — they are price-takers who accept the market price as given."
  type: true-false
  answer: true
  explanation: "This is the defining feature of perfect competition: each firm is so small relative to the market that its individual output decision has a negligible effect on the total quantity supplied, and therefore on price. The market price is determined by the intersection of the market supply curve (aggregated across all firms) and the market demand curve. Any individual firm that tried to charge above the market price would lose all its customers to competitors offering identical products at the market price."

- question: "A competitive market equilibrium guarantees that most firms in the market are earning at least normal (zero economic) profit."
  type: true-false
  answer: false
  explanation: "Short-run competitive equilibrium guarantees allocative efficiency, not profitability. The equilibrium price is set by supply and demand, not by firms' average costs. At the short-run equilibrium, some firms may earn positive economic profits, some may break even, and some may sustain losses — depending on their individual cost structures. Profitability drives long-run entry and exit, which ultimately pushes toward zero economic profit in the long run, but short-run equilibrium carries no such guarantee."

- question: "A perfectly competitive equilibrium is called 'allocatively efficient.' What exactly is efficient about it, and from whose perspective?"
  type: short-answer
  answer: "Allocative efficiency means the total quantity produced is exactly the amount where the value of the last unit to consumers (the demand curve) equals the cost of producing it (the supply curve). No reallocation could increase the combined welfare of buyers and sellers — total consumer surplus plus producer surplus is maximized. It is efficient from society's aggregate perspective, not from any individual firm's perspective."
  explanation: "The efficiency is in the aggregate: no potential trade goes unrealized, and no resources are wasted producing units that cost more than they are worth. This contrasts with, say, a monopoly, which produces less than the efficient quantity and creates deadweight loss. It is not efficiency in the sense of being good for individual firms — a firm in competitive equilibrium may be losing money, and from its perspective, a higher price would be preferable. The social optimality result holds only under perfect competition's full assumptions (no externalities, no market power, complete information)."
```

## Explainer

You already know how an individual competitive firm determines its supply: it produces where price equals marginal cost, tracing out an upward-sloping supply curve as price varies. To get from individual firm behavior to market outcomes, you aggregate. The **market supply curve** is the horizontal sum of every firm's supply curve — at any given price, add up all the quantities that individual firms are willing to sell. This sounds mechanical, but the insight is significant: changes in the number of firms shift the entire market supply curve. More entrants push market supply rightward; exits shift it leftward.

Market equilibrium occurs where this aggregated market supply meets the market demand curve. At the equilibrium price, the quantity all firms together want to sell exactly equals the quantity all consumers want to buy. No unsold inventory piles up; no willing buyer is turned away. This is the self-correcting mechanism of competitive markets: if price is above equilibrium, supply exceeds demand and prices are bid down; if price is below equilibrium, demand exceeds supply and prices are bid up. The equilibrium is stable because deviations generate forces that restore it.

An important subtlety: a competitive equilibrium need not be profitable for individual firms. The market price is determined by the intersection of supply and demand, regardless of firms' average costs. At equilibrium, firms might earn economic profits, break even at normal returns, or sustain losses. This matters because profitability drives long-run **entry and exit** — the mechanism behind the zero-profit equilibrium you'll study next. What short-run competitive equilibrium guarantees is not profit, but **allocative efficiency**: output is produced up to the quantity where the last unit's value to consumers (the demand curve) equals the cost of producing it (the supply curve), maximizing the total of **consumer surplus** and **producer surplus**.

The efficiency result is one of economics' deepest insights: millions of self-interested individuals, coordinating only through prices, produce an allocation that a benevolent central planner would struggle to improve upon. Each **price-taker** firm accepts the market price as given and responds by adjusting quantity — and the aggregate of those individual responses happens to generate the socially optimal output level. This holds, however, only under the assumptions of perfect competition — no market power, no externalities, complete information. Real markets deviate from these assumptions in important ways, which is precisely what motivates the remainder of microeconomic theory.
