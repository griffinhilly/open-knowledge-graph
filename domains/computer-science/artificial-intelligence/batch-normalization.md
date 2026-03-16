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
- id: mean-median-mode
  type: soft
- id: variance-of-random-variables
  type: soft
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

## Explainer

You already understand backpropagation and stochastic gradient descent — how gradients flow backward through a network and how parameters get updated in minibatch steps. You also know that the mean and variance describe the center and spread of a distribution. **Batch normalization** applies these statistical concepts directly inside the network: at each layer, it forces the inputs to have zero mean and unit variance across the current minibatch before passing them through the activation function. This seemingly simple operation has a dramatic effect on how deep networks train.

Here is the mechanics. For a given layer, batch normalization computes the mean μ and variance σ² of each feature across all examples in the minibatch. It then normalizes: x̂ = (x − μ) / √(σ² + ε), where ε is a small constant for numerical stability. But forcing zero mean and unit variance everywhere would severely limit what the network can represent — for instance, a sigmoid activation works best with inputs in a specific range, not always centered at zero. So batch normalization introduces two **learnable parameters per feature**: a scale γ and a shift β. The final output is y = γx̂ + β. If the network learns γ = σ and β = μ, it recovers the original unnormalized values. This means batch normalization can never hurt representational capacity — it gives the network the *option* to normalize while letting gradient descent decide how much normalization is actually helpful.

The practical benefits are substantial. Without batch normalization, each layer's input distribution shifts as the layers before it update their weights — a phenomenon originally called **internal covariate shift**. While recent research debates whether this is the true mechanism, the empirical effect is clear: batch normalization **smooths the loss landscape**, making it less sensitive to learning rate and initialization choices. You can use much larger learning rates (often 5–10x) without diverging, which directly accelerates convergence. It also acts as a mild **regularizer** because the normalization statistics from a minibatch are noisy estimates of the true population statistics, injecting randomness similar to dropout.

There is one critical subtlety: the difference between **training and inference behavior**. During training, batch normalization uses the minibatch mean and variance. During inference, you typically process one example at a time, so there is no minibatch to compute statistics from. The solution is to maintain **running averages** of the mean and variance during training (computed as exponential moving averages across minibatches) and use these fixed population statistics at test time. This train/test discrepancy can cause bugs if not handled correctly — for example, forgetting to switch the model to evaluation mode before inference, or using very small batch sizes during training where the batch statistics are poor estimates of the population. Understanding this dual behavior is essential to using batch normalization correctly in practice.
