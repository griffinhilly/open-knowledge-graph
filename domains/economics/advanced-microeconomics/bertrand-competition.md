---
id: bertrand-competition
title: 'Bertrand Competition: Price Competition in Oligopoly'
domain: economics
course: advanced-microeconomics
prerequisites:
- id: oligopoly-and-strategic-behavior
  type: hard
- id: cournot-competition
  type: soft
- id: cartel-and-collusion
  type: soft
builds-toward:
- product-differentiation
tags:
- industrial-organization
- oligopoly
stage: expert
status: validated
---
# Bertrand Competition: Price Competition in Oligopoly

## Core Idea
Firms simultaneously set prices; consumers buy from the cheapest seller. With homogeneous products, any firm can undercut competitors to capture the entire market. This drives prices to marginal cost (near-perfect-competition outcome) with just two firms. Bertrand equilibrium illustrates the importance of product differentiation: differentiation creates pricing power by reducing substitutability.

## Questions

```yaml
- question: "Two identical airlines operate the same route with the same cost per seat. Neither can charge above the other's price and still sell tickets. According to Bertrand competition logic, what should equilibrium prices look like?"
  type: multiple-choice
  options:
    - "Prices settle midway between monopoly and competitive levels, as in Cournot competition."
    - "Prices converge to marginal cost, earning each airline near-zero economic profit, because each has an incentive to undercut the other until no profitable undercut remains."
    - "Prices rise to monopoly levels over time because both firms recognize their mutual dependence."
    - "Prices are indeterminate — game theory cannot predict an outcome without knowing demand elasticity."
  answer: 1
  explanation: "With homogeneous products (identical seats on the same route), unlimited capacity, and simultaneous price setting, the Bertrand logic applies: if either airline charges above marginal cost, the other can undercut slightly and capture the entire market. This undercutting cascade continues until both charge marginal cost, at which point no profitable deviation exists. The result is the Bertrand paradox: a duopoly produces the perfectly competitive outcome. The assumption of homogeneous products (identical routes, no brand loyalty) is doing critical work here."

- question: "Which set of assumptions is most critical for the Bertrand paradox — two firms earning zero economic profit — to hold?"
  type: multiple-choice
  options:
    - "Firms have identical cost functions and operate in a regulated industry."
    - "Products are homogeneous (perfect substitutes), each firm has unlimited capacity, and competition is simultaneous and one-shot."
    - "The market has high barriers to entry and firms cannot observe each other's prices."
    - "Firms face downward-sloping demand curves and compete through advertising."
  answer: 1
  explanation: "All three assumptions are load-bearing. Homogeneous products mean consumers switch entirely to whichever firm charges less — even a penny cheaper captures the whole market. Unlimited capacity means undercutting is viable; if a firm cannot serve the whole market, undercutting is less attractive (this is the Edgeworth paradox). Simultaneous and one-shot competition removes the threat of future retaliation that could sustain above-cost pricing. Relax any one: differentiated products give firms pricing power; capacity constraints lead to Cournot-like outcomes; repeated interaction enables tacit collusion."

- question: "In Bertrand competition with homogeneous goods, a third firm entering a duopoly market drives prices even lower than marginal cost because the competitive pressure from three rivals exceeds what two can generate."
  type: true-false
  answer: false
  explanation: "With homogeneous products and unlimited capacity, the Bertrand equilibrium is already at marginal cost with just two firms. Adding more firms does not and cannot lower prices further below marginal cost — that would require selling at a loss. The 'Bertrand paradox' is precisely that you do not need many firms to reach the competitive outcome; two suffice. Additional firms may affect industry dynamics in other ways (e.g., increasing risk of mistakes, changing repeated-game incentives), but the one-shot equilibrium price cannot fall below marginal cost regardless of firm count."

- question: "Product differentiation allows Bertrand competitors to sustain prices above marginal cost at equilibrium, even in a one-shot game."
  type: true-false
  answer: true
  explanation: "With differentiated products, each firm faces a downward-sloping demand curve because consumers have heterogeneous preferences — some prefer Firm A's product even at a higher price. This means undercutting by a tiny amount does NOT capture the entire market (only the most price-sensitive consumers switch). Firms therefore have pricing power: the profit-maximizing price is above marginal cost, and the equilibrium markup depends on the degree of product substitutability. This is why branding, design, and service differentiation are so strategically important: they transform a commodity market (Bertrand → zero profit) into a differentiated one (positive markups)."

- question: "Explain the Bertrand paradox: what result does it produce, why is it 'paradoxical,' and which single assumption, if relaxed, is most important for understanding how real oligopolists sustain prices above marginal cost?"
  type: short-answer
  answer: "The Bertrand paradox is that two firms competing on price with homogeneous products and unlimited capacity reach the perfectly competitive outcome: price equals marginal cost and economic profit is zero. This is paradoxical because oligopoly is typically associated with market power and supranormal profits — yet two firms suffice to eliminate both entirely, which seems to contradict common intuition and empirical observation. The most important assumption to relax is product homogeneity. With differentiated products, each firm has captive consumers who prefer its product even at higher prices, giving the firm a downward-sloping demand curve and positive equilibrium markup. Almost all real oligopolies involve some degree of differentiation — through branding, location, quality tiers, or service — which is why they can sustain prices above cost."
  explanation: "The other assumptions (unlimited capacity, one-shot game) are also important but differentiation is the most empirically relevant. Most industries with a small number of firms compete on differentiation rather than pure price, which is why the Bertrand paradox, while theoretically illuminating, does not describe most actual markets."
```

## Explainer

From your study of oligopoly and strategic behavior, you know that firms in concentrated markets must consider rivals' actions when making decisions. In Cournot competition, firms choose quantities and the market determines the price. **Bertrand competition** flips the strategic variable: firms simultaneously choose prices, and consumers decide whom to buy from. This seemingly small change — competing on price rather than quantity — produces a dramatically different and initially startling result.

Consider the simplest case: two firms producing identical products with the same constant marginal cost *c*. Each firm posts a price, and consumers buy entirely from whichever firm charges less (splitting evenly if prices are equal). Now think about best responses. If Firm 1 charges any price above *c*, Firm 2 can undercut by a tiny amount, capture the entire market, and earn positive profit. But then Firm 1 would want to undercut Firm 2. This undercutting logic cascades until both firms charge exactly *c*. At that point, neither can profitably deviate — cutting price below cost means losses, and raising price means losing all customers. The result is the **Bertrand paradox**: just two firms are enough to reproduce the perfectly competitive outcome of price equals marginal cost and zero economic profit. This is paradoxical because we typically associate oligopoly with market power and supranormal profits, yet price competition between two identical firms eliminates both entirely.

The Bertrand paradox depends critically on three assumptions: products are **homogeneous** (perfect substitutes), firms have **unlimited capacity** (each can serve the entire market), and competition is **simultaneous and one-shot**. Relaxing any of these dissolves the paradox. If products are differentiated — as in most real markets — each firm faces a downward-sloping demand curve because some consumers prefer its version even at a higher price. With differentiation, equilibrium prices exceed marginal cost, and firms earn positive markups that depend on the degree of substitutability. This is why branding, product design, and marketing are so strategically important: they create the differentiation that sustains pricing power. If firms face capacity constraints, undercutting cannot capture the whole market, and the equilibrium resembles Cournot outcomes. And if the game is repeated, firms may sustain higher prices through tacit collusion — the threat of future price wars disciplines short-run temptations to undercut.

The contrast between Bertrand and Cournot highlights a deeper lesson about oligopoly theory: the choice of strategic variable matters enormously. When firms compete on quantity (Cournot), equilibrium prices lie between monopoly and competitive levels. When they compete on price (Bertrand) with homogeneous goods, the competitive outcome emerges immediately. Real markets often fall between these extremes, and determining which model better fits a given industry depends on whether firms primarily commit to production levels (as in manufacturing with long lead times) or primarily set prices (as in retail or services). Understanding both models gives you the theoretical brackets within which real oligopoly outcomes typically fall.
