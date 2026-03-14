---
id: actor-critic-methods
title: Actor-Critic Methods
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: policy-gradient-methods
  type: hard
tags:
- reinforcement-learning
- policy-optimization
- temporal-difference
stage: advanced
status: draft
---

# Actor-Critic Methods

## Core Idea
Actor-critic combines policy gradient (actor) with value function (critic). Actor updates via policy gradients; critic provides TD targets reducing variance. Critic uses bootstrapping for sample efficiency. A3C extends to parallel workers.
