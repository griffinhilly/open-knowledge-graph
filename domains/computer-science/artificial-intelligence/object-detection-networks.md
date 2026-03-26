---
id: object-detection-networks
title: Object Detection Networks
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: convolutional-neural-networks
  type: hard
- id: transfer-learning-neural
  type: soft
builds-toward:
- semantic-segmentation
tags:
- computer-vision
- deep-learning
- object-detection
- localization
stage: advanced
status: validated
---

# Object Detection Networks

## Core Idea
Object detection networks locate and classify objects in images by predicting bounding boxes and class probabilities. Region-based methods (R-CNN, Faster R-CNN) propose regions then classify them; single-shot methods (YOLO, SSD) predict boxes directly, trading accuracy for speed; modern architectures use feature pyramids for multi-scale detection and non-maximum suppression to handle overlapping detections.

## How It's Best Learned
Implement object detection on images using a pretrained model, then fine-tune on a custom dataset to understand the tradeoffs between speed and accuracy.

## Questions

```yaml
- question: "Two object detection systems are benchmarked: System A runs at 4 FPS with 87% mean average precision (mAP); System B runs at 50 FPS with 76% mAP. Which architectural family most likely corresponds to each?"
  type: multiple-choice
  options:
    - "A: YOLO-style single-shot detector; B: Faster R-CNN two-stage detector"
    - "A: Faster R-CNN two-stage detector; B: YOLO-style single-shot detector"
    - "A: R-CNN with selective search; B: SSD single-shot detector"
    - "A: sliding-window CNN classifier; B: Faster R-CNN with Feature Pyramid Network"
  answer: 1
  explanation: "Two-stage detectors (Faster R-CNN family) propose regions and then classify them, achieving higher accuracy at the cost of speed. Single-shot detectors (YOLO, SSD family) predict boxes directly in one forward pass, enabling real-time speeds at a modest accuracy penalty. The 4 FPS / high accuracy profile is characteristic of two-stage methods; 50 FPS / slightly lower accuracy is characteristic of single-shot methods."

- question: "A detector produces 18 overlapping bounding boxes around the same cat in an image, all with varying confidence scores. What technique selects the single best prediction and discards the rest?"
  type: multiple-choice
  options:
    - "Feature Pyramid Network (FPN), which merges multi-scale features into one prediction"
    - "Region Proposal Network (RPN), which filters out redundant proposals before classification"
    - "Non-maximum suppression (NMS), which keeps the highest-confidence box and removes overlapping duplicates"
    - "Anchor box matching, which assigns each object to exactly one grid cell"
  answer: 2
  explanation: "Non-maximum suppression (NMS) is the post-processing step that resolves duplicate detections. It sorts candidate boxes by confidence, keeps the highest-scoring box, and suppresses all other boxes with high IoU (intersection over union) overlap with the kept box, iterating until no duplicates remain. FPN solves multi-scale detection; RPN generates proposals but does not resolve duplicates; anchor matching assigns proposals but does not suppress them."

- question: "In Faster R-CNN, the convolutional backbone processes the image only once, and the resulting feature map is shared between the Region Proposal Network and the classification head."
  type: true-false
  answer: true
  explanation: "Shared feature computation is the key innovation of Faster R-CNN over its predecessor Fast R-CNN and the original R-CNN. Rather than running a separate CNN on each candidate region (thousands of forward passes), Faster R-CNN computes the feature map once and allows both the RPN and classifier to operate on the same features. This dramatically reduces computation and is what makes two-stage detection tractable at near-real-time speeds."

- question: "Object detection is fundamentally equivalent to running an image classifier on a sliding window at nearly every possible location and scale, making it a straightforward extension of image classification."
  type: true-false
  answer: false
  explanation: "Sliding-window classification is the brute-force baseline that deep detection networks were designed to replace. Modern detectors (R-CNN family, YOLO, SSD) do not exhaustively scan all positions and scales — they learn to directly predict bounding box coordinates and class scores in ways that are far more computationally efficient. Single-shot methods like YOLO treat detection as a regression problem with a fixed-size output tensor, which is fundamentally different from applying a classifier thousands of times."

- question: "Explain why Feature Pyramid Networks (FPN) are used in object detection, and what problem they solve that a single feature map from the last convolutional layer cannot handle."
  type: short-answer
  answer: "A single feature map from the last layer has low spatial resolution and high-level semantics — it can recognize large objects but misses small ones because the spatial detail has been pooled away. FPN builds a multi-scale feature hierarchy by combining high-resolution, low-level features (which retain spatial detail for detecting small objects) with low-resolution, high-level features (which have rich semantic information for detecting large objects). Predictions are made at multiple scales simultaneously, allowing the detector to handle objects of vastly different sizes in the same image."
  explanation: "The scale variation problem is one of the central challenges in detection: a person far away appears tiny while one up close fills the frame. Without FPN, a detector optimized for large objects misses small ones and vice versa. FPN solves this by making predictions at multiple feature pyramid levels, each tuned to a different scale range."
```

## Explainer

From your study of convolutional neural networks, you know how to classify an entire image into a single category — "this image contains a dog." But real scenes contain multiple objects at different locations and scales. **Object detection** extends classification by answering two questions simultaneously for every object in an image: *what is it?* and *where is it?* The output is a set of **bounding boxes** (rectangles defined by coordinates) each paired with a class label and a confidence score.

The earliest deep learning approach to detection, **R-CNN**, took a brute-force strategy: generate ~2,000 candidate regions using a traditional algorithm (selective search), then run each region through a CNN independently to classify it. This worked but was painfully slow — thousands of forward passes per image. **Faster R-CNN** improved this dramatically with a **Region Proposal Network (RPN)** that shares convolutional features with the classifier. The CNN processes the image once to produce a feature map, the RPN proposes regions from that feature map, and a small head classifies and refines each proposal. This sharing makes two-stage detectors much faster while maintaining high accuracy.

**Single-shot detectors** like **YOLO** (You Only Look Once) and **SSD** take a fundamentally different approach. Instead of proposing regions and then classifying them, they divide the image into a grid and predict bounding boxes and class probabilities directly at each grid cell in a single forward pass. YOLO treats detection as a regression problem: the network outputs a fixed-size tensor encoding all boxes and scores simultaneously. The tradeoff is that single-shot methods are dramatically faster (enabling real-time detection at 30+ FPS) but historically less accurate on small objects. Modern versions have largely closed this gap.

A critical challenge in detection is handling objects at different scales — a person far away occupies a tiny patch while one nearby fills the frame. **Feature Pyramid Networks (FPN)** address this by building a multi-scale feature hierarchy: high-resolution, low-level features detect small objects while low-resolution, high-level features detect large ones. After prediction, **non-maximum suppression (NMS)** removes duplicate detections: when multiple overlapping boxes detect the same object, only the highest-confidence box is kept. If you have explored transfer learning, you will recognize that most practical detection systems start from a backbone CNN pretrained on ImageNet, then fine-tune the detection heads on task-specific data — few teams train from scratch.
