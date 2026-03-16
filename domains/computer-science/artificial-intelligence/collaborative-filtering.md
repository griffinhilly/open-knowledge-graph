---
id: collaborative-filtering
title: Collaborative Filtering
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: recommendation-systems
  type: hard
- id: dimensionality-reduction
  type: soft
builds-toward:
- matrix-factorization
- neural-collaborative-filtering
tags:
- collaborative-filtering
- matrix-factorization
- user-item
stage: advanced
status: draft
---

# Collaborative Filtering

## Core Idea
Collaborative filtering predicts preferences by finding patterns in user-item interaction matrices. User-based approaches find similar users; item-based find similar items. Matrix factorization decomposes the interaction matrix into latent user and item factors. The core assumption is that similar users like similar items.

## Explainer

From your study of recommendation systems, you know the basic goal: predict whether a user will like an item they haven't interacted with yet. Content-based approaches do this by analyzing item features (genre, description, attributes), but **collaborative filtering** takes a radically different approach — it ignores item features entirely and works solely from the pattern of who liked what. The fundamental insight is that if two users agreed on many items in the past, they are likely to agree on items in the future. You don't need to know *why* they liked those items — the agreement pattern is enough.

**User-based collaborative filtering** implements this directly. To predict whether user A will like a movie, find the users most similar to A (based on their shared rating history), then average those similar users' ratings for the movie in question. Similarity is typically measured by cosine similarity or Pearson correlation across the ratings vector. **Item-based collaborative filtering** flips the perspective: instead of finding similar users, it finds items similar to ones user A already liked (where "similar" means they tend to be rated similarly by the same users) and predicts ratings based on those item similarities. Item-based approaches tend to be more stable in practice because item similarity patterns change less frequently than user similarity patterns, and they scale better when there are fewer items than users.

Both approaches face a critical problem: the **user-item matrix is extremely sparse**. A typical platform might have millions of users and hundreds of thousands of items, but each user has interacted with only a tiny fraction — often less than 1% of all items. Computing similarities from such sparse vectors is noisy and unreliable. **Matrix factorization** addresses this by decomposing the sparse user-item matrix R into two smaller dense matrices: a user matrix U (each row is a user's latent factor vector) and an item matrix V (each row is an item's latent factor vector), such that R ≈ UV^T. Each latent factor captures an abstract dimension of taste — perhaps one factor corresponds roughly to "preference for action vs. drama" and another to "tolerance for long runtime," though the factors are learned automatically and are not always interpretable.

The elegance of matrix factorization is that predicting user i's rating for item j becomes simply the dot product of their latent vectors: r̂ᵢⱼ = uᵢ · vⱼ. Training learns U and V by minimizing the prediction error on observed ratings (often with regularization to prevent overfitting to the sparse data). This approach, famously used by the winning entry in the Netflix Prize, handles sparsity gracefully because the low-rank factorization forces the model to generalize — it cannot simply memorize the few observed entries but must find coherent latent patterns that explain the entire matrix. The trade-off is the cold-start problem: collaborative filtering cannot recommend items that no one has rated yet, or make predictions for brand-new users with no history, since there are no interaction patterns to leverage.
