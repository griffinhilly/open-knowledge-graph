---
id: dbscan-clustering
title: DBSCAN Clustering
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: kmeans-clustering
  type: hard
- id: algorithm-design-basics
  type: soft
- id: metric-spaces-definition
  type: soft
tags:
- clustering
- density-based
- unsupervised-learning
- outlier-detection
stage: advanced
status: draft
---

# DBSCAN Clustering

## Core Idea
DBSCAN groups points that are density-connected, identifying clusters of arbitrary shape while labeling low-density points as noise. Unlike k-means, DBSCAN does not require specifying k and is robust to outliers; it is sensitive to distance metric and density parameters (eps, min_pts), and performance degrades in high dimensions.

## How It's Best Learned
Apply DBSCAN to datasets with non-convex clusters and compare results with k-means, then vary eps to observe how it affects cluster structure.
