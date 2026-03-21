---
id: stackelberg-sequential-moves
title: Stackelberg Sequential Competition
domain: economics
course: advanced-microeconomics
prerequisites:
- id: cournot-quantity-competition
  type: soft
- id: bertrand-price-competition
  type: soft
tags:
- industrial-organization
- oligopoly
- sequential-games
stage: advanced
status: draft
---

# Stackelberg Sequential Competition

## Core Idea
Stackelberg competition models leader-follower move structure: a leader chooses quantity (or price) first, and the follower responds optimally. The leader gains a first-mover advantage by restricting supply (if quantity leader) or setting low price (if price leader) to commit to aggressive competition, inducing a less competitive follower response.

## Questions

```yaml
- question: "In a symmetric Cournot duopoly, each firm produces 30 units at equilibrium. If one firm becomes the Stackelberg leader, which outcome best describes the new equilibrium?"
  type: multiple-choice
  options:
    - "The leader reduces its output below 30 to avoid triggering aggressive retaliation from the follower"
    - "The leader increases its output above 30, and the follower — observing this commitment — reduces its output below 30; the leader earns higher profit than in Cournot"
    - "Both firms produce 30 units; the sequential structure changes the timing but not the quantities or profits"
    - "The leader increases output above 30 and the follower also increases output, resulting in higher industry total and higher profits for both"
  answer: 1
  explanation: "The Stackelberg leader uses backward induction: it knows the follower's best-response function and sets its own quantity to maximize profit given that the follower will respond optimally. This leads the leader to produce more than the Cournot quantity. The follower, seeing a large committed output, optimally produces less than the Cournot quantity. The leader earns higher profit than in Cournot because it exploits the follower's predictable reaction; the follower earns less. Industry output rises and price falls compared to Cournot."

- question: "Does the Stackelberg first-mover advantage that applies in quantity competition also apply in Bertrand price competition?"
  type: multiple-choice
  options:
    - "Yes — committing to a price first gives the leader time to build brand loyalty before the follower enters"
    - "Yes — the leader can set price just above marginal cost, forcing the follower into an unviable position"
    - "No — in Bertrand price competition, the follower can always undercut the leader's price, so moving first exposes the leader to being undercut rather than granting an advantage"
    - "No — Bertrand price games have no Nash equilibrium in sequential form, making first-mover advantage undefined"
  answer: 2
  explanation: "In Stackelberg quantity competition, quantities are strategic substitutes: if one firm produces more, the other's best response is to produce less. The leader exploits this by committing to a high quantity. In Bertrand price competition, prices are strategic complements: if one firm charges more, the other can profitably undercut and capture the market. A leader who sets a high price invites the follower to undercut. Moving first in price competition is a disadvantage, not an advantage. Whether first-mover timing helps or hurts depends critically on whether the strategic variable involves substitutes or complements."

- question: "The Stackelberg follower earns higher profit than in the simultaneous Cournot equilibrium because it observes the leader's quantity before choosing its own, giving it an informational advantage."
  type: true-false
  answer: false
  explanation: "The follower's informational advantage — observing the leader's committed output — actually hurts it. Seeing a large committed leader output, the follower's best response is to produce less, giving up market share. The follower earns less profit in Stackelberg than in Cournot equilibrium, not more. The leader gains at the follower's expense. The follower would prefer the simultaneous Cournot game where neither player can exploit the other's predictable reaction. Stackelberg transfers surplus from follower to leader through the commitment mechanism."

- question: "The Stackelberg leader commits to producing more than the Cournot quantity, and this commitment is credible because the leader's output choice is observable and irreversible before the follower acts."
  type: true-false
  answer: true
  explanation: "Credibility is the core of Stackelberg's strategic logic. If the leader merely announced its intended quantity without committing, the follower could ignore the announcement and both would revert to Cournot reasoning. The sequential structure means the leader's choice is actually made — and observable — before the follower decides. The follower has no strategic incentive to ignore it because it cannot change what has already happened. This irreversibility is what gives commitment value. In a simultaneous game, no such commitment is possible, so the advantage disappears."

- question: "Explain why a Stackelberg leader chooses to produce more than the Cournot quantity, and why this strategy works — that is, why doesn't the follower simply ignore the leader's output choice and produce the Cournot quantity anyway?"
  type: short-answer
  answer: "The leader uses backward induction: it first solves the follower's best-response function (which tells it exactly how the follower will react to any leader output), then substitutes that function into its own profit equation. This reveals that producing more than the Cournot quantity forces the follower's optimal response to a lower output, increasing the leader's profit. The strategy works because the leader's output is already committed and observable when the follower decides. The follower cannot profitably ignore it: its profit-maximizing choice given the leader's large output IS to produce less. Producing the Cournot quantity against a large leader output would leave the follower with lower profit than its true best response."
  explanation: "In Cournot, each firm guesses the other's output and plays a best response to that guess. In Stackelberg, the follower doesn't guess — it observes. Given leader output Q_L, the follower's profit-maximizing choice is its reaction function Q_F*(Q_L), which decreases in Q_L (strategic substitutes). The leader internalizes this relationship and picks Q_L to maximize its profit given that Q_F = Q_F*(Q_L). The result is a higher Q_L than in Cournot because the leader knows its extra output will cause more than an offsetting reduction in the follower's output, raising the leader's market share and profit."
```

## Explainer

In Cournot competition, both firms choose quantities simultaneously — neither knows what the other will do, so each plays a best response to its expectation of the rival's output. Stackelberg competition changes the timing: one firm moves first and the other observes that choice before responding. This sequential structure transforms the strategic logic. The leader does not simply pick the same quantity it would in Cournot; instead, it exploits the fact that the follower will react predictably to whatever quantity the leader commits to producing.

The key mechanism is **backward induction**. The leader reasons forward by first solving the follower's problem: "If I produce quantity Q_L, the follower will observe Q_L and choose its best response Q_F*(Q_L)." The follower's best-response function is the same reaction function from Cournot analysis — it maps any leader quantity to the follower's profit-maximizing reply. The leader then substitutes this reaction function into its own profit equation, effectively choosing its quantity knowing exactly how the follower will respond. This is what gives the leader its advantage: it optimizes over the follower's entire reaction function rather than guessing at a single point on it.

Consider a concrete example. Suppose two firms face a linear demand curve P = 100 − Q and both have marginal cost of 20. In the symmetric Cournot equilibrium, each firm produces about 26.67 units. In the Stackelberg game, the leader produces 40 units — substantially more — and the follower, seeing this large commitment, scales back to just 20 units. The leader earns higher profit than in Cournot; the follower earns less. Total industry output is higher (60 vs. 53.33), so the market price is lower and consumers benefit. The leader's aggression is credible precisely because it has already committed — the output is produced and cannot be taken back.

This illustrates a broader principle in sequential games: **commitment has strategic value**. In simultaneous games, firms cannot commit because moves are reversible up to the point of play. In sequential games, the first mover's choice is observable and irreversible, which constrains the rival's options. However, first-mover advantage is not automatic. It depends on the nature of competition. In Stackelberg quantity competition, the leader gains because producing more forces the follower to produce less (quantities are **strategic substitutes**). In Bertrand price competition, by contrast, the first mover to set a price can be undercut, so moving first may be a disadvantage. Whether sequential timing helps or hurts depends on whether the strategic variable involves substitutes or complements — a distinction that connects Stackelberg analysis to the deeper structure of oligopoly theory.
