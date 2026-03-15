---
id: policy-gradient-methods
title: Policy Gradient Methods
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: reinforcement-learning-intro
  type: hard
- id: gradient-descent-optimization
  type: hard
- id: derivatives-of-exponential-functions
  type: soft
- id: expected-value
  type: soft
tags:
- reinforcement-learning
- policy-optimization
- on-policy
stage: advanced
status: draft
---

# Policy Gradient Methods

## Core Idea
Policy gradient methods directly optimize the policy π(a|s) via gradient ascent on expected return. REINFORCE uses full episode returns; advantage actor-critic uses value baselines. Methods are on-policy but handle continuous actions naturally.
