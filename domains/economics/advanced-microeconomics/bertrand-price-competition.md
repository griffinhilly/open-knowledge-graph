---
id: bertrand-price-competition
title: Bertrand Price Competition
domain: economics
course: advanced-microeconomics
prerequisites:
- id: oligopoly-and-strategic-behavior
  type: hard
- id: monopoly-microeconomics
  type: hard
- id: game-theory-basics-microeconomics
  type: hard
- id: optimization-multivariable-basics
  type: hard
builds-toward:
- stackelberg-sequential-moves
tags:
- industrial-organization
- oligopoly
- pricing
stage: expert
status: validated
---

# Bertrand Price Competition

## Core Idea
Bertrand competition models firms simultaneously choosing prices, with demand allocating to the lowest-priced firm. The Bertrand paradox arises: with homogeneous products and identical costs, even two firms produce the competitive outcome (price equals marginal cost, zero profit). This contrasts sharply with Cournot, illustrating the sensitivity of oligopoly results to competition mode.

## Questions

```yaml
- question: "Two firms sell identical products with the same marginal cost of $10. They compete by simultaneously setting prices. In the Nash equilibrium, what price do both firms charge and what profit does each earn?"
  type: multiple-choice
  options:
    - "Both charge the monopoly price and split monopoly profits equally, since coordination is the rational outcome"
    - "Both charge $10 and earn zero profit — the perfectly competitive outcome despite there being only two firms"
    - "Both charge a price between $10 and the monopoly price, earning moderate positive profits as in Cournot competition"
    - "One firm charges the monopoly price and the other charges slightly below it, with the undercutter capturing the entire market"
  answer: 1
  explanation: "This is the Bertrand paradox. Any price above $10 invites undercutting: if firm A prices at $15, firm B can price at $14.99 and capture all demand. But firm A can then respond with $14.98, and so on. This cascades until P = MC = $10, where neither firm can profitably undercut (going below $10 means selling at a loss) and neither can raise price without losing all customers. The result is zero economic profit for both firms — identical to perfect competition, despite only two competitors. This sharply contrasts with Cournot duopoly, where both firms earn positive profits."

- question: "Two airlines operate the same route. Airline A has a marginal cost of $120 per seat; Airline B has $125 per seat. Both compete on price and the product (a seat on the route) is homogeneous. What is the Bertrand equilibrium?"
  type: multiple-choice
  options:
    - "Both airlines price at their own marginal cost — A at $120, B at $125 — and each serves its segment"
    - "Airline A prices just below $125 (e.g., $124.99), captures the entire market, and earns positive profit"
    - "Both airlines price at the average cost of $122.50 and split the market equally"
    - "Airline B exits the market immediately, leaving A as a monopolist charging the monopoly price"
  answer: 1
  explanation: "With asymmetric costs, the standard zero-profit paradox breaks down. Airline A can price just below B's marginal cost ($125) — say $124.99 — and capture the entire market. At this price, A earns a profit of approximately $4.99 per seat while B (unable to match without losing money) serves no passengers. This is the unique equilibrium: A prices at B's cost minus ε, B sells nothing. This extension illustrates that the Bertrand paradox (zero profit) depends on identical costs; even a small cost difference restores positive profit for the efficient firm."

- question: "In Bertrand competition with homogeneous products and identical costs, the Nash equilibrium price equals marginal cost even with only two firms."
  type: true-false
  answer: true
  explanation: "This is the Bertrand paradox in its exact form. The undercutting logic — that any price above MC invites profitable undercutting — cascades to P = MC regardless of how few firms there are. With just two firms, this produces the same outcome as a perfectly competitive market with infinitely many firms. The result is often called a 'paradox' because it defies the intuition that duopoly should yield market power and profits. The Nash equilibrium criterion confirms it: at P = MC, neither firm can profitably deviate (undercutting means losses; raising price loses all customers)."

- question: "The Bertrand paradox implies that price competition always leads to the competitive outcome, so any industry where firms set prices will earn zero profit in equilibrium."
  type: true-false
  answer: false
  explanation: "The paradox applies under specific conditions: homogeneous products, identical marginal costs, no capacity constraints, and simultaneous price-setting. Each relaxation restores positive profits. Product differentiation means a price cut no longer steals all customers — some consumers prefer the rival's product even at a slightly higher price. Capacity constraints prevent a firm from serving the entire market at a lower price, reducing the incentive to undercut. Asymmetric costs give the low-cost firm positive profit. The paradox is a useful benchmark, not a general prediction; its value is in identifying which real-world features are necessary for firms to earn positive profits in price-competing markets."

- question: "Why does the Bertrand paradox disappear when firms sell differentiated products, even if they still compete on price?"
  type: short-answer
  answer: "With homogeneous products, a tiny price cut captures the entire market — all consumers immediately switch to the cheaper seller. This extreme sensitivity makes undercutting irresistible until P = MC. With differentiated products, a price cut does not steal all rivals' customers, because some consumers value the rival's distinct characteristics (brand, quality, location) enough to stay despite the price difference. The demand curve facing each firm becomes downward-sloping rather than perfectly elastic. Each firm therefore has some pricing power: raising price above MC no longer loses all customers, so the undercutting incentive is diminished. The equilibrium price exceeds MC and firms earn positive profit, as each firm effectively has a mini-monopoly over consumers who strongly prefer its variety."
  explanation: "The key economic mechanism is the degree of substitutability. Perfect substitutes → perfectly elastic demand for each firm → Bertrand paradox. Imperfect substitutes → downward-sloping demand → market power. Product differentiation models (Hotelling's spatial competition, Dixit-Stiglitz monopolistic competition) formalize exactly this: firms earn profits in proportion to how differentiated their product is from rivals."
```

## Explainer

From your study of oligopoly and game theory, you know that a small number of firms interact strategically — each firm's optimal choice depends on what rivals do. In Cournot competition, firms choose quantities. **Bertrand competition** flips the strategic variable: firms simultaneously choose prices, and consumers buy from whichever firm charges less. This seemingly minor modeling choice produces dramatically different results, which is precisely why the Bertrand model is important — it reveals how sensitive oligopoly outcomes are to the nature of competition.

The logic behind the **Bertrand paradox** is elegant. Suppose two firms sell identical products with the same constant marginal cost c. If firm A charges any price above c, firm B can capture the entire market by undercutting slightly. But firm A reasons the same way about firm B. This undercutting logic cascades until both firms price at marginal cost — the perfectly competitive outcome — even though there are only two firms. Neither firm can profitably deviate: pricing below c means losses, and pricing above c means losing all customers. This is a Nash equilibrium, applying the concept you already know: each firm's price is a best response to the other's.

The paradox is striking because it contradicts the intuition that fewer firms means more market power. With Cournot competition among the same two firms, both earn positive profits. The difference arises because price competition with homogeneous goods is inherently more aggressive than quantity competition — a tiny price cut steals the entire market, whereas a small quantity increase only modestly affects the market price. This sensitivity to the competition mode is one of the most important lessons in industrial organization: the structure of strategic interaction matters as much as the number of competitors.

The Bertrand paradox motivates several important extensions that restore positive profits. **Product differentiation** breaks the paradox because a small price cut no longer captures the entire market — some consumers prefer the rival's variant. **Capacity constraints** also matter: if firms cannot serve the entire market at marginal cost, undercutting is less profitable. **Asymmetric costs** give the lower-cost firm positive profit since it can price just below its rival's cost. Each extension reveals which real-world features prevent the extreme competitive outcome the basic Bertrand model predicts, and understanding the paradox is essential for evaluating which modeling assumptions are appropriate for any given industry.
