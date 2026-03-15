---
id: backpropagation
title: Backpropagation Algorithm
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: neural-networks-intro
  type: hard
- id: chain-rule-multivariable
  type: hard
- id: chain-rule
  type: soft
- id: partial-derivatives
  type: soft
tags:
- neural-networks
- training-algorithms
- gradient-computation
stage: advanced
status: draft
---

# Backpropagation Algorithm

## Core Idea
Backpropagation computes gradients efficiently via the chain rule in two phases: forward pass computes activations, backward pass propagates error signals layer-by-layer. Complexity is O(n) for n parameters, enabling large-scale neural network training.

## How It's Best Learned
Implement backpropagation from scratch, deriving gradients by hand and verifying with numerical gradients.

## Common Misconceptions
Backpropagation applies to any differentiable computation, not just neural networks. Vanishing/exploding gradients require normalization techniques.
