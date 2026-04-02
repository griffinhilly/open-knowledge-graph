---
id: model-based-reinforcement-learning
title: Model-Based Reinforcement Learning
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: reinforcement-learning-intro
  type: hard
- id: markov-decision-processes
  type: hard
builds-toward:
- monte-carlo-tree-search
tags:
- reinforcement-learning
- planning
- model-learning
- world-models
stage: expert
status: validated
---

# Model-Based Reinforcement Learning

## Core Idea
Model-based RL learns a model of the environment's dynamics (state transitions and rewards) and uses planning (e.g., MCTS, dynamic programming) to find good policies. Planning can be more sample-efficient than model-free methods but accuracy depends on the learned model; hybrid approaches use models to generate trajectories for model-free learning, balancing efficiency and robustness.

## How It's Best Learned
Implement Dyna-Q which interleaves model learning and planning, comparing sample efficiency with pure model-free Q-learning.

## Questions

```yaml
- question: "An agent trained with model-based RL achieves near-perfect performance in simulation but fails catastrophically when deployed in the real environment. What is the most likely cause?"
  type: multiple-choice
  options:
    - "The agent's policy network was too small to generalize beyond the training distribution"
    - "Model-free updates are incompatible with simulated experience"
    - "The learned world model contains errors that the agent exploited, producing a policy tuned to the model's mistakes rather than the real environment"
    - "The agent did not collect enough real interactions before beginning to plan"
  answer: 2
  explanation: "This is the model exploitation problem — the defining failure mode of model-based RL. Planning algorithms are very good at finding optimal policies relative to whatever model they are given. If the model is imperfect, planning will find policies that look optimal in simulation by taking advantage of the model's inaccuracies. The agent becomes an expert at the simulation, not the real task. This is why uncertainty-aware models and hybrid approaches that periodically check real-world data are essential."

- question: "Why is Dyna-Q more sample-efficient than pure Q-learning on the same task?"
  type: multiple-choice
  options:
    - "Dyna-Q uses a larger neural network that generalizes better across states"
    - "Dyna-Q skips the Q-learning update after real environment steps to save computation"
    - "Each real interaction updates a world model, which then generates n additional simulated transitions used for Q-learning updates without further real-world steps"
    - "Dyna-Q applies model-free updates exclusively on high-reward trajectories, filtering out uninformative experiences"
  answer: 2
  explanation: "Dyna-Q's insight is simple but powerful: after each real step, update the model with the observed transition, then run n additional Q-learning updates using transitions sampled from the model. Each real experience thus produces n+1 learning updates instead of one. With n=50, the agent extracts 51 policy improvements per real step. The model acts as a multiplier on data efficiency — the key mechanism behind model-based RL's sample efficiency advantage."

- question: "Model-based RL is generally preferable to model-free RL because it learns from fewer real environment interactions."
  type: true-false
  answer: false
  explanation: "Sample efficiency is the primary advantage of model-based RL, but it comes with a critical cost: model error. A learned world model is never perfectly accurate, and planning over an imperfect model can lead to model exploitation — policies optimized for the simulation rather than reality. Model-free methods are more robust because they learn directly from real experience and cannot exploit a model they don't have. The right choice depends on whether sample efficiency or robustness is more important for the task."

- question: "In model-based RL, the agent can improve its policy by planning over simulated trajectories generated from a learned world model, without additional real-world interactions during the planning phase."
  type: true-false
  answer: true
  explanation: "This is the core mechanism and main advantage of model-based RL. Once the world model has been learned from some initial real interactions, the agent can run arbitrarily many planning steps in simulation — dynamic programming, Monte Carlo rollouts, or model-free updates on imagined trajectories — all without touching the real environment. Real interactions are only needed to update the model itself, not for every policy improvement step."

- question: "What is the central tension in model-based reinforcement learning, and how do modern approaches try to manage it?"
  type: short-answer
  answer: "The central tension is between sample efficiency and model accuracy. A world model enables policy improvement through planning without costly real interactions, but any model errors can be exploited by the planner, yielding policies that fail in the real environment. Modern approaches address this through uncertainty-aware models (that refuse to plan confidently in unfamiliar regions), ensemble methods (that act conservatively where multiple models disagree), and hybrid architectures like Dreamer that ground predictions in periodic real-world data."
  explanation: "Understanding this tension is key to understanding the entire model-based RL literature. Every design choice — how often to collect real data, how to represent uncertainty, how many planning steps to perform — is a response to this tradeoff. The tradeoff also explains why model-free methods remain competitive despite lower sample efficiency: in complex environments, model accuracy is hard to guarantee, and robustness sometimes matters more than efficiency."
```

## Explainer

In model-free reinforcement learning, the agent learns entirely through trial and error — it takes actions, observes rewards, and slowly updates its value estimates or policy. This works, but it can be extraordinarily wasteful. Imagine learning to navigate a maze by physically walking through it thousands of times. **Model-based reinforcement learning** takes a different approach: the agent learns a **world model** — an internal simulation of how the environment works — and then plans inside that simulation before acting in the real world. Instead of walking the maze a thousand times, you study the map and plan your route mentally.

Formally, the world model learns the environment's **transition function** T(s, a) → s' and **reward function** R(s, a) — the same components you encountered in Markov decision processes. Once these are learned from a relatively small number of real interactions, the agent can generate **simulated experience** by "imagining" trajectories through the model. It can then apply any planning algorithm — dynamic programming, Monte Carlo tree search, or even model-free updates on the simulated data — to improve its policy without additional real-world samples. This is why model-based methods are typically far more **sample-efficient** than their model-free counterparts: each real interaction teaches the agent about the world's dynamics, and that knowledge multiplies into many planned improvements.

The classic algorithm that demonstrates this idea is **Dyna-Q**. After each real step in the environment, Dyna-Q does two things: it updates the model with the observed transition, and it performs *n* additional Q-learning updates using transitions sampled from the model. With even a modest number of planning steps (say, n = 50), Dyna-Q converges dramatically faster than pure Q-learning on the same problem. The real experience feeds the model, and the model amplifies the learning — a virtuous cycle.

The central challenge of model-based RL is **model error**. No learned model is perfect, and planning with an inaccurate model can lead to policies that exploit the model's mistakes rather than solving the actual task — a phenomenon called **model exploitation**. If the model incorrectly predicts that a dangerous action is safe, the agent will confidently walk into disaster. Modern approaches address this through uncertainty-aware models that know what they do not know, ensemble methods that maintain multiple models and act conservatively where they disagree, and hybrid architectures like **Dreamer** that learn world models as latent-space dynamics and use them to train policies via imagination while periodically grounding predictions in real data. The tradeoff between sample efficiency and model accuracy is the defining tension of the field.
