---
id: monopoly-output-and-pricing
title: Monopoly Output and Pricing Decisions
domain: economics
course: microeconomics
prerequisites:
- id: monopoly-microeconomics
  type: hard
builds-toward:
- deadweight-loss-monopoly
- price-discrimination
tags:
- market structure
- monopoly
- pricing
stage: formal-systems
status: validated
---

# Monopoly Output and Pricing Decisions

## Core Idea
A monopolist faces the downward-sloping market demand and maximizes profit by setting output where marginal revenue equals marginal cost, then charging the corresponding demand price. Since MR < P for a monopolist, equilibrium output is lower and price higher than competitive level. The monopolist earns economic profit in long run (no entry threat), and can maintain barriers to entry through patents, scale economies, or control of inputs.

## Questions

```yaml
- question: "A monopolist determines that at an output of 200 units, marginal revenue equals marginal cost ($15). The demand curve shows consumers will pay $25 for the 200th unit. What price does the profit-maximizing monopolist charge?"
  type: multiple-choice
  options:
    - "$15 — the monopolist sets price equal to marginal revenue at the profit-maximizing quantity"
    - "$15 — the monopolist sets price equal to marginal cost to cover costs"
    - "$25 — the monopolist reads the price off the demand curve at the profit-maximizing quantity"
    - "$20 — the monopolist splits the difference between marginal cost and the demand price"
  answer: 2
  explanation: "Monopoly pricing is a two-step procedure: (1) find Q* where MR = MC — this gives the profit-maximizing quantity of 200 units. (2) Charge the price the demand curve will bear at Q* — consumers will pay $25 for 200 units, so P* = $25. The monopolist does NOT set P = MR. MR = MC determines how much to produce; the demand curve then determines what to charge for that quantity. The gap between P ($25) and MC ($15) is the per-unit markup that generates economic profit."

- question: "Why is a monopolist's marginal revenue always less than the price it charges?"
  type: multiple-choice
  options:
    - "Because monopolists are less efficient producers, so their revenues are reduced by higher costs"
    - "Because government regulations cap the revenue monopolists can earn per unit sold"
    - "Because to sell one more unit, the monopolist must lower the price on all units sold — the gain from the extra unit is reduced by the revenue lost on previous units"
    - "Because monopolists face upward-sloping supply curves that reduce their per-unit revenue"
  answer: 2
  explanation: "A competitive firm is a price-taker — it can sell as much as it wants at the going market price, so each extra unit adds exactly P to revenue (MR = P). A monopolist faces the downward-sloping market demand directly: to sell one additional unit, it must lower the price for all units (since all buyers face the same posted price). The revenue gained from the extra unit is partially offset by the revenue lost on all previous units due to the price reduction. This is why MR < P and why the MR curve lies below the demand curve."

- question: "A profit-maximizing monopolist maximizes its total revenue by producing the quantity where marginal revenue equals zero."
  type: true-false
  answer: false
  explanation: "A monopolist maximizes *profit*, not *revenue*. Revenue is maximized at MR = 0 (the point where the last unit adds nothing to total revenue). But profit equals revenue minus cost, so the profit-maximizing monopolist stops short of that — at MR = MC. Since MC is typically positive, the profit-maximizing output is less than the revenue-maximizing output. Confusing these two objectives is a common error: setting MR = 0 would mean producing units that add to revenue but add more to cost, reducing profit."

- question: "Even without government intervention, a monopolist produces less than the socially efficient quantity, because restricting output allows it to charge a higher price than would prevail under competition."
  type: true-false
  answer: true
  explanation: "The socially efficient outcome is where P = MC — all mutually beneficial trades occur. A monopolist sets MR = MC and then charges P > MC. This means some trades that would benefit both the buyer (who values the good above MC) and the firm (which can produce at MC) simply don't happen, because the monopolist restricts output to maintain the higher price. The value of these forgone transactions is deadweight loss — the efficiency cost of monopoly. The output restriction is not accidental; it is the mechanism by which the monopolist maintains price above marginal cost."

- question: "Explain the two steps a profit-maximizing monopolist uses to set price and quantity, and why it does not simply charge the highest possible price."
  type: short-answer
  answer: "Step 1: Find Q* where MR = MC — this is the profit-maximizing quantity. Step 2: Charge the price the demand curve will bear at Q* — the highest price consumers will pay for exactly Q* units. The monopolist does not charge the absolute maximum (the demand intercept for a single unit) because that would sacrifice all the profit from the many units it could profitably sell at lower prices. MR = MC balances marginal revenue against marginal cost to find the quantity that maximizes total profit, not per-unit markup."
  explanation: "The monopolist is constrained by the demand curve — it cannot independently set both price and quantity. Higher prices require selling fewer units; lower prices allow more sales. The MR = MC rule finds the quantity that maximizes the difference between total revenue and total cost. Charging more than P* would mean selling fewer units than Q*, and the lost revenue would exceed the gain per unit. The two-step procedure — find Q* from MR = MC, then read P* off demand — is what separates monopoly analysis from competitive analysis, where P = MR = MC."
```

## Explainer

From your study of monopoly, you know that a monopolist is the sole seller in a market, which means it faces the downward-sloping market demand curve directly. This single fact drives everything else about monopoly pricing. In a competitive market, each firm is a price-taker — it can sell as much as it wants at the going market price, so its marginal revenue equals the price. For a monopolist, selling one more unit requires lowering the price on all units sold (because the demand curve slopes down). This means **marginal revenue (MR) is always less than price** for a monopolist — the extra revenue from selling the additional unit is reduced by the price cut applied to all previous units.

The profit-maximizing output rule is the same as always: produce where MR = MC. But the pricing step is different. Once the monopolist finds the profit-maximizing quantity Q* where MR = MC, it does not charge that MR — it looks up to the demand curve to find the highest price consumers will pay for Q*. This two-step process — find Q* from the MR = MC intersection, then read P* off the demand curve above it — is the defining procedure of monopoly analysis. The gap between price and marginal cost at Q* is the monopolist's **markup**, and it represents a transfer of value from consumers to the firm.

The efficiency cost is real. At the competitive outcome, price equals marginal cost and all mutually beneficial trades occur. The monopolist restricts output below that level to maintain a higher price, which means some trades that would benefit both buyer and seller do not happen. This forgone surplus is **deadweight loss** — the hallmark of monopoly inefficiency. The further price is above marginal cost (captured by the Lerner index: (P − MC)/P = 1/|ε|, where ε is the price elasticity of demand), the greater the distortion.

What sustains the monopoly in the long run is the **barrier to entry**. In competitive markets, economic profit attracts entry until profit is competed away. A monopolist earns persistent economic profit only if entry is blocked — by a patent granting exclusive rights, by economies of scale so large that a new entrant cannot compete profitably (natural monopoly), or by exclusive control of a critical input. Understanding which barrier applies in a given market is essential for predicting whether regulation, antitrust enforcement, or natural erosion of the barrier will eventually restore competitive pricing.
