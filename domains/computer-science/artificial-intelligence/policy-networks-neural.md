---
id: policy-networks-neural
title: Policy Networks and Policy Gradients
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: policy-gradient-methods
  type: hard
- id: neural-networks-intro
  type: hard
builds-toward:
- actor-critic-methods
tags:
- reinforcement-learning
- policy-based
- actor-methods
- policy-gradient
stage: advanced
status: draft
---

# Policy Networks and Policy Gradients

## Core Idea
Policy networks directly parameterize the policy π(a|s) using a neural network, enabling learning for continuous action spaces and stochastic policies. Policy gradient algorithms estimate policy parameter gradients using trajectory samples; the REINFORCE algorithm uses returns, while more sophisticated methods reduce variance through baselines and advantage functions.

## How It's Best Learned
Implement REINFORCE and train a policy network on a continuous control task, then add a baseline to reduce variance and observe faster convergence.
