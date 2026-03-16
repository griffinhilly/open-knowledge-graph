---
id: convolutional-neural-networks
title: Convolutional Neural Networks
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: backpropagation
  type: hard
- id: matrix-multiplication
  type: soft
- id: partial-derivatives
  type: soft
- id: matrix-operations
  type: soft
tags:
- deep-learning
- computer-vision
- neural-networks
stage: advanced
status: draft
---

# Convolutional Neural Networks

## Core Idea
CNNs exploit spatial structure with convolutional layers learning local filters. Pooling reduces dimensionality preserving features. Shared weights reduce parameters and improve translation equivariance. CNNs dominate computer vision tasks.

## Explainer

From backpropagation, you know how to train a fully connected neural network by computing gradients of a loss function with respect to every weight. Now imagine feeding a 256×256 color image into such a network. The input has 256 × 256 × 3 ≈ 196,000 values. If the first hidden layer has just 1,000 neurons, that is nearly 200 million weights in a single layer — far too many to train effectively, and the network would have no understanding that nearby pixels are more related than distant ones. **Convolutional neural networks** solve both problems by replacing full connections with small, sliding filters that exploit the spatial structure of images.

A **convolutional layer** applies a small filter (typically 3×3 or 5×5 pixels) that slides across the entire input, computing a dot product at each position. This produces a **feature map** — a 2D output where each value indicates how strongly that local patch of the image matches the filter's pattern. A single layer applies many such filters in parallel, each learning to detect a different feature. In early layers, filters typically learn edges, corners, and color gradients. In deeper layers, they compose these into textures, parts (like eyes or wheels), and eventually whole objects. The critical insight is **weight sharing**: the same filter with the same weights is applied at every spatial position. This means the network uses the same detector everywhere, dramatically reducing the number of parameters and making the network **translation equivariant** — if a cat's ear moves 50 pixels to the right in the image, the corresponding activation in the feature map also shifts by 50 pixels.

**Pooling layers** (typically max pooling) follow convolutional layers and reduce the spatial dimensions by summarizing small regions — for example, taking the maximum value in each 2×2 block. This serves two purposes: it reduces the computational cost for subsequent layers, and it introduces a degree of **translation invariance** — small shifts in the input produce the same pooled output. The combination of convolution (detecting local features with shared weights) followed by pooling (compressing spatial resolution) is repeated several times, creating a hierarchy of increasingly abstract representations. The final feature maps are flattened and fed into one or more fully connected layers that produce the classification output.

Training a CNN uses the same backpropagation algorithm you already know, but the gradient computation is adapted for the convolution operation. Because weights are shared across all spatial positions, the gradient for each filter weight is the sum of gradients from every position where that filter was applied. This makes CNNs not only more parameter-efficient but also faster to train than equivalently expressive fully connected networks. Modern architectures like ResNet, VGG, and EfficientNet are variations on this theme, adding skip connections, deeper stacks, and architecture search. The core principle remains unchanged: by building spatial locality and weight sharing into the network's structure, CNNs encode a powerful **inductive bias** — the assumption that the same local patterns are relevant regardless of where they appear — that makes them extraordinarily effective for images, video, audio spectrograms, and any data with grid-like spatial structure.
