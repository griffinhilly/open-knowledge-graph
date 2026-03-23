---
id: monopoly-pricing-markup
title: Monopoly Pricing and Markup Behavior
domain: economics
course: microeconomics
prerequisites:
- id: monopoly-sources-barriers
  type: hard
- id: profit-maximization-output-level
  type: hard
builds-toward:
- consumer-surplus-deadweight-loss-policy
tags:
- monopoly-pricing
- markup
- deadweight-loss
- economic-profit
stage: formal-systems
status: validated
---

# Monopoly Pricing and Markup Behavior

## Core Idea
A monopolist faces the entire market demand curve and chooses output where MR = MC, then sets price on the demand curve above this quantity. The monopolist prices above marginal cost (P > MC), earning a markup that covers fixed costs and generates economic profit. This pricing power creates deadweight loss by restricting output below the socially efficient level where P = MC. The extent of markup depends on demand elasticity: more elastic demand limits pricing power.

## How It's Best Learned
Compare monopoly and competition outcomes graphically and numerically, calculating price, output, profit, and deadweight loss in each case. Use the Lerner Index (L = (P - MC) / P) to measure markup and relate it to elasticity.

## Common Misconceptions
- Thinking monopolists maximize profit by maximizing markups—they maximize profit where MR = MC, which may or may not involve high markups.
- Assuming monopolists always earn economic profit—in some cases, demand and cost structures may leave monopolists with losses.

## Questions

```yaml
- question: "A monopolist is currently producing at quantity Q* where MR = MC, charging price P* = $20 with MC = $8. A consultant advises raising the price to $25 to capture more profit per unit. Why is this advice likely wrong?"
  type: multiple-choice
  options:
    - "Monopolists are legally required to keep prices within a regulated range of MC"
    - "Raising price above the MR = MC point reduces total profit because the revenue lost from selling fewer units exceeds the gain from a higher price per unit"
    - "Higher prices always reduce total revenue for any firm with a downward-sloping demand curve"
    - "The consultant is correct — monopolists always maximize profit by charging the highest possible price"
  answer: 1
  explanation: "The profit-maximizing rule is MR = MC, not 'maximize the markup.' At Q* (where MR = MC), the monopolist has already pushed output to the point where the marginal profit from an additional unit is zero. Raising price further means selling fewer units than Q* — each of those lost sales had MR > MC (positive marginal profit), so eliminating them reduces total profit. Option D is the classic misconception: charging the highest possible price typically means selling zero units."

- question: "A pharmaceutical firm with a patented drug (few substitutes) and a commodity grain producer both behave as price-setters. Which firm can sustain a larger markup, and why?"
  type: multiple-choice
  options:
    - "The grain producer — commodity markets are larger and more profitable"
    - "The pharmaceutical firm — inelastic demand means consumers are less price-sensitive, so a large markup loses relatively few sales"
    - "Both face the same markup constraint since both apply the MR = MC rule"
    - "The pharmaceutical firm — it faces a steeper demand curve, which always implies higher marginal revenue"
  answer: 1
  explanation: "The Lerner Index L = (P − MC)/P = −1/ε shows that markup depends on demand elasticity. With inelastic demand (small |ε|), raising price loses few sales, so the markup can be large. The pharmaceutical firm with no substitutes faces very inelastic demand. The grain producer faces elastic demand (buyers can easily switch to another supplier), so a large markup would cause severe sales losses. This is the direct empirical prediction of monopoly theory."

- question: "The deadweight loss from monopoly pricing represents value destroyed by the monopolist's output restriction — it belongs to neither the monopolist nor consumers."
  type: true-false
  answer: true
  explanation: "Deadweight loss consists of units between Q* (monopoly output) and Q_c (competitive output) where demand exceeds MC — buyers value these units more than they cost to produce — but they go unproduced because the monopolist has restricted output. This value is not captured by the firm as profit, nor is it received by consumers as surplus; it simply does not exist. The monopolist's profit itself is a transfer from consumers to the firm, not a social loss. The DWL is the pure social cost of monopoly."

- question: "A monopolist maximizes profit by maximizing the markup (P − MC) per unit, since a larger markup means more profit on every unit sold."
  type: true-false
  answer: false
  explanation: "Profit maximization requires MR = MC, not maximum markup. The markup and profit-maximizing quantity are jointly determined by demand and cost conditions. Setting an extreme markup means very few units sold — total profit (markup × quantity) can be far below the MR = MC optimum. A monopolist could technically charge $1 million per unit but sell zero. Maximum markup and maximum profit are generally different outcomes."

- question: "Why is a monopolist's marginal revenue less than its price, and how does this difference drive the MR = MC profit-maximizing rule?"
  type: short-answer
  answer: "A monopolist faces a downward-sloping demand curve, so to sell one more unit it must lower the price on all units sold. The revenue gained from the extra unit equals P, but the firm loses (the price reduction) multiplied by (all previous units sold). MR = P + Q·(dP/dQ) < P because dP/dQ < 0 for downward-sloping demand. For linear demand, MR has the same intercept but twice the slope. Profit is maximized where MR = MC: if MR > MC, producing more adds profit; if MR < MC, producing more destroys profit. The optimal Q* is where these exactly balance."
  explanation: "This infra-marginal effect is the fundamental reason monopoly pricing differs from competitive pricing. A competitive firm takes price as given (faces a horizontal demand curve) so MR = P. The monopolist internalizes the price effect of its own output decision, which depresses MR below P and drives the wedge P > MC at the optimum — the source of both the monopoly markup and the deadweight loss."
```

## Explainer

A competitive firm takes price as given and produces where P = MC — it can't charge more because rivals offer the same good at lower prices. A monopolist faces no such discipline. It is the only seller, so the demand curve it faces is the entire market demand curve. But this doesn't mean the monopolist can charge any price it wants — it must choose a point on the demand curve. Higher prices mean fewer units sold, so there is a genuine trade-off.

The profit-maximizing decision follows directly from the logic you learned in general output choice: produce where **marginal revenue equals marginal cost** (MR = MC). The critical difference from competition is that the monopolist's **marginal revenue** is less than price. When you sell one more unit, you earn the price for that unit — but you've had to lower the price on all previous units (since the demand curve slopes down). This loss on infra-marginal units reduces MR below P for any downward-sloping demand. For a linear demand curve, MR has the same intercept but twice the slope — MR falls twice as fast as price as output rises.

To find the monopoly outcome: locate Q* where MR = MC, then go up to the demand curve to find the **monopoly price** P*. This price exceeds MC — the monopolist charges a **markup**. The **Lerner Index** quantifies this: L = (P − MC)/P = −1/ε, where ε is the price elasticity of demand. An elasticity of −2 gives L = 0.5, meaning price is 100% above marginal cost; an elasticity of −5 gives L = 0.2. More elastic demand disciplines the monopolist — consumers are price-sensitive and a large markup loses too many sales. Less elastic demand grants more pricing power. This is why pharmaceutical firms with patented drugs (inelastic demand — there are no substitutes) can charge enormous markups while commodity producers facing elastic demand cannot.

The social cost of monopoly is **deadweight loss**: the value of transactions that would have occurred under competition but don't occur under monopoly because output is restricted. Units between Q* and the competitive quantity Q_c have demand exceeding MC — buyers value them more than they cost to produce — yet they go unproduced. This lost value belongs to neither the monopolist nor consumers; it's destroyed. The monopolist's profit represents a transfer from consumers to the firm (consumer surplus captured as producer surplus), but the deadweight loss is a pure social loss. This is the fundamental economic rationale for antitrust law and regulation of monopoly pricing: the private optimum is socially inefficient.
