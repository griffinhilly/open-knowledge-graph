---
id: activation-functions
title: Activation Functions in Neural Networks
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: neural-networks-intro
  type: hard
- id: multilayer-perceptrons
  type: hard
- id: derivatives-of-exponential-functions
  type: soft
- id: exponential-functions-and-graphs
  type: soft
builds-toward:
- deep-learning-foundations
- vanishing-gradient-problem
tags:
- activation
- nonlinearity
- neural-networks
stage: advanced
status: draft
---

# Activation Functions in Neural Networks

## Core Idea
Activation functions introduce nonlinearity into neural networks, enabling them to learn complex patterns beyond linear transformations. ReLU dominates modern networks for hidden layers due to computational efficiency and reduced vanishing gradient. Sigmoid and tanh are historically important. Output layer activation depends on task: softmax for multi-class, sigmoid for binary.
