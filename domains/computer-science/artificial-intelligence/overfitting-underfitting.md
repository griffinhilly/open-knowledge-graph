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
status: validated
---

# Overfitting, Underfitting, and Model Capacity

## Core Idea
Overfitting occurs when a model memorizes training data and fails to generalize; underfitting means the model is too simple to capture patterns. Model capacity—determined by parameters and architecture—must match problem complexity. Detecting overfitting requires separate validation data and monitoring the train-validation gap.

## Questions

```yaml
- question: "A neural network achieves 99% accuracy on training data but only 61% accuracy on the held-out validation set. Which condition does this describe, and what is the most appropriate remedy?"
  type: multiple-choice
  options:
    - "Underfitting; increase model depth or add more input features"
    - "Overfitting; the model has memorized training noise — apply regularization, dropout, or gather more training data"
    - "Underfitting; the training set is too small to represent the problem"
    - "Overfitting; reduce training time by stopping after fewer gradient steps regardless of validation trend"
  answer: 1
  explanation: "The large train-validation gap (99% vs 61%) is the classic signature of overfitting: the model has learned the specific noise and idiosyncrasies of the training set rather than the generalizable pattern. The fix targets capacity versus data: add more training data (so there is less room for noise to dominate), apply regularization (constrain weights), or use dropout (prevent co-adaptation of neurons). Simply stopping early (option D) can help but is incomplete — the core issue is model capacity relative to data."

- question: "While training a model, you plot training loss and validation loss over epochs. Training loss decreases steadily throughout; validation loss decreases for the first 30 epochs, then starts rising. What does this pattern indicate?"
  type: multiple-choice
  options:
    - "Underfitting — the model cannot learn the training data and is struggling"
    - "Ideal convergence — both losses will eventually meet at a low value if training continues"
    - "The onset of overfitting — after epoch 30 the model begins memorizing noise, harming generalization"
    - "A bug in validation loss calculation — valid loss cannot rise if training loss is still falling"
  answer: 2
  explanation: "This divergence pattern is the definitive signature of overfitting in progress. Up to epoch 30, the model is extracting real patterns that generalize — both losses improve. After that, the model is fitting the noise unique to the training set; training loss keeps dropping (better memorization) while validation loss rises (worse generalization). Epoch 30 is the sweet spot — the point of best generalization before memorization dominates. Techniques like early stopping use exactly this signal."

- question: "A model that achieves low training error and low validation error, with a small gap between them, has achieved well-matched capacity for the problem."
  type: true-false
  answer: true
  explanation: "Low and similar errors on both training and validation data indicate the model has learned patterns that generalize: it neither memorizes noise (which would inflate the train-validation gap) nor oversimplifies (which would leave both errors high). This is the diagnostic target — the training-validation gap is the key signal for diagnosing capacity problems."

- question: "A model with very high training error is almost certainly overfitting the training data."
  type: true-false
  answer: false
  explanation: "High training error indicates underfitting — the model cannot capture patterns even in the data it was trained on. Overfitting requires the opposite: the model fits the training data very well (low training error) but fails to generalize (high validation error). The confusion arises because both are 'failure modes,' but they point in opposite directions: overfitting is too much capacity, underfitting is too little. The distinction is critical because they call for opposite remedies."

- question: "Why does achieving low training error fail as a sufficient criterion for evaluating a machine learning model?"
  type: short-answer
  answer: "Low training error can be achieved by memorizing the training data rather than learning the underlying pattern. A sufficiently complex model can fit any finite dataset perfectly — including its noise and measurement artifacts — while making nonsensical predictions on new data. Validation error on held-out data is required because it exposes whether the model generalizes: a model that truly learned the pattern will perform well on examples it has never seen, while a memorized model will not."
  explanation: "This is the fundamental distinction between memorization and generalization. The entire discipline of model evaluation exists because training performance is a necessary but wildly insufficient indicator of real-world performance. Every production ML workflow requires a held-out test set precisely because training performance tells you how well the model knows the training set, not how well it understands the problem."
```

## Explainer

From the bias-variance tradeoff, you know that prediction error comes from two sources: bias (systematic inaccuracy from overly simple assumptions) and variance (sensitivity to the particular training data you happened to draw). **Overfitting** and **underfitting** are the practical manifestations of this tradeoff. Understanding them transforms the bias-variance concept from theory into a diagnostic you can apply to every model you build.

**Underfitting** means your model cannot capture the real patterns in the data. Imagine fitting a straight line to data that follows a parabola — no matter how much data you collect, the line will systematically miss the curve. The model's **capacity** (its ability to represent complex functions) is too low for the problem. Underfitting shows up as poor performance on *both* the training data and new data. The fix is straightforward: use a more flexible model, add features, or reduce excessive regularization. You can usually spot underfitting immediately because training accuracy itself is disappointing.

**Overfitting** is subtler and more dangerous. Here the model has *too much* capacity relative to the amount of training data. Instead of learning the underlying pattern, it memorizes noise — the random fluctuations specific to your particular training set. A polynomial of degree 50 can pass exactly through 50 data points, achieving zero training error, while making absurd predictions between those points. The telltale signature is a gap: training performance is excellent, but validation performance is significantly worse. The model has learned to ace the exam by memorizing answers rather than understanding the subject.

The key diagnostic tool is the **training-validation gap**. You split your data, train on one portion, and evaluate on the held-out portion. If both errors are high, you are underfitting. If training error is low but validation error is high, you are overfitting. If both are low and close together, your model's capacity is well-matched to the problem. During training, you can plot both curves over time: the training loss typically decreases steadily, while the validation loss decreases at first (the model is learning real patterns) and then starts increasing (the model is beginning to memorize noise). The point where validation loss begins to climb is the sweet spot — training beyond it buys you nothing on new data and actively hurts generalization. This monitoring discipline, combined with techniques like regularization and early stopping, is what separates models that perform well in the lab from models that perform well in the real world.
