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
- id: partial-derivatives
  type: hard
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

## Explainer

Most reinforcement learning methods you have seen so far work by estimating value functions — figuring out how good each state or action is, then deriving a policy indirectly by picking the highest-value action. Policy gradient methods take a fundamentally different approach: they **parameterize the policy directly** as a function π_θ(a|s) and optimize its parameters θ to maximize expected return. Instead of asking "what is the value of this action?" and choosing the best one, they ask "how should I adjust the probability of each action to get more reward?"

This direct approach solves a problem that value-based methods struggle with: **continuous action spaces**. If your agent controls a robotic arm with joint torques that can take any real-valued number, you cannot enumerate all possible actions to find the one with the highest Q-value. But a parameterized policy can output a probability distribution over continuous actions — for instance, a Gaussian with a learned mean and variance — and gradient ascent smoothly adjusts these parameters. Your background in gradient descent and partial derivatives applies directly here, except you are ascending (maximizing) the expected return J(θ) rather than descending a loss.

The key theoretical result is the **policy gradient theorem**, which gives a tractable expression for ∇_θ J(θ). The simplest algorithm built on it is **REINFORCE**: run a full episode under the current policy, compute the return G_t from each time step, and update θ in the direction of ∇_θ log π_θ(a_t|s_t) · G_t. Intuitively, this increases the probability of actions that led to high returns and decreases the probability of actions that led to low returns. The log-probability gradient tells you which direction in parameter space makes the chosen action more likely; the return G_t scales how strongly you push. REINFORCE is simple and unbiased, but it suffers from high variance because G_t depends on everything that happens after time t.

The standard remedy is to subtract a **baseline** from the return — typically a learned value function V(s_t). The quantity A_t = G_t − V(s_t) is called the **advantage**: it measures how much better the actual return was compared to the expected return from that state. If an action achieves average performance, its advantage is near zero and the policy barely changes. Only actions that perform surprisingly well or surprisingly poorly produce large updates. This is the **actor-critic** architecture: the "actor" is the policy π_θ, and the "critic" is the value function V that provides the baseline. The critic reduces variance without introducing bias (since subtracting a state-dependent baseline does not change the expected gradient), making learning significantly more stable and sample-efficient than raw REINFORCE.
