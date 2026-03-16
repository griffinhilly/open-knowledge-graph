---
id: few-shot-learning
title: Few-Shot Learning
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: transfer-learning-neural
  type: hard
builds-toward:
- zero-shot-learning
- prototypical-networks
tags:
- few-shot
- low-data
- rapid-adaptation
stage: advanced
status: draft
---

# Few-Shot Learning

## Core Idea
Few-shot learning enables models to learn new classes from very few examples (1-shot, 5-shot) by leveraging prior knowledge. Metric learning approaches learn similarity functions; model-agnostic meta-learning discovers good initializations. Prototypical networks classify based on distances to learned class prototypes in embedding space.

## Explainer

From your study of transfer learning, you know that a model trained on one task can be adapted to a new task by reusing learned representations — typically by fine-tuning a pretrained network on new labeled data. But what if you have only one or five examples of each new class? Standard fine-tuning on so little data will catastrophically overfit. **Few-shot learning** addresses this extreme low-data regime by training models that are explicitly designed to generalize from minimal examples, typically framed as **N-way K-shot** problems: classify among N new classes given only K labeled examples per class.

The training paradigm is fundamentally different from standard supervised learning. Instead of training on a fixed set of classes, few-shot learning uses **episodic training**: each training episode samples a small subset of classes and a handful of examples per class, mimicking the few-shot scenario the model will face at test time. The model learns not to classify specific classes, but to *learn how to classify* — a form of **meta-learning** (learning to learn). Over thousands of episodes with different class subsets, the model develops general-purpose abilities for rapid adaptation.

The two dominant approaches differ in what they meta-learn. **Metric learning** methods learn an embedding function that maps examples into a space where same-class examples cluster together and different-class examples are far apart. **Prototypical networks** are the clearest example: embed all K support examples for each class, compute the mean embedding (the **prototype**) for each class, and classify a new query by finding the nearest prototype. The training objective simply pushes the embedding network to create clusters that are tight within each class and well-separated between classes. **Siamese networks** take a pairwise approach, learning to predict whether two examples belong to the same class. These methods are elegant because at test time, they require no gradient updates — just a forward pass and a distance computation.

**Model-Agnostic Meta-Learning (MAML)** takes the alternative approach of meta-learning an initialization. The idea is to find a set of network parameters that, when fine-tuned with just a few gradient steps on K examples of new classes, rapidly achieves good performance. MAML trains by simulating this inner fine-tuning loop across many episodes and optimizing the initial parameters so that the post-fine-tuning performance is maximized. This requires computing gradients through gradients (second-order optimization), which is computationally expensive but remarkably flexible — it works with any model architecture and any differentiable loss. The intuition is that MAML finds a point in parameter space that is close to good solutions for many tasks simultaneously, so a few steps of gradient descent on any specific task lands in the right neighborhood.
