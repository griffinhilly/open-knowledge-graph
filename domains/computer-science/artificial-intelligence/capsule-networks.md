---
id: capsule-networks
title: Capsule Networks
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: convolutional-neural-networks
  type: hard
- id: neural-networks-intro
  type: hard
builds-toward:
- 3d-vision
- routing-algorithms
tags:
- capsule-network
- capsnet
- routing
stage: advanced
status: draft
---

# Capsule Networks

## Core Idea
Capsule networks replace scalar neurons with vector-valued capsules encoding domain-specific properties (position, rotation). Routing-by-agreement algorithms dynamically route information based on capsule predictions. CapsNets improve viewpoint equivariance and reduce data requirements compared to CNNs, though computation is higher.

## Explainer

From your study of convolutional neural networks, you know that CNNs detect features hierarchically — edges in early layers, textures and parts in middle layers, whole objects in later layers. But CNNs have a fundamental limitation rooted in their use of **max pooling**: they detect whether a feature is present somewhere in a region but discard precise information about where it is, what orientation it has, and how it relates spatially to other features. A CNN trained on faces can detect two eyes and a mouth, but after pooling, it has limited ability to verify that they are in the correct spatial arrangement. A jumbled face with eyes below the mouth might still activate the same "face" neurons. **Capsule networks** were designed to fix this by preserving spatial relationships between parts.

The key architectural change is replacing scalar-output neurons with **capsules** — small groups of neurons whose output is a vector rather than a single number. The vector's length represents the probability that a particular entity (an edge, a nose, a face) exists, while its orientation encodes **instantiation parameters**: the entity's position, size, rotation, texture, and other properties. For example, a "mouth capsule" might output a vector whose length indicates confidence that a mouth is present, while the direction encodes the mouth's position, width, and tilt. This is fundamentally more expressive than a CNN neuron that can only say "mouth detected with 0.92 confidence."

The mechanism connecting capsules across layers is **routing by agreement**, which replaces the fixed pooling operations in CNNs. Each lower-level capsule (say, a "nose" capsule) makes a prediction about what the higher-level capsule (say, a "face" capsule) should look like, based on the spatial relationship it has learned. If the nose is detected at position (x, y) with a certain orientation, it predicts the face should be at a particular position and orientation. Multiple part-capsules all make their own predictions about the whole, and if these predictions **agree** — the nose, eyes, and mouth all predict a face in roughly the same place and pose — the routing algorithm strengthens those connections and activates the face capsule. Disagreement (parts predicting inconsistent wholes) weakens the connections. This is fundamentally different from pooling: instead of discarding spatial information, routing by agreement uses it to verify geometric consistency.

The practical consequence is improved **viewpoint equivariance**. When an object rotates, all part capsules update their instantiation parameters in a geometrically consistent way, and the routing algorithm still achieves agreement — the face is recognized regardless of pose. CNNs achieve viewpoint tolerance mainly through brute-force data augmentation (training on many rotated examples), while capsule networks achieve it structurally. This means CapsNets can generalize to novel viewpoints from fewer training examples. The tradeoff is computational cost: routing by agreement requires multiple iterative passes between layers, making capsule networks significantly slower to train than equivalently sized CNNs. This computational overhead, combined with difficulty scaling to large images, has limited CapsNet adoption in practice, though the ideas continue to influence research on geometric deep learning and equivariant architectures.
