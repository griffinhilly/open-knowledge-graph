---
id: overfitting-underfitting
title: Overfitting, Underfitting, and Model Capacity
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: bias-variance-tradeoff
  type: hard
- id: supervised-learning-intro
  type: hard
builds-toward:
- regularization-techniques
- cross-validation-techniques
tags:
- overfitting
- underfitting
- generalization
stage: advanced
status: draft
---

# Overfitting, Underfitting, and Model Capacity

## Core Idea
Overfitting occurs when a model memorizes training data and fails to generalize; underfitting means the model is too simple to capture patterns. Model capacity—determined by parameters and architecture—must match problem complexity. Detecting overfitting requires separate validation data and monitoring the train-validation gap.
