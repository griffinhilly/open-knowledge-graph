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
- id: chain-rule
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

## Explainer

From your study of multilayer perceptrons, you know that a neural network is built from layers of neurons, each computing a weighted sum of its inputs plus a bias. Without activation functions, stacking layers would be pointless — a composition of linear transformations is just another linear transformation. No matter how many layers you add, the network could only learn linear decision boundaries. The **activation function** applied after each neuron's weighted sum is what breaks this linearity and gives deep networks their power to approximate arbitrarily complex functions.

The **sigmoid** function σ(x) = 1/(1 + e^(−x)) was the original workhorse activation. It squashes any input to the range (0, 1), which has a nice probabilistic interpretation and smooth gradients everywhere. The closely related **tanh** function maps inputs to (−1, 1), centering outputs around zero, which often helps training converge faster. However, both functions suffer from a critical problem: for large positive or negative inputs, the derivative approaches zero. During backpropagation, gradients get multiplied through many layers, and near-zero derivatives cause the gradient signal to vanish — the **vanishing gradient problem**. This makes deep networks with sigmoid or tanh very difficult to train, because early layers receive almost no learning signal.

The **Rectified Linear Unit (ReLU)**, defined as f(x) = max(0, x), solved this problem with elegant simplicity. For positive inputs, the derivative is exactly 1 — gradients flow through without shrinking, no matter how deep the network. For negative inputs, the output and derivative are both 0, which creates sparsity (many neurons output zero at any given time) and reduces computation. ReLU's combination of computational cheapness, gradient-friendly behavior, and empirical effectiveness made it the default choice for hidden layers in modern deep learning. Its main weakness is the **dying ReLU problem**: if a neuron's weights drift so that its input is always negative, it outputs zero for all inputs and can never recover. Variants like **Leaky ReLU** (which allows a small slope for negative inputs instead of zero) and **ELU** address this.

Choosing the right activation for the **output layer** is a separate decision driven by the task, not by gradient flow. For binary classification, a sigmoid output gives a probability between 0 and 1. For multi-class classification, **softmax** converts a vector of raw scores into a probability distribution that sums to 1. For regression, a linear (identity) activation is standard because the output should be an unconstrained real number. Getting the output activation wrong — say, using ReLU for regression where targets can be negative — silently clips your predictions and degrades performance without any obvious error message, making it one of the most common beginner mistakes in neural network design.
