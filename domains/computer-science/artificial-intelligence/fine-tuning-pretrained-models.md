---
id: fine-tuning-pretrained-models
title: Fine-Tuning Pretrained Models
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: transfer-learning-neural
  type: hard
- id: backpropagation
  type: hard
- id: hyperparameter-optimization
  type: soft
- id: gradient-descent-optimization
  type: soft
tags:
- transfer-learning
- optimization
- adaptation
- feature-learning
stage: advanced
status: draft
---

# Fine-Tuning Pretrained Models

## Core Idea
Fine-tuning adapts a pretrained model to a new task by continuing training on task-specific data, often with a lower learning rate to avoid catastrophically forgetting learned features. The number of layers to fine-tune balances adaptation (more layers) with regularization (fewer layers); layer-wise learning rates (lower for early layers) are effective for training stability.

## How It's Best Learned
Compare different fine-tuning strategies: frozen base layers only, unfrozen with low learning rate, and layer-wise varying learning rates, measuring final accuracy and computational cost.

## Explainer

From transfer learning, you know that a neural network trained on a large dataset learns features that are useful far beyond its original task. The early layers of an image classifier trained on ImageNet learn edge detectors, texture recognizers, and color patterns; the middle layers learn parts and shapes; the later layers learn task-specific compositions. **Fine-tuning** is the process of taking such a pretrained model and adapting it to your specific task — say, classifying medical images or identifying bird species — by continuing training on your (typically smaller) dataset.

The simplest approach is **feature extraction**: freeze all the pretrained layers, replace the final classification head with a new one matching your number of classes, and train only that new head. This treats the pretrained network as a fixed feature extractor. It works well when your task is similar to the original and your dataset is small, because you are only optimizing a few parameters and cannot overfit easily. But if your task differs significantly from the pretraining domain (e.g., medical X-rays versus natural photos), the frozen features may not transfer perfectly, and you need to let deeper layers adapt.

Full fine-tuning unfreezes all layers and trains the entire network on your data, but this requires care. The key risk is **catastrophic forgetting**: if you train with a normal learning rate, the useful features in the early layers get overwritten before the network can adapt them to the new task. The solution is to use a **much lower learning rate** than you would for training from scratch — typically 10× to 100× smaller. This lets the weights drift gently toward task-specific solutions without destroying the pretrained representations. Think of it as nudging the network rather than retraining it.

The most sophisticated strategy uses **discriminative (layer-wise) learning rates**, where early layers get the smallest learning rate and later layers get progressively larger ones. The rationale is that early features (edges, textures) are nearly universal and need minimal adjustment, while later features are more task-specific and need more adaptation. A common recipe is to set the last layer's learning rate to some base value and reduce it by a factor of 2-3 for each preceding layer group. Combined with techniques like gradual unfreezing — starting by training only the head, then unfreezing one layer group at a time — this approach consistently achieves strong performance even with very small datasets. The number of layers to fine-tune becomes a regularization knob: fewer unfrozen layers means less capacity to adapt but also less risk of overfitting, making this a balance you tune based on dataset size and domain similarity.
