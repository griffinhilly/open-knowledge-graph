---
id: data-augmentation
title: Data Augmentation Techniques
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: supervised-learning-intro
  type: hard
builds-toward:
- transfer-learning-neural
- neural-networks-intro
tags:
- augmentation
- synthetic-data
- regularization
stage: advanced
status: draft
---

# Data Augmentation Techniques

## Core Idea
Data augmentation generates synthetic training examples through domain-appropriate transformations (image rotations, text paraphrasing) without collecting new labels. This increases effective dataset size and improves robustness. Domain knowledge is critical: augmentations must preserve label semantics to avoid introducing noise.
