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

## Questions

```yaml
- question: "An agent uses Monte Carlo value estimation. After 10 episodes, its estimate for a state fluctuates wildly. After 10,000 episodes, the estimate converges. This pattern is best explained by:"
  type: multiple-choice
  options:
    - "Monte Carlo uses bootstrapping, which introduces bias that corrects itself with more data"
    - "Monte Carlo estimates are unbiased but have high variance; averaging many complete returns is needed for convergence"
    - "Early episodes use a discount factor of γ=1, causing instability that is corrected in later training"
    - "The reward signal was incorrectly calibrated in the first 10 episodes"
  answer: 1
  explanation: "Monte Carlo methods do NOT bootstrap — they use the actual return from each complete episode, making estimates unbiased. However, each episode's return is just one noisy sample of the true expected return: random events throughout the episode add variance. With only 10 samples, the average is unreliable; with 10,000, the law of large numbers drives the sample mean toward the true value. The high-variance, low-bias tradeoff is intrinsic to MC's design of using full episode returns."

- question: "You have logs from an old policy and want to evaluate a new policy without collecting new data. Which Monte Carlo approach makes this possible?"
  type: multiple-choice
  options:
    - "Every-visit Monte Carlo, which averages over all visits to each state within an episode"
    - "Off-policy Monte Carlo with importance sampling, which reweights each return by the ratio of target to behavior policy probabilities"
    - "First-visit Monte Carlo, restricted to only the first visit to each state per episode"
    - "Model-based Monte Carlo, which builds an explicit transition model from the logged trajectories"
  answer: 1
  explanation: "Importance sampling corrects for the mismatch between the behavior policy (which generated the data) and the target policy (which we want to evaluate). Each return is multiplied by the product of probability ratios along the trajectory — how likely was this sequence of actions under the target policy vs. the behavior policy. This reweighting makes the estimates valid for the target policy, enabling learning from historical data without new interaction."

- question: "Monte Carlo methods in RL bootstrap — they update value estimates using other estimated values — which is why they require only partial episodes to update."
  type: true-false
  answer: false
  explanation: "This describes temporal-difference (TD) learning, not Monte Carlo. Monte Carlo methods do the opposite: they wait for the complete episode to end, then use the actual observed return (not any estimated value) to update. This is why MC cannot update mid-episode and why its estimates are unbiased — there is no estimated value injected into the update, only real observed outcomes."

- question: "Ordinary importance sampling in off-policy Monte Carlo produces unbiased estimates but can have extremely high variance when the target and behavior policies differ substantially."
  type: true-false
  answer: true
  explanation: "When the target policy assigns high probability to actions that the behavior policy rarely took, the importance sampling ratio becomes very large, causing individual weighted returns to be enormous — inflating variance dramatically. Weighted importance sampling addresses this by normalizing, reducing variance at the cost of a small bias. This variance-bias tradeoff is a core practical consideration when choosing between the two variants."

- question: "What does it mean for Monte Carlo value estimates to be 'unbiased but high variance,' and why does this tradeoff arise from the method's design?"
  type: short-answer
  answer: "Unbiased means the expected value of the estimate equals the true value function — given enough data, Monte Carlo converges to the correct answer without systematic error. High variance means individual estimates can differ wildly from the true value because each estimate is based on a single episode's return, which depends on every random event from that state to the end of the episode. The tradeoff is fundamental: using complete actual returns (no bootstrapping) guarantees no bias from incorrect value estimates, but it also means each sample carries the full noise of an entire episode rather than a one-step correction."
  explanation: "This contrasts with TD learning, which bootstraps (uses estimated values), introducing bias but dramatically reducing variance by updating based on a single step rather than a full episode. The MC/TD tradeoff is one of the core tensions in RL: pure MC is unbiased but slow to converge due to variance; pure TD is biased but lower-variance; methods like TD(λ) interpolate between them."
```

## Explainer

From your introduction to reinforcement learning, you know the core problem: an agent interacts with an environment, collecting rewards, and needs to learn which states are valuable and which actions lead to high long-term return. The fundamental challenge is estimating **value functions** — how good is it to be in a particular state, or to take a particular action in a particular state? Monte Carlo methods answer this question in the most straightforward way possible: let the agent play out complete episodes, observe what actually happened, and average the results.

Consider a concrete example. An agent plays 1,000 games of blackjack. In game 47, it visits state "holding 18, dealer shows 6" and ultimately wins, receiving a return of +1 from that state onward. In game 203, it visits the same state but loses, receiving −1. After all 1,000 games, the Monte Carlo estimate for that state's value is simply the average of all the returns observed when the agent was in that state. This is the **first-visit Monte Carlo** method — it uses only the first time a state appears in each episode. **Every-visit Monte Carlo** averages over all visits, including multiple visits within the same episode. Both converge to the true value as the number of episodes grows, because they are computing sample means of an unbiased estimator: the actual return.

The strength of Monte Carlo methods is also their limitation. Because they use the complete return from a state to the end of the episode, they make no assumptions about the environment's dynamics — they do not need a model of transition probabilities, and they do not **bootstrap** (estimate values based on other estimated values). This makes them unbiased: given enough episodes, the estimates converge to the true values. But waiting for the full episode introduces **high variance**, because a single episode's return depends on every random event from that state onward. A state might truly be valuable, but one unlucky episode can produce a very low return, and the estimate swings widely until enough data accumulates.

A powerful extension is **off-policy** Monte Carlo learning using **importance sampling**. Suppose you have logged data from a previous policy (the **behavior policy**) but want to evaluate or improve a different policy (the **target policy**). The returns observed under the behavior policy are "wrong" for the target policy — the agent took different actions than the target would have. Importance sampling corrects for this by weighting each return by the ratio of probabilities: how likely was this trajectory under the target policy divided by how likely it was under the behavior policy. Ordinary importance sampling is unbiased but can have extreme variance when the ratio is large; **weighted importance sampling** reduces variance at the cost of introducing a small bias. This off-policy capability makes Monte Carlo methods valuable in real-world settings where you cannot always re-collect data — you can learn from historical logs, past experiments, or demonstrations by another agent.
