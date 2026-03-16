---
id: confusion-matrix
title: Confusion Matrix and Classification Metrics
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: supervised-learning-intro
  type: hard
- id: probability-axioms
  type: soft
builds-toward:
- classification-metrics
- multi-class-evaluation
tags:
- confusion-matrix
- tp
- fp
- tn
- fn
stage: advanced
status: draft
---

# Confusion Matrix and Classification Metrics

## Core Idea
A confusion matrix tabulates true positives, false positives, true negatives, and false negatives for binary classification (generalizes to multi-class). It enables computing precision, recall, specificity, and F1-score. Visualizing confusion matrices reveals which classes are confused, guiding targeted model improvements.

## Explainer

From supervised learning, you know that a classifier is trained on labeled examples and then evaluated on held-out data. But "how accurate is my model?" turns out to be a dangerously simplistic question. If 95% of emails are not spam, a model that always predicts "not spam" achieves 95% accuracy while being completely useless at its actual job. The **confusion matrix** replaces this single number with a complete picture of what your classifier gets right and wrong, broken down by class.

For binary classification, the confusion matrix is a 2×2 table. One axis represents the actual class (positive or negative), the other represents the predicted class. This creates four cells: **true positives** (TP) — correctly identified positives; **false positives** (FP) — negatives incorrectly called positive; **true negatives** (TN) — correctly identified negatives; and **false negatives** (FN) — positives incorrectly called negative. In a medical screening example, a TP is a sick patient correctly diagnosed, an FP is a healthy patient incorrectly flagged (a false alarm), a TN is a healthy patient correctly cleared, and an FN is a sick patient missed by the test. Each type of error has different real-world costs, and the confusion matrix forces you to confront them separately.

From these four numbers, you can derive every standard classification metric. **Precision** = TP/(TP+FP) answers "of everything the model called positive, how many actually were?" **Recall** (or sensitivity) = TP/(TP+FN) answers "of all actual positives, how many did the model catch?" **Specificity** = TN/(TN+FP) answers the same question for negatives. The **F1-score** = 2·(precision·recall)/(precision+recall) is the harmonic mean of precision and recall, useful when you want a single number that balances both. The key insight is that precision and recall trade off against each other: making a model more aggressive (predicting positive more often) increases recall but decreases precision, and vice versa. The confusion matrix makes this tradeoff visible and quantifiable.

For multi-class problems, the confusion matrix extends to an N×N table where entry (i, j) counts how many examples of class i were predicted as class j. The diagonal contains correct predictions; off-diagonal entries reveal specific confusions. If a digit recognizer frequently puts "7" in the "1" column, you know exactly which pair of classes needs attention — perhaps adding training examples that emphasize the crossbar of the 7, or engineering features that distinguish vertical strokes from angled ones. This diagnostic power is why the confusion matrix is the first thing experienced practitioners examine after training a classifier, long before looking at any aggregate metric.
