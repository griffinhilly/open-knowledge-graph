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
- id: partial-derivatives
  type: soft
- id: optimization-problems
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

## Explainer

From supervised learning, you know that neural networks learn to map inputs to outputs by finding patterns in training data. A well-trained image classifier might achieve 95% accuracy on test images — but what happens if you take a correctly classified image of a panda and add a tiny, carefully computed perturbation that is invisible to the human eye? The network confidently classifies it as a gibbon. This perturbed input is an **adversarial example**, and its existence reveals something fundamental about how neural networks represent the world.

The key insight is that neural networks, despite their complexity, behave approximately linearly in high-dimensional spaces. Consider a network with input dimension d. Even a tiny perturbation ε applied to each input dimension can accumulate a total effect of ε × d on the output, which can be enormous when d is large (a 224×224 RGB image has d ≈ 150,000 dimensions). The **Fast Gradient Sign Method (FGSM)** exploits this directly: it computes the gradient of the loss with respect to each input pixel, then adds a small perturbation in the direction that maximizes the loss. Because you already understand partial derivatives and optimization, you can see that FGSM is simply one step of gradient ascent on the input space instead of gradient descent on the weight space. Stronger attacks like **Projected Gradient Descent (PGD)** iterate this process multiple times, staying within a small ε-ball around the original input.

Why do adversarial examples matter beyond academic curiosity? They expose a gap between human perception and machine perception. Humans classify images based on semantic features — shapes, textures, objects. Neural networks often rely on subtle statistical patterns in pixel values that happen to correlate with labels in the training data but have no semantic meaning. Adversarial perturbations exploit these brittle features. In safety-critical applications — self-driving cars, medical imaging, security systems — adversarial vulnerability is not just an inconvenience but a potential attack vector.

The primary defense is **adversarial training**: augmenting the training set with adversarial examples generated during training, so the model learns to classify them correctly. This forces the network to rely on more robust features, but it comes at a cost — adversarially trained models typically sacrifice a few percentage points of accuracy on clean (unperturbed) inputs. This robustness-accuracy tradeoff appears to be fundamental, not just a limitation of current methods. Other approaches include **certified defenses** that mathematically prove no perturbation within a given ε-ball can change the prediction, and input preprocessing techniques that attempt to remove perturbations before classification. The field remains an arms race: stronger attacks break existing defenses, motivating new defenses, which in turn face new attacks. The broader lesson is that high test accuracy does not imply genuine understanding, and robustness must be evaluated and engineered as a separate property.
