---
id: expectation-maximization
title: Expectation-Maximization Algorithm
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: probabilistic-graphical-models
  type: hard
- id: hidden-markov-models
  type: soft
builds-toward:
- mixture-models
- latent-variable-models
tags:
- em
- expectation-maximization
- latent
stage: advanced
status: draft
---

# Expectation-Maximization Algorithm

## Core Idea
The EM algorithm iteratively estimates parameters of models with latent (unobserved) variables. The E-step computes expected latent values given current parameters; the M-step optimizes parameters given expected latents. EM guarantees monotonic likelihood improvement and is widely used for clustering, mixture models, and HMM training.
