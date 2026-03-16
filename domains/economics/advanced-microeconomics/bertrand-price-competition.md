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
stage: advanced
status: draft
---

# Bertrand Price Competition

## Core Idea
Bertrand competition models firms simultaneously choosing prices, with demand allocating to the lowest-priced firm. The Bertrand paradox arises: with homogeneous products and identical costs, even two firms produce the competitive outcome (price equals marginal cost, zero profit). This contrasts sharply with Cournot, illustrating the sensitivity of oligopoly results to competition mode.

## Explainer

From your study of oligopoly and game theory, you know that a small number of firms interact strategically — each firm's optimal choice depends on what rivals do. In Cournot competition, firms choose quantities. **Bertrand competition** flips the strategic variable: firms simultaneously choose prices, and consumers buy from whichever firm charges less. This seemingly minor modeling choice produces dramatically different results, which is precisely why the Bertrand model is important — it reveals how sensitive oligopoly outcomes are to the nature of competition.

The logic behind the **Bertrand paradox** is elegant. Suppose two firms sell identical products with the same constant marginal cost c. If firm A charges any price above c, firm B can capture the entire market by undercutting slightly. But firm A reasons the same way about firm B. This undercutting logic cascades until both firms price at marginal cost — the perfectly competitive outcome — even though there are only two firms. Neither firm can profitably deviate: pricing below c means losses, and pricing above c means losing all customers. This is a Nash equilibrium, applying the concept you already know: each firm's price is a best response to the other's.

The paradox is striking because it contradicts the intuition that fewer firms means more market power. With Cournot competition among the same two firms, both earn positive profits. The difference arises because price competition with homogeneous goods is inherently more aggressive than quantity competition — a tiny price cut steals the entire market, whereas a small quantity increase only modestly affects the market price. This sensitivity to the competition mode is one of the most important lessons in industrial organization: the structure of strategic interaction matters as much as the number of competitors.

The Bertrand paradox motivates several important extensions that restore positive profits. **Product differentiation** breaks the paradox because a small price cut no longer captures the entire market — some consumers prefer the rival's variant. **Capacity constraints** also matter: if firms cannot serve the entire market at marginal cost, undercutting is less profitable. **Asymmetric costs** give the lower-cost firm positive profit since it can price just below its rival's cost. Each extension reveals which real-world features prevent the extreme competitive outcome the basic Bertrand model predicts, and understanding the paradox is essential for evaluating which modeling assumptions are appropriate for any given industry.
