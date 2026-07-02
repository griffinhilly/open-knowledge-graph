---
id: policy-gradient-methods
title: Policy Gradient Methods
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: reinforcement-learning-intro
  type: hard
- id: gradient-descent-optimization
  type: hard
- id: derivatives-of-exponential-functions
  type: soft
- id: expected-value
  type: soft
- id: partial-derivatives
  type: hard
- id: chain-rule-multivariable
  type: hard
tags:
- reinforcement-learning
- policy-optimization
- on-policy
stage: expert
status: validated
---

# Policy Gradient Methods

## Core Idea
Policy gradient methods directly optimize the policy π(a|s) via gradient ascent on expected return. REINFORCE uses full episode returns; advantage actor-critic uses value baselines. Methods are on-policy but handle continuous actions naturally.

## Questions

```yaml
- question: "An actor-critic agent in state s_t takes action a_t and receives a total return G_t = 10. The critic's value estimate for that state is V(s_t) = 9.5. How does the actor update its policy?"
  type: multiple-choice
  options:
    - "It strongly increases the probability of a_t, because G_t = 10 is a large positive return"
    - "It slightly increases the probability of a_t, because the advantage A_t = G_t − V(s_t) = 0.5 is small but positive"
    - "It decreases the probability of a_t, because V(s_t) = 9.5 indicates the state is already high-value and this action underperformed"
    - "It does not update, because a_t produced a return above the value estimate and no correction is needed"
  answer: 1
  explanation: "The advantage A_t = G_t − V(s_t) = 10 − 9.5 = 0.5 measures how much *better than expected* the action performed. A small positive advantage yields a small upward adjustment to the action's probability. The key insight is that the update is relative to the baseline, not absolute: a return of 10 in a state that typically yields 9.5 is only marginally good, not exceptional. Without the baseline (raw REINFORCE), the large raw return of 10 would cause a stronger, noisier update regardless of context — the baseline removes this variance."

- question: "Why are policy gradient methods generally preferred over value-based methods like Q-learning for tasks with continuous action spaces?"
  type: multiple-choice
  options:
    - "Policy gradient methods are guaranteed to converge to the globally optimal policy, while Q-learning may converge to suboptimal policies"
    - "Value-based methods require enumerating all possible actions to select the maximum Q-value, which is infeasible when actions are continuous"
    - "Policy gradient methods do not require a reward signal, making them more versatile"
    - "Q-learning cannot handle stochastic environments, while policy gradients can"
  answer: 1
  explanation: "In Q-learning, the greedy policy requires argmax_a Q(s,a) — finding the action that maximizes Q. When actions are discrete and finite, you enumerate them. When actions are real-valued (e.g., continuous torques for a robotic arm), enumeration is impossible and even optimization over the action space at every step is expensive. Policy gradient methods sidestep this entirely: a parameterized policy directly outputs an action or a distribution over actions, with gradient ascent updating the parameters. Continuous action spaces — Gaussian policies, for example — are handled naturally."

- question: "REINFORCE is considered a biased gradient estimator because the return G_t is computed from a single sampled trajectory rather than the true expected return."
  type: true-false
  answer: false
  explanation: "REINFORCE is actually *unbiased* — in expectation, the gradient estimate ∇_θ log π_θ(a_t|s_t) · G_t points in the correct direction of steepest ascent for J(θ). The problem with REINFORCE is not bias but *high variance*: G_t depends on everything that happens after time t, and a single trajectory is a noisy sample of the expected return. This variance makes learning slow and unstable. The actor-critic remedy — subtracting a value baseline — reduces variance without introducing bias, because the expected value of a state-dependent baseline multiplied by the log-gradient is zero."

- question: "Subtracting a learned value baseline V(s_t) from the return G_t in a policy gradient update reduces variance in the gradient estimate without changing the expected (average) direction of the update."
  type: true-false
  answer: true
  explanation: "This is a key theoretical property of baselines. The expected value of ∇_θ log π_θ(a_t|s_t) · b(s_t) is zero for any function b that depends only on the state (not the action), because E[∇_θ log π_θ(a|s)] = 0 by the log-derivative trick and normalization of the policy. Therefore, subtracting b(s_t) = V(s_t) from G_t leaves the expected gradient unchanged — no bias is introduced. But the variance is reduced because the advantage A_t = G_t − V(s_t) has smaller fluctuations than G_t alone: the baseline absorbs the 'background level' of return, leaving only the surprising component."

- question: "Explain in your own words what the advantage A_t = G_t − V(s_t) measures, and why using it instead of the raw return G_t makes policy gradient updates more informative and stable."
  type: short-answer
  answer: "The advantage measures how much better (or worse) the actual return from action a_t was compared to what the agent would typically expect from state s_t. A positive advantage means a_t led to a better-than-average outcome; a negative advantage means it led to a worse-than-average outcome. Using raw G_t is noisy because even mediocre actions get large positive updates in high-reward environments. The advantage centers the signal: an action that achieves the expected return gets nearly zero update, while only surprisingly good or bad actions produce strong updates. This reduces variance in the gradient estimate, leading to more stable and efficient learning — the policy changes meaningfully only when an action is genuinely above or below expectations."
  explanation: "The advantage concept also reveals why the actor-critic architecture is powerful: the critic learns the value function V(s) from experience, essentially building a model of 'what's normal' for each state, which the actor then uses to calibrate whether its actions are exceptional. The separation of policy (actor) from value function (critic) — two different neural networks with different objectives — is central to most modern deep RL algorithms including PPO and A3C."
```

## Explainer

Most reinforcement learning methods you have seen so far work by estimating value functions — figuring out how good each state or action is, then deriving a policy indirectly by picking the highest-value action. Policy gradient methods take a fundamentally different approach: they **parameterize the policy directly** as a function π_θ(a|s) and optimize its parameters θ to maximize expected return. Instead of asking "what is the value of this action?" and choosing the best one, they ask "how should I adjust the probability of each action to get more reward?"

This direct approach solves a problem that value-based methods struggle with: **continuous action spaces**. If your agent controls a robotic arm with joint torques that can take any real-valued number, you cannot enumerate all possible actions to find the one with the highest Q-value. But a parameterized policy can output a probability distribution over continuous actions — for instance, a Gaussian with a learned mean and variance — and gradient ascent smoothly adjusts these parameters. Your background in gradient descent and partial derivatives applies directly here, except you are ascending (maximizing) the expected return J(θ) rather than descending a loss.

The key theoretical result is the **policy gradient theorem**, which gives a tractable expression for ∇_θ J(θ). The simplest algorithm built on it is **REINFORCE**: run a full episode under the current policy, compute the return G_t from each time step, and update θ in the direction of ∇_θ log π_θ(a_t|s_t) · G_t. Intuitively, this increases the probability of actions that led to high returns and decreases the probability of actions that led to low returns. The log-probability gradient tells you which direction in parameter space makes the chosen action more likely; the return G_t scales how strongly you push. REINFORCE is simple and unbiased, but it suffers from high variance because G_t depends on everything that happens after time t.

The standard remedy is to subtract a **baseline** from the return — typically a learned value function V(s_t). The quantity A_t = G_t − V(s_t) is called the **advantage**: it measures how much better the actual return was compared to the expected return from that state. If an action achieves average performance, its advantage is near zero and the policy barely changes. Only actions that perform surprisingly well or surprisingly poorly produce large updates. This is the **actor-critic** architecture: the "actor" is the policy π_θ, and the "critic" is the value function V that provides the baseline. The critic reduces variance without introducing bias (since subtracting a state-dependent baseline does not change the expected gradient), making learning significantly more stable and sample-efficient than raw REINFORCE.
