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
status: validated
---

# Imbalanced Classification and Class Weighting

## Core Idea
In imbalanced datasets, one class vastly outnumbers others, causing models to bias toward the majority and perform poorly on minorities. Solutions include class weighting (penalizing majority errors more), oversampling minorities, undersampling majorities, and threshold adjustment. Choice depends on problem costs and data constraints.

## Questions

```yaml
- question: "A fraud detection model reports 99.8% accuracy on a dataset where 0.2% of transactions are fraudulent. What is the most important concern about this result?"
  type: multiple-choice
  options:
    - "The accuracy is impressive and the model should be deployed immediately"
    - "The model is overfit and needs regularization to improve generalization"
    - "99.8% accuracy is achievable by predicting 'not fraud' for every transaction — the model may be catching zero actual fraud cases"
    - "The accuracy threshold is too low; fraud models require 99.99% accuracy"
  answer: 2
  explanation: "This is the central trap of imbalanced classification. A trivial classifier that always outputs the majority label achieves exactly the majority class frequency as its accuracy — here, 99.8%. Such a model is useless for fraud detection because it never identifies a fraudulent transaction. High accuracy on imbalanced data is a misleading metric precisely because the loss function during training rewards majority-class correctness. The right question to ask is: what is the model's recall (sensitivity) for the minority class?"

- question: "You have a medical diagnosis model with 50:1 class imbalance (healthy vs. diseased). Which intervention most directly addresses the training algorithm's bias toward predicting 'healthy' for every patient?"
  type: multiple-choice
  options:
    - "Collecting more data from healthy patients to improve the majority-class decision boundary"
    - "Assigning higher loss weights to misclassified diseased patients so the optimizer treats each missed diagnosis as seriously as many missed healthy predictions"
    - "Increasing model complexity so the decision boundary can separate the classes"
    - "Reducing the learning rate to allow the model to find a more balanced optimum"
  answer: 1
  explanation: "Class weighting directly modifies the loss function so that a minority-class error contributes proportionally more to the total loss. With a 50:1 imbalance, weighting minority errors 50× more heavily means missing one diseased patient costs as much as misclassifying 50 healthy ones — which is often the correct reflection of clinical costs. This is more targeted than data-level interventions (oversampling/undersampling) because it preserves the original data distribution while correcting the learning objective. Model complexity and learning rate adjustments do not address the fundamental class imbalance problem."

- question: "A model that achieves 99% accuracy on an imbalanced dataset is likely performing well on the minority class."
  type: true-false
  answer: false
  explanation: "High accuracy on imbalanced data is almost meaningless as a quality signal. If the minority class represents 1% of cases, a model that never predicts it achieves 99% accuracy trivially. Minority-class performance must be evaluated using metrics that directly measure it: precision (what fraction of positive predictions are correct), recall (what fraction of true positives are caught), F1-score (harmonic mean of precision and recall), or the precision-recall curve. Accuracy alone conflates majority-class performance with overall quality."

- question: "Lowering the classification threshold (e.g., from 0.5 to 0.1) in a probabilistic classifier increases recall for the minority class at the cost of more false positives."
  type: true-false
  answer: true
  explanation: "A classifier typically predicts the positive (minority) class when the estimated probability exceeds a threshold. Lowering this threshold means the model classifies more examples as positive — it catches more true positives (higher recall) but also flags more negatives incorrectly (more false positives, lower precision). This tradeoff is visualized in the precision-recall curve. The optimal threshold depends on the relative cost of false negatives versus false positives: in cancer screening, high recall (missing few cases) matters more than high precision."

- question: "Why is accuracy a misleading metric for imbalanced classification, and what alternative metrics should be used?"
  type: short-answer
  answer: "Accuracy rewards correct predictions proportionally across all classes. When one class dominates, a classifier can achieve high accuracy simply by always predicting the majority label, without ever identifying a minority-class example. Useful alternatives are precision (fraction of positive predictions that are true positives), recall (fraction of actual positives correctly identified), F1-score (harmonic mean of precision and recall), and the area under the precision-recall curve — all of which measure minority-class performance directly."
  explanation: "The problem is that accuracy treats every error equally regardless of which class is misclassified. In fraud detection or disease diagnosis, a false negative (missing a fraud or disease) is far more costly than a false positive. The choice of metric should reflect the asymmetry of error costs in the application. Precision-recall curves make this tradeoff explicit across all possible thresholds, letting practitioners choose the operating point appropriate for their use case."
```

## Explainer

Imagine training a fraud detection model where only 1 in 1,000 transactions is fraudulent. A classifier that simply predicts "not fraud" for every transaction achieves 99.9% accuracy — and catches zero actual fraud. This is the fundamental problem of **imbalanced classification**: when one class vastly outnumbers another, standard supervised learning algorithms optimize for overall accuracy and effectively ignore the minority class. The model learns that always predicting the majority label minimizes its loss, which is technically correct but practically useless.

The most direct fix is **class weighting**, which adjusts the loss function so that misclassifying a minority example costs more than misclassifying a majority example. If you recall from supervised learning how the model minimizes a loss function during training, class weighting simply multiplies the loss contribution of minority samples by a factor proportional to the imbalance ratio. A dataset with 100:1 imbalance might weight minority errors 100 times more heavily, so the optimizer treats one missed fraud case as seriously as missing 100 legitimate transactions. Most classifiers — including the logistic regression classifier you may already know — accept a class_weight parameter that does exactly this.

Another family of solutions operates on the data itself rather than the loss function. **Oversampling** creates additional copies of minority examples (or synthesizes new ones using techniques like SMOTE, which interpolates between existing minority points in feature space). **Undersampling** discards majority examples to bring the class ratio closer to balance. Oversampling risks overfitting to the specific minority examples you have; undersampling throws away potentially useful majority data. Hybrid approaches combine both, and the best choice depends on dataset size — undersampling works well when you have abundant data, while oversampling helps when data is scarce.

Finally, **threshold adjustment** changes how the model's output probabilities translate into class predictions. By default, a classifier predicts the positive class when its estimated probability exceeds 0.5, but on imbalanced data, lowering this threshold to 0.1 or 0.05 lets the model catch more minority cases at the cost of more false positives. The right threshold depends on the relative cost of errors: missing a cancer diagnosis is far more expensive than ordering an unnecessary follow-up test. Precision-recall curves and the F1 score become essential evaluation tools here, because accuracy is misleading when classes are imbalanced.
