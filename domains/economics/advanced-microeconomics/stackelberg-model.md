---
id: stackelberg-model
title: Stackelberg Competition
domain: economics
course: advanced-microeconomics
prerequisites:
- id: subgame-perfect-equilibrium
  type: hard
- id: cournot-competition
  type: soft
- id: optimization-multivariable-basics
  type: hard
- id: backward-induction
  type: soft
tags:
- industrial-organization
- sequential-games
- first-mover-advantage
stage: abstract-reasoning
status: draft
---

# Stackelberg Competition

## Core Idea
Stackelberg competition is sequential quantity competition: a leader firm moves first choosing quantity, then a follower observes and chooses. Using backward induction, the follower's best response is found, then the leader maximizes by anticipating this response. The leader enjoys a first-mover advantage: higher profit than in Cournot, where firms move simultaneously.

## Explainer

In Cournot competition, both firms choose quantities simultaneously — neither knows the other's decision when acting. Stackelberg competition changes one thing: the **leader** moves first, and the **follower** observes the leader's quantity before responding. This sequential structure transforms the strategic problem fundamentally, because the leader can now commit to a quantity and force the follower to react to it.

The solution method is **backward induction**, which you already know from sequential games. Start at the end: given any quantity the leader might choose, what is the follower's best response? The follower faces a standard profit-maximization problem — it observes the leader's output, treats it as fixed, and picks the quantity that maximizes its own profit. This gives a **best-response function** mapping every possible leader quantity to the follower's optimal reply, exactly as in Cournot. The difference is what happens next: instead of finding where two best-response functions intersect, the leader substitutes the follower's best-response function directly into its own profit function and maximizes over its own quantity. The leader effectively chooses a point on the follower's best-response curve — the point that maximizes the leader's profit.

The result is the **first-mover advantage**: the leader produces more and earns higher profit than either firm would in the symmetric Cournot equilibrium, while the follower produces less and earns lower profit. The intuition is that commitment has strategic value. By credibly committing to a large quantity (because the choice is observable and irreversible), the leader forces the follower into a smaller, less profitable position. Total industry output is higher than in Cournot and price is lower, so consumers benefit from sequential competition. The Stackelberg outcome is also the subgame-perfect equilibrium of this game — the follower's strategy is optimal at every subgame, not just on the equilibrium path.

A concrete example helps: suppose two firms face inverse demand P = 100 − Q with zero marginal cost. In Cournot, each produces 33.3 units for profit of about 1,111. In Stackelberg, the leader produces 50 units, the follower best-responds with 25, price falls to 25, leader profit is 1,250 and follower profit is 625. The leader gains at the follower's expense — and at the expense of the Cournot outcome — purely because of the sequential structure. This illustrates a broader principle in game theory: the ability to move first and commit can be worth more than flexibility, provided the commitment is credible.
