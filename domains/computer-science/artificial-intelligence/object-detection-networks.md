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
