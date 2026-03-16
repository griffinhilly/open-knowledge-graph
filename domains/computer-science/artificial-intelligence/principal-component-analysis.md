---
id: principal-component-analysis
title: Principal Component Analysis
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: linear-algebra-basics
  type: hard
- id: eigenvalues-eigenvectors
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
status: draft
---

# Principal Component Analysis

## Core Idea
PCA finds orthogonal directions capturing maximum data variance via covariance matrix eigendecomposition. It reduces dimensionality preserving variance. Explained variance ratio guides component selection. PCA is linear; non-linear variants (UMAP, t-SNE) handle complex structure.

## Explainer

Imagine you have a dataset with 50 features per observation. Many of those features are correlated — height and weight move together, income and education overlap. **Principal Component Analysis** (PCA) finds a new set of axes, called **principal components**, that capture the most important patterns in the data using as few dimensions as possible. The key prerequisite concepts here are eigenvalues and eigenvectors from linear algebra: PCA is, at its core, an eigendecomposition of the data's covariance matrix.

Here is the procedure. First, center the data by subtracting the mean of each feature. Then compute the **covariance matrix**, which summarizes how every pair of features varies together — you know this from your study of covariance and correlation. The covariance matrix is symmetric and positive semi-definite, which means it can be diagonalized (as you learned in linear algebra). Its eigenvectors define the directions of maximum variance in the data, and its eigenvalues tell you how much variance each direction captures. The eigenvector with the largest eigenvalue points along the direction where the data is most spread out — this becomes the first principal component. The second eigenvector, orthogonal to the first, captures the next most variance, and so on.

To reduce dimensionality, you keep only the top *k* principal components — the ones whose eigenvalues are largest — and project your data onto this lower-dimensional subspace. The **explained variance ratio** for each component is its eigenvalue divided by the sum of all eigenvalues, telling you what fraction of total data variance that component captures. A common heuristic is to keep enough components to explain 90–95% of total variance. If 50 features can be summarized by 5 components capturing 95% of variance, you have dramatically simplified the data while losing very little information.

PCA is powerful but strictly **linear** — it finds flat subspaces that best approximate the data cloud. If the true structure of your data lies on a curved manifold (imagine data distributed along a spiral), PCA will fail to capture it efficiently because no flat plane aligns well with a curve. This is where non-linear dimensionality reduction methods like t-SNE and UMAP come in, which can unfold complex geometric structures that PCA misses. Nonetheless, PCA remains a foundational tool: it is fast, well-understood, deterministic, and often the right first step before exploring more complex alternatives.
