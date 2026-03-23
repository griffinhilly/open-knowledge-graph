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
stage: expert
status: validated
---

# Stackelberg Competition: Sequential Quantity Leadership

## Core Idea
The leader chooses quantity first; the follower observes and responds optimally. Using backward induction, the leader anticipates the follower's response and optimizes, achieving higher profit than in simultaneous Cournot. The leader's commitment advantage comes from moving first and constraining the follower's profitable response. The follower is worse off than in Cournot competition.

## Questions

```yaml
- question: "In a Stackelberg duopoly, Firm A (the leader) commits to a large output quantity. Firm B (the follower) observes this and plays its best response. Compared to the Cournot simultaneous-game outcome, which result is expected?"
  type: multiple-choice
  options:
    - "Firm A produces less and earns more; Firm B produces more and earns less"
    - "Firm A produces more and earns more; Firm B produces less and earns less"
    - "Both firms produce more than Cournot, and both earn higher profits due to higher total output"
    - "Both firms produce the same quantities as in Cournot, but at a lower equilibrium price"
  answer: 1
  explanation: "The leader commits to a quantity larger than the Cournot level. Faced with this, the follower's best response is to produce less than it would in Cournot (since the market is already being flooded by the leader). Total output rises, price falls, but the leader captures enough of the market to earn higher profit than in Cournot, while the follower is left with a smaller share and earns less. The follower would prefer the simultaneous Cournot game but cannot credibly commit to ignoring the leader's choice."

- question: "The Stackelberg leader uses backward induction by doing which of the following?"
  type: multiple-choice
  options:
    - "Choosing the output level that maximizes joint industry profit and announcing it to the follower"
    - "Guessing the follower's likely output and best-responding as in Cournot, but moving first"
    - "Substituting the follower's best-response function into its own profit function, then maximizing"
    - "Setting price rather than quantity, which forces the follower to take the residual market"
  answer: 2
  explanation: "The leader does not guess — it knows the follower is rational and will play its best response. So the leader substitutes the follower's reaction function (which is the same as in Cournot) directly into its own profit expression. This converts the problem into an unconstrained single-variable optimization. The result is a quantity larger than the Cournot level, which then forces the follower into a smaller response. This is the essence of backward induction: start from the end of the game tree, work backward, and optimize at each node."

- question: "In Stackelberg competition, total industry output is higher and the market price is lower than in the equivalent Cournot duopoly."
  type: true-false
  answer: true
  explanation: "The leader produces more than its Cournot quantity, and even though the follower produces less than its Cournot quantity, the net effect is that total output increases. A higher total quantity on a downward-sloping demand curve means a lower market price. This is why the follower is worse off: lower price combined with lower output yields strictly lower profit than the Cournot benchmark."

- question: "The Stackelberg leader gains its first-mover advantage primarily because it is more efficient or has lower production costs than the follower."
  type: true-false
  answer: false
  explanation: "The first-mover advantage in Stackelberg competition has nothing to do with efficiency or cost differences. It comes entirely from the sequential structure of the game: the leader's commitment is observable and irreversible, forcing the follower to treat the leader's quantity as given. If both firms were identical in costs, the leader still gains by exploiting the follower's rationality through commitment. This is why sequential timing — not competitive advantage — is the defining feature of the model."

- question: "Why does moving first give the Stackelberg leader an advantage, and what would happen to that advantage if the leader could secretly revise its quantity after observing the follower's decision?"
  type: short-answer
  answer: "Moving first confers an advantage only when the commitment is credible and irreversible — once the leader has produced (or contracted) a large quantity, the follower must accept that as a fixed constraint and choose its best response given that output. The leader exploits the follower's rationality: by committing to a large quantity, it forces the follower to scale back, capturing more market share. If the leader could secretly revise its quantity after the follower decided, the commitment would not be credible — the follower would anticipate the revision and the game would collapse to the simultaneous Cournot outcome, eliminating the first-mover advantage."
  explanation: "This is the core insight about sequential games: commitment value requires irreversibility. An action that can be undone provides no strategic leverage. The Stackelberg result rests on the assumption that the leader's output choice is observable and binding before the follower chooses. This is also why the model applies to real-world settings like capacity investment (hard to reverse) but not to settings where rivals can respond before production decisions are finalized."
```

## Explainer

In Cournot competition, two firms choose quantities simultaneously, each guessing what the other will produce. Stackelberg competition changes one thing: the firms move **sequentially** rather than simultaneously. One firm — the **leader** — commits to a quantity first, and the other firm — the **follower** — observes that choice before deciding its own output. This single change in timing transforms the strategic landscape, because the leader can exploit the follower's rationality.

The solution method is **backward induction**, which you know from extensive-form games. Start at the end: given any quantity the leader might choose, what is the follower's best response? The follower faces exactly the same optimization problem as in Cournot — maximize profit given the other firm's output — so the follower's **best response function** is identical to a Cournot reaction function. The key difference is that in Stackelberg, the leader *knows* the follower will play this best response. So rather than guessing, the leader substitutes the follower's reaction function directly into its own profit function and maximizes. This is constrained optimization with the follower's rationality built into the constraint.

The result is striking: the leader produces *more* than the Cournot quantity, and the follower produces *less*. Total industry output is higher than in Cournot, so the market price is lower. The leader earns higher profit than in the simultaneous game, while the follower earns less. This is the **first-mover advantage** — by committing to a large quantity before the follower can respond, the leader effectively forces the follower into a smaller, less profitable position. The follower would prefer to return to the simultaneous Cournot game, but it cannot credibly commit to ignoring the leader's choice.

Why can't the follower just ignore the leader and produce the Cournot quantity anyway? Because doing so would be irrational — given the leader's large output, the follower's Cournot quantity would flood the market and reduce the follower's own profit below what its best response yields. The leader's commitment is credible precisely because the output is already produced (or contracted). This illustrates a deep principle in sequential games: the ability to move first and commit is valuable only when the commitment is irreversible and the rival responds rationally. If the leader could secretly revise its quantity, or if the follower acted irrationally, the first-mover advantage would dissolve.
