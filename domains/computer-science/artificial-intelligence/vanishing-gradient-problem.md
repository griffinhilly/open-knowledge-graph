---
id: vanishing-gradient-problem
title: Vanishing Gradient Problem
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: backpropagation
  type: hard
- id: multilayer-perceptrons
  type: hard
builds-toward:
- batch-normalization
- lstm-gated-networks
tags:
- training-dynamics
- deep-networks
- optimization
- gradient-flow
stage: advanced
status: draft
---

# Vanishing Gradient Problem

## Core Idea
During backpropagation, gradients multiply across layers; with saturating activation functions like sigmoid, gradients near zero cause deep layers to learn very slowly (vanishing gradients) or gradients can grow uncontrollably (exploding gradients). Solutions include careful weight initialization (Xavier, He initialization), gradient clipping, non-saturating activations (ReLU), and architectural innovations like skip connections and gating mechanisms.

## How It's Best Learned
Train deep networks with sigmoid activations and observe layer-wise gradient magnitudes, then compare with ReLU networks to see how activation choice affects gradient flow.
