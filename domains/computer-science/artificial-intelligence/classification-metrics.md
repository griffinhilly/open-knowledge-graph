---
id: classification-metrics
title: Classification Metrics and Evaluation
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: supervised-learning-intro
  type: hard
- id: conditional-probability
  type: soft
builds-toward:
- roc-auc
- confusion-matrix
tags:
- metrics
- evaluation
- performance
stage: advanced
status: draft
---

# Classification Metrics and Evaluation

## Core Idea
Classification metrics quantify performance beyond accuracy. Precision measures false positive rate; recall measures false negatives. F1 balances both. Macro-averaging treats all classes equally; weighted-averaging accounts for class frequency. Metric choice depends on problem costs: precision matters when false positives are expensive, recall when false negatives are costly.
