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
- id: metric-spaces-definition
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

## Explainer

From K-means, you know the basic clustering setup: group data points so that similar points end up together and dissimilar points end up apart. But K-means has a hard constraint — you must specify the number of clusters K in advance, and every point gets a flat assignment to exactly one cluster. **Hierarchical clustering** removes this limitation by producing a complete hierarchy of nested clusters, from individual points at the bottom to a single cluster containing everything at the top. You can then choose any level of granularity after the fact.

The most common approach is **agglomerative (bottom-up) clustering**. The algorithm starts with each data point as its own singleton cluster. At each step, it merges the two closest clusters into one, reducing the total number of clusters by one. This continues until all points belong to a single cluster. The result is a binary tree called a **dendrogram**, where the height of each merge indicates the distance at which those clusters were joined. To obtain a specific number of clusters, you simply cut the dendrogram at the desired height — a horizontal line through the tree. Points in the same subtree below the cut belong to the same cluster. This is powerful because you can explore multiple clustering solutions from a single computation by varying the cut height.

The definition of "distance between two clusters" is where things get interesting, and this is controlled by the **linkage criterion**. You know about distances between individual points from your metric spaces prerequisite — but once points are grouped into clusters, you need to define distance between sets of points. **Single linkage** uses the minimum distance between any pair of points in the two clusters; it tends to produce elongated, chain-like clusters and is sensitive to noise. **Complete linkage** uses the maximum distance, producing compact, roughly spherical clusters. **Average linkage** takes the mean of all pairwise distances, offering a balance. **Ward's method** merges the pair of clusters that produces the smallest increase in total within-cluster variance — it tends to produce the most evenly sized, compact clusters and is often the default choice for many applications.

The main tradeoff compared to K-means is computational cost. Naive agglomerative clustering requires computing and maintaining a distance matrix between all pairs of clusters, running in O(n³) time and O(n²) space. This makes it impractical for very large datasets — K-means at O(nKt) is far cheaper. However, hierarchical clustering offers things K-means cannot: a multi-scale view of cluster structure, no need to prespecify K, and the ability to capture non-spherical cluster shapes (especially with single linkage). In practice, the dendrogram itself is often the most valuable output, revealing the natural grouping structure of the data — whether there are two clear clusters, five, or a continuum with no sharp boundaries.
