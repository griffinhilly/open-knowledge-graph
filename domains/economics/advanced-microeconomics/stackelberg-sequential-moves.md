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

## Explainer

In Cournot competition, both firms choose quantities simultaneously — neither knows what the other will do, so each plays a best response to its expectation of the rival's output. Stackelberg competition changes the timing: one firm moves first and the other observes that choice before responding. This sequential structure transforms the strategic logic. The leader does not simply pick the same quantity it would in Cournot; instead, it exploits the fact that the follower will react predictably to whatever quantity the leader commits to producing.

The key mechanism is **backward induction**. The leader reasons forward by first solving the follower's problem: "If I produce quantity Q_L, the follower will observe Q_L and choose its best response Q_F*(Q_L)." The follower's best-response function is the same reaction function from Cournot analysis — it maps any leader quantity to the follower's profit-maximizing reply. The leader then substitutes this reaction function into its own profit equation, effectively choosing its quantity knowing exactly how the follower will respond. This is what gives the leader its advantage: it optimizes over the follower's entire reaction function rather than guessing at a single point on it.

Consider a concrete example. Suppose two firms face a linear demand curve P = 100 − Q and both have marginal cost of 20. In the symmetric Cournot equilibrium, each firm produces about 26.67 units. In the Stackelberg game, the leader produces 40 units — substantially more — and the follower, seeing this large commitment, scales back to just 20 units. The leader earns higher profit than in Cournot; the follower earns less. Total industry output is higher (60 vs. 53.33), so the market price is lower and consumers benefit. The leader's aggression is credible precisely because it has already committed — the output is produced and cannot be taken back.

This illustrates a broader principle in sequential games: **commitment has strategic value**. In simultaneous games, firms cannot commit because moves are reversible up to the point of play. In sequential games, the first mover's choice is observable and irreversible, which constrains the rival's options. However, first-mover advantage is not automatic. It depends on the nature of competition. In Stackelberg quantity competition, the leader gains because producing more forces the follower to produce less (quantities are **strategic substitutes**). In Bertrand price competition, by contrast, the first mover to set a price can be undercut, so moving first may be a disadvantage. Whether sequential timing helps or hurts depends on whether the strategic variable involves substitutes or complements — a distinction that connects Stackelberg analysis to the deeper structure of oligopoly theory.
