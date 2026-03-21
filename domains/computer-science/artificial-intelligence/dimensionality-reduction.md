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

## Questions

```yaml
- question: "A data scientist wants to reduce 500-dimensional gene expression data to 10 dimensions as input features for a supervised classifier. She runs t-SNE to produce a 10-dimensional embedding and uses those coordinates as features. What is the fundamental problem with this approach?"
  type: multiple-choice
  options:
    - "t-SNE cannot handle more than 100 dimensions, so it will fail on 500-dimensional input"
    - "t-SNE is non-parametric: it cannot project new data points, so the test set cannot be embedded using the training embedding"
    - "t-SNE preserves too much global structure, making it unsuitable for classification tasks"
    - "10 dimensions is too many for t-SNE, which only works for 2D or 3D output"
  answer: 1
  explanation: "t-SNE (and UMAP) are non-parametric methods — they produce an embedding of the training data but there is no learned function that can map new data points into the same space. This makes them unsuitable for feature engineering before supervised learning. PCA, by contrast, learns a linear projection that can be applied to any new data. The 2D/3D output restriction (option D) is a practical norm, not a hard limit, and option C has it backwards — t-SNE actually preserves local structure well but sacrifices global structure."

- question: "You have high-dimensional data that you suspect lies on a curved, Swiss-roll-shaped manifold. You want to understand the cluster structure for a research presentation. Which method is most appropriate?"
  type: multiple-choice
  options:
    - "PCA, because it is interpretable and invertible"
    - "ICA, because it finds statistically independent components rather than just uncorrelated ones"
    - "t-SNE or UMAP, because they capture nonlinear manifold structure and reveal cluster geometry"
    - "An autoencoder, because it is the only parametric nonlinear method"
  answer: 2
  explanation: "PCA and ICA are linear methods — they project onto flat hyperplanes and will distort the intrinsic geometry of a curved manifold like a Swiss roll. t-SNE and UMAP are nonlinear methods specifically designed to reveal cluster structure in high-dimensional data for visualization. An autoencoder (option D) could learn the manifold but requires substantial training and is harder to interpret visually. For a research presentation aimed at understanding cluster structure, t-SNE or UMAP is the right tool."

- question: "Unlike t-SNE and UMAP, a trained autoencoder encoder network can project new, unseen data points into the latent space."
  type: true-false
  answer: true
  explanation: "This is the critical distinction between parametric and non-parametric methods. t-SNE and UMAP are non-parametric: they produce coordinates for the training data only, with no learned function applicable to new data. An autoencoder encoder is a trained neural network — a parametric function — that can accept any input and map it to the latent representation. This makes autoencoders usable for feature engineering and downstream tasks, while t-SNE and UMAP are visualization tools only."

- question: "PCA is generally the best dimensionality reduction method for revealing complex cluster structure in high-dimensional biological data, because it is fast, interpretable, and widely used."
  type: true-false
  answer: false
  explanation: "PCA can only capture linear relationships. If the meaningful structure in the data lies on a curved manifold — which is common in biological datasets like single-cell RNA sequencing — PCA's linear projections will distort or obscure that structure. Nonlinear methods like t-SNE and UMAP routinely reveal tight, well-separated clusters in biological data that PCA collapses into indistinguishable blobs. PCA is the right starting point for feature engineering before supervised models, but not for exploratory visualization of complex cluster geometry."

- question: "Why can the axes in a t-SNE or UMAP embedding not be meaningfully interpreted or compared across runs, even when the overall cluster structure looks similar?"
  type: short-answer
  answer: "t-SNE and UMAP are non-parametric optimization procedures — they find a low-dimensional configuration that preserves local neighborhood structure, but the solution is not unique and involves random initialization. The axes have no fixed interpretation (unlike PCA where each axis corresponds to a direction of maximum variance in the original space). Distances between clusters may also not be comparable between runs or between different embeddings of different datasets."
  explanation: "This matters practically: you cannot compare the x-axis value of a point across two different t-SNE runs and conclude anything about its relationship to points in the other run. The coordinate system is arbitrary. PCA avoids this: the first principal component always points in the direction of maximum variance in the data, giving each axis a consistent geometric meaning."
```

## Explainer

From your study of PCA, you already understand the foundational idea: high-dimensional data often lives on or near a lower-dimensional structure, and you can find that structure by identifying the directions of greatest variance. PCA does this by computing eigenvectors of the covariance matrix and projecting data onto the top-k eigenvectors. Dimensionality reduction as a broader field asks: what if the underlying structure isn't a flat plane but a curved surface, and what other objectives beyond variance preservation might be useful?

**Linear methods** like PCA and **Independent Component Analysis (ICA)** find lower-dimensional representations through matrix operations. PCA maximizes variance along each successive component, making it ideal when the signal lives in directions of high spread. ICA instead seeks components that are statistically independent (not just uncorrelated), which is useful for separating mixed signals — the classic cocktail party problem where multiple speakers are recorded by multiple microphones. Both methods are fast, interpretable (each component is a linear combination of original features), and invertible (you can reconstruct an approximation of the original data). Their limitation is that they can only capture linear relationships: if the data lies on a curved manifold — imagine points arranged on a Swiss roll in 3D — linear projections will distort the intrinsic structure.

**t-SNE** and **UMAP** are **nonlinear methods** designed specifically for visualization of high-dimensional data in 2D or 3D. t-SNE converts pairwise distances in the original space into probabilities (nearby points get high probability, distant points get low), then finds a low-dimensional arrangement that preserves those probabilities as well as possible. It excels at revealing cluster structure — groups of similar points form tight, well-separated clusters in the embedding. UMAP works on similar principles but is faster, better preserves global structure, and produces more interpretable distances between clusters. Both methods are non-parametric (they produce an embedding of the training data but can't directly project new points) and non-invertible (you can't reconstruct the original data from the 2D embedding). They are visualization tools, not feature engineering tools — the coordinates in the embedding have no intrinsic meaning.

**Autoencoders** use neural networks to learn nonlinear dimensionality reduction. An encoder network compresses the input to a low-dimensional **bottleneck** (the latent representation), and a decoder network reconstructs the original input from this bottleneck. Training minimizes reconstruction error, forcing the bottleneck to capture the most important features. Unlike t-SNE and UMAP, autoencoders are parametric (the encoder can project new data) and the latent dimensions can be used as features for downstream tasks. Variational autoencoders (VAEs) add a probabilistic structure to the latent space, making it smooth and continuous, which enables generation of new data by sampling from the latent space.

The choice of method depends on your goal. For exploratory visualization, use t-SNE or UMAP — they will reveal cluster structure and outliers that linear methods might miss. For feature engineering before a supervised model, PCA is often the right starting point because it is fast, interpretable, and deterministic. For learning rich, reusable representations from large datasets, autoencoders offer the most flexibility. In all cases, the fundamental tradeoff is between the expressiveness of the dimensionality reduction (how complex a structure it can capture) and the interpretability and stability of the result.
