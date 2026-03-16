---
id: recommendation-systems
title: Recommendation Systems
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: supervised-learning-intro
  type: hard
builds-toward:
- collaborative-filtering
- content-based-filtering
tags:
- recommendation
- personalization
- ranking
stage: advanced
status: draft
---

# Recommendation Systems

## Core Idea
Recommendation systems predict user preferences to suggest relevant items. Core challenges include data sparsity (few user-item interactions), cold-start (new users/items with no history), and scalability. Systems range from popularity-based baselines to collaborative filtering, content-based approaches, and neural architectures.

## Explainer

A recommendation system answers a deceptively simple question: given what we know about a user and a catalog of items, which items would this user most likely enjoy? You encounter these systems constantly — Netflix suggesting movies, Spotify building playlists, Amazon proposing products. The core challenge is that the interaction matrix between users and items is extraordinarily **sparse**: a typical user has rated or clicked on a tiny fraction of available items, so the system must generalize from very limited observations.

The simplest approach is **content-based filtering**, which draws on your supervised learning background directly. Each item has features (a movie's genre, director, actors; a product's category, price, description), and the system learns a model of each user's preferences over those features. If you have watched and enjoyed several sci-fi thrillers, the system predicts you will like other sci-fi thrillers. This is essentially a per-user classification or regression problem. The strength is that it works for new items immediately — as long as the item has features, the model can score it. The weakness is that it can only recommend items similar to what the user has already consumed, creating a **filter bubble** with no capacity for serendipity.

**Collaborative filtering** takes a fundamentally different approach: it ignores item features entirely and relies on the patterns in user-item interactions. The insight is that users who agreed in the past tend to agree in the future. If users A and B both loved movies X, Y, and Z, and user A also loved movie W, the system recommends W to user B — even without knowing anything about what these movies are about. **Matrix factorization** formalizes this by decomposing the sparse user-item interaction matrix into two low-rank matrices: one mapping each user to a latent vector and one mapping each item to a latent vector. The predicted rating is the dot product of the user and item vectors. These latent dimensions are learned automatically and often correspond to interpretable concepts like "preference for action" or "tolerance for slow pacing."

The practical challenges are where recommendation systems get interesting. The **cold-start problem** is fundamental: collaborative filtering cannot recommend for a new user with no history or score a new item that nobody has interacted with. Real systems address this with hybrid approaches — using content-based features to bootstrap and switching to collaborative signals as interactions accumulate. **Data sparsity** means that even established users have rated less than 1% of items, making the signal-to-noise ratio low. **Scalability** matters because real catalogs contain millions of items and inference must happen in milliseconds. Production systems typically use a two-stage architecture: a fast retrieval stage that narrows millions of candidates to hundreds using approximate nearest neighbors, followed by a precise ranking stage that scores those candidates with a more expensive model. Evaluation is also subtle — accuracy metrics like RMSE on ratings tell you less than ranking metrics like precision@k or NDCG, because users care about the top few recommendations, not whether the system accurately predicts the difference between a 3-star and 4-star rating.
