---
id: multi-task-learning
title: Multi-Task Learning
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: neural-networks-intro
  type: hard
- id: supervised-learning-intro
  type: hard
builds-toward:
- transfer-learning-neural
- representation-learning
tags:
- multi-task
- shared-representation
- auxiliary
stage: advanced
status: draft
---

# Multi-Task Learning

## Core Idea
Multi-task learning trains a single model on multiple related tasks simultaneously, sharing intermediate representations. Shared layers learn generalizable features beneficial to all tasks, improving generalization and reducing overfitting. Task weighting balances conflicting objectives across different prediction targets.
