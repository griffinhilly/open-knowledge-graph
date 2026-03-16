---
id: self-supervised-learning
title: Self-Supervised Learning
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: neural-networks-intro
  type: hard
builds-toward:
- contrastive-learning
- transfer-learning-neural
tags:
- self-supervised
- pretext-task
- contrastive
stage: advanced
status: draft
---

# Self-Supervised Learning

## Core Idea
Self-supervised learning creates training signals from unlabeled data via pretext tasks (predicting rotations, masked token reconstruction). Contrastive methods maximize agreement between augmented views of the same instance. This approach learns rich, transferable representations without manual annotation, enabling powerful transfer learning.

## Explainer

Supervised learning requires labeled data — images tagged with categories, sentences paired with translations, audio matched to transcripts. Labeling is expensive, slow, and limited by human effort. Meanwhile, the internet overflows with *unlabeled* data: billions of images, pages of text, hours of video. **Self-supervised learning** (SSL) bridges this gap by creating supervision signals from the data itself, turning an unsupervised problem into a supervised one without any human annotation.

The trick is designing a **pretext task** — a problem where the labels can be generated automatically from the input. For images, early pretext tasks included predicting the rotation angle of a randomly rotated image, solving jigsaw puzzles of image patches, or colorizing grayscale photos. For text, the classic pretext task is **masked language modeling**: hide a word in a sentence and train the network to predict it from context (this is how BERT was trained). In each case, the model must learn meaningful representations of the input to solve the task. A network that can predict a missing word must understand grammar, semantics, and world knowledge; one that can predict rotation must understand object shape and orientation.

**Contrastive learning** has emerged as the dominant paradigm in self-supervised vision. The idea is elegant: take an image, create two different augmented views of it (crop, color-jitter, blur), and train the network to produce similar representations for these two views while pushing apart representations of different images. The model learns that both augmented views depict the same underlying content despite surface differences — forcing it to capture semantic features rather than low-level pixel statistics. Frameworks like SimCLR and MoCo implement this idea with different architectural choices for how negative examples are managed.

The representations learned through self-supervised pretraining are not an end in themselves — their value lies in **transfer**. After pretraining on a large unlabeled dataset, the model's weights encode general-purpose features that can be fine-tuned on a small labeled dataset for a specific downstream task. This two-stage approach — pretrain with self-supervision, then fine-tune with supervision — consistently outperforms training from scratch, especially when labeled data is scarce. It has become the dominant paradigm in modern AI: large language models, vision transformers, and multimodal systems all rely on self-supervised pretraining as their foundation.
