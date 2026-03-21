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

## Questions

```yaml
- question: "A CNN trained on faces correctly classifies a normal face image. When shown an image with two eyes positioned below the mouth (spatially scrambled), the CNN still outputs high confidence for 'face.' What architectural feature of CNNs explains this failure?"
  type: multiple-choice
  options:
    - "CNNs use too few layers to detect complex features like faces"
    - "Max pooling discards spatial position information, so the CNN detects that face parts are present but cannot verify their geometric arrangement"
    - "CNNs use ReLU activations which cannot represent negative spatial relationships"
    - "Softmax output layers normalize confidence scores in a way that ignores spatial order"
  answer: 1
  explanation: "Max pooling is specifically designed to detect whether a feature is present somewhere in a region while being invariant to exactly where. This is useful for translation tolerance, but it means pooled representations lose precise spatial information. After several pooling layers, the network knows it saw eyes and a mouth, but the spatial relationship between them has been summarized away. Capsule networks were designed to address exactly this limitation by preserving instantiation parameters (position, orientation) throughout the network."

- question: "In a capsule network, a 'mouth capsule' outputs a vector with length 0.95 and a specific orientation. What does each component represent?"
  type: multiple-choice
  options:
    - "The length represents the capsule's learning rate; the orientation represents the error gradient direction"
    - "The length represents the probability that a mouth is present; the orientation encodes instantiation parameters like position, size, and tilt"
    - "The length represents the number of training examples containing mouths; orientation encodes the class label"
    - "Both length and orientation together represent the capsule's confidence score, similar to a scalar neuron"
  answer: 1
  explanation: "This is the key architectural difference between capsules and conventional neurons. A scalar neuron outputs a single number (e.g., 'mouth detected with 0.95 confidence') that encodes only presence. A capsule's vector encodes two things simultaneously: its length encodes the probability that the entity exists, while its direction encodes how it exists — position, orientation, size, texture. This richer representation is what enables routing by agreement to verify geometric consistency between parts and wholes."

- question: "In routing by agreement, connections between lower-level capsules (parts) and higher-level capsules (wholes) are strengthened when the part capsules' predictions about the parent capsule are geometrically consistent with each other."
  type: true-false
  answer: true
  explanation: "This is the core mechanism of routing by agreement. Each part capsule makes a prediction about where and how a parent capsule should appear, based on the learned spatial transformation. If the nose capsule predicts a face at position (x, y) and the eye capsule predicts a face at approximately the same position and orientation, these predictions 'agree,' and the routing algorithm strengthens those connections, activating the face capsule. Disagreement weakens connections. This geometric verification is what allows capsule networks to reject spatially scrambled inputs that CNNs wrongly accept."

- question: "Capsule networks are more computationally efficient than CNNs because routing by agreement eliminates the need for multiple convolutional layers."
  type: true-false
  answer: false
  explanation: "The opposite is true. Routing by agreement requires multiple iterative passes between capsule layers — each iteration updates coupling coefficients based on agreement — making capsule networks significantly more computationally expensive than equivalently sized CNNs. This computational overhead has been a major barrier to scaling capsule networks to large images and datasets, limiting their practical adoption despite the theoretical elegance of the approach."

- question: "Why does a capsule's vector output achieve viewpoint equivariance more structurally than a CNN's pooling-based approach?"
  type: short-answer
  answer: "When an object rotates, all part capsules update their instantiation parameters (position, orientation) in a geometrically consistent way. Routing by agreement then still finds consensus among the updated predictions, activating the correct parent capsule. The recognition is tied to geometric relationships rather than specific pixel patterns, so novel viewpoints are handled by the same mechanism as familiar ones. CNNs, lacking explicit pose representation, achieve viewpoint tolerance mainly through data augmentation — training on many rotated examples — which is brittle and requires much more data."
  explanation: "Equivariance is different from invariance: equivariance means the output changes in a predictable way when the input transforms, while invariance means the output doesn't change at all. CNNs use pooling to achieve approximate invariance, discarding spatial information. Capsule networks are equivariant — when the input transforms, the capsule vectors update correspondingly, allowing the network to recognize the object in any pose it hasn't necessarily seen before."
```

## Explainer

From your study of convolutional neural networks, you know that CNNs detect features hierarchically — edges in early layers, textures and parts in middle layers, whole objects in later layers. But CNNs have a fundamental limitation rooted in their use of **max pooling**: they detect whether a feature is present somewhere in a region but discard precise information about where it is, what orientation it has, and how it relates spatially to other features. A CNN trained on faces can detect two eyes and a mouth, but after pooling, it has limited ability to verify that they are in the correct spatial arrangement. A jumbled face with eyes below the mouth might still activate the same "face" neurons. **Capsule networks** were designed to fix this by preserving spatial relationships between parts.

The key architectural change is replacing scalar-output neurons with **capsules** — small groups of neurons whose output is a vector rather than a single number. The vector's length represents the probability that a particular entity (an edge, a nose, a face) exists, while its orientation encodes **instantiation parameters**: the entity's position, size, rotation, texture, and other properties. For example, a "mouth capsule" might output a vector whose length indicates confidence that a mouth is present, while the direction encodes the mouth's position, width, and tilt. This is fundamentally more expressive than a CNN neuron that can only say "mouth detected with 0.92 confidence."

The mechanism connecting capsules across layers is **routing by agreement**, which replaces the fixed pooling operations in CNNs. Each lower-level capsule (say, a "nose" capsule) makes a prediction about what the higher-level capsule (say, a "face" capsule) should look like, based on the spatial relationship it has learned. If the nose is detected at position (x, y) with a certain orientation, it predicts the face should be at a particular position and orientation. Multiple part-capsules all make their own predictions about the whole, and if these predictions **agree** — the nose, eyes, and mouth all predict a face in roughly the same place and pose — the routing algorithm strengthens those connections and activates the face capsule. Disagreement (parts predicting inconsistent wholes) weakens the connections. This is fundamentally different from pooling: instead of discarding spatial information, routing by agreement uses it to verify geometric consistency.

The practical consequence is improved **viewpoint equivariance**. When an object rotates, all part capsules update their instantiation parameters in a geometrically consistent way, and the routing algorithm still achieves agreement — the face is recognized regardless of pose. CNNs achieve viewpoint tolerance mainly through brute-force data augmentation (training on many rotated examples), while capsule networks achieve it structurally. This means CapsNets can generalize to novel viewpoints from fewer training examples. The tradeoff is computational cost: routing by agreement requires multiple iterative passes between layers, making capsule networks significantly slower to train than equivalently sized CNNs. This computational overhead, combined with difficulty scaling to large images, has limited CapsNet adoption in practice, though the ideas continue to influence research on geometric deep learning and equivariant architectures.
