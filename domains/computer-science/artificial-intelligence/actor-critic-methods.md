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

## Explainer

From your study of policy gradient methods, you know the fundamental idea: adjust policy parameters in the direction that increases expected return, using sampled trajectories to estimate the gradient. You also know the central problem — policy gradient estimates are noisy. The return from a single trajectory is a high-variance signal because it depends on every random action and state transition in the episode. Subtracting a baseline helps, but the question becomes: what is the best baseline? **Actor-critic methods** answer this by learning the baseline itself, creating a two-component architecture where each part does what it is best at.

The **actor** is the policy network — it maps states to action probabilities (or action distributions) and is updated via policy gradients, just as you learned before. The **critic** is a separate value function network that estimates how good a state (or state-action pair) is. Instead of waiting for the full episode return to update the actor, the critic provides an immediate estimate of future value using **temporal difference (TD) learning**: it bootstraps from its own predictions at the next state. The actor then uses the **advantage** — the difference between the actual reward-plus-estimated-future-value and the critic's current estimate — as its gradient signal. When the advantage is positive, the action was better than expected, so the policy shifts toward it; when negative, the policy shifts away.

This decomposition solves two problems simultaneously. The critic reduces variance because its value estimate is a learned function of the state, not a noisy sample of future rewards. The actor maintains the ability to learn stochastic policies and handle continuous action spaces, which pure value-based methods like Q-learning struggle with. The critic also enables **bootstrapping** — updating estimates based on other estimates rather than waiting for complete episodes — which dramatically improves sample efficiency. You can update the policy after every single step rather than waiting for an episode to finish, making actor-critic methods practical for environments with long or infinite horizons.

The **A3C (Asynchronous Advantage Actor-Critic)** algorithm extends this idea to parallel computation: multiple independent workers each interact with their own copy of the environment and asynchronously update shared actor and critic parameters. The asynchronous updates naturally decorrelate the training data (different workers see different states), removing the need for a replay buffer. Its synchronous variant, **A2C**, collects batches from all workers before a single update and is often preferred in practice for more stable training. These actor-critic foundations underpin most modern reinforcement learning systems, from robotics control to game-playing agents, because they combine the theoretical guarantees of policy gradients with the practical efficiency of value function learning.
