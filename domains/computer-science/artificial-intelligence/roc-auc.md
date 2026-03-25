---
id: roc-auc
title: ROC Curves and AUC Metrics
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: classification-metrics
  type: hard
tags:
- roc
- auc
- roc-curve
stage: advanced
status: validated
---

# ROC Curves and AUC Metrics

## Core Idea
ROC (Receiver Operating Characteristic) curves plot true positive rate vs. false positive rate across classification thresholds. AUC (Area Under Curve) summarizes the curve as a single score (0 to 1): 0.5 = random, 1.0 = perfect. ROC is threshold-independent, ideal for imbalanced problems. AUC estimates the probability that the classifier ranks a random positive higher than a random negative.

## Questions

```yaml
- question: "A fraud detection model achieves 99.9% accuracy on a dataset where only 0.1% of transactions are fraudulent. What does this tell us about the model's AUC?"
  type: multiple-choice
  options:
    - "The model's AUC must be close to 1.0, since high accuracy implies strong discrimination"
    - "We cannot determine the AUC from accuracy alone — a model that predicts 'not fraud' for every transaction achieves 99.9% accuracy but has AUC of 0.5"
    - "The model's AUC is guaranteed to exceed 0.5, since it outperforms a random baseline"
    - "AUC and accuracy always agree on imbalanced datasets"
  answer: 1
  explanation: "A model that always predicts 'not fraud' achieves 99.9% accuracy on this dataset — equal to the class imbalance ratio — while ranking every example identically and thus having AUC = 0.5 (no better than chance). AUC measures ranking quality (does the model assign higher scores to positives than negatives?), not raw correctness. High accuracy on imbalanced data tells you almost nothing about discrimination ability. This is the central reason ROC-AUC exists."

- question: "A classifier achieves AUC = 0.85. Which interpretation is correct?"
  type: multiple-choice
  options:
    - "The model correctly classifies 85% of examples regardless of threshold"
    - "If you randomly pick one positive and one negative example, the model assigns a higher score to the positive one 85% of the time"
    - "The model achieves 85% sensitivity at the threshold that maximizes accuracy"
    - "The model achieves 85% precision across all thresholds"
  answer: 1
  explanation: "AUC has a precise probabilistic interpretation: it equals the probability that the classifier ranks a randomly chosen positive example higher than a randomly chosen negative example. This is about ranking quality, not accuracy at any specific threshold. Options A, C, and D all confuse AUC with threshold-specific metrics. The power of AUC is that it summarizes the model's discriminative ability across ALL possible thresholds, not just one."

- question: "An ROC curve is constructed by varying the classification threshold and recording how the true positive rate and false positive rate change at each threshold."
  type: true-false
  answer: true
  explanation: "This is the correct construction: sweep the threshold from maximum (classify nothing as positive) to minimum (classify everything as positive), computing TPR and FPR at each step. Each threshold gives one (FPR, TPR) coordinate on the curve. At maximum threshold, you are at (0, 0); at minimum threshold, at (1, 1). The shape of the curve between these points reveals how effectively the model trades off catching true positives versus generating false alarms."

- question: "A model with AUC = 0.75 will achieve higher accuracy at every possible threshold than a model with AUC = 0.65."
  type: true-false
  answer: false
  explanation: "AUC measures ranking quality — the probability of correctly ordering a positive above a negative — not accuracy at any particular threshold. A model with higher AUC can still have lower accuracy than a lower-AUC model at specific thresholds, especially if the two models are calibrated differently or if class imbalance affects the accuracy comparison. AUC tells you which model is better at discrimination; threshold selection based on operating costs is a separate decision."

- question: "Why is AUC more informative than accuracy when evaluating a classifier on an imbalanced dataset? What does each metric actually measure?"
  type: short-answer
  answer: "Accuracy measures the proportion of correct classifications at a fixed threshold, which is dominated by the majority class when data is imbalanced. A model that always predicts the majority class achieves high accuracy despite being useless. AUC, by contrast, measures ranking quality: the probability that the model assigns a higher score to a random positive than a random negative. It evaluates the classifier's underlying discrimination ability across all possible thresholds, independently of class proportions, because TPR and FPR are each computed within their own class."
  explanation: "The key distinction is that accuracy conflates the model's predictions with the class distribution, while ROC-AUC eliminates the class distribution by normalizing within each class. This makes AUC the right metric when you care about the model's ability to separate classes — and then separately choose the threshold based on the actual cost of false positives vs. false negatives in the application."
```

## Explainer

From your work with classification metrics, you know that a binary classifier's performance depends on the **threshold** you choose: above the threshold, predict positive; below, predict negative. Moving the threshold changes the tradeoff between catching true positives and generating false positives. A low threshold catches most positives but flags many negatives incorrectly; a high threshold is conservative, missing some positives but making fewer false alarms. The ROC curve captures this entire tradeoff in one picture.

To build an **ROC curve**, you sweep the threshold from its maximum to its minimum. At each threshold, you compute two quantities: the **true positive rate** (TPR, also called recall or sensitivity) — the fraction of actual positives correctly identified — and the **false positive rate** (FPR) — the fraction of actual negatives incorrectly flagged as positive. Each threshold gives you one (FPR, TPR) point, and connecting all these points produces the ROC curve. The curve always starts at (0, 0) — where the threshold is so high nothing is predicted positive — and ends at (1, 1) — where the threshold is so low everything is predicted positive. A perfect classifier reaches the top-left corner (0, 1): it achieves 100% TPR with 0% FPR. A random classifier follows the diagonal from (0, 0) to (1, 1), because its TPR and FPR increase at the same rate.

The **AUC** (Area Under the ROC Curve) collapses the curve into a single number between 0 and 1. An AUC of 0.5 means the classifier is no better than random guessing; an AUC of 1.0 means perfect separation. The most useful interpretation is probabilistic: AUC equals the probability that, if you randomly pick one positive example and one negative example, the classifier assigns a higher score to the positive one. This makes AUC a measure of **ranking quality** — how well the model separates positives from negatives in its raw scores, regardless of what threshold you eventually choose.

This threshold-independence is what makes ROC-AUC especially valuable. Accuracy can be misleading when classes are imbalanced — a model that predicts "no cancer" for every patient achieves 99% accuracy if only 1% of patients have cancer, but it is useless. The ROC curve ignores the class distribution entirely because TPR and FPR are computed within each class separately. However, when class imbalance is extreme, **precision-recall curves** may be more informative than ROC curves, because ROC can look optimistic when the number of negatives vastly exceeds positives. In practice, AUC is best used to compare models or tune hyperparameters — it tells you which model is better at ranking, and you separately choose the operating threshold based on the costs of false positives versus false negatives in your specific application.
