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
- id: genetic-algorithms
  type: soft
- id: loss-functions
  type: hard
builds-toward:
- backpropagation
- hyperparameter-optimization
tags:
- optimization
- gradient
- adam
- rmsprop
stage: advanced
status: validated
---
# Optimization Algorithms: SGD, Adam, RMSprop

## Core Idea
Modern optimizers like Adam and RMSprop adapt learning rates per parameter using gradient history, improving convergence over vanilla SGD. Adam (Adaptive Moment Estimation) combines momentum and RMSprop, making it robust across diverse problems. Optimizer choice affects convergence speed and stability, though learning rate scheduling may be necessary regardless.

## Questions

```yaml
- question: "A team trains a deep neural network with Adam and achieves fast training convergence but poor generalization to the test set. Switching to well-tuned SGD with momentum achieves similar training loss but significantly better test accuracy. What best explains this pattern?"
  type: multiple-choice
  options:
    - "Adam is fundamentally broken for deep learning and should be replaced in all cases"
    - "Adam's per-parameter adaptive learning rates can converge to sharp minima that interpolate the training data but generalize poorly; SGD with momentum may find flatter minima that generalize better"
    - "Adam uses too much memory, corrupting gradient estimates and causing poor generalization"
    - "SGD with momentum escapes local minima more easily because it lacks adaptive learning rates"
  answer: 1
  explanation: "Adam's adaptive scaling can cause it to converge to sharp minima in the loss landscape — regions with narrow, steep valleys that fit training data well but generalize poorly. SGD with momentum, despite being slower to converge, can find flatter minima associated with better generalization. This is a known empirical pattern and motivates AdamW (Adam with decoupled weight decay) and learning rate schedules as partial remedies."

- question: "What specific problem does RMSprop solve that vanilla SGD with momentum does not?"
  type: multiple-choice
  options:
    - "Oscillation caused by the learning rate being too high in all parameter directions simultaneously"
    - "Different parameters having vastly different gradient magnitudes, so a single learning rate is too large for some and too small for others"
    - "The inability of gradient descent to escape saddle points in the loss landscape"
    - "The computational cost of computing full-batch gradients on large datasets"
  answer: 1
  explanation: "RMSprop tracks the running average of squared gradients per parameter. Parameters whose gradients are consistently large get their effective learning rate divided by a large number (dampened); parameters whose gradients are small get their learning rate scaled up. This per-parameter adaptation solves the problem of heterogeneous gradient scales that a single global learning rate cannot handle. Momentum addresses a different problem: smoothing noisy gradient direction."

- question: "Adam's bias correction step is necessary because the first and second moment estimates are initialized at zero and would underestimate true gradient statistics early in training without it."
  type: true-false
  answer: true
  explanation: "The exponential moving averages for m (first moment) and v (second moment) start at 0. Early in training, when relatively few gradient steps have been taken, these averages are biased toward zero regardless of actual gradient magnitudes. Bias correction divides each estimate by (1 − β^t), where t is the time step, scaling the estimates upward to remove this initialization bias and ensuring numerically stable step sizes from the first iteration."

- question: "Because Adam adapts the learning rate individually for each parameter, the global learning rate hyperparameter α becomes irrelevant and does not need to be tuned."
  type: true-false
  answer: false
  explanation: "Adam adapts learning rates per-parameter by dividing the global step by a parameter-specific scale factor, but the global learning rate α still multiplies the final update. It remains the most important hyperparameter to tune — the adaptive mechanism makes Adam less sensitive to α than vanilla SGD, but the right order of magnitude still matters significantly for convergence speed and final solution quality."

- question: "Explain how Adam combines the properties of SGD with momentum and RMSprop, and what problem each component solves."
  type: short-answer
  answer: "SGD with momentum maintains a running average of past gradients (first moment), which smooths noisy gradient direction and accelerates movement through flat regions of the loss landscape. RMSprop tracks the running average of squared gradient magnitudes (second moment) to scale each parameter's learning rate by its recent gradient size — large gradients get dampened, small gradients get amplified. Adam combines both: the first moment provides directional inertia, the second moment provides per-parameter scaling, and bias correction ensures both estimates are accurate early in training when the running averages would otherwise be biased toward zero."
  explanation: "The combination makes Adam robust: it is fast through flat regions (momentum), adapts to curvature per parameter (adaptive scaling), and is stable from the first step (bias correction). Its default hyperparameters (β₁=0.9, β₂=0.999, ε=10⁻⁸) work acceptably across diverse problems, which is why it became the default optimizer for neural network training."
```

## Explainer

You already understand that stochastic gradient descent updates parameters by stepping in the direction opposite to the gradient, scaled by a learning rate. The problem is that a single fixed learning rate rarely works well across all parameters. Some parameters may have steep, well-defined gradients and converge quickly, while others sit on flat plateaus where the gradient is tiny and progress is glacially slow. Worse, the loss landscape often has different curvatures in different directions — narrow ravines where the gradient oscillates wildly along one axis while barely moving along the perpendicular one. The family of **adaptive optimizers** solves this by giving each parameter its own effective learning rate, automatically tuned from gradient history.

**SGD with momentum** is the first step beyond vanilla SGD. Instead of using only the current gradient, it maintains a **running average of past gradients** (the "velocity") and uses that to update parameters. This smooths out noisy oscillations and accelerates movement through flat regions — like a ball rolling downhill that accumulates speed. Mathematically, the velocity v is updated as v ← βv + (1 − β)∇L, and then parameters are updated by θ ← θ − α·v, where β (typically 0.9) controls how much history to keep. Momentum solves the oscillation problem but still uses a single learning rate α for every parameter.

**RMSprop** (Root Mean Square Propagation) takes a different approach. Instead of accumulating gradient direction, it tracks the **magnitude** of recent gradients for each parameter using an exponential moving average of squared gradients. Parameters whose gradients have been consistently large get their learning rate reduced; parameters with small gradients get a boost. The update divides the gradient by the square root of this running average: θ ← θ − (α / √(E[g²] + ε)) · g. This per-parameter scaling means the optimizer automatically adapts to the local curvature of the loss surface — steep directions get dampened, flat directions get amplified.

**Adam** (Adaptive Moment Estimation) combines both ideas. It maintains two running averages: the **first moment** (mean of gradients, like momentum) and the **second moment** (mean of squared gradients, like RMSprop). It also applies **bias correction** to account for the fact that these running averages start at zero and are initially biased toward smaller values. The result is an optimizer that both accelerates through flat regions (momentum) and adapts step sizes per parameter (RMSprop), with the bias correction ensuring stable behavior in early training. Adam's default hyperparameters (β₁ = 0.9, β₂ = 0.999, ε = 10⁻⁸) work well across a remarkably wide range of problems, which is why it has become the default choice for training neural networks. However, Adam can sometimes generalize worse than well-tuned SGD with momentum, and variants like **AdamW** (which decouples weight decay from the adaptive update) address some of these shortcomings.
