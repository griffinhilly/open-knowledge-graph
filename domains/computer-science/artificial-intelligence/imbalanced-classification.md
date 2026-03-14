---
id: imbalanced-classification
title: Imbalanced Classification and Class Weighting
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: supervised-learning-intro
  type: hard
- id: logistic-regression-classifier
  type: soft
builds-toward:
- classification-metrics
- oversampling-undersampling
tags:
- imbalance
- class-weight
- minority-class
stage: advanced
status: draft
---

# Imbalanced Classification and Class Weighting

## Core Idea
In imbalanced datasets, one class vastly outnumbers others, causing models to bias toward the majority and perform poorly on minorities. Solutions include class weighting (penalizing majority errors more), oversampling minorities, undersampling majorities, and threshold adjustment. Choice depends on problem costs and data constraints.
