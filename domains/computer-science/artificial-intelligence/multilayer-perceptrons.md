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

## Explainer

From your study of basic neural networks and backpropagation, you know that a single neuron computes a weighted sum of its inputs, adds a bias, and passes the result through an activation function. A single layer of such neurons can only learn linear decision boundaries — it literally draws straight lines (or hyperplanes) through the input space. The XOR problem is the classic demonstration of this limitation: no single straight line can separate the inputs (0,0) and (1,1) from (0,1) and (1,0). A **multilayer perceptron** solves this by stacking layers, where the output of one layer becomes the input to the next.

The key insight is what happens in the **hidden layers** — the layers between input and output. Each neuron in a hidden layer applies a **nonlinear activation function** (such as ReLU, which outputs zero for negative inputs and the input itself for positive ones, or sigmoid, which squashes values to the range 0–1). Without nonlinearity, stacking layers would be pointless: a composition of linear functions is still linear, so ten layers would have no more representational power than one. The nonlinearity allows each layer to carve the input space into increasingly complex regions. The first hidden layer might learn simple features (edges in an image, individual word patterns in text), and subsequent layers combine those features into higher-level abstractions (shapes, phrases, objects).

The **universal approximation theorem** guarantees that an MLP with even a single hidden layer containing enough neurons can approximate any continuous function to arbitrary precision. This sounds like depth is unnecessary, but "enough neurons" can mean an astronomically large number. In practice, **deep networks** — those with multiple hidden layers — learn the same functions with far fewer total parameters because they compose simple features hierarchically. Think of it like building with LEGO: you could theoretically construct any shape from a single layer of tiny bricks laid flat, but it is vastly more efficient to stack layers and build upward. Each layer of a deep MLP reuses features learned by the previous layer rather than learning everything from scratch.

Training an MLP means using backpropagation to compute how much each weight contributed to the error, then adjusting weights via gradient descent. The matrix multiplication you know from linear algebra is central here: the forward pass through each layer is a matrix-vector product (weights times inputs) followed by the activation function, and the backward pass propagates gradients through the transpose of those same weight matrices. The architecture choices — how many hidden layers, how many neurons per layer, which activation function — determine the network's capacity and training dynamics. Too few neurons and the network underfits; too many and it may overfit or become difficult to train, which connects directly to challenges like the vanishing gradient problem you will encounter next.
