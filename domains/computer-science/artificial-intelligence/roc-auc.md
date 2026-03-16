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

## Explainer

From your work with classification metrics, you know that a binary classifier's performance depends on the **threshold** you choose: above the threshold, predict positive; below, predict negative. Moving the threshold changes the tradeoff between catching true positives and generating false positives. A low threshold catches most positives but flags many negatives incorrectly; a high threshold is conservative, missing some positives but making fewer false alarms. The ROC curve captures this entire tradeoff in one picture.

To build an **ROC curve**, you sweep the threshold from its maximum to its minimum. At each threshold, you compute two quantities: the **true positive rate** (TPR, also called recall or sensitivity) — the fraction of actual positives correctly identified — and the **false positive rate** (FPR) — the fraction of actual negatives incorrectly flagged as positive. Each threshold gives you one (FPR, TPR) point, and connecting all these points produces the ROC curve. The curve always starts at (0, 0) — where the threshold is so high nothing is predicted positive — and ends at (1, 1) — where the threshold is so low everything is predicted positive. A perfect classifier reaches the top-left corner (0, 1): it achieves 100% TPR with 0% FPR. A random classifier follows the diagonal from (0, 0) to (1, 1), because its TPR and FPR increase at the same rate.

The **AUC** (Area Under the ROC Curve) collapses the curve into a single number between 0 and 1. An AUC of 0.5 means the classifier is no better than random guessing; an AUC of 1.0 means perfect separation. The most useful interpretation is probabilistic: AUC equals the probability that, if you randomly pick one positive example and one negative example, the classifier assigns a higher score to the positive one. This makes AUC a measure of **ranking quality** — how well the model separates positives from negatives in its raw scores, regardless of what threshold you eventually choose.

This threshold-independence is what makes ROC-AUC especially valuable. Accuracy can be misleading when classes are imbalanced — a model that predicts "no cancer" for every patient achieves 99% accuracy if only 1% of patients have cancer, but it is useless. The ROC curve ignores the class distribution entirely because TPR and FPR are computed within each class separately. However, when class imbalance is extreme, **precision-recall curves** may be more informative than ROC curves, because ROC can look optimistic when the number of negatives vastly exceeds positives. In practice, AUC is best used to compare models or tune hyperparameters — it tells you which model is better at ranking, and you separately choose the operating threshold based on the costs of false positives versus false negatives in your specific application.
