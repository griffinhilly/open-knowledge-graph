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

## Questions

```yaml
- question: "A k-NN classifier is trained on a dataset with two features: age (range 0–80 years) and annual income (range $0–$500,000). No feature scaling is applied. What is the most likely consequence?"
  type: multiple-choice
  options:
    - "The model will fail to converge because k-NN requires normalized inputs to compute gradients"
    - "Income will dominate the distance calculation, effectively making age irrelevant to the predictions"
    - "Age will dominate because biological age has more predictive power than income for most tasks"
    - "Both features contribute equally, because k-NN uses rank-order comparisons rather than raw distances"
  answer: 1
  explanation: "k-NN computes distances directly in feature space. Income spans 500,000 units while age spans only 80 — a difference of 1 in income is negligible, but it swamps a difference of 1 year in age. In Euclidean distance, the feature with the larger numeric range dominates the distance calculation, rendering smaller-scale features nearly invisible. This is why feature scaling (standardization or min-max normalization) is not optional for k-NN — it is a prerequisite for meaningful distance computation. k-NN has no training phase that could 'learn' to weight features correctly."

- question: "A k-NN model with k=1 achieves 100% accuracy on training data but only 62% on held-out test data. Increasing k to 15 gives 88% training accuracy and 85% test accuracy. What best explains this pattern?"
  type: multiple-choice
  options:
    - "k=1 memorizes each training point perfectly — there is always a neighbor with distance zero — but overfits to noise; larger k smooths the decision boundary by averaging over more neighbors"
    - "k=1 is computationally faster, so it processes more training data before the time limit, learning more patterns"
    - "k=15 selects from a larger pool of training examples, effectively training on 15 times as much data"
    - "Increasing k introduces beneficial randomness that prevents the model from latching onto spurious correlations"
  answer: 0
  explanation: "With k=1, every training point is its own nearest neighbor, giving 100% training accuracy by definition — but this extreme overfitting means the decision boundary zigzags to accommodate every training example, including mislabeled or noisy ones. Increasing k requires a majority vote among k neighbors, smoothing out individual errors. This is the bias-variance tradeoff in k-NN: k=1 has high variance (sensitive to noise), large k has higher bias (misses local structure). k-NN has no explicit training step, so training speed is irrelevant."

- question: "One advantage of k-NN over parametric models like logistic regression is that k-NN becomes faster to make predictions as the training set grows larger."
  type: true-false
  answer: false
  explanation: "The opposite is true. Because k-NN stores all training examples and computes distances to every one at prediction time, query time scales as O(n) in the number of training examples. As the dataset grows, predictions get slower. By contrast, parametric models like logistic regression compress training data into a fixed set of parameters — prediction time stays constant regardless of training set size. This is a core practical limitation of lazy learning: the 'free' training phase is paid for at prediction time."

- question: "Removing irrelevant features from a dataset can significantly improve k-NN accuracy, even if those same features would have negligible effect on a logistic regression model's performance."
  type: true-false
  answer: true
  explanation: "Irrelevant features add noise to every distance calculation in k-NN, distorting the notion of 'nearest neighbor' — two examples that are genuinely similar may appear far apart because they differ on meaningless dimensions. As irrelevant features accumulate (related to the curse of dimensionality), distances become increasingly uniform and less informative. Logistic regression can learn near-zero weights for irrelevant features, effectively ignoring them. k-NN has no equivalent mechanism: all features contribute to distance unless explicitly removed or down-weighted."

- question: "Explain what makes k-NN a 'lazy learner' and describe the key computational tradeoff this creates compared to 'eager' algorithms like logistic regression or decision trees."
  type: short-answer
  answer: "k-NN is lazy because it defers all computation to prediction time: it stores every training example without building any model, and only when queried does it compute distances to all training points, find the k nearest, and return a majority vote. Eager algorithms like logistic regression and decision trees do the opposite: they perform expensive computation during training to compress the data into a compact model (weights or a tree), then make predictions cheaply using that model. The tradeoff: k-NN has essentially zero training cost but linear prediction cost (O(n) per query); eager algorithms have significant training cost but constant-time prediction regardless of training set size."
  explanation: "This lazy/eager distinction also explains why k-NN can trivially incorporate new training data (just add it to storage) while eager algorithms must retrain. The practical consequence is that k-NN is well-suited for small, stable datasets with complex local structure, while eager algorithms are preferred for large datasets or applications requiring fast repeated prediction."
```

## Explainer

Most supervised learning algorithms you have encountered so far follow a two-phase pattern: first learn a model from training data, then use that model to make predictions. k-nearest neighbors (k-NN) skips the first phase entirely. Instead of compressing training data into parameters or decision boundaries, it simply stores every training example and defers all computation to prediction time. When a new instance arrives, k-NN finds the k training examples closest to it, polls their labels, and returns the majority vote for classification or the average for regression. This makes k-NN a **lazy learner** — it does no work until someone asks a question.

The "nearest" in k-nearest neighbors depends on a **distance metric**, and the choice of metric shapes everything about the algorithm's behavior. Euclidean distance treats feature space like physical space and works well when features are on similar scales. Manhattan distance sums absolute differences along each axis, making it more robust to outliers in individual dimensions. Cosine similarity measures the angle between feature vectors rather than their magnitude, which is useful when you care about proportions rather than absolute values (as in text data). Because k-NN relies directly on distances, **feature scaling** is critical — a feature measured in thousands will dominate one measured in decimals unless you normalize first. This is a direct consequence of working in vector spaces: the geometry of your feature space determines what "similar" means.

The parameter **k** controls the tradeoff between sensitivity and stability. With k=1, the algorithm simply copies the label of the single nearest neighbor, which captures fine-grained local patterns but is extremely sensitive to noise — one mislabeled training point changes the prediction. As k increases, predictions smooth out because more neighbors vote, but the algorithm loses the ability to capture tight local structure. A useful mental model: k=1 draws a complex, jagged decision boundary that perfectly memorizes the training set, while large k draws a smoother boundary that generalizes better but may miss genuine local patterns. Cross-validation on your data tells you where the sweet spot lies.

The major practical limitation of k-NN is computational cost at prediction time. Every prediction requires computing distances to all training examples, which scales linearly with the training set size. For small datasets this is fine, but for millions of examples it becomes prohibitive. Data structures like **KD-trees** and **ball trees** accelerate nearest-neighbor search by partitioning the feature space, reducing average lookup time from linear to logarithmic in favorable conditions. However, these structures lose their advantage in high-dimensional spaces — a phenomenon related to the curse of dimensionality, where distances between points become increasingly uniform and less informative as dimensions grow. Despite these limitations, k-NN remains a powerful baseline: it makes no assumptions about the shape of decision boundaries, adapts to arbitrarily complex local patterns, and is trivially easy to update with new data.
