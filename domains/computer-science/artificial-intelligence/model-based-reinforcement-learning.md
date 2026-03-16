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
stage: advanced
status: draft
---

# Model-Based Reinforcement Learning

## Core Idea
Model-based RL learns a model of the environment's dynamics (state transitions and rewards) and uses planning (e.g., MCTS, dynamic programming) to find good policies. Planning can be more sample-efficient than model-free methods but accuracy depends on the learned model; hybrid approaches use models to generate trajectories for model-free learning, balancing efficiency and robustness.

## How It's Best Learned
Implement Dyna-Q which interleaves model learning and planning, comparing sample efficiency with pure model-free Q-learning.

## Explainer

In model-free reinforcement learning, the agent learns entirely through trial and error — it takes actions, observes rewards, and slowly updates its value estimates or policy. This works, but it can be extraordinarily wasteful. Imagine learning to navigate a maze by physically walking through it thousands of times. **Model-based reinforcement learning** takes a different approach: the agent learns a **world model** — an internal simulation of how the environment works — and then plans inside that simulation before acting in the real world. Instead of walking the maze a thousand times, you study the map and plan your route mentally.

Formally, the world model learns the environment's **transition function** T(s, a) → s' and **reward function** R(s, a) — the same components you encountered in Markov decision processes. Once these are learned from a relatively small number of real interactions, the agent can generate **simulated experience** by "imagining" trajectories through the model. It can then apply any planning algorithm — dynamic programming, Monte Carlo tree search, or even model-free updates on the simulated data — to improve its policy without additional real-world samples. This is why model-based methods are typically far more **sample-efficient** than their model-free counterparts: each real interaction teaches the agent about the world's dynamics, and that knowledge multiplies into many planned improvements.

The classic algorithm that demonstrates this idea is **Dyna-Q**. After each real step in the environment, Dyna-Q does two things: it updates the model with the observed transition, and it performs *n* additional Q-learning updates using transitions sampled from the model. With even a modest number of planning steps (say, n = 50), Dyna-Q converges dramatically faster than pure Q-learning on the same problem. The real experience feeds the model, and the model amplifies the learning — a virtuous cycle.

The central challenge of model-based RL is **model error**. No learned model is perfect, and planning with an inaccurate model can lead to policies that exploit the model's mistakes rather than solving the actual task — a phenomenon called **model exploitation**. If the model incorrectly predicts that a dangerous action is safe, the agent will confidently walk into disaster. Modern approaches address this through uncertainty-aware models that know what they do not know, ensemble methods that maintain multiple models and act conservatively where they disagree, and hybrid architectures like **Dreamer** that learn world models as latent-space dynamics and use them to train policies via imagination while periodically grounding predictions in real data. The tradeoff between sample efficiency and model accuracy is the defining tension of the field.
