---
id: actor-critic-methods
title: Actor-Critic Methods
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: policy-gradient-methods
  type: hard
tags:
- reinforcement-learning
- policy-optimization
- temporal-difference
stage: advanced
status: draft
---

# Actor-Critic Methods

## Core Idea
Actor-critic combines policy gradient (actor) with value function (critic). Actor updates via policy gradients; critic provides TD targets reducing variance. Critic uses bootstrapping for sample efficiency. A3C extends to parallel workers.

## Questions

```yaml
- question: "Why does using the critic's value estimate as a baseline reduce variance in the actor's gradient updates compared to using the full episode return?"
  type: multiple-choice
  options:
    - "The critic filters out noisy rewards by averaging them before passing them to the actor"
    - "The critic's state-value estimate is a learned function of the current state, while the full episode return varies randomly based on all future actions and transitions"
    - "The critic reduces variance because it uses a larger batch of samples to estimate the gradient"
    - "The actor's gradient is inherently lower variance because the critic replaces the policy gradient entirely"
  answer: 1
  explanation: "The full episode return is a high-variance signal because it is the sum of all future rewards along a specific trajectory — every random action and stochastic transition contributes noise. The critic's value estimate, V(s), is a smoothed function of the current state learned over many updates; it is stable relative to a single trajectory's return. The advantage A = r + γV(s') - V(s) subtracts a well-calibrated baseline, dramatically reducing variance while preserving the correct direction of the gradient. Option C is incorrect: the variance reduction comes from the quality of the baseline, not batch size."

- question: "An agent is learning to play a video game where episodes last 50,000 steps. Which scenario makes actor-critic most beneficial compared to a pure Monte Carlo policy gradient?"
  type: multiple-choice
  options:
    - "The game has a sparse reward (only +1 at victory after 50,000 steps), making it impractical to wait for full episode returns before updating"
    - "The game has dense rewards every step, so the full episode return is easy to compute and the critic adds unnecessary complexity"
    - "The action space is discrete, so value-based methods like Q-learning are always preferred"
    - "The game has a deterministic transition function, eliminating stochasticity in the return"
  answer: 0
  explanation: "Sparse, long-horizon environments are exactly where actor-critic excels. With a reward only at the episode's end (50,000 steps), a pure Monte Carlo policy gradient must wait for the complete episode before making a single update — slow and sample-inefficient. The actor-critic critic can bootstrap using TD learning (r + γV(s')), enabling updates after every step even when the reward is sparse. Option B misidentifies the problem: dense rewards make the return *computable* but still noisy; the critic still helps by providing a baseline. Option C is wrong: actor-critic handles continuous action spaces better than Q-learning."

- question: "In an actor-critic system, the actor can be updated after every individual time step rather than waiting for a complete episode to end."
  type: true-false
  answer: true
  explanation: "This is one of the defining advantages of actor-critic over pure Monte Carlo policy gradient. Because the critic uses TD bootstrapping — estimating value from the immediate reward plus a discounted estimate of the next state's value — it can provide a learning signal after a single step. The actor then uses this TD-based advantage to update its policy immediately. This step-by-step learning is what makes actor-critic practical for long-horizon and continuing (non-episodic) tasks."

- question: "In an actor-critic architecture, both the actor and the critic are updated using Monte Carlo estimates from complete episode returns."
  type: true-false
  answer: false
  explanation: "Only the actor uses something conceptually related to returns — and even then, through the advantage signal, not raw returns. The defining feature of actor-critic is that the critic uses temporal difference (TD) learning: it bootstraps from its own prediction at the next state rather than waiting for the episode to end. This bootstrapping is what enables step-by-step updates and improved sample efficiency. If the critic used full Monte Carlo returns, you would lose the key benefit of actor-critic over pure policy gradient methods."

- question: "What does the 'advantage' signal measure in actor-critic, and why is it used instead of the raw reward to update the actor?"
  type: short-answer
  answer: "The advantage A(s,a) = r + γV(s') - V(s) measures how much better (or worse) taking action a in state s turned out to be compared to what the critic expected. A positive advantage means the action exceeded expectations; a negative advantage means it underperformed. The raw reward is used instead of raw reward because the reward alone doesn't account for how good the state was to begin with — an action that yields reward 5 is excellent from a bad state but mediocre from a good state. The advantage centers this comparison around the critic's learned expectation."
  explanation: "Using the advantage rather than raw reward is a variance reduction technique that also provides better credit assignment. If you update the actor using raw reward, actions in naturally high-reward states always get positive updates and actions in low-reward states always get negative updates — regardless of whether those actions were actually good or bad relative to alternatives. The advantage removes this baseline bias: it asks 'was this action better than average for this state?' rather than 'was the reward positive?' This makes gradient estimates more informative and less noisy."
```

## Explainer

From your study of policy gradient methods, you know the fundamental idea: adjust policy parameters in the direction that increases expected return, using sampled trajectories to estimate the gradient. You also know the central problem — policy gradient estimates are noisy. The return from a single trajectory is a high-variance signal because it depends on every random action and state transition in the episode. Subtracting a baseline helps, but the question becomes: what is the best baseline? **Actor-critic methods** answer this by learning the baseline itself, creating a two-component architecture where each part does what it is best at.

The **actor** is the policy network — it maps states to action probabilities (or action distributions) and is updated via policy gradients, just as you learned before. The **critic** is a separate value function network that estimates how good a state (or state-action pair) is. Instead of waiting for the full episode return to update the actor, the critic provides an immediate estimate of future value using **temporal difference (TD) learning**: it bootstraps from its own predictions at the next state. The actor then uses the **advantage** — the difference between the actual reward-plus-estimated-future-value and the critic's current estimate — as its gradient signal. When the advantage is positive, the action was better than expected, so the policy shifts toward it; when negative, the policy shifts away.

This decomposition solves two problems simultaneously. The critic reduces variance because its value estimate is a learned function of the state, not a noisy sample of future rewards. The actor maintains the ability to learn stochastic policies and handle continuous action spaces, which pure value-based methods like Q-learning struggle with. The critic also enables **bootstrapping** — updating estimates based on other estimates rather than waiting for complete episodes — which dramatically improves sample efficiency. You can update the policy after every single step rather than waiting for an episode to finish, making actor-critic methods practical for environments with long or infinite horizons.

The **A3C (Asynchronous Advantage Actor-Critic)** algorithm extends this idea to parallel computation: multiple independent workers each interact with their own copy of the environment and asynchronously update shared actor and critic parameters. The asynchronous updates naturally decorrelate the training data (different workers see different states), removing the need for a replay buffer. Its synchronous variant, **A2C**, collects batches from all workers before a single update and is often preferred in practice for more stable training. These actor-critic foundations underpin most modern reinforcement learning systems, from robotics control to game-playing agents, because they combine the theoretical guarantees of policy gradients with the practical efficiency of value function learning.
