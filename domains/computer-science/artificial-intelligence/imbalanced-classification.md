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

## Explainer

Imagine training a fraud detection model where only 1 in 1,000 transactions is fraudulent. A classifier that simply predicts "not fraud" for every transaction achieves 99.9% accuracy — and catches zero actual fraud. This is the fundamental problem of **imbalanced classification**: when one class vastly outnumbers another, standard supervised learning algorithms optimize for overall accuracy and effectively ignore the minority class. The model learns that always predicting the majority label minimizes its loss, which is technically correct but practically useless.

The most direct fix is **class weighting**, which adjusts the loss function so that misclassifying a minority example costs more than misclassifying a majority example. If you recall from supervised learning how the model minimizes a loss function during training, class weighting simply multiplies the loss contribution of minority samples by a factor proportional to the imbalance ratio. A dataset with 100:1 imbalance might weight minority errors 100 times more heavily, so the optimizer treats one missed fraud case as seriously as missing 100 legitimate transactions. Most classifiers — including the logistic regression classifier you may already know — accept a class_weight parameter that does exactly this.

Another family of solutions operates on the data itself rather than the loss function. **Oversampling** creates additional copies of minority examples (or synthesizes new ones using techniques like SMOTE, which interpolates between existing minority points in feature space). **Undersampling** discards majority examples to bring the class ratio closer to balance. Oversampling risks overfitting to the specific minority examples you have; undersampling throws away potentially useful majority data. Hybrid approaches combine both, and the best choice depends on dataset size — undersampling works well when you have abundant data, while oversampling helps when data is scarce.

Finally, **threshold adjustment** changes how the model's output probabilities translate into class predictions. By default, a classifier predicts the positive class when its estimated probability exceeds 0.5, but on imbalanced data, lowering this threshold to 0.1 or 0.05 lets the model catch more minority cases at the cost of more false positives. The right threshold depends on the relative cost of errors: missing a cancer diagnosis is far more expensive than ordering an unnecessary follow-up test. Precision-recall curves and the F1 score become essential evaluation tools here, because accuracy is misleading when classes are imbalanced.
