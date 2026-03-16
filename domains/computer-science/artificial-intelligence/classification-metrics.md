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

## Explainer

From supervised learning, you know that a classifier learns to assign inputs to categories — spam or not spam, malignant or benign, cat or dog. The natural first question is "how often does it get the right answer?" and **accuracy** (correct predictions / total predictions) seems like the obvious metric. But accuracy hides critical information. Imagine a disease screening test where only 1% of patients are actually sick. A classifier that always predicts "healthy" achieves 99% accuracy — yet it is completely useless because it misses every sick patient. This is the fundamental problem that motivates the richer set of classification metrics.

The foundation is the **confusion matrix**, a table that cross-tabulates predictions against reality. For a binary classifier, it has four cells: **true positives** (TP — correctly predicted positive), **true negatives** (TN — correctly predicted negative), **false positives** (FP — predicted positive but actually negative, also called Type I errors), and **false negatives** (FN — predicted negative but actually positive, Type II errors). Every classification metric is some combination of these four numbers. **Precision** = TP / (TP + FP) answers: "Of everything the model flagged as positive, how many actually were?" **Recall** (also called sensitivity) = TP / (TP + FN) answers: "Of all the actual positives, how many did the model catch?" These two metrics trade off against each other — you can achieve perfect recall by predicting everything as positive (but precision collapses), or perfect precision by only predicting positive when you're extremely confident (but recall collapses).

The **F1 score** = 2 × (precision × recall) / (precision + recall) is the harmonic mean of precision and recall, providing a single number that balances both. The harmonic mean is used instead of the arithmetic mean because it penalizes extreme imbalances: if either precision or recall is very low, F1 will also be low, even if the other is high. For problems where false positives and false negatives have different costs, you can use the **Fβ score**, which weights recall β times more than precision. In practice, which metric to prioritize depends on the stakes: a spam filter should favor precision (annoying to lose a real email), while a cancer screening test should favor recall (dangerous to miss a malignant case).

When you move beyond binary classification to multiple classes, you need strategies for combining per-class metrics. **Macro-averaging** computes the metric independently for each class and then takes the unweighted mean — this treats all classes as equally important regardless of their frequency. **Weighted averaging** weights each class's metric by its proportion in the dataset — this reflects overall performance but can obscure poor performance on rare classes. **Micro-averaging** pools all TP, FP, and FN across classes before computing the metric, which in the multiclass case reduces to accuracy. Choosing the right averaging method depends on whether you care equally about all classes (use macro) or proportionally to their frequency (use weighted). Understanding these distinctions is essential for honest model evaluation, especially in real-world datasets where class imbalance is the norm rather than the exception.
