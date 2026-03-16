---
id: overfitting-underfitting
title: Overfitting, Underfitting, and Model Capacity
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: bias-variance-tradeoff
  type: hard
- id: supervised-learning-intro
  type: hard
builds-toward:
- regularization-techniques
- cross-validation-techniques
tags:
- overfitting
- underfitting
- generalization
stage: advanced
status: draft
---

# Overfitting, Underfitting, and Model Capacity

## Core Idea
Overfitting occurs when a model memorizes training data and fails to generalize; underfitting means the model is too simple to capture patterns. Model capacity—determined by parameters and architecture—must match problem complexity. Detecting overfitting requires separate validation data and monitoring the train-validation gap.

## Explainer

From the bias-variance tradeoff, you know that prediction error comes from two sources: bias (systematic inaccuracy from overly simple assumptions) and variance (sensitivity to the particular training data you happened to draw). **Overfitting** and **underfitting** are the practical manifestations of this tradeoff. Understanding them transforms the bias-variance concept from theory into a diagnostic you can apply to every model you build.

**Underfitting** means your model cannot capture the real patterns in the data. Imagine fitting a straight line to data that follows a parabola — no matter how much data you collect, the line will systematically miss the curve. The model's **capacity** (its ability to represent complex functions) is too low for the problem. Underfitting shows up as poor performance on *both* the training data and new data. The fix is straightforward: use a more flexible model, add features, or reduce excessive regularization. You can usually spot underfitting immediately because training accuracy itself is disappointing.

**Overfitting** is subtler and more dangerous. Here the model has *too much* capacity relative to the amount of training data. Instead of learning the underlying pattern, it memorizes noise — the random fluctuations specific to your particular training set. A polynomial of degree 50 can pass exactly through 50 data points, achieving zero training error, while making absurd predictions between those points. The telltale signature is a gap: training performance is excellent, but validation performance is significantly worse. The model has learned to ace the exam by memorizing answers rather than understanding the subject.

The key diagnostic tool is the **training-validation gap**. You split your data, train on one portion, and evaluate on the held-out portion. If both errors are high, you are underfitting. If training error is low but validation error is high, you are overfitting. If both are low and close together, your model's capacity is well-matched to the problem. During training, you can plot both curves over time: the training loss typically decreases steadily, while the validation loss decreases at first (the model is learning real patterns) and then starts increasing (the model is beginning to memorize noise). The point where validation loss begins to climb is the sweet spot — training beyond it buys you nothing on new data and actively hurts generalization. This monitoring discipline, combined with techniques like regularization and early stopping, is what separates models that perform well in the lab from models that perform well in the real world.
