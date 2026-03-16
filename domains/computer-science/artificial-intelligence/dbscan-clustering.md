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

## Explainer

From k-means clustering, you know the basic idea of grouping data points into clusters by minimizing distance to cluster centers. But k-means has fundamental limitations: it assumes clusters are roughly spherical and equally sized, it requires you to specify the number of clusters k in advance, and it assigns every point to some cluster — even outliers that do not belong anywhere. **DBSCAN** (Density-Based Spatial Clustering of Applications with Noise) takes a completely different approach by defining clusters as dense regions of points separated by sparse regions, which lets it discover clusters of arbitrary shape and naturally identify noise.

DBSCAN uses two parameters: **eps** (ε), a distance radius, and **min_pts**, a minimum number of neighbors. For each point, the algorithm counts how many other points fall within distance ε. A point with at least min_pts neighbors within ε is called a **core point** — it sits in a dense region. A point that is not a core point but falls within ε of one is called a **border point** — it is on the edge of a dense region. Any point that is neither core nor border is labeled **noise**. A cluster is then defined as a maximal set of density-connected points: start from any core point, include all points within ε, then recursively include all points within ε of any core point already in the cluster. This chain reaction of expanding from core point to core point is what allows DBSCAN to trace out elongated, curved, or ring-shaped clusters that k-means would split apart.

Consider a dataset shaped like two interlocking crescents — a classic benchmark. K-means, which can only draw straight-line boundaries between spherical clusters, fails completely on this data regardless of initialization. DBSCAN traces the dense curves of each crescent naturally, because density-connectedness follows the shape of the data rather than imposing a geometric assumption. Points in the sparse gap between crescents become noise or border points of the correct cluster. This ability to find clusters of arbitrary shape without prespecifying k is DBSCAN's greatest strength.

The tradeoff is sensitivity to its two parameters. If **eps** is too small, most points lack enough neighbors and the algorithm labels everything as noise. If eps is too large, distinct clusters merge into one. The **min_pts** parameter controls the minimum density a region must have to qualify as a cluster — higher values make the algorithm more conservative, requiring denser regions. A common heuristic is to set min_pts to at least the dimensionality of the data plus one, then plot the sorted k-nearest-neighbor distances (the "k-distance plot") to find a natural elbow that suggests a good eps. DBSCAN also struggles with datasets where clusters have widely varying densities, because a single eps cannot simultaneously capture both dense and sparse clusters — extensions like HDBSCAN address this by adapting the density threshold hierarchically.
