---
id: principal-component-analysis
title: Principal Component Analysis
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: eigenvalues-and-eigenvectors
  type: hard
- id: eigenvalues-and-eigenvectors
  type: soft
- id: diagonalization
  type: hard
- id: covariance-correlation-theory
  type: soft
tags:
- unsupervised-learning
- dimensionality-reduction
- linear
stage: advanced
status: validated
---

# Principal Component Analysis

## Core Idea
PCA finds orthogonal directions capturing maximum data variance via covariance matrix eigendecomposition. It reduces dimensionality preserving variance. Explained variance ratio guides component selection. PCA is linear; non-linear variants (UMAP, t-SNE) handle complex structure.

## Questions

```yaml
- question: "You run PCA on a 100-feature dataset. The first 3 principal components explain 82% of total variance. A colleague says 'PCA found the 3 most important features.' What is wrong with this statement?"
  type: multiple-choice
  options:
    - "Nothing is wrong — PCA selects the 3 features with the highest variance"
    - "PCA found 3 new axes that are linear combinations of all 100 original features, not a subset of 3 features"
    - "PCA selects features by correlation, not by variance, so 82% refers to correlation explained"
    - "The colleague is right, except the number should be higher — PCA typically retains at least 10 features"
  answer: 1
  explanation: "Principal components are new directions in the original feature space — linear combinations of all 100 features — not selections from them. The first PC is the direction of maximum variance across all features simultaneously. Feature selection (keeping original features) and feature extraction (creating new axes via PCA) are fundamentally different operations. After PCA, each component may load on all 100 original features with different weights, so 'the most important features' is a category error."

- question: "A dataset's true structure lies on a two-dimensional Swiss roll (a curved, spiral surface) embedded in three-dimensional space. You apply PCA to reduce to 2 dimensions. What will most likely happen?"
  type: multiple-choice
  options:
    - "PCA will perfectly recover the 2D structure, since the data truly lives in 2 dimensions"
    - "PCA will fail to capture the intrinsic structure because it can only find flat (linear) subspaces, and no flat plane efficiently aligns with a curved manifold"
    - "PCA will fail because it cannot handle 3D data — it only works on high-dimensional datasets"
    - "PCA will succeed if you first normalize the features, since normalization linearizes the structure"
  answer: 1
  explanation: "PCA finds the best flat (affine) subspace to project onto, as determined by the covariance matrix eigendecomposition. A Swiss roll has meaningful geometric structure, but it is curved — no 2D plane captures both the separation across the roll and the variation along it. The result is that PCA will project points that are far apart on the manifold (but happen to be close in 3D Euclidean space) onto the same location. Non-linear methods like UMAP or t-SNE, which can 'unfold' curved manifolds, are needed for this type of data."

- question: "The first principal component is the eigenvector of the covariance matrix corresponding to the largest eigenvalue, and it points in the direction of maximum variance in the data."
  type: true-false
  answer: true
  explanation: "This is the exact definition. PCA solves for the directions (eigenvectors) along which the projected data has the most spread (variance), ranked by their eigenvalues. The covariance matrix Σ is symmetric positive semi-definite, so it has an orthogonal eigendecomposition. The eigenvector with the largest eigenvalue λ₁ defines the direction of maximum variance — the first PC. Successive PCs are orthogonal to all previous ones and capture decreasing amounts of variance. The eigenvalue itself quantifies the variance along that direction."

- question: "PCA removes noise from a dataset by keeping only the principal components with large eigenvalues and discarding the rest."
  type: true-false
  answer: false
  explanation: "PCA is agnostic about what constitutes 'signal' versus 'noise' — it retains directions of high variance and discards directions of low variance. If noise happens to be high-variance and signal low-variance, PCA will do the opposite of what is intended. True noise reduction requires either domain knowledge about which directions are meaningful, or methods that explicitly model noise (like probabilistic PCA or factor analysis). PCA is a dimensionality-reduction technique that preserves variance, not a denoising technique in the general sense."

- question: "Why must data be centered (mean-subtracted) before applying PCA, and what artifact arises if this step is skipped?"
  type: short-answer
  answer: "PCA finds the directions of maximum variance in the data. If the data is not centered, the first principal component will point toward the mean of the data (the direction with the largest squared distances from the origin), not the direction of greatest spread. This is because variance is defined relative to the mean; without centering, the 'variance' PCA maximizes is actually the second moment about the origin, which conflates the data's spread with its offset from zero. After centering, every PC captures genuine spread in the data rather than a combination of spread and mean direction."
  explanation: "The covariance matrix Σ = (1/n)XᵀX requires centered data (X having zero mean columns). Without centering, the computed matrix is the second-moment matrix (1/n)XᵀX, whose top eigenvector points toward the mean. For data far from the origin (e.g., heights in centimeters, which are all ~170), this artifact dominates all others. The practical fix is always to subtract the column means before computing the covariance matrix."
```

## Explainer

Imagine you have a dataset with 50 features per observation. Many of those features are correlated — height and weight move together, income and education overlap. **Principal Component Analysis** (PCA) finds a new set of axes, called **principal components**, that capture the most important patterns in the data using as few dimensions as possible. The key prerequisite concepts here are eigenvalues and eigenvectors from linear algebra: PCA is, at its core, an eigendecomposition of the data's covariance matrix.

Here is the procedure. First, center the data by subtracting the mean of each feature. Then compute the **covariance matrix**, which summarizes how every pair of features varies together — you know this from your study of covariance and correlation. The covariance matrix is symmetric and positive semi-definite, which means it can be diagonalized (as you learned in linear algebra). Its eigenvectors define the directions of maximum variance in the data, and its eigenvalues tell you how much variance each direction captures. The eigenvector with the largest eigenvalue points along the direction where the data is most spread out — this becomes the first principal component. The second eigenvector, orthogonal to the first, captures the next most variance, and so on.

To reduce dimensionality, you keep only the top *k* principal components — the ones whose eigenvalues are largest — and project your data onto this lower-dimensional subspace. The **explained variance ratio** for each component is its eigenvalue divided by the sum of all eigenvalues, telling you what fraction of total data variance that component captures. A common heuristic is to keep enough components to explain 90–95% of total variance. If 50 features can be summarized by 5 components capturing 95% of variance, you have dramatically simplified the data while losing very little information.

PCA is powerful but strictly **linear** — it finds flat subspaces that best approximate the data cloud. If the true structure of your data lies on a curved manifold (imagine data distributed along a spiral), PCA will fail to capture it efficiently because no flat plane aligns well with a curve. This is where non-linear dimensionality reduction methods like t-SNE and UMAP come in, which can unfold complex geometric structures that PCA misses. Nonetheless, PCA remains a foundational tool: it is fast, well-understood, deterministic, and often the right first step before exploring more complex alternatives.
