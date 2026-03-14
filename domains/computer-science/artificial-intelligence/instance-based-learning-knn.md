---
id: instance-based-learning-knn
title: Instance-Based Learning (k-NN)
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: supervised-learning-intro
  type: hard
- id: algorithm-design-basics
  type: soft
tags:
- classification
- instance-based
- distance-metrics
- lazy-learning
stage: advanced
status: draft
---

# Instance-Based Learning (k-NN)

## Core Idea
k-nearest neighbors classifies instances by finding the k most similar neighbors in training data and using their labels (majority vote for classification, average for regression). It is a lazy learner (no training phase), making it sensitive to feature scaling and slow at prediction time, but it performs well with complex local patterns and requires no assumptions about data distribution.

## How It's Best Learned
Implement k-NN and experiment with k values and distance metrics (Euclidean, Manhattan, cosine) on datasets with different geometry.
