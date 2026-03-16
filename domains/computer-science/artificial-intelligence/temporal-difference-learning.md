---
id: temporal-difference-learning
title: Temporal Difference Learning
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: reinforcement-learning-intro
  type: hard
- id: markov-decision-processes
  type: hard
- id: markov-chains
  type: hard
- id: expected-value
  type: soft
builds-toward:
- deep-q-networks
- q-learning
tags:
- reinforcement-learning
- value-based
- temporal-difference
- bootstrapping
stage: advanced
status: draft
---

# Temporal Difference Learning

## Core Idea
Temporal difference learning updates value estimates using the difference between successive value predictions (TD error), enabling online learning without full episode returns. TD combines sample-based learning (Monte Carlo) and bootstrapping (dynamic programming); the TD(λ) framework generalizes TD(0) and Monte Carlo through an eligibility trace parameter λ.

## How It's Best Learned
Implement TD(0) and TD(1) on a simple domain and observe convergence differences; then implement TD(λ) with eligibility traces to understand the spectrum between TD(0) and Monte Carlo.

## Explainer

From reinforcement learning, you know the central problem: an agent in a Markov decision process must estimate how valuable each state is (the value function) in order to act well. Two classic approaches exist. **Monte Carlo** methods wait until an episode finishes, then use the actual total return to update value estimates — accurate but slow, since you learn nothing until the end. **Dynamic programming** uses the Bellman equation to update values based on the estimated values of successor states — fast but requires a complete model of the environment's transition probabilities. **Temporal difference learning** combines the best of both: it learns from raw experience (no model needed, like Monte Carlo) but updates after every single step (no waiting for episode end, like dynamic programming).

The core mechanism is the **TD error**, defined as δ = r + γV(s') − V(s), where r is the reward received, γ is the discount factor, s' is the next state, and V(s) is the current estimate. Think of it as a prediction error: V(s) is what you expected to get from state s, and r + γV(s') is a better estimate now that you have actually observed the immediate reward and the next state. The update rule V(s) ← V(s) + α·δ simply nudges your old estimate toward this new, partially-observed reality. This is called **bootstrapping** because you are updating one estimate using another estimate — V(s') is itself just a guess — rather than waiting for the true outcome.

The simplest version, **TD(0)**, updates the value of each state using only the immediate next state's estimated value. At the other extreme, **TD(1)** is equivalent to Monte Carlo — it effectively waits for the full return before updating. The framework **TD(λ)** interpolates between these extremes using a parameter λ ∈ [0,1]. When λ = 0, you get TD(0); when λ = 1, you get Monte Carlo. Intermediate values of λ use **eligibility traces**, which keep a decaying memory of recently visited states. When a TD error occurs, it propagates backward to update not just the current state but all recently visited states, with the update strength decaying by λ at each step backward. States visited many steps ago get small updates; states visited just before the error get large ones.

Why does this matter in practice? TD methods converge faster than Monte Carlo on many problems because they do not waste information — each transition teaches the agent something immediately, rather than requiring a complete trajectory. The bootstrapping also reduces variance at the cost of some bias (since V(s') may be wrong). This bias-variance tradeoff, controlled by λ, is the central design choice. TD(0) has the lowest variance but highest bias; Monte Carlo has zero bias but high variance. Most practical algorithms — including Q-learning, SARSA, and the deep Q-networks you will study next — are built on the TD framework, making temporal difference learning the backbone of modern reinforcement learning.
