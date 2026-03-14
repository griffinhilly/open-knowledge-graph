---
id: monte-carlo-methods-rl
title: Monte Carlo Methods in Reinforcement Learning
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: reinforcement-learning-intro
  type: hard
builds-toward:
- temporal-difference-learning
tags:
- reinforcement-learning
- value-estimation
- off-policy-learning
- importance-sampling
stage: advanced
status: draft
---

# Monte Carlo Methods in Reinforcement Learning

## Core Idea
Monte Carlo methods estimate value functions by averaging complete episode returns, enabling learning from any state visited in episodes. Unlike temporal difference methods, they do not bootstrap and have high variance but unbiased estimates; importance sampling corrects for off-policy trajectories, extending applicability to learning from previously logged data.
