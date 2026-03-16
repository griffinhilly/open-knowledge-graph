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

## Explainer

From your work on policy gradient methods, you know the core idea: adjust the policy parameters so that actions leading to higher returns become more probable. From neural networks, you know how to build flexible function approximators that map inputs to outputs through layers of learned transformations. A **policy network** combines these two ideas — it is a neural network that takes a state as input and outputs a probability distribution over actions, directly representing the policy π(a|s; θ) where θ are the network weights.

The simplest policy gradient algorithm is **REINFORCE**. After the agent completes an episode, REINFORCE computes the return (cumulative discounted reward) for each time step, then updates the network weights to make actions with higher returns more likely. The gradient has an intuitive form: ∇θ log π(aₜ|sₜ; θ) × Gₜ. The log-probability gradient points in the direction that would increase the probability of action aₜ, and the return Gₜ scales how far you step in that direction. Good actions get reinforced; bad actions get suppressed. Because the network outputs a full probability distribution — perhaps a softmax over discrete actions or the parameters of a Gaussian for continuous actions — this approach naturally handles stochastic policies and continuous action spaces that value-based methods struggle with.

The central challenge with REINFORCE is **high variance**. Returns from individual episodes fluctuate wildly — a lucky rollout might give a high return to a mediocre action, and an unlucky one might penalize a good action. This noise makes learning slow and unstable. The standard fix is to subtract a **baseline** from the return: instead of scaling the gradient by Gₜ, you scale by Gₜ − b(sₜ), where b is an estimate of the expected return from state sₜ. This does not change the expected gradient (the math works out to be unbiased) but dramatically reduces variance. The quantity Gₜ − b(sₜ) is called the **advantage** — it tells you whether this action was better or worse than average for this state, which is a much cleaner learning signal than the raw return.

In practice, the baseline is often a separate neural network — a value network V(s; φ) — trained alongside the policy network. This leads naturally to actor-critic architectures, where the "actor" (policy network) decides what to do and the "critic" (value network) evaluates how good the decision was. Policy networks have proven essential for complex control tasks — robotic locomotion, game playing, and any domain where the action space is continuous or the optimal behavior is inherently stochastic. Their ability to directly optimize the quantity you care about (expected return) without needing to enumerate all possible actions makes them a cornerstone of modern reinforcement learning.
