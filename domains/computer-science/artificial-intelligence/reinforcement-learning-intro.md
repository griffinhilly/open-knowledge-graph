---
id: reinforcement-learning-intro
title: Introduction to Reinforcement Learning
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: markov-decision-processes
  type: hard
- id: probability-axioms-and-rules
  type: soft
- id: expected-value-and-variance
  type: soft
- id: optimization-multivariable-basics
  type: soft
tags:
- reinforcement-learning
- learning-paradigm
stage: advanced
status: draft
---

# Introduction to Reinforcement Learning

## Core Idea
RL learns from interaction with an environment. Agents select actions, receive rewards, and observe state transitions. Goal is maximizing cumulative discounted reward. Model-free methods learn value/policy directly; model-based methods learn transition/reward models.

## Explainer

From your study of Markov decision processes, you know the formal framework: states, actions, transition probabilities, and rewards. An MDP defines the rules of a game. **Reinforcement learning** is the process of learning to play that game well — without being told the rules in advance. The agent does not know the transition function or the reward function; it must discover them through experience, like a child learning that touching a hot stove hurts by touching it.

The RL loop is deceptively simple. At each time step, the agent observes its current **state**, selects an **action**, receives a **reward** signal, and transitions to a new state. The agent's goal is to learn a **policy** — a mapping from states to actions — that maximizes the expected **cumulative discounted reward**, which you know from MDPs as the value function V(s) = E[Σ γᵗrₜ]. The discount factor γ controls how much the agent cares about future rewards versus immediate ones. A γ close to 1 makes the agent far-sighted; a γ close to 0 makes it myopic. This objective connects directly to the expected value concepts you have studied in probability.

The central challenge of RL is the **exploration-exploitation tradeoff**. The agent must balance exploiting actions it already knows are good against exploring unknown actions that might be better. If a robot discovers that turning left yields a small reward, should it keep turning left or try turning right on the chance of finding a larger reward? Too much exploitation and the agent gets stuck in suboptimal behavior; too much exploration and it wastes time on bad actions. Strategies like **ε-greedy** (act greedily most of the time, but explore randomly with probability ε) and **upper confidence bounds** (prefer actions with uncertain value estimates) address this tradeoff.

RL methods split into two families. **Model-free** methods learn the value function or policy directly from experience without building an explicit model of the environment. Q-learning, for instance, learns Q(s, a) — the expected return of taking action a in state s — by updating estimates after each real transition. **Model-based** methods instead learn the transition and reward functions, then plan using the learned model. Model-free methods are simpler and more robust to model errors, but they require many more interactions to converge. Model-based methods are sample-efficient but only as good as their learned model. Understanding this distinction is the gateway to the rest of the RL landscape, from deep Q-networks to policy gradient methods and beyond.
