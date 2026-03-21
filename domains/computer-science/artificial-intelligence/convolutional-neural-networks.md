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

## Questions

```yaml
- question: "A CNN is trained on images of stop signs appearing in the center of frames. A new image has a stop sign in the upper-left corner. What does the CNN's convolutional architecture predict?"
  type: multiple-choice
  options:
    - "The network fails — it learned weights specific to the center position and must be retrained"
    - "The activation for the stop sign feature shifts to the upper-left of the feature map, because CNNs are translation equivariant"
    - "Pooling layers correct for position, producing the same output regardless of where the sign appears"
    - "The network detects the sign only if it was also trained on images with upper-left stop signs"
  answer: 1
  explanation: "Translation equivariance is the core property of convolutional layers: the same filter slides across every position, so detecting a feature in a new location simply means the corresponding activation appears at the new position in the feature map. This is fundamentally different from a fully connected network, where each input position has unique weights — a pattern at a new position truly would require retraining. The equivariance property is not an accident; it is a direct consequence of weight sharing. Note that pooling adds approximate translation invariance (the final output may not change at all for small shifts), but equivariance in the feature maps comes from convolution itself."

- question: "Why does weight sharing in a convolutional layer dramatically reduce the number of parameters compared to a fully connected layer processing the same input?"
  type: multiple-choice
  options:
    - "Convolutional layers use simpler activation functions that require fewer computations"
    - "The same small filter (e.g., 3×3 weights) is applied at every spatial position, so filter parameters are not duplicated per position"
    - "Pooling layers remove most neurons before any learned weights are applied"
    - "CNNs process each color channel independently, reducing the effective input size"
  answer: 1
  explanation: "In a fully connected layer, every input pixel has its own unique weight connecting it to every neuron — for a 256×256 image with 1,000 hidden neurons, that is ~200 million weights. In a convolutional layer with a 3×3 filter, those 9 weights (plus a bias) are shared across all spatial positions. If the input is 256×256, the same 9 weights are applied at each of ~65,000 positions. Parameter count drops from millions to single digits per filter. The network learns fewer numbers but applies them everywhere — which also encodes the assumption that the same local feature detector is useful throughout the image."

- question: "A convolutional layer is translation equivariant: moving a feature in the input produces a corresponding shift in the feature map output."
  type: true-false
  answer: true
  explanation: "Translation equivariance is a defining property of convolution. Because the filter slides across the entire input with the same weights, detecting a pattern at position (x, y) produces an activation at the corresponding location in the output feature map. If the pattern moves to (x+5, y+3), the activation shifts by the same amount. This is not translation invariance (same output regardless of position) — the output changes, but in a perfectly predictable, consistent way. Equivariance is what allows early layers to detect features and later layers to combine them regardless of absolute position."

- question: "Max pooling layers are what give CNNs their translation equivariance property."
  type: true-false
  answer: false
  explanation: "Translation equivariance comes from the convolutional layers, not from pooling. Pooling provides a related but different property: approximate translation invariance — small shifts in the input may produce the same pooled output, because the maximum value within a region is unaffected by small displacements. Equivariance (output shifts with input) is a property of convolution. Invariance (output stays the same) is what pooling adds. Conflating the two is a common error. Many tasks benefit from equivariance in intermediate representations (to locate features) and invariance at the final output (to classify regardless of exact position)."

- question: "What inductive bias does a CNN encode, and why does this make it more appropriate than a fully connected network for image classification?"
  type: short-answer
  answer: "A CNN encodes the inductive bias that useful visual features are local (detectable from small patches) and position-independent (the same feature detector should work everywhere in the image). This is captured by small filters (locality) and weight sharing (position independence). A fully connected network has no such bias — it treats every pixel as equally related to every other, must independently learn that the same edge detector is useful at the top-left and bottom-right, and requires far more data and parameters to match a CNN's performance on images."
  explanation: "An inductive bias is a prior assumption about the structure of the problem baked into the architecture. CNNs encode two: local connectivity (nearby pixels are more related than distant ones) and translation equivariance (the same patterns matter regardless of position). These assumptions are almost always true for natural images, which is why CNNs are so effective at image tasks even with limited training data. Fully connected networks can theoretically represent the same functions, but they need exponentially more data to discover these spatial regularities from scratch."
```

## Explainer

From backpropagation, you know how to train a fully connected neural network by computing gradients of a loss function with respect to every weight. Now imagine feeding a 256×256 color image into such a network. The input has 256 × 256 × 3 ≈ 196,000 values. If the first hidden layer has just 1,000 neurons, that is nearly 200 million weights in a single layer — far too many to train effectively, and the network would have no understanding that nearby pixels are more related than distant ones. **Convolutional neural networks** solve both problems by replacing full connections with small, sliding filters that exploit the spatial structure of images.

A **convolutional layer** applies a small filter (typically 3×3 or 5×5 pixels) that slides across the entire input, computing a dot product at each position. This produces a **feature map** — a 2D output where each value indicates how strongly that local patch of the image matches the filter's pattern. A single layer applies many such filters in parallel, each learning to detect a different feature. In early layers, filters typically learn edges, corners, and color gradients. In deeper layers, they compose these into textures, parts (like eyes or wheels), and eventually whole objects. The critical insight is **weight sharing**: the same filter with the same weights is applied at every spatial position. This means the network uses the same detector everywhere, dramatically reducing the number of parameters and making the network **translation equivariant** — if a cat's ear moves 50 pixels to the right in the image, the corresponding activation in the feature map also shifts by 50 pixels.

**Pooling layers** (typically max pooling) follow convolutional layers and reduce the spatial dimensions by summarizing small regions — for example, taking the maximum value in each 2×2 block. This serves two purposes: it reduces the computational cost for subsequent layers, and it introduces a degree of **translation invariance** — small shifts in the input produce the same pooled output. The combination of convolution (detecting local features with shared weights) followed by pooling (compressing spatial resolution) is repeated several times, creating a hierarchy of increasingly abstract representations. The final feature maps are flattened and fed into one or more fully connected layers that produce the classification output.

Training a CNN uses the same backpropagation algorithm you already know, but the gradient computation is adapted for the convolution operation. Because weights are shared across all spatial positions, the gradient for each filter weight is the sum of gradients from every position where that filter was applied. This makes CNNs not only more parameter-efficient but also faster to train than equivalently expressive fully connected networks. Modern architectures like ResNet, VGG, and EfficientNet are variations on this theme, adding skip connections, deeper stacks, and architecture search. The core principle remains unchanged: by building spatial locality and weight sharing into the network's structure, CNNs encode a powerful **inductive bias** — the assumption that the same local patterns are relevant regardless of where they appear — that makes them extraordinarily effective for images, video, audio spectrograms, and any data with grid-like spatial structure.
