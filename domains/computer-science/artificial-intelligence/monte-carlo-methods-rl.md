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

## Explainer

From your introduction to reinforcement learning, you know the core problem: an agent interacts with an environment, collecting rewards, and needs to learn which states are valuable and which actions lead to high long-term return. The fundamental challenge is estimating **value functions** — how good is it to be in a particular state, or to take a particular action in a particular state? Monte Carlo methods answer this question in the most straightforward way possible: let the agent play out complete episodes, observe what actually happened, and average the results.

Consider a concrete example. An agent plays 1,000 games of blackjack. In game 47, it visits state "holding 18, dealer shows 6" and ultimately wins, receiving a return of +1 from that state onward. In game 203, it visits the same state but loses, receiving −1. After all 1,000 games, the Monte Carlo estimate for that state's value is simply the average of all the returns observed when the agent was in that state. This is the **first-visit Monte Carlo** method — it uses only the first time a state appears in each episode. **Every-visit Monte Carlo** averages over all visits, including multiple visits within the same episode. Both converge to the true value as the number of episodes grows, because they are computing sample means of an unbiased estimator: the actual return.

The strength of Monte Carlo methods is also their limitation. Because they use the complete return from a state to the end of the episode, they make no assumptions about the environment's dynamics — they do not need a model of transition probabilities, and they do not **bootstrap** (estimate values based on other estimated values). This makes them unbiased: given enough episodes, the estimates converge to the true values. But waiting for the full episode introduces **high variance**, because a single episode's return depends on every random event from that state onward. A state might truly be valuable, but one unlucky episode can produce a very low return, and the estimate swings widely until enough data accumulates.

A powerful extension is **off-policy** Monte Carlo learning using **importance sampling**. Suppose you have logged data from a previous policy (the **behavior policy**) but want to evaluate or improve a different policy (the **target policy**). The returns observed under the behavior policy are "wrong" for the target policy — the agent took different actions than the target would have. Importance sampling corrects for this by weighting each return by the ratio of probabilities: how likely was this trajectory under the target policy divided by how likely it was under the behavior policy. Ordinary importance sampling is unbiased but can have extreme variance when the ratio is large; **weighted importance sampling** reduces variance at the cost of introducing a small bias. This off-policy capability makes Monte Carlo methods valuable in real-world settings where you cannot always re-collect data — you can learn from historical logs, past experiments, or demonstrations by another agent.
