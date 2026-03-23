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
stage: expert
status: validated
---

# Stackelberg Competition

## Core Idea
Stackelberg competition is sequential quantity competition: a leader firm moves first choosing quantity, then a follower observes and chooses. Using backward induction, the follower's best response is found, then the leader maximizes by anticipating this response. The leader enjoys a first-mover advantage: higher profit than in Cournot, where firms move simultaneously.

## Questions

```yaml
- question: "In Stackelberg competition with P = 100 − Q and zero costs, the leader produces 50 units. The follower's best response is 25 units. Why doesn't the follower also produce 50 to maximize total market output?"
  type: multiple-choice
  options:
    - "The follower lacks the information to observe that 50 is the optimal quantity"
    - "Given 50 units already in the market, producing 25 maximizes the follower's individual profit — adding more would lower price enough to reduce the follower's own revenue"
    - "A government regulation prevents the follower from matching the leader's output"
    - "The follower is constrained to produce at most half the leader's quantity by the Stackelberg structure"
  answer: 1
  explanation: "The follower is a rational profit-maximizer who takes the leader's output as given. With Q_L = 50 already committed, the follower's profit π_F = (100 − 50 − Q_F)Q_F = (50 − Q_F)Q_F. Maximizing: 50 − 2Q_F = 0, so Q_F = 25. Producing 50 would push total output to 100, price to 0, and the follower earns nothing. The follower doesn't want maximum total output — it wants maximum own profit given the leader's irreversible commitment."

- question: "The Stackelberg leader produces more than in the symmetric Cournot equilibrium and earns higher profit. What is the core mechanism that creates this first-mover advantage?"
  type: multiple-choice
  options:
    - "The leader has lower marginal costs due to economies of scale from producing first"
    - "The leader has private information about market demand that the follower lacks"
    - "The leader commits to a quantity the follower must observe and react to, allowing the leader to choose the profit-maximizing point on the follower's best-response curve"
    - "The leader can revise its quantity after seeing the follower's response, optimizing in both rounds"
  answer: 2
  explanation: "The advantage is commitment, not information or cost. By choosing first and making the choice observable, the leader credibly commits to a quantity. The follower's best-response function is now a constraint rather than a simultaneous reaction — the leader exploits it by plugging it into its own profit function and maximizing. This is backward induction. Option D reverses the logic: the leader CANNOT change its quantity; the irreversibility of commitment is what makes the strategy credible and valuable."

- question: "In Stackelberg competition, the first mover benefits primarily because it gains superior information about market demand before the follower must decide."
  type: true-false
  answer: false
  explanation: "The first-mover advantage has nothing to do with information about demand — both firms know the demand function in the standard Stackelberg model. The advantage comes from commitment: by moving first and having the choice observed by the follower, the leader can credibly 'lock in' a large quantity. The follower's rational best response to a large committed quantity is to produce less, which is exactly what the leader wants. In fact, first-mover advantage can be harmful in other game structures (e.g., price competition under Bertrand conditions) — it is not a universal benefit."

- question: "In Stackelberg competition, the leader produces more than in the symmetric Cournot outcome, total industry output is higher, and consumers face a lower equilibrium price than under Cournot."
  type: true-false
  answer: true
  explanation: "Using P = 100 − Q, zero costs: Cournot gives each firm 33.3 units (total Q = 66.7, P ≈ 33.3). Stackelberg gives leader 50, follower 25 (total Q = 75, P = 25). Total output is higher and price is lower in Stackelberg. The leader gains at the follower's expense — leader earns 1,250 vs. 1,111 in Cournot; follower earns 625 vs. 1,111. So consumers benefit from the sequential structure at the follower's expense."

- question: "What is the key strategic mechanism behind the Stackelberg first-mover advantage? Why would the leader want to commit to a larger quantity than the Cournot equilibrium amount?"
  type: short-answer
  answer: "The mechanism is strategic commitment. In Cournot, each firm best-responds to the other's quantity simultaneously, landing at a symmetric equilibrium where neither can gain by deviating alone. In Stackelberg, the leader's quantity is observable and irreversible before the follower acts. By committing to a quantity larger than the Cournot level, the leader exploits the follower's rational best-response function: a larger leader output forces the follower to reduce output (best-response functions in quantity competition are downward sloping — higher rival output means lower own output is optimal). The leader effectively moves the follower to a less profitable position. The leader chooses the point on the follower's best-response curve that maximizes leader profit, trading a lower market price for the strategic gain of reducing follower output by more."
  explanation: "The insight is that in quantity competition, being aggressive (high quantity) is strategically dominant if committed first, because it forces the rival to back down. This would not work in simultaneous play — both firms would react to each other and the aggressive stance would not be credible without commitment."
```

## Explainer

In Cournot competition, both firms choose quantities simultaneously — neither knows the other's decision when acting. Stackelberg competition changes one thing: the **leader** moves first, and the **follower** observes the leader's quantity before responding. This sequential structure transforms the strategic problem fundamentally, because the leader can now commit to a quantity and force the follower to react to it.

The solution method is **backward induction**, which you already know from sequential games. Start at the end: given any quantity the leader might choose, what is the follower's best response? The follower faces a standard profit-maximization problem — it observes the leader's output, treats it as fixed, and picks the quantity that maximizes its own profit. This gives a **best-response function** mapping every possible leader quantity to the follower's optimal reply, exactly as in Cournot. The difference is what happens next: instead of finding where two best-response functions intersect, the leader substitutes the follower's best-response function directly into its own profit function and maximizes over its own quantity. The leader effectively chooses a point on the follower's best-response curve — the point that maximizes the leader's profit.

The result is the **first-mover advantage**: the leader produces more and earns higher profit than either firm would in the symmetric Cournot equilibrium, while the follower produces less and earns lower profit. The intuition is that commitment has strategic value. By credibly committing to a large quantity (because the choice is observable and irreversible), the leader forces the follower into a smaller, less profitable position. Total industry output is higher than in Cournot and price is lower, so consumers benefit from sequential competition. The Stackelberg outcome is also the subgame-perfect equilibrium of this game — the follower's strategy is optimal at every subgame, not just on the equilibrium path.

A concrete example helps: suppose two firms face inverse demand P = 100 − Q with zero marginal cost. In Cournot, each produces 33.3 units for profit of about 1,111. In Stackelberg, the leader produces 50 units, the follower best-responds with 25, price falls to 25, leader profit is 1,250 and follower profit is 625. The leader gains at the follower's expense — and at the expense of the Cournot outcome — purely because of the sequential structure. This illustrates a broader principle in game theory: the ability to move first and commit can be worth more than flexibility, provided the commitment is credible.
