---
id: policy-networks-neural
title: Policy Networks and Policy Gradients
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: policy-gradient-methods
  type: hard
- id: neural-networks-intro
  type: hard
builds-toward:
- actor-critic-methods
tags:
- reinforcement-learning
- policy-based
- actor-methods
- policy-gradient
stage: advanced
status: validated
---

# Policy Networks and Policy Gradients

## Core Idea
Policy networks directly parameterize the policy π(a|s) using a neural network, enabling learning for continuous action spaces and stochastic policies. Policy gradient algorithms estimate policy parameter gradients using trajectory samples; the REINFORCE algorithm uses returns, while more sophisticated methods reduce variance through baselines and advantage functions.

## How It's Best Learned
Implement REINFORCE and train a policy network on a continuous control task, then add a baseline to reduce variance and observe faster convergence.

## Questions

```yaml
- question: "An agent using REINFORCE takes a mediocre action in a given state, but the rest of the episode happens to go very well (due to luck), resulting in a high return. What does the unmodified REINFORCE algorithm do, and why is this a problem?"
  type: multiple-choice
  options:
    - "It correctly ignores the high return because it knows the initial action was mediocre"
    - "It strongly reinforces the mediocre action because it scales the gradient update by the high return, regardless of whether the action deserved credit"
    - "It skips the update for that episode because the variance is too high"
    - "It penalizes the action because the return was unusually high compared to the baseline"
  answer: 1
  explanation: "REINFORCE scales the log-probability gradient by the raw episode return Gₜ. It has no way to distinguish whether the high return resulted from the action taken or from lucky subsequent events — it simply reinforces whatever action was taken, in proportion to the total return. This is the variance problem: returns from individual episodes are noisy estimators of an action's true value. A mediocre action that happens to precede a lucky sequence gets reinforced as if it were excellent, slowing and destabilizing learning. A baseline that estimates the expected return from that state provides a reference point so only actions that beat expectations get reinforced."

- question: "In REINFORCE with a baseline, the policy gradient is scaled by (Gₜ − b(sₜ)) instead of Gₜ. What does this change accomplish, and what property makes it mathematically valid?"
  type: multiple-choice
  options:
    - "It biases the gradient toward higher returns, making the algorithm converge faster at the cost of accuracy"
    - "It eliminates variance entirely by normalizing all returns to zero mean"
    - "It reduces variance while keeping the gradient estimate unbiased, because the expected value of a state-dependent baseline over all actions is zero"
    - "It converts the policy gradient into a value-based update, making the algorithm equivalent to Q-learning"
  answer: 2
  explanation: "The mathematical key is that Eₐ[∇θ log π(a|s; θ) × b(s)] = b(s) × ∇θ Eₐ[log π(a|s; θ)] = b(s) × 0 = 0, because log-probabilities over all actions sum to zero in expectation. This means subtracting any state-dependent baseline leaves the expected gradient unchanged — the estimate is still unbiased. But individual samples now compare each action against b(s), dramatically reducing the variance of the estimate. The quantity Gₜ − b(sₜ) is the 'advantage' — positive when this action was better than expected, negative when worse — which is a much lower-variance signal than the raw return."

- question: "Subtracting a state-dependent baseline from the return in REINFORCE introduces bias into the policy gradient estimate."
  type: true-false
  answer: false
  explanation: "This is the central mathematical insight of the baseline technique. A state-dependent baseline b(sₜ) does not bias the gradient because, in expectation over actions, the baseline term cancels out. The expected gradient with the baseline is identical to the expected gradient without it. What changes is the variance — individual gradient estimates become much lower-variance because actions are now scored relative to what was expected in that state, not by their absolute returns. An unbiased, lower-variance estimator is strictly better for learning."

- question: "Policy networks are better suited than value-based methods (like Q-learning) for tasks with continuous action spaces."
  type: true-false
  answer: true
  explanation: "Value-based methods like Q-learning require computing or approximating Q(s, a) for all actions, then selecting the action that maximizes this value. In continuous action spaces, that maximization over infinitely many actions is generally intractable. Policy networks sidestep this by directly outputting a probability distribution over actions — for instance, the mean and variance of a Gaussian for continuous control — and can be trained purely through gradient ascent on expected return. This makes policy-based methods the natural choice for robotics, locomotion, and any domain where the action space cannot be discretized without losing important precision."

- question: "Why does the REINFORCE algorithm suffer from high variance, and how does introducing an advantage function (return minus baseline) address this problem?"
  type: short-answer
  answer: "REINFORCE is high-variance because each gradient update uses the full episode return, which conflates the quality of the specific action taken with all subsequent luck and chance outcomes. A single episode's return is a noisy sample of the true expected return, and this noise directly scales the gradient update. The advantage function (Gₜ − b(sₜ)) addresses this by comparing the actual return to an estimate of what was expected from that state. If b(sₜ) ≈ V(sₜ), then the advantage is near zero on average and varies only with whether the specific action was better or worse than average — a much lower-variance signal that isolates the true contribution of the action."
  explanation: "The key insight is that raw returns measure everything that happened in an episode, while advantages measure only whether this particular action made things better or worse than expected. The latter is what you actually want to learn from, and it can be estimated with far less noise. This is why virtually every practical policy gradient method uses some form of advantage estimation rather than raw returns."
```

## Explainer

From your work on policy gradient methods, you know the core idea: adjust the policy parameters so that actions leading to higher returns become more probable. From neural networks, you know how to build flexible function approximators that map inputs to outputs through layers of learned transformations. A **policy network** combines these two ideas — it is a neural network that takes a state as input and outputs a probability distribution over actions, directly representing the policy π(a|s; θ) where θ are the network weights.

The simplest policy gradient algorithm is **REINFORCE**. After the agent completes an episode, REINFORCE computes the return (cumulative discounted reward) for each time step, then updates the network weights to make actions with higher returns more likely. The gradient has an intuitive form: ∇θ log π(aₜ|sₜ; θ) × Gₜ. The log-probability gradient points in the direction that would increase the probability of action aₜ, and the return Gₜ scales how far you step in that direction. Good actions get reinforced; bad actions get suppressed. Because the network outputs a full probability distribution — perhaps a softmax over discrete actions or the parameters of a Gaussian for continuous actions — this approach naturally handles stochastic policies and continuous action spaces that value-based methods struggle with.

The central challenge with REINFORCE is **high variance**. Returns from individual episodes fluctuate wildly — a lucky rollout might give a high return to a mediocre action, and an unlucky one might penalize a good action. This noise makes learning slow and unstable. The standard fix is to subtract a **baseline** from the return: instead of scaling the gradient by Gₜ, you scale by Gₜ − b(sₜ), where b is an estimate of the expected return from state sₜ. This does not change the expected gradient (the math works out to be unbiased) but dramatically reduces variance. The quantity Gₜ − b(sₜ) is called the **advantage** — it tells you whether this action was better or worse than average for this state, which is a much cleaner learning signal than the raw return.

In practice, the baseline is often a separate neural network — a value network V(s; φ) — trained alongside the policy network. This leads naturally to actor-critic architectures, where the "actor" (policy network) decides what to do and the "critic" (value network) evaluates how good the decision was. Policy networks have proven essential for complex control tasks — robotic locomotion, game playing, and any domain where the action space is continuous or the optimal behavior is inherently stochastic. Their ability to directly optimize the quantity you care about (expected return) without needing to enumerate all possible actions makes them a cornerstone of modern reinforcement learning.
