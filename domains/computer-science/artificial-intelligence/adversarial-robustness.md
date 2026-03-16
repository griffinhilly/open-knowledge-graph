---
id: adversarial-robustness
title: Adversarial Robustness and Certified Defenses
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: adversarial-examples-robustness
  type: hard
- id: neural-networks-intro
  type: hard
builds-toward:
- adversarial-training
- certified-defense
tags:
- adversarial
- robustness
- defense
stage: advanced
status: draft
---

# Adversarial Robustness and Certified Defenses

## Core Idea
Adversarial robustness measures resilience to adversarially-crafted inputs designed to fool models. Certified defenses mathematically guarantee robustness within perturbation budgets, unlike empirical defenses which may break under stronger attacks. Techniques include adversarial training, randomized smoothing, and provable bounds via interval analysis.

## Explainer

From your study of adversarial examples, you know that neural networks can be fooled by tiny, carefully crafted perturbations — an image of a panda plus an imperceptible noise pattern gets classified as a gibbon with high confidence. Adversarial robustness is the systematic study of how to defend against such attacks and, more importantly, how to prove that a defense actually works rather than just hoping it does.

The core challenge is the arms race between attacks and defenses. Early defenses like input preprocessing (blurring, JPEG compression) or defensive distillation appeared effective against known attacks but were quickly broken by adaptive adversaries who designed attacks specifically targeting those defenses. This pattern — defense proposed, defense broken — repeated so frequently that the field developed a deep skepticism toward **empirical defenses**, which are evaluated only by testing against specific attack algorithms. The problem is fundamental: showing that your model resists FGSM, PGD, and C&W attacks does not guarantee it resists the next attack someone invents.

**Adversarial training** directly incorporates adversarial examples into the training process. Instead of training on clean data alone, the model trains on a mix of clean and adversarially perturbed inputs, forcing it to learn features that are robust to small perturbations. The standard approach uses **PGD (Projected Gradient Descent)** to generate strong adversarial examples during each training step: for every training batch, compute the worst-case perturbation within an ε-ball around each input, then update the model to classify those worst-case inputs correctly. This is effective but expensive — training time increases by roughly an order of magnitude — and it tends to reduce clean accuracy somewhat, revealing a fundamental tension between standard and robust performance.

**Certified defenses** take a different approach entirely: rather than empirically testing against attacks, they provide mathematical guarantees. **Randomized smoothing** is the most scalable certified method. The idea is to create a smoothed classifier by averaging predictions over random Gaussian noise added to the input. If the base classifier consistently predicts class A when the input is jittered by Gaussian noise, then no adversarial perturbation within a computable radius can change the smoothed classifier's prediction. The guarantee follows from the geometry of Gaussian distributions, not from any assumption about the attacker's strategy. Other certified approaches use **interval bound propagation** or **abstract interpretation** to propagate sets of possible inputs through the network and verify that all inputs within the perturbation budget map to the same class.

The practical landscape involves tradeoffs along several axes. Certified defenses provide guarantees but currently certify robustness only for small perturbation radii — enough for imperceptible pixel changes but not for larger semantic perturbations. Adversarial training scales better but offers no formal guarantee. Both approaches sacrifice some clean accuracy. The perturbation model itself is a simplification: real-world attacks may involve rotations, color shifts, or physical-world perturbations (printed patches, 3D-printed objects) that don't fit neatly into an Lp-norm ball. As you continue to work with robustness, the key question shifts from "can I defend against this attack?" to "what threat model am I defending against, and can I verify my defense within that model?"
