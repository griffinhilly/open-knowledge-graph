---
id: generative-adversarial-networks
title: Generative Adversarial Networks
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: neural-networks-intro
  type: hard
- id: probability-basics
  type: soft
- id: probability-distributions
  type: soft
- id: probability-axioms
  type: soft
- id: optimization-multivariable-basics
  type: soft
- id: optimization-problems
  type: hard
- id: probability-density-functions
  type: soft
- id: probability-density-functions-theory
  type: soft
tags:
- deep-learning
- generative-models
- adversarial
stage: advanced
status: draft
---

# Generative Adversarial Networks

## Core Idea
GANs train a generator creating data and discriminator classifying real vs. generated samples in adversarial competition. Generator minimizes discriminator's accuracy; discriminator maximizes it. Training is unstable but produces realistic samples at equilibrium.

## How It's Best Learned
Implement a simple GAN on MNIST, observing mode collapse and experimenting with loss variations.

## Common Misconceptions
GANs do not reliably produce high-quality samples; mode collapse is common. Discriminator loss alone does not indicate sample quality.

## Explainer

From neural networks, you know how to train a model to map inputs to outputs by minimizing a loss function. From probability and optimization, you know that distributions can be complex and high-dimensional. **Generative adversarial networks** combine these ideas in a surprising way: instead of training one network to solve a task, you train two networks that compete against each other, and the byproduct of their competition is a generator capable of producing realistic synthetic data.

The **generator** G takes random noise z sampled from a simple distribution (typically a multivariate Gaussian) and transforms it through a neural network into a synthetic data sample — an image, audio clip, or any structured output. The **discriminator** D is a separate neural network that receives either a real sample from the training set or a fake sample from G and outputs a probability that the input is real. Training alternates between two steps: first, update D to better distinguish real from fake (maximizing its classification accuracy); then, update G to better fool D (minimizing D's ability to tell the difference). Formally, this is a **minimax game**: G minimizes and D maximizes the objective V(D, G) = E[log D(x)] + E[log(1 − D(G(z)))]. At the theoretical optimum, G produces samples indistinguishable from real data, and D outputs 0.5 for everything — it literally cannot tell the difference.

The elegance of this framework is that it requires no explicit density estimation. Unlike variational autoencoders, which learn an approximate posterior, or normalizing flows, which construct invertible transformations, GANs learn to sample from the data distribution implicitly. The generator never sees the training data directly — it only receives gradient signals from the discriminator telling it how to adjust its output to be more convincing. This indirect learning is both a strength (it can model very complex distributions without restrictive assumptions) and a weakness (training dynamics are notoriously unstable).

The most common failure mode is **mode collapse**, where the generator learns to produce only a small subset of the possible outputs. For example, a GAN trained on handwritten digits might produce excellent 7s and 3s but never generate a 9. This happens because the generator finds a few outputs that reliably fool the discriminator and over-exploits them rather than exploring the full diversity of the data distribution. Training instability more broadly manifests as oscillations where G and D chase each other without converging, or as vanishing gradients when D becomes too strong and G receives no useful learning signal. Practical remedies include Wasserstein loss (which provides smoother gradients), spectral normalization (which stabilizes discriminator training), progressive growing (which starts with low-resolution images and gradually increases detail), and careful hyperparameter tuning of learning rates and update ratios. Despite these challenges, GANs have produced some of the most visually striking results in generative modeling, from photorealistic face synthesis to style transfer and image super-resolution.
