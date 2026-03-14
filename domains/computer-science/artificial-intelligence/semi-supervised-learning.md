---
id: semi-supervised-learning
title: Semi-Supervised Learning
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: supervised-learning-intro
  type: hard
builds-toward:
- self-supervised-learning
- pseudo-labeling
tags:
- semi-supervised
- unlabeled-data
- self-training
stage: advanced
status: draft
---

# Semi-Supervised Learning

## Core Idea
Semi-supervised learning leverages both labeled and abundant unlabeled data. Techniques include self-training (pseudo-labeling unlabeled data), consistency regularization (enforcing prediction invariance under perturbations), and co-training (multiple models train each other). This practical approach handles scenarios where labeling is expensive but unlabeled data is plentiful.
