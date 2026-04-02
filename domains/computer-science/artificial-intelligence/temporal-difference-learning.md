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
- id: actor-critic-methods
  type: soft
builds-toward:
- deep-q-networks
- q-learning
tags:
- reinforcement-learning
- value-based
- temporal-difference
- bootstrapping
stage: expert
status: validated
---
# Temporal Difference Learning

## Core Idea
Temporal difference learning updates value estimates using the difference between successive value predictions (TD error), enabling online learning without full episode returns. TD combines sample-based learning (Monte Carlo) and bootstrapping (dynamic programming); the TD(λ) framework generalizes TD(0) and Monte Carlo through an eligibility trace parameter λ.

## How It's Best Learned
Implement TD(0) and TD(1) on a simple domain and observe convergence differences; then implement TD(λ) with eligibility traces to understand the spectrum between TD(0) and Monte Carlo.

## Questions

```yaml
- question: "An agent in state s takes an action, receives reward r = -5, and transitions to state s'. The current value estimates are V(s) = 10 and V(s') = 8, with discount γ = 0.9 and learning rate α = 0.1. What is the TD(0) update to V(s)?"
  type: multiple-choice
  options:
    - "V(s) ← 10 + 0.1 × (−5 + 0.9 × 8 − 10) = 10 + 0.1 × (−7.8) = 9.22"
    - "V(s) ← 10 + 0.1 × (−5 − 10) = 8.5"
    - "V(s) ← −5 + 0.9 × 8 = 2.2"
    - "V(s) ← 10 − 0.1 × 8 = 9.2"
  answer: 0
  explanation: "The TD error is δ = r + γV(s') − V(s) = −5 + 0.9×8 − 10 = −5 + 7.2 − 10 = −7.8. The update is V(s) ← V(s) + α·δ = 10 + 0.1×(−7.8) = 9.22. The key insight is that δ measures the gap between what the agent expected (V(s) = 10) and what it now believes based on one step of observation (r + γV(s') = 2.2). The large negative TD error nudges the estimate downward, but only by α = 10% of the gap."

- question: "Compared to Monte Carlo methods, TD(0) has lower variance but higher bias in its value estimates. What is the source of this bias?"
  type: multiple-choice
  options:
    - "TD(0) uses a smaller learning rate, which causes estimates to converge to a slightly different value"
    - "TD(0) updates use V(s') — itself just an estimate — rather than a true observed return, so errors in V(s') propagate into the update for V(s)"
    - "TD(0) discounts future rewards with γ < 1, which systematically undervalues long-horizon states"
    - "TD(0) only updates the immediately visited state, missing contributions from earlier states in the trajectory"
  answer: 1
  explanation: "This is the bootstrapping bias. Monte Carlo methods use the actual observed return (unbiased, because it is a real sample of the true value) but have high variance (because the full return is noisy). TD(0) uses r + γV(s') as the update target, but V(s') is itself an estimate — possibly wrong. If V(s') is too high, the update for V(s) will be pulled too high as well. This error in the estimate propagates through the value function. The tradeoff is intentional: bootstrapping reduces variance (you only need one step of experience) at the cost of introducing this estimation bias."

- question: "TD learning can update value estimates after every single step, without waiting for an episode to complete."
  type: true-false
  answer: true
  explanation: "This is the defining advantage of TD methods over Monte Carlo. The TD update only requires the immediate reward and the estimated value of the next state — both available after a single step. Monte Carlo methods must wait until the episode ends to observe the true return. For continuing tasks (no natural episode end) or long episodes, this online learning capability makes TD methods far more practical. The cost is bootstrapping bias, but the benefit is immediate learning from every transition."

- question: "TD(λ) with λ = 1 is equivalent to TD(0) because eligibility traces decay to zero after one step when λ = 1."
  type: true-false
  answer: false
  explanation: "This reverses the relationship. TD(λ) with λ = 0 gives TD(0) — updates use only the immediately next state's value, with no trace memory. TD(λ) with λ = 1 gives Monte Carlo — eligibility traces decay by λ = 1 per step (no decay), so all previously visited states receive full credit, equivalent to using the complete episode return. The λ parameter interpolates between TD(0) (λ=0, most bootstrapping, lowest variance, highest bias) and Monte Carlo (λ=1, no bootstrapping, zero bias, highest variance)."

- question: "What is bootstrapping in the context of TD learning, and why does it allow TD methods to learn online while also introducing bias?"
  type: short-answer
  answer: "Bootstrapping means updating one value estimate using another value estimate rather than using a true observed outcome. In TD learning, V(s) is updated using r + γV(s') as the target, where V(s') is itself an estimate of the state value — not a real return from completing the episode. Because V(s') is immediately available after one step (unlike the true return, which requires the episode to finish), bootstrapping enables online updates after every transition. The bias arises because V(s') may be inaccurate; if the value function is poorly estimated early in training, these errors propagate into updates for V(s). As training progresses and V(s') improves, the bias decreases."
  explanation: "The analogy is to self-referential learning: you are updating your belief using your own beliefs as evidence, rather than waiting for external ground truth. This is efficient but initially unreliable. Monte Carlo avoids bootstrapping by always waiting for real ground truth (the full return), getting unbiased but high-variance estimates. Most practical RL algorithms — Q-learning, SARSA, DQN — use TD bootstrapping because online learning and sample efficiency outweigh the manageable bias."
```

## Explainer

From reinforcement learning, you know the central problem: an agent in a Markov decision process must estimate how valuable each state is (the value function) in order to act well. Two classic approaches exist. **Monte Carlo** methods wait until an episode finishes, then use the actual total return to update value estimates — accurate but slow, since you learn nothing until the end. **Dynamic programming** uses the Bellman equation to update values based on the estimated values of successor states — fast but requires a complete model of the environment's transition probabilities. **Temporal difference learning** combines the best of both: it learns from raw experience (no model needed, like Monte Carlo) but updates after every single step (no waiting for episode end, like dynamic programming).

The core mechanism is the **TD error**, defined as δ = r + γV(s') − V(s), where r is the reward received, γ is the discount factor, s' is the next state, and V(s) is the current estimate. Think of it as a prediction error: V(s) is what you expected to get from state s, and r + γV(s') is a better estimate now that you have actually observed the immediate reward and the next state. The update rule V(s) ← V(s) + α·δ simply nudges your old estimate toward this new, partially-observed reality. This is called **bootstrapping** because you are updating one estimate using another estimate — V(s') is itself just a guess — rather than waiting for the true outcome.

The simplest version, **TD(0)**, updates the value of each state using only the immediate next state's estimated value. At the other extreme, **TD(1)** is equivalent to Monte Carlo — it effectively waits for the full return before updating. The framework **TD(λ)** interpolates between these extremes using a parameter λ ∈ [0,1]. When λ = 0, you get TD(0); when λ = 1, you get Monte Carlo. Intermediate values of λ use **eligibility traces**, which keep a decaying memory of recently visited states. When a TD error occurs, it propagates backward to update not just the current state but all recently visited states, with the update strength decaying by λ at each step backward. States visited many steps ago get small updates; states visited just before the error get large ones.

Why does this matter in practice? TD methods converge faster than Monte Carlo on many problems because they do not waste information — each transition teaches the agent something immediately, rather than requiring a complete trajectory. The bootstrapping also reduces variance at the cost of some bias (since V(s') may be wrong). This bias-variance tradeoff, controlled by λ, is the central design choice. TD(0) has the lowest variance but highest bias; Monte Carlo has zero bias but high variance. Most practical algorithms — including Q-learning, SARSA, and the deep Q-networks you will study next — are built on the TD framework, making temporal difference learning the backbone of modern reinforcement learning.
