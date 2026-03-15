---
id: support-vector-machines
title: Support Vector Machines
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: linear-algebra-basics
  type: hard
- id: dot-product
  type: soft
- id: vector-spaces
  type: soft
- id: constrained-optimization
  type: soft
- id: inner-product-spaces
  type: soft
- id: optimization-multivariable-basics
  type: soft
- id: optimization-problems
  type: hard
- id: matrix-operations
  type: soft
tags:
- supervised-learning
- classification
- margin-based
stage: advanced
status: draft
---

# Support Vector Machines

## Core Idea
SVMs find hyperplanes maximizing the margin between classes. Soft-margin SVMs tolerate misclassification via slack variables. Kernels map to high-dimensional spaces enabling non-linear classification without explicit computation.
