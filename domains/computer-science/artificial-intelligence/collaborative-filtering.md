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
