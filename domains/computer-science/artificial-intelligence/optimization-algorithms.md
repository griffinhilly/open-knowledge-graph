---
id: optimization-algorithms
title: 'Optimization Algorithms: SGD, Adam, RMSprop'
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: gradient-descent-optimization
  type: hard
- id: stochastic-gradient-descent
  type: hard
- id: partial-derivatives
  type: soft
- id: critical-points-extrema
  type: soft
builds-toward:
- training-neural-networks
- hyperparameter-optimization
tags:
- optimization
- gradient
- adam
- rmsprop
stage: advanced
status: draft
---

# Optimization Algorithms: SGD, Adam, RMSprop

## Core Idea
Modern optimizers like Adam and RMSprop adapt learning rates per parameter using gradient history, improving convergence over vanilla SGD. Adam (Adaptive Moment Estimation) combines momentum and RMSprop, making it robust across diverse problems. Optimizer choice affects convergence speed and stability, though learning rate scheduling may be necessary regardless.

## Explainer

You already understand that stochastic gradient descent updates parameters by stepping in the direction opposite to the gradient, scaled by a learning rate. The problem is that a single fixed learning rate rarely works well across all parameters. Some parameters may have steep, well-defined gradients and converge quickly, while others sit on flat plateaus where the gradient is tiny and progress is glacially slow. Worse, the loss landscape often has different curvatures in different directions — narrow ravines where the gradient oscillates wildly along one axis while barely moving along the perpendicular one. The family of **adaptive optimizers** solves this by giving each parameter its own effective learning rate, automatically tuned from gradient history.

**SGD with momentum** is the first step beyond vanilla SGD. Instead of using only the current gradient, it maintains a **running average of past gradients** (the "velocity") and uses that to update parameters. This smooths out noisy oscillations and accelerates movement through flat regions — like a ball rolling downhill that accumulates speed. Mathematically, the velocity v is updated as v ← βv + (1 − β)∇L, and then parameters are updated by θ ← θ − α·v, where β (typically 0.9) controls how much history to keep. Momentum solves the oscillation problem but still uses a single learning rate α for every parameter.

**RMSprop** (Root Mean Square Propagation) takes a different approach. Instead of accumulating gradient direction, it tracks the **magnitude** of recent gradients for each parameter using an exponential moving average of squared gradients. Parameters whose gradients have been consistently large get their learning rate reduced; parameters with small gradients get a boost. The update divides the gradient by the square root of this running average: θ ← θ − (α / √(E[g²] + ε)) · g. This per-parameter scaling means the optimizer automatically adapts to the local curvature of the loss surface — steep directions get dampened, flat directions get amplified.

**Adam** (Adaptive Moment Estimation) combines both ideas. It maintains two running averages: the **first moment** (mean of gradients, like momentum) and the **second moment** (mean of squared gradients, like RMSprop). It also applies **bias correction** to account for the fact that these running averages start at zero and are initially biased toward smaller values. The result is an optimizer that both accelerates through flat regions (momentum) and adapts step sizes per parameter (RMSprop), with the bias correction ensuring stable behavior in early training. Adam's default hyperparameters (β₁ = 0.9, β₂ = 0.999, ε = 10⁻⁸) work well across a remarkably wide range of problems, which is why it has become the default choice for training neural networks. However, Adam can sometimes generalize worse than well-tuned SGD with momentum, and variants like **AdamW** (which decouples weight decay from the adaptive update) address some of these shortcomings.
