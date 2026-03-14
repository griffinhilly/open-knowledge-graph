---
id: mixture-models
title: Mixture Models and Gaussian Mixture Models
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: expectation-maximization
  type: hard
- id: kmeans-clustering
  type: hard
builds-toward:
- probabilistic-clustering
- latent-class-analysis
tags:
- mixture-model
- gmm
- gaussian-mixture
stage: advanced
status: draft
---

# Mixture Models and Gaussian Mixture Models

## Core Idea
Mixture models represent data as weighted combinations of K component distributions. Gaussian Mixture Models (GMM) use Gaussian components fit via EM. GMMs provide soft assignments (membership probabilities) unlike k-means' hard assignments. GMMs enable principled model selection via likelihood and provide density estimation.
