---
id: stackelberg-competition
title: 'Stackelberg Competition: Sequential Quantity Leadership'
domain: economics
course: advanced-microeconomics
prerequisites:
- id: cournot-competition
  type: hard
- id: extensive-form-games-and-subgame-perfection
  type: hard
- id: game-theory-basics-microeconomics
  type: hard
- id: constrained-optimization
  type: hard
tags:
- industrial-organization
- sequential-games
stage: advanced
status: draft
---

# Stackelberg Competition: Sequential Quantity Leadership

## Core Idea
The leader chooses quantity first; the follower observes and responds optimally. Using backward induction, the leader anticipates the follower's response and optimizes, achieving higher profit than in simultaneous Cournot. The leader's commitment advantage comes from moving first and constraining the follower's profitable response. The follower is worse off than in Cournot competition.

## Explainer

In Cournot competition, two firms choose quantities simultaneously, each guessing what the other will produce. Stackelberg competition changes one thing: the firms move **sequentially** rather than simultaneously. One firm — the **leader** — commits to a quantity first, and the other firm — the **follower** — observes that choice before deciding its own output. This single change in timing transforms the strategic landscape, because the leader can exploit the follower's rationality.

The solution method is **backward induction**, which you know from extensive-form games. Start at the end: given any quantity the leader might choose, what is the follower's best response? The follower faces exactly the same optimization problem as in Cournot — maximize profit given the other firm's output — so the follower's **best response function** is identical to a Cournot reaction function. The key difference is that in Stackelberg, the leader *knows* the follower will play this best response. So rather than guessing, the leader substitutes the follower's reaction function directly into its own profit function and maximizes. This is constrained optimization with the follower's rationality built into the constraint.

The result is striking: the leader produces *more* than the Cournot quantity, and the follower produces *less*. Total industry output is higher than in Cournot, so the market price is lower. The leader earns higher profit than in the simultaneous game, while the follower earns less. This is the **first-mover advantage** — by committing to a large quantity before the follower can respond, the leader effectively forces the follower into a smaller, less profitable position. The follower would prefer to return to the simultaneous Cournot game, but it cannot credibly commit to ignoring the leader's choice.

Why can't the follower just ignore the leader and produce the Cournot quantity anyway? Because doing so would be irrational — given the leader's large output, the follower's Cournot quantity would flood the market and reduce the follower's own profit below what its best response yields. The leader's commitment is credible precisely because the output is already produced (or contracted). This illustrates a deep principle in sequential games: the ability to move first and commit is valuable only when the commitment is irreversible and the rival responds rationally. If the leader could secretly revise its quantity, or if the follower acted irrationally, the first-mover advantage would dissolve.
