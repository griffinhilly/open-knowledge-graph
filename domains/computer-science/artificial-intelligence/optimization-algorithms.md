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
