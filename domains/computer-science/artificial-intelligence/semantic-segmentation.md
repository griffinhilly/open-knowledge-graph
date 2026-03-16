---
id: semantic-segmentation
title: Semantic Segmentation
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: convolutional-neural-networks
  type: hard
- id: object-detection-networks
  type: soft
tags:
- computer-vision
- dense-prediction
- deep-learning
- pixel-classification
stage: advanced
status: draft
---

# Semantic Segmentation

## Core Idea
Semantic segmentation assigns class labels to every pixel in an image, treating it as a dense prediction task. Encoder-decoder architectures and fully convolutional networks (FCNs) preserve spatial resolution; U-Net and DeepLab use skip connections and dilated convolutions to maintain receptive field while preserving detail; postprocessing with conditional random fields refines boundaries.

## How It's Best Learned
Implement semantic segmentation on a dataset and visualize segmentation masks, then study how architectural choices (skip connections, dilation) affect boundary quality.

## Explainer

Standard image classification, which you studied with convolutional neural networks, answers "what is in this image?" with a single label. Object detection goes further, drawing bounding boxes around individual objects. **Semantic segmentation** takes the final step: it assigns a class label to every single pixel. The output is not a label or a box but a **dense prediction map** the same size as the input image, where each pixel is colored by its predicted category — road, car, person, sky, building. This pixel-level understanding is essential for applications like autonomous driving, medical imaging, and satellite analysis, where knowing *where* objects are at precise boundaries matters as much as knowing *what* they are.

The fundamental challenge is that standard CNNs for classification progressively reduce spatial resolution through pooling and striding — by the time features reach the final layers, the spatial map might be 7×7 when the input was 224×224. Classification does not care about this loss because it only needs a single label, but segmentation needs to output a full-resolution map. **Fully convolutional networks** (FCNs) address this by replacing fully connected layers with convolutional ones and adding **upsampling** layers (transposed convolutions or bilinear interpolation) that gradually restore spatial resolution. The result is an **encoder-decoder** architecture: the encoder compresses the image into a compact, semantically rich representation, and the decoder expands it back to full resolution with per-pixel class predictions.

The problem with a simple encode-then-decode approach is that fine spatial details — object edges, thin structures, small objects — are lost during encoding and cannot be recovered by the decoder alone. **Skip connections** solve this by forwarding feature maps from early encoder layers directly to corresponding decoder layers. The early layers contain high-resolution spatial information (edges, textures) but limited semantic understanding, while deep layers have rich semantic information but coarse spatial resolution. Skip connections combine both, allowing the decoder to produce sharp boundaries informed by semantics. **U-Net**, originally designed for biomedical image segmentation, popularized this pattern with its symmetric encoder-decoder structure and dense skip connections at every level.

Another key architectural innovation is the **dilated (atrous) convolution**, used prominently in the DeepLab family of models. A standard 3×3 convolution looks at a 3×3 patch of pixels. A dilated convolution spaces out the kernel elements, so a 3×3 kernel with dilation rate 2 covers a 5×5 region while still using only 9 parameters. This expands the **receptive field** — the area of the input image that influences each output pixel — without adding parameters or reducing resolution. A large receptive field is important because correct pixel classification often depends on broad context: knowing a pixel belongs to "road" might require seeing the lane markings 50 pixels away. DeepLab combines dilated convolutions at multiple rates (**atrous spatial pyramid pooling**) to capture context at several scales simultaneously, and optionally refines boundaries with a conditional random field post-processing step that encourages neighboring pixels with similar colors to share labels.
