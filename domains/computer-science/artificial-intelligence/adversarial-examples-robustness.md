---
id: adversarial-examples-robustness
title: Adversarial Examples and Robustness
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: neural-networks-intro
  type: hard
- id: supervised-learning-intro
  type: hard
- id: ai-ethics-fairness-bias
  type: soft
tags:
- adversarial-ml
- robustness
- security
- perturbations
stage: advanced
status: draft
---

# Adversarial Examples and Robustness

## Core Idea
Adversarial examples are inputs crafted to fool neural networks, sometimes by adding imperceptible perturbations; they reveal model brittleness and exist in high-dimensional spaces due to model linearities and feature overfitting. Defenses include adversarial training (training on adversarial examples), certified defenses (provable robustness), and regularization, though robust models often sacrifice clean accuracy.

## How It's Best Learned
Generate adversarial examples using FGSM and PGD attacks on an image classifier, then implement adversarial training and observe robustness improvements and accuracy tradeoffs.
