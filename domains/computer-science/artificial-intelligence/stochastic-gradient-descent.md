---
id: stochastic-gradient-descent
title: Stochastic Gradient Descent and Variants
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: gradient-descent-optimization
  type: hard
- id: partial-derivatives
  type: soft
- id: probability
  type: soft
tags:
- optimization
- learning-algorithms
stage: advanced
status: draft
---

# Stochastic Gradient Descent and Variants

## Core Idea
SGD updates parameters using single examples or small batches instead of full datasets, enabling online learning and large-scale training. Mini-batch SGD balances gradient quality and efficiency. Momentum, Adam, and adaptive methods adjust learning rates per parameter.

## Explainer

Standard gradient descent computes the gradient of the loss function over the entire training set before making a single parameter update. You know from your study of gradient descent that this gives you the true gradient direction — the steepest downhill path on the loss surface. But when your dataset has millions of examples, computing the full gradient for every single step is prohibitively expensive. **Stochastic gradient descent** makes a simple trade: instead of computing the exact gradient, estimate it from a single randomly sampled training example (or a small **mini-batch** of examples) and update immediately. Each individual estimate is noisy — it might point somewhat away from the true gradient direction — but on average across many updates, it points the right way.

This noise is not purely a disadvantage. The stochastic fluctuations help SGD escape shallow local minima and saddle points that would trap full-batch gradient descent. Think of it like navigating a hilly landscape in fog: full-batch descent carefully computes the exact slope and walks precisely downhill, but it might get stuck in a small depression. SGD stumbles around more randomly, but that stumbling can bounce it out of shallow traps and toward deeper, more robust valleys. In practice, **mini-batch SGD** — using batches of 32 to 512 examples — strikes the best balance. The batch is large enough to smooth out the wildest noise and exploit GPU parallelism, but small enough to retain the regularizing benefit of stochasticity and allow many updates per pass through the data.

The learning rate is the most critical hyperparameter. Too large, and the updates overshoot, causing the loss to diverge. Too small, and convergence is painfully slow. **Momentum** addresses a related problem: in narrow valleys of the loss landscape, vanilla SGD oscillates back and forth across the valley while making slow progress along it. Momentum adds a velocity term — each update accumulates a fraction of previous gradients, smoothing the trajectory. It is analogous to a ball rolling downhill that builds speed in consistent directions and dampens oscillations in inconsistent ones.

**Adaptive methods** like AdaGrad, RMSProp, and **Adam** take this further by maintaining separate learning rates for each parameter. Parameters with consistently large gradients get smaller effective learning rates (preventing overshooting), while parameters with small or infrequent gradients get larger ones (accelerating learning in flat directions). Adam combines momentum with per-parameter rate adaptation and includes bias corrections for the early training steps. It has become the default optimizer in deep learning because it is robust across a wide range of architectures and hyperparameter settings — though for some tasks, well-tuned SGD with momentum still achieves better final performance, trading convenience for a slight edge in generalization.
