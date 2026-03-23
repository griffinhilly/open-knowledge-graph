---
id: semi-supervised-learning
title: Semi-Supervised Learning
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: supervised-learning-intro
  type: hard
builds-toward:
- self-supervised-learning
- pseudo-labeling
tags:
- semi-supervised
- unlabeled-data
- self-training
stage: advanced
status: validated
---

# Semi-Supervised Learning

## Core Idea
Semi-supervised learning leverages both labeled and abundant unlabeled data. Techniques include self-training (pseudo-labeling unlabeled data), consistency regularization (enforcing prediction invariance under perturbations), and co-training (multiple models train each other). This practical approach handles scenarios where labeling is expensive but unlabeled data is plentiful.

## Questions

```yaml
- question: "A machine learning team has 200 labeled examples and 200,000 unlabeled examples. They apply a semi-supervised method and find it performs worse than a supervised model trained only on the 200 labeled examples. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "200,000 unlabeled examples is too many; semi-supervised methods work best with a 1:10 labeled-to-unlabeled ratio"
    - "The cluster assumption does not hold — class boundaries pass through dense regions of the feature space, so unlabeled data misleads the model"
    - "Semi-supervised learning requires at least 1,000 labeled examples to function properly"
    - "The model architecture was too simple to exploit the unlabeled data structure"
  answer: 1
  explanation: "Semi-supervised methods assume that data in the same cluster share a label, so the unlabeled data reveals cluster structure that guides the decision boundary into low-density gaps. When this assumption fails — when class boundaries run through the middle of dense clusters — unlabeled data actively misleads the model, pushing decision boundaries into the wrong places. More unlabeled data then makes things worse, not better. The cluster (or smoothness) assumption is a prerequisite, not a guarantee."

- question: "In self-training (pseudo-labeling), a model assigns confident predictions to unlabeled examples and adds them to the training set. What is the primary risk of this approach?"
  type: multiple-choice
  options:
    - "The model will label too few examples, failing to benefit from the unlabeled data"
    - "Confident but incorrect pseudo-labels compound through subsequent retraining iterations, amplifying early errors"
    - "The approach violates the i.i.d. assumption because pseudo-labels are correlated with the original predictions"
    - "The model will overfit the labeled data because pseudo-labels lack the diversity of real annotations"
  answer: 1
  explanation: "Self-training's fundamental risk is error propagation. If the initial model makes a confident but wrong prediction, that pseudo-label enters the training set, reinforcing the mistake in the next iteration. The next model becomes more confidently wrong on those examples, labels more similar examples incorrectly, and the error compounds. Confidence thresholds mitigate but do not eliminate this — the initial model must be reasonably accurate, and the threshold must be high enough to filter out most mistakes."

- question: "Semi-supervised methods like FixMatch rely on the principle that a model's prediction should be consistent across different augmented views of the same unlabeled example, which pushes decision boundaries away from dense data regions."
  type: true-false
  answer: true
  explanation: "This is consistency regularization, the key principle behind methods like MixMatch, UDA, and FixMatch. By penalizing prediction differences between weakly and strongly augmented versions of the same input, the model is forced to place its decision boundary where small perturbations don't flip the prediction — which tends to be in low-density gaps between clusters. This is more principled than raw pseudo-labeling because it doesn't require the initial model to make correct predictions, only consistent ones."

- question: "Adding more unlabeled data to a semi-supervised learning system will always improve or at least not harm model performance compared to supervised learning on the labeled set alone."
  type: true-false
  answer: false
  explanation: "This is a common and dangerous misconception. When the cluster assumption fails, unlabeled data actively degrades performance by steering the decision boundary in the wrong direction. Semi-supervised methods can legitimately underperform a purely supervised baseline when class boundaries are not aligned with density structure. This is well-documented empirically. The decision to use SSL should depend on whether the data distribution satisfies the assumption, not on the availability of unlabeled data."

- question: "What is the cluster assumption in semi-supervised learning, and why does whether it holds determine whether SSL helps or hurts?"
  type: short-answer
  answer: "The cluster assumption states that data points in the same cluster in feature space tend to share the same class label — equivalently, that decision boundaries should pass through low-density regions between clusters, not through dense regions. When this holds, unlabeled data reveals cluster structure (which clusters exist and where they are), and even a few labeled points per cluster are enough to assign labels to the whole cluster. When it fails, the cluster structure is irrelevant to or contradicts the class boundaries, so unlabeled data misleads the model about where to place those boundaries."
  explanation: "The cluster assumption is the core precondition that makes SSL useful. It connects unsupervised structure (density, clusters) to supervised signal (labels). Without it, unlabeled data provides no useful information about the decision boundary and may actively corrupt the model by pushing boundaries into class-dense regions."
```

## Explainer

In supervised learning, every training example comes with a label, and the model learns the mapping from inputs to outputs. But labeling data is often expensive — a radiologist must examine each X-ray, a linguist must annotate each sentence, a human must categorize each support ticket. Meanwhile, *unlabeled* data is cheap and abundant: the internet is full of images, text, and recordings that nobody has annotated. **Semi-supervised learning** bridges this gap by using a small set of labeled examples together with a large pool of unlabeled examples, extracting structural information from the unlabeled data to improve predictions.

The simplest semi-supervised technique is **self-training** (also called pseudo-labeling). You train a supervised model on your labeled data, use it to predict labels for the unlabeled data, then add the most confident predictions to your training set and retrain. This bootstrapping process iteratively expands the labeled pool. The risk is obvious: if the initial model makes confident but wrong predictions, those errors propagate and compound. Self-training works best when the initial model is reasonably accurate and the confidence threshold for accepting pseudo-labels is set high enough to filter out mistakes.

**Consistency regularization** takes a more principled approach based on a smoothness assumption: if two inputs are similar, their predictions should also be similar. The model is shown an unlabeled example and a perturbed version of that same example (with noise, data augmentation, or dropout), and the loss penalizes any difference between the two predictions. This forces the decision boundary away from dense regions of the input space, pushing it into low-density gaps between clusters — which is where you want it. **FixMatch**, a widely used method, combines pseudo-labeling with consistency regularization: it generates a pseudo-label from a weakly augmented view of an unlabeled example, then trains the model to predict that label from a strongly augmented view, only keeping examples where the weak-augmentation prediction exceeds a confidence threshold.

**Co-training** uses a different strategy: train two models on different "views" of the data (different feature subsets or different architectures) and have each model label unlabeled examples for the other. Because the models have different inductive biases, they tend to make different mistakes — so one model's confident predictions on examples the other finds ambiguous provide genuinely informative training signal. The key assumption underlying all semi-supervised methods is the **cluster assumption**: that data points in the same cluster in feature space tend to share a label. When this assumption holds, unlabeled data reveals the cluster structure, and even a few labeled points per cluster are enough to assign labels to the rest. When the assumption fails — when class boundaries run through the middle of dense clusters — semi-supervised methods can actually hurt performance compared to supervised learning on the labeled data alone.
