---
id: monopolistic-competition
title: Monopolistic Competition
domain: economics
course: microeconomics
prerequisites:
- id: perfect-competition
  type: hard
- id: monopoly-microeconomics
  type: hard
builds-toward:
- oligopoly-and-strategic-behavior
tags:
- monopolistic competition
- product differentiation
- excess capacity
- zero profit
stage: formal-systems
status: validated
---

# Monopolistic Competition

## Core Idea
Monopolistic competition features many firms selling differentiated products, free entry and exit, and some degree of market power for each firm due to differentiation. In the short run, firms can earn positive economic profit; in the long run, entry drives profit to zero (as in perfect competition). The long-run equilibrium has each firm on the downward-sloping portion of its LRAC (excess capacity), meaning the industry is not at minimum efficient scale. This is the cost of product variety.

## How It's Best Learned
Contrast long-run equilibrium in perfect competition (P = min LRAC) with monopolistic competition (P = LRAC but above min LRAC, with excess capacity). Examples from retail and restaurants make the model concrete.

## Common Misconceptions
- Zero long-run profit in monopolistic competition does not mean the outcome is efficient; excess capacity and markup over MC are present, unlike perfect competition.
- Product differentiation means each firm faces a downward-sloping (not horizontal) demand curve even with free entry.

## Questions

```yaml
- question: "Many Thai restaurants operate in a city under monopolistic competition. A popular new Thai restaurant opens nearby. In the long run, what happens to the economic profit of existing Thai restaurants?"
  type: multiple-choice
  options:
    - "It increases — more restaurants attract more customers to the area overall"
    - "It remains positive — product differentiation protects each firm's market power from new entrants"
    - "It falls to zero — free entry shifts each incumbent's demand curve leftward until economic profit is eliminated"
    - "It falls to zero only if the new restaurant is an exact substitute; differentiation prevents full profit erosion"
  answer: 2
  explanation: "Free entry is the key mechanism. New entrants steal customers from incumbents, shifting each firm's demand curve leftward and making it more elastic. This reduces both price and quantity for existing firms. Entry continues until economic profit reaches zero. Product differentiation gives each firm a downward-sloping demand curve (some market power), but it does not prevent the profit-eroding effect of free entry. The same mechanism operates in perfect competition; the long-run equilibrium condition is the same, but the location on the LRAC curve differs."

- question: "In the long-run equilibrium of a monopolistically competitive market, what is the primary source of economic inefficiency?"
  type: multiple-choice
  options:
    - "Firms produce below minimum efficient scale, resulting in excess capacity and price above marginal cost"
    - "Firms earn accounting losses that prevent them from covering fixed costs in the long run"
    - "Advertising expenditures by firms generate negative externalities for competing firms"
    - "Consumer welfare is reduced because there are too many product varieties to evaluate"
  answer: 0
  explanation: "In long-run monopolistic competition, the demand curve is tangent to the LRAC curve to the left of its minimum. Firms operate with excess capacity — producing less than the output that minimizes average cost. At this tangency point, P = LRAC (zero economic profit) but P > MC and LRAC > min LRAC. Both signal inefficiency: P > MC means allocative inefficiency, and LRAC > min LRAC means productive inefficiency. This is the 'cost of variety': society gets differentiated products but pays in higher average costs than a world of standardized goods would require."

- question: "In long-run equilibrium, both perfect competition and monopolistic competition achieve P = LRAC (zero economic profit), so they have identical efficiency outcomes."
  type: true-false
  answer: false
  explanation: "Both reach P = LRAC, but the location on the LRAC curve is fundamentally different. In perfect competition, P = min LRAC — firms operate at efficient scale, the lowest possible average cost. In monopolistic competition, the tangency condition gives P = LRAC at a point above and to the left of the minimum, meaning firms have excess capacity and higher-than-minimum average cost. The zero-profit condition is the same; the efficiency properties are not."

- question: "Product differentiation gives each firm in monopolistic competition a downward-sloping demand curve, even after long-run entry drives economic profit to zero."
  type: true-false
  answer: true
  explanation: "Unlike perfectly competitive firms (horizontal demand curves), monopolistically competitive firms face downward-sloping demand because their products are imperfect substitutes. Consumers who prefer a specific brand won't immediately switch when the price rises slightly. This market power persists in long-run equilibrium — what free entry eliminates is the profit, not the market power. In long-run equilibrium the demand curve is still downward-sloping; it has shifted leftward until it is tangent to the LRAC curve."

- question: "Explain why long-run zero economic profit in monopolistic competition does not mean the market is productively efficient, using the concept of excess capacity."
  type: short-answer
  answer: "In monopolistic competition's long-run equilibrium, the demand curve is tangent to the LRAC curve to the left of the minimum point. Each firm produces less than the output that would minimize average cost — it operates with excess capacity. Average cost is higher than the minimum achievable, so resources aren't used as efficiently as possible. Productive efficiency requires P = min LRAC (as in perfect competition); here P = LRAC > min LRAC. Zero economic profit only means firms cover their costs — not that they cover them at the lowest possible cost per unit."
  explanation: "The excess capacity result is the 'cost of variety': society gets more differentiated products but pays in higher average costs than a standardized-goods world would require. Whether the variety is worth the inefficiency is normative, but the productive inefficiency itself is unambiguous. This is the key contrast to memorize: zero profit is the same condition in both market structures; excess capacity is what makes monopolistic competition distinctively inefficient."
```

## Explainer

Monopolistic competition sits between the two market structures you already know. From perfect competition, it inherits two features: **many firms** and **free entry and exit**. From monopoly, it inherits one: each firm has some **market power** because it sells a product that is distinct from its competitors' products. Think of restaurants, clothing brands, or hair salons. There are many of them, anyone can open one, but your preferred Thai restaurant is not a perfect substitute for the Vietnamese place next door. This product differentiation gives each seller a downward-sloping demand curve — if it raises its price slightly, it loses some but not all customers. This is the defining characteristic that separates monopolistic competition from perfect competition, where the firm faces a horizontal demand curve.

In the **short run**, monopolistically competitive firms behave like monopolists within their niche: they set output where MR = MC and charge a price above marginal cost. If demand is strong enough, they earn positive economic profit. But this profit is temporary. Free entry means new competitors will enter, stealing customers and shifting each incumbent's demand curve leftward and making it more elastic. This entry continues until economic profit is driven to zero — the same long-run result as perfect competition. The mechanism is identical: profit attracts entry, entry reduces demand for each existing firm, profits fall until the incentive to enter disappears.

The **long-run equilibrium** looks different from perfect competition's, however. In perfect competition, zero-profit equilibrium occurs where P = min LRAC — the firm operates at efficient scale, the lowest possible average cost. In monopolistic competition, zero-profit equilibrium requires only that the demand curve be *tangent* to the LRAC curve — touching it at a point to the left of the minimum. At this tangency point, price equals average cost (zero profit), but the firm is operating with **excess capacity**: it is producing less than the output that would minimize average cost. Average cost is higher than the minimum achievable, and price exceeds marginal cost (P > MC), so the market outcome is not allocatively efficient.

This **excess capacity theorem** is the key welfare result for monopolistic competition. The gap between actual output and efficient-scale output is the cost of product variety. Society gets a wider range of differentiated products — more flavor options, more restaurant cuisines, more clothing styles — but pays for it in higher average costs and prices than a world of standardized goods would require. Whether this tradeoff is worthwhile is a normative question: consumers may value variety enough to accept higher costs. The point is simply that variety is not free, and monopolistic competition makes the price of variety explicit.
