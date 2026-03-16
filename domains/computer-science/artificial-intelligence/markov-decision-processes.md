---
id: markov-decision-processes
title: Markov Decision Processes
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: markov-chains
  type: hard
- id: dynamic-programming-intro
  type: hard
- id: probability-axioms-and-rules
  type: soft
- id: probability-axioms
  type: soft
- id: expected-value
  type: soft
- id: expected-value-and-variance
  type: soft
tags:
- decision-making
- markov-models
- optimization
stage: advanced
status: draft
---

# Markov Decision Processes

## Core Idea
MDPs extend Markov chains with actions and rewards, modeling sequential decision-making under uncertainty. States, actions, transition probabilities, and reward functions define an MDP. Value iteration and policy iteration compute optimal policies maximizing expected cumulative reward.

## Questions

```yaml
- question: "In an MDP, the Markov property means that:"
  type: multiple-choice
  options:
    - "The reward only depends on the current action"
    - "The next state depends only on the current state and action, not on history"
    - "The optimal policy must be deterministic"
    - "Transition probabilities are uniform across all actions"
  answer: 1
  explanation: "The Markov property states that the future (next state and reward) depends only on the current state and action, not on the full history of states and actions. This makes MDPs tractable — you don't need to store or remember the entire sequence of past events to make optimal decisions."

- question: "In an MDP with a discount factor γ = 1 and an infinite horizon, value iteration is guaranteed to converge to the optimal value function in a finite number of iterations."
  type: true-false
  answer: false
  explanation: "When γ = 1 there is no geometric contraction, so the Bellman operator is not a contraction mapping and value iteration may fail to converge in an infinite-horizon setting. With γ < 1, the contraction mapping property guarantees convergence at a rate of γ per iteration. γ = 1 is safe only in episodic (finite-horizon) MDPs where episodes always terminate."

- question: "What is the difference between a policy and a value function in an MDP, and how are they related?"
  type: short-answer
  answer: "A policy maps states to actions (or probability distributions over actions) and specifies the agent's behavior. A value function assigns each state a scalar representing the expected cumulative discounted reward when following a particular policy from that state. They are related through the Bellman equations: given a policy, its value function can be computed by policy evaluation; given a value function, an improved policy can be extracted by choosing the action that maximizes expected future value."
  explanation: "This relationship is the engine of both policy iteration and value iteration. Policy iteration alternates between evaluating the current policy's value function and improving the policy greedily with respect to it; value iteration collapses both steps into one Bellman backup. Understanding that a policy and a value function are complementary representations of agent behavior is the conceptual foundation of reinforcement learning."
```

## Explainer

A Markov chain describes a system that hops between states according to fixed transition probabilities — you have no control over what happens next. A Markov Decision Process (MDP) adds two new ingredients: *actions* and *rewards*. At each step, an agent observes the current state, chooses an action, receives a reward, and transitions to a new state. The key insight is that the agent's goal is not to respond to a single event but to maximize the *total* reward accumulated over time — which means current decisions must account for their downstream consequences.

The MDP is defined by four objects: a set of states S, a set of actions A, a transition function T(s, a, s') giving the probability of reaching s' when taking action a in state s, and a reward function R(s, a) giving the immediate payoff. The Markov property — that T depends only on the current state and action, not on history — is what makes this tractable. Without it, an agent would need to track the entire sequence of past states to plan optimally.

To find the best behavior, we define a *value function* V(s): the maximum expected cumulative reward achievable from state s. The Bellman optimality equation expresses V(s) recursively — the value of a state is the best immediate reward plus the discounted value of the best next state. Value iteration repeatedly applies this equation until V converges, then extracts the optimal policy by choosing, in each state, the action that achieves that maximum. Policy iteration takes a different route: start with any policy, evaluate it (compute its value function), improve it greedily, and repeat — provably converging to the optimal policy in finite steps.

The discount factor γ ∈ [0, 1) controls how much the agent values future rewards relative to immediate ones. γ close to 1 means the agent is patient and plans far ahead; γ close to 0 means it is myopic. Mathematically, γ < 1 also guarantees that the infinite sum of rewards converges to a finite number, and it makes the Bellman operator a contraction — the property that makes value iteration converge.

MDPs are the theoretical backbone of reinforcement learning. Real-world RL algorithms like Q-learning and policy gradient methods can be understood as solving MDPs when the transition and reward functions are unknown and must be estimated from experience. Mastering the MDP framework — its structure, its Bellman equations, and its solution algorithms — gives you the conceptual tools to reason about any sequential decision problem under uncertainty.
