---
id: multilayer-perceptrons
title: Multilayer Perceptrons (MLPs)
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: neural-networks-intro
  type: hard
- id: backpropagation
  type: hard
- id: matrix-multiplication
  type: soft
- id: vectors-in-rn
  type: soft
builds-toward:
- vanishing-gradient-problem
tags:
- neural-networks
- deep-learning
- supervised-learning
- universal-approximation
stage: advanced
status: draft
---

# Multilayer Perceptrons (MLPs)

## Core Idea
Multilayer perceptrons stack fully-connected layers with nonlinear activations (ReLU, tanh, sigmoid) to learn complex nonlinear functions. The universal approximation theorem guarantees that MLPs with one hidden layer can approximate any continuous function, but deep networks learn hierarchical features more efficiently and require fewer parameters than shallow networks.

## How It's Best Learned
Train MLPs on XOR and other nonlinear problems to understand why hidden layers are necessary, then observe how depth affects learning efficiency.
