---
id: image-classification-remote-sensing
title: Image Classification in Remote Sensing
domain: earth-and-space-sciences
course: remote-sensing-and-gis
prerequisites:
- id: multispectral-imaging
  type: hard
- id: image-preprocessing-remote-sensing
  type: hard
builds-toward:
- change-detection-remote-sensing
- land-use-land-cover-mapping
tags:
- image-classification
- supervised-classification
- unsupervised-classification
- machine-learning
stage: advanced
status: validated
---

# Image Classification in Remote Sensing

## Core Idea
Image classification assigns each pixel (or object) in a remote sensing image to a land cover or land use category based on its spectral, spatial, or temporal characteristics. Supervised classification trains an algorithm on labeled samples (training data) where the analyst has identified known examples of each class; the algorithm then extends these labels to the entire image. Unsupervised classification groups pixels by spectral similarity without prior labels, and the analyst interprets the groups afterward. Modern approaches include object-based classification (grouping pixels into meaningful segments first), deep learning (convolutional neural networks), and multi-temporal classification using time-series phenology.

## Questions

```yaml
- question: "A supervised classification of Landsat imagery produces a land cover map with 85% overall accuracy, but the 'wetland' class has only 40% producer's accuracy. What does this metric indicate?"
  type: multiple-choice
  options:
    - "Only 40% of the map's wetland pixels are actually wetland"
    - "Only 40% of the actual wetland areas were correctly classified as wetland (the rest were misclassified as other classes)"
    - "The wetland class covers 40% of the study area"
    - "40% of training samples were wetlands"
  answer: 1
  explanation: "Producer's accuracy (recall) measures how well a class is detected -- it is the percentage of reference samples for that class that were correctly classified. A 40% producer's accuracy means 60% of actual wetland areas were misclassified as other classes (errors of omission). This differs from user's accuracy (precision), which measures how reliable the classified wetland pixels are."

- question: "Unsupervised classification is always inferior to supervised classification because it does not use training data."
  type: true-false
  answer: false
  explanation: "Unsupervised classification can be superior when the analyst lacks sufficient knowledge of the study area to define classes or collect training data, when the goal is exploratory data analysis to discover natural spectral groupings, or when the study area is too large or inaccessible for training data collection. It also avoids biases introduced by subjective training sample selection. The best approaches often combine both -- using unsupervised clustering to refine class definitions before supervised classification."

- question: "Explain why object-based image analysis (OBIA) often outperforms pixel-based classification for high-resolution satellite imagery."
  type: short-answer
  answer: "At high resolution (sub-meter), individual pixels capture only fragments of real-world objects (part of a roof, a single tree branch, a shadow). Pixel-based classification of these fragments produces noisy, speckled results because spectrally similar pixels from different classes are intermixed. OBIA first segments the image into meaningful objects (groups of spectrally and spatially similar pixels), then classifies these objects using spectral, shape, texture, and contextual properties. This reduces noise, incorporates spatial information that pixel-based methods ignore, and produces results that match real-world objects and boundaries."
  explanation: "As resolution increases, the ratio of within-class to between-class spectral variance increases, degrading pixel-based classification. Segmentation reduces this variance by averaging pixels into meaningful objects."
```

## Explainer

The fundamental goal of most remote sensing projects is not just to look at pretty images but to convert imagery into thematic information -- maps showing what is on the ground. Image classification is the core technique for this conversion, transforming continuous spectral data into discrete categories like forest, cropland, water, or urban.

Supervised classification follows a workflow: collect training samples (pixels with known labels), extract their spectral signatures, train a classifier (maximum likelihood, random forest, support vector machine, or neural network), apply the classifier to the full image, and validate results with independent test data. The quality of training data largely determines classification accuracy -- the algorithm cannot learn distinctions the training data does not represent.

Unsupervised classification takes the opposite approach. Algorithms like K-means or ISODATA cluster pixels into groups based on spectral similarity alone, without any labeled data. The analyst then examines each cluster and assigns it a thematic label. This is particularly useful for initial exploration of unfamiliar imagery, discovering spectral classes that may not correspond to predefined categories.

The accuracy assessment is as important as the classification itself. A confusion matrix compares classified labels against reference data, yielding overall accuracy, producer's accuracy (how well each class is detected), user's accuracy (how reliable each class label is), and kappa coefficient (accounting for chance agreement). Without rigorous accuracy assessment, a classification map has no quantified reliability and cannot support decision-making.
