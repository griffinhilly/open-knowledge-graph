---
id: q-learning
title: Q-Learning Algorithm
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: markov-decision-processes
  type: hard
- id: dynamic-programming-intro
  type: hard
tags:
- reinforcement-learning
- temporal-difference
- off-policy
stage: advanced
status: draft
---

# Q-Learning Algorithm

## Core Idea
Q-Learning learns optimal action values Q(s,a) via temporal difference updates: Q(s,a) ← Q(s,a) + α[r + γ max_a' Q(s',a') - Q(s,a)]. It is off-policy, learning from explorative actions, and guarantees convergence with appropriate learning rates.

## How It's Best Learned
Implement Q-Learning for grid-world navigation, visualizing Q-value convergence and comparing policies.

## Common Misconceptions
Q-Learning requires exploration; pure greedy policies converge to suboptimal solutions. Large state/action spaces demand function approximation introducing error.
