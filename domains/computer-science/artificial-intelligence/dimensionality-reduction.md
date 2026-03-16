---
id: dimensionality-reduction
title: Dimensionality Reduction Techniques
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: principal-component-analysis
  type: hard
- id: linear-independence
  type: soft
- id: eigenvalues-and-eigenvectors
  type: soft
- id: linear-transformations
  type: soft
tags:
- unsupervised-learning
- feature-reduction
- representation-learning
stage: advanced
status: draft
---

# Dimensionality Reduction Techniques

## Core Idea
Dimensionality reduction compresses high-dimensional data preserving structure. Linear methods (PCA, ICA) are interpretable; non-linear methods (t-SNE, UMAP) capture complex structure but are non-invertible. Autoencoders learn representations via neural networks.

## Explainer

From your study of PCA, you already understand the foundational idea: high-dimensional data often lives on or near a lower-dimensional structure, and you can find that structure by identifying the directions of greatest variance. PCA does this by computing eigenvectors of the covariance matrix and projecting data onto the top-k eigenvectors. Dimensionality reduction as a broader field asks: what if the underlying structure isn't a flat plane but a curved surface, and what other objectives beyond variance preservation might be useful?

**Linear methods** like PCA and **Independent Component Analysis (ICA)** find lower-dimensional representations through matrix operations. PCA maximizes variance along each successive component, making it ideal when the signal lives in directions of high spread. ICA instead seeks components that are statistically independent (not just uncorrelated), which is useful for separating mixed signals — the classic cocktail party problem where multiple speakers are recorded by multiple microphones. Both methods are fast, interpretable (each component is a linear combination of original features), and invertible (you can reconstruct an approximation of the original data). Their limitation is that they can only capture linear relationships: if the data lies on a curved manifold — imagine points arranged on a Swiss roll in 3D — linear projections will distort the intrinsic structure.

**t-SNE** and **UMAP** are **nonlinear methods** designed specifically for visualization of high-dimensional data in 2D or 3D. t-SNE converts pairwise distances in the original space into probabilities (nearby points get high probability, distant points get low), then finds a low-dimensional arrangement that preserves those probabilities as well as possible. It excels at revealing cluster structure — groups of similar points form tight, well-separated clusters in the embedding. UMAP works on similar principles but is faster, better preserves global structure, and produces more interpretable distances between clusters. Both methods are non-parametric (they produce an embedding of the training data but can't directly project new points) and non-invertible (you can't reconstruct the original data from the 2D embedding). They are visualization tools, not feature engineering tools — the coordinates in the embedding have no intrinsic meaning.

**Autoencoders** use neural networks to learn nonlinear dimensionality reduction. An encoder network compresses the input to a low-dimensional **bottleneck** (the latent representation), and a decoder network reconstructs the original input from this bottleneck. Training minimizes reconstruction error, forcing the bottleneck to capture the most important features. Unlike t-SNE and UMAP, autoencoders are parametric (the encoder can project new data) and the latent dimensions can be used as features for downstream tasks. Variational autoencoders (VAEs) add a probabilistic structure to the latent space, making it smooth and continuous, which enables generation of new data by sampling from the latent space.

The choice of method depends on your goal. For exploratory visualization, use t-SNE or UMAP — they will reveal cluster structure and outliers that linear methods might miss. For feature engineering before a supervised model, PCA is often the right starting point because it is fast, interpretable, and deterministic. For learning rich, reusable representations from large datasets, autoencoders offer the most flexibility. In all cases, the fundamental tradeoff is between the expressiveness of the dimensionality reduction (how complex a structure it can capture) and the interpretability and stability of the result.
