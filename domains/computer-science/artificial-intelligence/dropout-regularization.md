---
id: dropout-regularization
title: Dropout Regularization
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: regularization-techniques
  type: hard
- id: neural-networks-intro
  type: hard
tags:
- regularization
- overfitting-prevention
- ensemble-methods
- model-averaging
stage: advanced
status: draft
---

# Dropout Regularization

## Core Idea
Dropout randomly disables (zeros) a fraction of neurons during training, forcing the network to learn redundant and distributed representations while preventing co-adaptation of neurons. This approximates an ensemble of exponentially many thinned networks and effectively reduces overfitting, especially in large networks; at test time, all neurons are active but weights are scaled to account for training dropout.
