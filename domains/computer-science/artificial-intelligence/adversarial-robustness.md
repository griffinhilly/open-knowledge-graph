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
