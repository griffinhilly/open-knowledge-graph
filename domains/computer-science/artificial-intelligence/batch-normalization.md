---
id: batch-normalization
title: Batch Normalization
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: backpropagation
  type: hard
- id: stochastic-gradient-descent
  type: hard
tags:
- normalization
- regularization
- training-acceleration
- internal-covariate-shift
stage: advanced
status: draft
---

# Batch Normalization

## Core Idea
Batch normalization normalizes layer inputs to have zero mean and unit variance within a minibatch, accelerating training and reducing sensitivity to weight initialization. It acts as a regularizer (reduces overfitting), smooths the loss landscape enabling higher learning rates, though batch statistics during training differ from population statistics during inference, requiring different behavior at test time.

## How It's Best Learned
Train deep networks with and without batch normalization and observe differences in training speed, final accuracy, and insensitivity to initialization.
