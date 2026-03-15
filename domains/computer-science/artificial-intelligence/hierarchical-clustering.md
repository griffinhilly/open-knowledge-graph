---
id: hierarchical-clustering
title: Hierarchical Clustering
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: kmeans-clustering
  type: hard
- id: vector-spaces
  type: soft
tags:
- clustering
- unsupervised-learning
- hierarchical-structures
- dendrograms
stage: advanced
status: draft
---

# Hierarchical Clustering

## Core Idea
Hierarchical clustering builds a tree (dendrogram) of nested clusters using agglomerative (bottom-up, starting with individual points) or divisive (top-down) methods. Linkage criteria (single, complete, average, Ward) define inter-cluster distance; dendrograms allow analysis at multiple scales without fixing the number of clusters a priori.

## How It's Best Learned
Perform hierarchical clustering on a dataset and visualize the dendrogram, then experiment with different linkage criteria to understand how they produce different clustering structures.
