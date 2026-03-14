---
id: contrastive-learning
title: Contrastive Learning
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: self-supervised-learning
  type: hard
- id: representation-learning
  type: hard
builds-toward:
- metric-learning
- similarity-learning
tags:
- contrastive
- similarity
- representation
stage: advanced
status: draft
---

# Contrastive Learning

## Core Idea
Contrastive learning learns representations by contrasting similar (positive) and dissimilar (negative) pairs. Methods like SimCLR and MoCo maximize agreement between augmented views of the same instance. The key insight is that semantically similar data should have similar representations. This is powerful for self-supervised pretraining without labels.
