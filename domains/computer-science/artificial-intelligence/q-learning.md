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

## Explainer

From your study of Markov decision processes, you know that an agent interacts with an environment described by states, actions, transition probabilities, and rewards, and that the goal is to find a policy that maximizes cumulative discounted reward. Dynamic programming methods like value iteration solve this when the transition model is known — you can compute expected values by sweeping through the state space. But what if the agent does not know the transition probabilities? It must learn from experience, updating its estimates as it takes actions and observes what happens. **Q-learning** solves this problem by learning action-value estimates directly from interaction, without ever needing a model of the environment.

The core object in Q-learning is the **Q-function**, Q(s, a), which estimates the total discounted reward the agent will receive by taking action a in state s and then following the optimal policy thereafter. The update rule after observing a transition from state s to state s' with reward r is: Q(s, a) ← Q(s, a) + α[r + γ max_a' Q(s', a') − Q(s, a)]. The term in brackets is the **temporal difference error** — the gap between the current estimate Q(s, a) and a better estimate constructed from the immediate reward plus the discounted value of the best action at the next state. The learning rate α controls how much each new experience shifts the estimate. Over many updates, the Q-values converge toward the true optimal action-values, and the optimal policy is simply: in each state, pick the action with the highest Q-value.

A critical property of Q-learning is that it is **off-policy**: the update uses max_a' Q(s', a'), which is the value of the *best* action at the next state, regardless of which action the agent actually takes next. This means the agent can explore freely — taking random or suboptimal actions to discover new parts of the environment — while still learning the optimal policy. The standard exploration strategy is **ε-greedy**: with probability ε take a random action, otherwise take the greedy action. Early in learning ε is high (explore a lot), and it is gradually reduced as the Q-values stabilize (exploit what you have learned). Without sufficient exploration, the agent may converge to a suboptimal policy because it never discovers better paths.

Q-learning with a table entry for every (state, action) pair works well when the state and action spaces are small and discrete, like a grid world. But real problems often have enormous or continuous state spaces — a robot's joint angles, a game's pixel screen, a car's position and velocity. Storing and updating a table entry for every possible state becomes impossible. This is where **function approximation** enters: instead of a table, you represent Q(s, a) with a parameterized function — a neural network, for example — and update its parameters using the temporal difference error as a loss signal. This extension, known as deep Q-learning, is powerful but introduces instability because the target (r + γ max_a' Q(s', a')) changes as the network's parameters change. Techniques like **experience replay** (storing past transitions and sampling mini-batches) and **target networks** (using a slowly-updated copy of the network for the target) stabilize training and made the famous Atari-playing DQN agent possible.
