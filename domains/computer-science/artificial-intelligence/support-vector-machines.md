---
id: support-vector-machines
title: Support Vector Machines
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: linear-algebra-basics
  type: hard
- id: dot-product
  type: soft
- id: vector-spaces
  type: soft
- id: constrained-optimization
  type: soft
- id: inner-product-spaces
  type: soft
- id: optimization-multivariable-basics
  type: soft
- id: optimization-problems
  type: hard
- id: matrix-operations
  type: soft
tags:
- supervised-learning
- classification
- margin-based
stage: advanced
status: draft
---

# Support Vector Machines

## Core Idea
SVMs find hyperplanes maximizing the margin between classes. Soft-margin SVMs tolerate misclassification via slack variables. Kernels map to high-dimensional spaces enabling non-linear classification without explicit computation.

## Questions

```yaml
- question: "In a trained hard-margin SVM, which training points directly determine the decision boundary?"
  type: multiple-choice
  options:
    - "All training points on the correct side of the boundary"
    - "Only the misclassified training points"
    - "The training points lying exactly on the margin boundaries (support vectors)"
    - "A random subset of training points selected during optimization"
  answer: 2
  explanation: "The SVM hyperplane is fully determined by the support vectors — the subset of training points closest to the decision boundary, lying exactly on the margin edges. All other correctly classified points can be removed from the training set without changing the learned hyperplane. This is why SVMs are memory-efficient at test time: only support vectors need to be stored."

- question: "In a hard-margin SVM, maximizing the margin directly reduces training error."
  type: true-false
  answer: false
  explanation: "Hard-margin SVMs require all training points to be correctly classified by definition — training error is zero regardless of margin width. The margin is maximized subject to this zero-error constraint. The margin does not measure how well the model fits training data; it measures how robust the boundary is to small perturbations, which relates to generalization (test error), not training error. Confusing margin size with training error is a common misconception."

- question: "Why can't a standard linear SVM classify XOR-distributed data, and how does the kernel trick address this limitation?"
  type: short-answer
  answer: "XOR data is not linearly separable — no hyperplane in the original 2D space correctly separates the two classes. The kernel trick implicitly maps data to a higher-dimensional feature space where a separating hyperplane exists. By replacing inner products in the SVM dual formulation with a kernel function k(x, x') = φ(x)·φ(x'), the algorithm finds a non-linear decision boundary in the original space without ever explicitly computing the high-dimensional mapping φ."
  explanation: "The kernel trick works because the SVM dual optimization and the prediction rule both involve only inner products between data points, never their explicit coordinates. Substituting a kernel function for these inner products is mathematically valid and can implicitly operate in infinite-dimensional feature spaces (as with the RBF kernel), making non-linear classification computationally feasible."
```

## Explainer

The intuition behind SVMs starts with a simple question: given two linearly separable classes, which separating hyperplane should you choose? Many hyperplanes separate the training data correctly, but some will fail on new points that are slightly off from what was seen during training. SVMs resolve this ambiguity by choosing the hyperplane that maximizes the *margin* — the distance between the boundary and the nearest training points on each side. A wider margin means the classifier is more robust: a test point can deviate further from the training distribution before being misclassified.

The training points that sit exactly on the margin boundaries are called *support vectors*, and they are the only points that matter for determining the hyperplane. Every other correctly classified point is irrelevant — you could remove it from the dataset and get the same model. This sparsity is both elegant and practical: at prediction time, you only need to store and compute distances to the support vectors, not to the full training set.

Real data is rarely perfectly separable, which is where the soft-margin SVM comes in. Slack variables ξᵢ allow individual points to violate the margin or even cross the decision boundary, but each violation is penalized. The regularization parameter C controls the tradeoff: large C penalizes violations heavily (the model tries hard to classify everything correctly, risking overfitting); small C allows more violations in exchange for a wider margin (the model generalizes better but may misclassify some training points). Choosing C is one of the main hyperparameter decisions in SVM training.

The kernel trick extends SVMs to non-linear boundaries without explicitly constructing a high-dimensional feature space. The SVM optimization and prediction formulas depend on the data only through pairwise inner products. If you replace each inner product ⟨xᵢ, xⱼ⟩ with a kernel function k(xᵢ, xⱼ) — which computes the inner product of the data in some (possibly infinite-dimensional) feature space — you get an SVM that finds non-linear boundaries in the original space. The RBF kernel k(x, x') = exp(−γ‖x − x'‖²) is the most common choice and can separate any distribution that has a smooth density structure.

SVMs were the dominant classification method before deep learning became practical. They remain valuable when data is high-dimensional relative to sample size (text classification, bioinformatics), when interpretability matters (support vectors have geometric meaning), and when you lack the labeled data to train deep networks. Understanding SVMs also gives you insight into the geometry of classification: the concept of margin, the duality between the primal and dual problems, and the kernel trick are ideas that reappear throughout machine learning theory.
