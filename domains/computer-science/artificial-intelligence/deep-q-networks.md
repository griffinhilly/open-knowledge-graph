---
id: deep-q-networks
title: Deep Q-Networks (DQN)
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: q-learning
  type: hard
- id: convolutional-neural-networks
  type: hard
tags:
- reinforcement-learning
- deep-learning
- value-based-methods
- atari-games
stage: advanced
status: draft
---

# Deep Q-Networks (DQN)

## Core Idea
Deep Q-Networks use neural networks to approximate Q-value functions in high-dimensional state spaces like images, enabling learning of complex control policies. Key innovations include experience replay (a memory buffer that breaks correlation between samples) and target networks (separate network that stabilizes training by reducing moving target problem), making deep RL practical.

## How It's Best Learned
Implement DQN with experience replay and train it on an Atari game or simple environment to understand how the algorithm handles high-dimensional states and long-term credit assignment.

## Explainer

From Q-learning, you know the core idea: maintain a table Q(s, a) estimating the expected future reward for taking action a in state s, and update it using the Bellman equation as you interact with the environment. This works well when the state space is small enough to visit every state repeatedly — a grid world, a simple game. But consider an Atari game where the state is a 210×160 pixel image with 128 possible colors per pixel. The number of possible states is astronomically large, and you will never visit the same exact screen twice. A Q-table is hopeless here, which is why **Deep Q-Networks (DQN)** replace the table with a neural network that takes a state (raw pixels) as input and outputs Q-values for every possible action.

The idea of function approximation for Q-values is natural, but early attempts at combining neural networks with Q-learning were notoriously unstable. DQN introduced two innovations that made it work. The first is **experience replay**: instead of learning from each transition (s, a, r, s') immediately and then discarding it, DQN stores transitions in a large memory buffer and samples random minibatches for training. This breaks the temporal correlation between consecutive samples — without replay, the network sees a stream of highly correlated states (consecutive game frames), which causes it to overfit to recent experience and forget earlier lessons. Random sampling from the buffer produces a more i.i.d.-like training distribution, which is what gradient descent expects.

The second innovation is the **target network**. In standard Q-learning, the same Q-function is used both to select actions and to compute the target value (r + γ max Q(s', a')). When Q is a neural network, updating the weights to better match today's targets immediately changes tomorrow's targets, creating a moving-target problem that can cause oscillation or divergence. DQN solves this by maintaining a separate copy of the network — the target network — whose weights are frozen and only updated periodically (every few thousand steps) by copying from the main network. This makes the targets temporarily stationary, giving the main network a stable objective to learn against.

With these two techniques, DQN achieved human-level performance on dozens of Atari games, learning directly from raw pixel inputs with no game-specific engineering. The agent receives only the screen image and the score, and it must discover through trial and error which sequences of joystick actions lead to high scores. The convolutional layers (from your CNN prerequisite) extract spatial features from the game frames, and the fully connected layers map those features to Q-values for each possible action. The significance of DQN extends beyond game-playing — it demonstrated that deep reinforcement learning could scale to high-dimensional perception problems, launching the modern era of deep RL and inspiring subsequent algorithms like Double DQN, Dueling DQN, and Prioritized Experience Replay that addressed remaining limitations.
