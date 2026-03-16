---
id: instance-based-learning-knn
title: Instance-Based Learning (k-NN)
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: supervised-learning-intro
  type: hard
- id: algorithm-design-basics
  type: soft
- id: vector-spaces
  type: soft
tags:
- classification
- instance-based
- distance-metrics
- lazy-learning
stage: advanced
status: draft
---

# Instance-Based Learning (k-NN)

## Core Idea
k-nearest neighbors classifies instances by finding the k most similar neighbors in training data and using their labels (majority vote for classification, average for regression). It is a lazy learner (no training phase), making it sensitive to feature scaling and slow at prediction time, but it performs well with complex local patterns and requires no assumptions about data distribution.

## How It's Best Learned
Implement k-NN and experiment with k values and distance metrics (Euclidean, Manhattan, cosine) on datasets with different geometry.

## Explainer

Most supervised learning algorithms you have encountered so far follow a two-phase pattern: first learn a model from training data, then use that model to make predictions. k-nearest neighbors (k-NN) skips the first phase entirely. Instead of compressing training data into parameters or decision boundaries, it simply stores every training example and defers all computation to prediction time. When a new instance arrives, k-NN finds the k training examples closest to it, polls their labels, and returns the majority vote for classification or the average for regression. This makes k-NN a **lazy learner** — it does no work until someone asks a question.

The "nearest" in k-nearest neighbors depends on a **distance metric**, and the choice of metric shapes everything about the algorithm's behavior. Euclidean distance treats feature space like physical space and works well when features are on similar scales. Manhattan distance sums absolute differences along each axis, making it more robust to outliers in individual dimensions. Cosine similarity measures the angle between feature vectors rather than their magnitude, which is useful when you care about proportions rather than absolute values (as in text data). Because k-NN relies directly on distances, **feature scaling** is critical — a feature measured in thousands will dominate one measured in decimals unless you normalize first. This is a direct consequence of working in vector spaces: the geometry of your feature space determines what "similar" means.

The parameter **k** controls the tradeoff between sensitivity and stability. With k=1, the algorithm simply copies the label of the single nearest neighbor, which captures fine-grained local patterns but is extremely sensitive to noise — one mislabeled training point changes the prediction. As k increases, predictions smooth out because more neighbors vote, but the algorithm loses the ability to capture tight local structure. A useful mental model: k=1 draws a complex, jagged decision boundary that perfectly memorizes the training set, while large k draws a smoother boundary that generalizes better but may miss genuine local patterns. Cross-validation on your data tells you where the sweet spot lies.

The major practical limitation of k-NN is computational cost at prediction time. Every prediction requires computing distances to all training examples, which scales linearly with the training set size. For small datasets this is fine, but for millions of examples it becomes prohibitive. Data structures like **KD-trees** and **ball trees** accelerate nearest-neighbor search by partitioning the feature space, reducing average lookup time from linear to logarithmic in favorable conditions. However, these structures lose their advantage in high-dimensional spaces — a phenomenon related to the curse of dimensionality, where distances between points become increasingly uniform and less informative as dimensions grow. Despite these limitations, k-NN remains a powerful baseline: it makes no assumptions about the shape of decision boundaries, adapts to arbitrarily complex local patterns, and is trivially easy to update with new data.
