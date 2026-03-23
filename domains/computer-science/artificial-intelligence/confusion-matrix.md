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
  - multi-class-evaluation
tags:
- confusion-matrix
- tp
- fp
- tn
- fn
stage: advanced
status: validated
---
# Confusion Matrix and Classification Metrics

## Core Idea
A confusion matrix tabulates true positives, false positives, true negatives, and false negatives for binary classification (generalizes to multi-class). It enables computing precision, recall, specificity, and F1-score. Visualizing confusion matrices reveals which classes are confused, guiding targeted model improvements.

## Questions

```yaml
- question: "A disease affects 1% of a population. A diagnostic test achieves 99% accuracy by always predicting 'healthy' for every patient. What is this test's recall for detecting the disease?"
  type: multiple-choice
  options:
    - "99% — matching its overall accuracy"
    - "1% — equal to the disease prevalence"
    - "0% — it correctly identifies zero sick patients"
    - "100% — it correctly identifies all healthy patients as healthy"
  answer: 2
  explanation: "Recall = TP / (TP + FN). A test that always predicts 'healthy' has TP = 0 (it never correctly identifies a sick patient) and FN = every sick patient. Therefore recall = 0/(0 + all_sick) = 0%. The 99% accuracy comes entirely from correctly labeling the 99% who are healthy — the test is clinically useless for its actual purpose. This is the central lesson of the confusion matrix: overall accuracy is a dangerously misleading metric when class distributions are imbalanced. Option D describes specificity (true negative rate), not recall."

- question: "A spam filter is evaluated on 9,200 emails: 600 spam correctly caught (TP), 400 ham misclassified as spam (FP), 8,000 ham correctly passed (TN), 200 spam that slipped through (FN). What is the filter's recall?"
  type: multiple-choice
  options:
    - "0.60 — computed as TP / (TP + FP)"
    - "0.75 — computed as TP / (TP + FN)"
    - "0.93 — computed as (TP + TN) / total"
    - "0.95 — computed as TN / (TN + FP)"
  answer: 1
  explanation: "Recall = TP / (TP + FN) = 600 / (600 + 200) = 600 / 800 = 0.75. Recall answers: 'Of all actual spam, what fraction did the filter catch?' Option A is precision (TP/(TP+FP) = 600/1000 = 0.60), which answers 'Of everything flagged as spam, how much really was?' Option C is overall accuracy = 8600/9200 ≈ 0.93. Notice that precision (0.60) and recall (0.75) diverge — making the filter more aggressive would increase recall but lower precision, illustrating the inherent tradeoff."

- question: "A classifier with 99% accuracy is necessarily better than one with 95% accuracy for a fraud detection task where only 1% of transactions are fraudulent."
  type: true-false
  answer: false
  explanation: "A model that labels every transaction as 'not fraud' achieves 99% accuracy — but catches zero fraud cases (0% recall). For a fraud detection system, the relevant metrics are precision and recall for the fraud class. A model with 95% overall accuracy that catches 80% of actual fraud has far greater practical value, despite lower aggregate accuracy. This is the core lesson of the confusion matrix: class-level metrics replace overall accuracy whenever class distributions are imbalanced or error costs are asymmetric."

- question: "Increasing a binary classifier's classification threshold (requiring higher confidence before predicting 'positive') generally increases precision while decreasing recall."
  type: true-false
  answer: true
  explanation: "A higher threshold makes the model more conservative — it only predicts positive when very confident. Fewer borderline cases are incorrectly called positive (FP decreases), which increases precision (TP/(TP+FP)). But more true positives fall below the stricter threshold and are missed (FN increases), which decreases recall (TP/(TP+FN)). This precision-recall tradeoff is inherent to any classifier with an adjustable threshold. The confusion matrix makes it quantifiable: adjusting the threshold shifts numbers between TP, FP, TN, and FN, changing all derived metrics simultaneously."

- question: "Explain why 'accuracy' is a misleading metric for a fraud detection system where 99% of transactions are legitimate, and identify two metrics that would be more informative."
  type: short-answer
  answer: "Accuracy measures the fraction of all predictions that are correct, but when 99% of cases are legitimate, a model that always predicts 'legitimate' achieves 99% accuracy while catching zero fraud. More informative metrics are precision (of transactions flagged as fraud, what fraction are actually fraudulent — measuring the false alarm rate) and recall (of all actual fraud cases, what fraction was detected — measuring detection capability). These class-specific metrics expose what accuracy hides: whether the model actually works for its purpose."
  explanation: "The confusion matrix was designed for exactly this situation: when the cost of different error types differs. Missing fraud (false negative) costs far more than a false alarm (false positive), yet accuracy weights both errors equally. In imbalanced settings, F1-score (harmonic mean of precision and recall) is also more meaningful than accuracy. The general principle: choose metrics based on which errors matter most in the application context, not on which metric is easiest to compute."
```

## Explainer

From supervised learning, you know that a classifier is trained on labeled examples and then evaluated on held-out data. But "how accurate is my model?" turns out to be a dangerously simplistic question. If 95% of emails are not spam, a model that always predicts "not spam" achieves 95% accuracy while being completely useless at its actual job. The **confusion matrix** replaces this single number with a complete picture of what your classifier gets right and wrong, broken down by class.

For binary classification, the confusion matrix is a 2×2 table. One axis represents the actual class (positive or negative), the other represents the predicted class. This creates four cells: **true positives** (TP) — correctly identified positives; **false positives** (FP) — negatives incorrectly called positive; **true negatives** (TN) — correctly identified negatives; and **false negatives** (FN) — positives incorrectly called negative. In a medical screening example, a TP is a sick patient correctly diagnosed, an FP is a healthy patient incorrectly flagged (a false alarm), a TN is a healthy patient correctly cleared, and an FN is a sick patient missed by the test. Each type of error has different real-world costs, and the confusion matrix forces you to confront them separately.

From these four numbers, you can derive every standard classification metric. **Precision** = TP/(TP+FP) answers "of everything the model called positive, how many actually were?" **Recall** (or sensitivity) = TP/(TP+FN) answers "of all actual positives, how many did the model catch?" **Specificity** = TN/(TN+FP) answers the same question for negatives. The **F1-score** = 2·(precision·recall)/(precision+recall) is the harmonic mean of precision and recall, useful when you want a single number that balances both. The key insight is that precision and recall trade off against each other: making a model more aggressive (predicting positive more often) increases recall but decreases precision, and vice versa. The confusion matrix makes this tradeoff visible and quantifiable.

For multi-class problems, the confusion matrix extends to an N×N table where entry (i, j) counts how many examples of class i were predicted as class j. The diagonal contains correct predictions; off-diagonal entries reveal specific confusions. If a digit recognizer frequently puts "7" in the "1" column, you know exactly which pair of classes needs attention — perhaps adding training examples that emphasize the crossbar of the 7, or engineering features that distinguish vertical strokes from angled ones. This diagnostic power is why the confusion matrix is the first thing experienced practitioners examine after training a classifier, long before looking at any aggregate metric.
