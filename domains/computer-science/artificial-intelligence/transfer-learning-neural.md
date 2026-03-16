---
id: transfer-learning-neural
title: Transfer Learning in Neural Networks
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: neural-networks-intro
  type: hard
- id: supervised-learning-intro
  type: hard
- id: convolutional-neural-networks
  type: soft
- id: linear-transformations
  type: soft
- id: gradient-descent-optimization
  type: soft
builds-toward:
- fine-tuning-pretrained-models
tags:
- transfer-learning
- domain-adaptation
- feature-reuse
- representation-learning
stage: advanced
status: draft
---

# Transfer Learning in Neural Networks

## Core Idea
Transfer learning reuses features learned on large source tasks (e.g., ImageNet) for small target tasks, dramatically reducing data and computation requirements. Early layers capture generic features shared across domains while later layers are task-specific; freezing early layers and fine-tuning later layers is an effective strategy when target data is limited.

## How It's Best Learned
Use a pretrained ImageNet model and fine-tune it on a small target dataset, comparing final accuracy with training from scratch to see transfer learning benefits.

## Explainer

Training a neural network from scratch requires vast amounts of labeled data and compute. A deep CNN for image classification might have millions of parameters, and fitting them all from random initialization on a small dataset — say, 500 images of medical scans — leads to severe overfitting. **Transfer learning** sidesteps this problem by starting from a network that has already been trained on a large, general dataset, then adapting it to the specific task at hand. The insight is that many of the features a network learns are not task-specific — they are reusable building blocks.

Research on CNNs has revealed a striking pattern in what different layers learn. **Early layers** (close to the input) learn generic, low-level features: edge detectors, color gradients, texture patterns. These features are useful for virtually any visual task — detecting edges matters whether you are classifying dogs, diagnosing tumors, or reading street signs. **Later layers** combine these primitives into increasingly task-specific representations: dog faces, tumor shapes, letter forms. This hierarchy means that a network trained on ImageNet's 1.2 million images across 1,000 categories has already learned a rich vocabulary of visual features that transfer broadly.

The standard **fine-tuning** procedure works as follows. Take a pretrained network (the **source model**), remove its final classification layer, and replace it with a new layer sized for your target task. Then retrain, typically with a small learning rate so the pretrained weights shift gently rather than being destroyed. A common strategy is to **freeze** the early layers entirely (their generic features are already good) and only update the later layers and the new classification head. When target data is very scarce, freezing more layers prevents overfitting; when target data is abundant, unfreezing more layers allows deeper adaptation. This is a spectrum, and the right balance depends on how similar the source and target domains are.

The effectiveness of transfer learning depends on **domain similarity**. Transferring from ImageNet to a medical imaging task works well because both involve natural images with edges, textures, and shapes — the low-level features transfer cleanly. Transferring from ImageNet to satellite imagery still helps but less so, because the visual statistics differ more. Transferring from images to audio spectrograms can even work, since spectrograms share some structural properties with images. The more distant the domains, the fewer layers are worth keeping frozen. In all cases, transfer learning dramatically reduces the data and compute needed to reach strong performance — a pretrained model fine-tuned on 500 examples routinely outperforms a model trained from scratch on 5,000.
