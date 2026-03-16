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
status: draft
---

# Object Detection Networks

## Core Idea
Object detection networks locate and classify objects in images by predicting bounding boxes and class probabilities. Region-based methods (R-CNN, Faster R-CNN) propose regions then classify them; single-shot methods (YOLO, SSD) predict boxes directly, trading accuracy for speed; modern architectures use feature pyramids for multi-scale detection and non-maximum suppression to handle overlapping detections.

## How It's Best Learned
Implement object detection on images using a pretrained model, then fine-tune on a custom dataset to understand the tradeoffs between speed and accuracy.

## Explainer

From your study of convolutional neural networks, you know how to classify an entire image into a single category — "this image contains a dog." But real scenes contain multiple objects at different locations and scales. **Object detection** extends classification by answering two questions simultaneously for every object in an image: *what is it?* and *where is it?* The output is a set of **bounding boxes** (rectangles defined by coordinates) each paired with a class label and a confidence score.

The earliest deep learning approach to detection, **R-CNN**, took a brute-force strategy: generate ~2,000 candidate regions using a traditional algorithm (selective search), then run each region through a CNN independently to classify it. This worked but was painfully slow — thousands of forward passes per image. **Faster R-CNN** improved this dramatically with a **Region Proposal Network (RPN)** that shares convolutional features with the classifier. The CNN processes the image once to produce a feature map, the RPN proposes regions from that feature map, and a small head classifies and refines each proposal. This sharing makes two-stage detectors much faster while maintaining high accuracy.

**Single-shot detectors** like **YOLO** (You Only Look Once) and **SSD** take a fundamentally different approach. Instead of proposing regions and then classifying them, they divide the image into a grid and predict bounding boxes and class probabilities directly at each grid cell in a single forward pass. YOLO treats detection as a regression problem: the network outputs a fixed-size tensor encoding all boxes and scores simultaneously. The tradeoff is that single-shot methods are dramatically faster (enabling real-time detection at 30+ FPS) but historically less accurate on small objects. Modern versions have largely closed this gap.

A critical challenge in detection is handling objects at different scales — a person far away occupies a tiny patch while one nearby fills the frame. **Feature Pyramid Networks (FPN)** address this by building a multi-scale feature hierarchy: high-resolution, low-level features detect small objects while low-resolution, high-level features detect large ones. After prediction, **non-maximum suppression (NMS)** removes duplicate detections: when multiple overlapping boxes detect the same object, only the highest-confidence box is kept. If you have explored transfer learning, you will recognize that most practical detection systems start from a backbone CNN pretrained on ImageNet, then fine-tune the detection heads on task-specific data — few teams train from scratch.
