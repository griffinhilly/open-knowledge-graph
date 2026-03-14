---
id: curriculum-learning
title: Curriculum Learning
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: neural-networks-intro
  type: hard
builds-toward:
- training-strategies
- sample-weighting
tags:
- curriculum
- difficulty-progression
- pacing
stage: advanced
status: draft
---

# Curriculum Learning

## Core Idea
Curriculum learning trains models on examples in meaningful difficulty progression, starting with easy instances and gradually introducing harder ones. This mirrors human learning and improves convergence speed and generalization. Difficulty can be based on training loss, distance to decision boundary, or domain expertise.
