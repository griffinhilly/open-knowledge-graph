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
status: draft
---

# Semi-Supervised Learning

## Core Idea
Semi-supervised learning leverages both labeled and abundant unlabeled data. Techniques include self-training (pseudo-labeling unlabeled data), consistency regularization (enforcing prediction invariance under perturbations), and co-training (multiple models train each other). This practical approach handles scenarios where labeling is expensive but unlabeled data is plentiful.

## Explainer

In supervised learning, every training example comes with a label, and the model learns the mapping from inputs to outputs. But labeling data is often expensive — a radiologist must examine each X-ray, a linguist must annotate each sentence, a human must categorize each support ticket. Meanwhile, *unlabeled* data is cheap and abundant: the internet is full of images, text, and recordings that nobody has annotated. **Semi-supervised learning** bridges this gap by using a small set of labeled examples together with a large pool of unlabeled examples, extracting structural information from the unlabeled data to improve predictions.

The simplest semi-supervised technique is **self-training** (also called pseudo-labeling). You train a supervised model on your labeled data, use it to predict labels for the unlabeled data, then add the most confident predictions to your training set and retrain. This bootstrapping process iteratively expands the labeled pool. The risk is obvious: if the initial model makes confident but wrong predictions, those errors propagate and compound. Self-training works best when the initial model is reasonably accurate and the confidence threshold for accepting pseudo-labels is set high enough to filter out mistakes.

**Consistency regularization** takes a more principled approach based on a smoothness assumption: if two inputs are similar, their predictions should also be similar. The model is shown an unlabeled example and a perturbed version of that same example (with noise, data augmentation, or dropout), and the loss penalizes any difference between the two predictions. This forces the decision boundary away from dense regions of the input space, pushing it into low-density gaps between clusters — which is where you want it. **FixMatch**, a widely used method, combines pseudo-labeling with consistency regularization: it generates a pseudo-label from a weakly augmented view of an unlabeled example, then trains the model to predict that label from a strongly augmented view, only keeping examples where the weak-augmentation prediction exceeds a confidence threshold.

**Co-training** uses a different strategy: train two models on different "views" of the data (different feature subsets or different architectures) and have each model label unlabeled examples for the other. Because the models have different inductive biases, they tend to make different mistakes — so one model's confident predictions on examples the other finds ambiguous provide genuinely informative training signal. The key assumption underlying all semi-supervised methods is the **cluster assumption**: that data points in the same cluster in feature space tend to share a label. When this assumption holds, unlabeled data reveals the cluster structure, and even a few labeled points per cluster are enough to assign labels to the rest. When the assumption fails — when class boundaries run through the middle of dense clusters — semi-supervised methods can actually hurt performance compared to supervised learning on the labeled data alone.
