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

## Explainer

In standard supervised learning, you train one model for one task: predict house prices, classify emails, detect objects. **Multi-task learning** (MTL) flips this assumption by training a single model on several related tasks at once, forcing the model's internal representations to be useful across all of them. The core insight is that related tasks share underlying structure, and learning that shared structure explicitly produces better features than any single task would discover alone.

The most common architecture is **hard parameter sharing**: the model has a shared trunk of layers (the backbone) that feeds into separate task-specific output heads. For example, a self-driving perception model might share convolutional layers and then branch into separate heads for lane detection, object classification, and depth estimation. The shared layers are forced to learn features that help all three tasks, acting as an implicit regularizer — the model cannot overfit to quirks of any single task because the shared weights must generalize. This is why MTL often improves performance even when you only care about one "main" task: the auxiliary tasks provide additional gradient signal that shapes better internal representations.

The key practical challenge is **task balancing**. Different tasks may have different loss scales, learning speeds, or even conflicting gradients. If one task dominates training — perhaps because its loss is numerically larger or its gradients are stronger — the shared layers become biased toward that task at the expense of others. Simple strategies include manually weighting each task's loss contribution, but more sophisticated approaches dynamically adjust weights during training based on each task's learning progress. The goal is to prevent any single task from hijacking the shared representation.

Not all task combinations help each other. Tasks must share meaningful structure for MTL to work — training a model to simultaneously predict housing prices and classify bird species would likely hurt both tasks, because the features useful for one are irrelevant to the other. The art of multi-task learning lies in choosing tasks that are complementary: they should require overlapping but not identical features, providing diverse gradient signals that reinforce a rich shared representation. When this alignment exists, MTL can achieve what no single-task model can — learning features that are more robust, more general, and more data-efficient.
