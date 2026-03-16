---
id: contrastive-learning
title: Contrastive Learning
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: self-supervised-learning
  type: hard
- id: representation-learning
  type: hard
builds-toward:
- metric-learning
- similarity-learning
tags:
- contrastive
- similarity
- representation
stage: advanced
status: draft
---

# Contrastive Learning

## Core Idea
Contrastive learning learns representations by contrasting similar (positive) and dissimilar (negative) pairs. Methods like SimCLR and MoCo maximize agreement between augmented views of the same instance. The key insight is that semantically similar data should have similar representations. This is powerful for self-supervised pretraining without labels.

## Explainer

From your study of self-supervised and representation learning, you know the central challenge: how do you learn useful feature representations without labeled data? Contrastive learning answers this by turning an unlabeled dataset into a classification-like task where the model learns to distinguish "same thing, different view" from "different things entirely."

The setup works like this. Take a single image — say, a photo of a dog. Apply two different random **data augmentations** (crop, color jitter, rotation, blur) to produce two views of the same image. These two views form a **positive pair**: they look different at the pixel level but depict the same semantic content. All other images in the batch serve as **negative pairs**. The model encodes both views through a shared neural network and is trained to make the representations of the positive pair similar (high cosine similarity) while pushing representations of negative pairs apart. The loss function — typically **InfoNCE** or **NT-Xent** — formalizes this as a softmax over similarities: the model tries to pick out the positive pair from a set of negatives, much like a classification task with one correct answer among many distractors.

**SimCLR** implements this directly: each training batch of N images produces 2N augmented views, yielding N positive pairs and 2(N−1) negatives per pair. The key findings were that (1) composition of multiple augmentations matters far more than any single augmentation, (2) a nonlinear **projection head** between the representation and the contrastive loss dramatically improves learned features, and (3) large batch sizes are critical because more negatives give the model harder discrimination tasks and richer gradients. **MoCo** (Momentum Contrast) addresses the batch size constraint by maintaining a large queue of negative representations from previous batches, updated through a slowly-moving momentum encoder. This decouples the number of negatives from the batch size, making contrastive learning practical on standard hardware.

Why does this work at all? The augmentations are chosen so that the information they preserve is exactly the semantic content that matters for downstream tasks — object identity, shape, texture relationships — while the information they destroy (exact position, color balance, scale) is irrelevant. By forcing the model to map augmented views of the same image to nearby points in representation space, contrastive learning implicitly teaches the network to encode the invariances that define meaningful visual similarity. The resulting representations transfer remarkably well: a ResNet pretrained with SimCLR on unlabeled ImageNet matches or approaches the performance of supervised pretraining when fine-tuned on downstream classification, detection, and segmentation tasks.

Recent advances have moved beyond pairwise contrasting. Methods like **BYOL** and **SimSiam** achieve comparable results without negative pairs at all, using only positive pairs with architectural tricks (stop-gradients, momentum encoders) to prevent the trivial solution of mapping everything to the same point. These developments suggest that the core mechanism is not contrast per se but rather learning augmentation-invariant representations — the negatives serve mainly to prevent collapse, and there are other ways to accomplish that. Nonetheless, the contrastive framework remains foundational: it established that self-supervised pretraining could compete with labels and provided the conceptual vocabulary (positive pairs, negative pairs, augmentation invariance) that the entire field now uses.
