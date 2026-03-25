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
- id: confusion-matrix
  type: soft
builds-toward:
- roc-auc
- confusion-matrix
tags:
- metrics
- evaluation
- performance
stage: advanced
status: validated
---
# Classification Metrics and Evaluation

## Core Idea
Classification metrics quantify performance beyond accuracy. Precision measures false positive rate; recall measures false negatives. F1 balances both. Macro-averaging treats all classes equally; weighted-averaging accounts for class frequency. Metric choice depends on problem costs: precision matters when false positives are expensive, recall when false negatives are costly.

## Questions

```yaml
- question: "A fraud detection model evaluated on a dataset where 0.1% of transactions are fraudulent achieves 99.9% accuracy by predicting 'not fraud' for every transaction. What is its recall for the fraud class?"
  type: multiple-choice
  options:
    - "99.9% — the model is correct nearly all the time"
    - "0% — it never predicts fraud, so it catches none of the actual fraud cases"
    - "0.1% — it correctly identifies the rare fraud cases"
    - "Undefined — recall cannot be computed on imbalanced datasets"
  answer: 1
  explanation: "Recall = TP / (TP + FN). This model predicts 'not fraud' for everything, so TP = 0 — it never correctly identifies a fraud case. All actual frauds become false negatives. Recall is therefore 0/0+all_fraud = 0%. This is the classic example motivating metrics beyond accuracy: 99.9% accuracy on a 0.1%-positive dataset is achieved trivially by predicting the majority class always, while being completely useless for the actual task."

- question: "A cancer screening model correctly identifies 95% of actual cancer cases but also flags 40% of healthy patients as potentially cancerous. How should this tradeoff be characterized?"
  type: multiple-choice
  options:
    - "High precision, low recall — the model is conservative and misses few real cases"
    - "Low precision, high recall — the model catches most real cases but generates many false alarms"
    - "High precision, high recall — catching 95% of cancers while flagging 40% of healthy patients is acceptable for screening"
    - "Low precision, low recall — a 40% false positive rate means the model is unreliable"
  answer: 1
  explanation: "Recall = TP/(TP+FN) = 95% (catches 95% of real cases — high). Precision = TP/(TP+FP) — with 40% of healthy patients flagged, there are many false positives relative to true positives, so precision is low. This tradeoff is often acceptable in initial cancer screening, where the cost of missing a true case (a missed diagnosis) is far higher than the cost of a false alarm (a follow-up test). The low precision means many patients get unnecessary follow-ups, but high recall ensures few cancers are missed."

- question: "F1 score is the arithmetic mean of precision and recall, so it equals (precision + recall) / 2."
  type: true-false
  answer: false
  explanation: "F1 uses the harmonic mean: F1 = 2 × (precision × recall) / (precision + recall). The harmonic mean is always ≤ the arithmetic mean and crucially penalizes extreme imbalances. If a model has precision = 1.0 and recall = 0.01, the arithmetic mean would be 0.505 — suggesting decent performance — but F1 = 0.0198, correctly signaling that the model is nearly useless. Using the harmonic mean ensures that a very low score on either metric drags the combined score down sharply."

- question: "Using macro-averaging to evaluate a multiclass classifier on an imbalanced dataset can make the classifier appear to perform worse than weighted-averaging, even if performance on the majority class is excellent."
  type: true-false
  answer: true
  explanation: "Macro-averaging computes the metric separately for each class and takes the unweighted mean, treating all classes as equally important. If the model performs poorly on rare classes, macro-averaging penalizes this equally alongside common-class performance. Weighted-averaging weights each class's contribution by its frequency — so the majority class dominates the score. A model that excels on a 98%-majority class but fails on 2%-minority classes will look much better under weighted averaging than macro averaging."

- question: "A hospital is deploying a classifier to screen patients for a rare but treatable disease. Should the classifier prioritize precision or recall, and why?"
  type: short-answer
  answer: "Recall (sensitivity), because the cost of a false negative — missing a patient who actually has the disease and sending them home untreated — is far higher than the cost of a false positive. Patients flagged by the screen will receive follow-up diagnostic testing, so a false positive results in an unnecessary test, not a harmful outcome. Optimizing for precision would reduce false alarms but risk missing real cases. In medical screening, the principle is: cast a wide net first, then refine with confirmatory testing."
  explanation: "This illustrates the core principle: metric choice depends on the asymmetric costs of different errors. When false negatives are dangerous (missed cancers, undetected fraud, failed structural safety inspections), maximize recall. When false positives are costly (wrongful arrests, unnecessary surgery, expensive follow-up procedures with their own risks), precision matters more. The F1 score is appropriate when both errors have roughly equal cost; in practice, most real-world classification problems have asymmetric costs."
```

## Explainer

From supervised learning, you know that a classifier learns to assign inputs to categories — spam or not spam, malignant or benign, cat or dog. The natural first question is "how often does it get the right answer?" and **accuracy** (correct predictions / total predictions) seems like the obvious metric. But accuracy hides critical information. Imagine a disease screening test where only 1% of patients are actually sick. A classifier that always predicts "healthy" achieves 99% accuracy — yet it is completely useless because it misses every sick patient. This is the fundamental problem that motivates the richer set of classification metrics.

The foundation is the **confusion matrix**, a table that cross-tabulates predictions against reality. For a binary classifier, it has four cells: **true positives** (TP — correctly predicted positive), **true negatives** (TN — correctly predicted negative), **false positives** (FP — predicted positive but actually negative, also called Type I errors), and **false negatives** (FN — predicted negative but actually positive, Type II errors). Every classification metric is some combination of these four numbers. **Precision** = TP / (TP + FP) answers: "Of everything the model flagged as positive, how many actually were?" **Recall** (also called sensitivity) = TP / (TP + FN) answers: "Of all the actual positives, how many did the model catch?" These two metrics trade off against each other — you can achieve perfect recall by predicting everything as positive (but precision collapses), or perfect precision by only predicting positive when you're extremely confident (but recall collapses).

The **F1 score** = 2 × (precision × recall) / (precision + recall) is the harmonic mean of precision and recall, providing a single number that balances both. The harmonic mean is used instead of the arithmetic mean because it penalizes extreme imbalances: if either precision or recall is very low, F1 will also be low, even if the other is high. For problems where false positives and false negatives have different costs, you can use the **Fβ score**, which weights recall β times more than precision. In practice, which metric to prioritize depends on the stakes: a spam filter should favor precision (annoying to lose a real email), while a cancer screening test should favor recall (dangerous to miss a malignant case).

When you move beyond binary classification to multiple classes, you need strategies for combining per-class metrics. **Macro-averaging** computes the metric independently for each class and then takes the unweighted mean — this treats all classes as equally important regardless of their frequency. **Weighted averaging** weights each class's metric by its proportion in the dataset — this reflects overall performance but can obscure poor performance on rare classes. **Micro-averaging** pools all TP, FP, and FN across classes before computing the metric, which in the multiclass case reduces to accuracy. Choosing the right averaging method depends on whether you care equally about all classes (use macro) or proportionally to their frequency (use weighted). Understanding these distinctions is essential for honest model evaluation, especially in real-world datasets where class imbalance is the norm rather than the exception.
