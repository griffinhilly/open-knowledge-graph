---
id: roc-auc
title: ROC Curves and AUC Metrics
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: classification-metrics
  type: hard
builds-toward:
- threshold-optimization
- ranking-metrics
tags:
- roc
- auc
- roc-curve
stage: advanced
status: draft
---

# ROC Curves and AUC Metrics

## Core Idea
ROC (Receiver Operating Characteristic) curves plot true positive rate vs. false positive rate across classification thresholds. AUC (Area Under Curve) summarizes the curve as a single score (0 to 1): 0.5 = random, 1.0 = perfect. ROC is threshold-independent, ideal for imbalanced problems. AUC estimates the probability that the classifier ranks a random positive higher than a random negative.
