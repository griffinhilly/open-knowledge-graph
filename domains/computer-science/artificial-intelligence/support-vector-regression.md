---
id: support-vector-regression
title: Support Vector Regression
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: support-vector-machines
  type: hard
- id: linear-regression-ml
  type: hard
builds-toward:
- kernel-methods
- regression-techniques
tags:
- svr
- support-vector
- regression
stage: advanced
status: draft
---

# Support Vector Regression

## Core Idea
Support Vector Regression extends SVMs to regression by fitting a hyperplane while constraining prediction errors within a margin. SVR handles non-linearity via kernels and is robust to outliers. The epsilon parameter controls the trade-off between model complexity and allowable error, providing intuitive control over generalization.
