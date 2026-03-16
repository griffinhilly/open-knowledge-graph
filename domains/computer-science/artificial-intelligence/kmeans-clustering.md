---
id: kmeans-clustering
title: K-Means Clustering
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: algorithm-design-basics
  type: soft
- id: vectors-in-rn
  type: soft
- id: optimization-multivariable-basics
  type: soft
- id: optimization-problems
  type: soft
- id: metric-spaces-definition
  type: soft
tags:
- unsupervised-learning
- clustering
- partitioning
stage: advanced
status: draft
---

# K-Means Clustering

## Core Idea
K-Means partitions data into k clusters by iteratively assigning points to nearest centroids and updating centroids. Fast and scalable but sensitive to initialization and assumes spherical clusters. Selecting k requires elbow method or silhouette scores.

## Explainer

Imagine you have a room full of unlabeled data points scattered across a space — customer purchase histories, sensor readings, or pixel colors in an image — and you want to discover natural groupings. **K-Means clustering** is an unsupervised algorithm that partitions these points into exactly *k* groups, where each group is defined by its center of mass, called a **centroid**. Unlike supervised learning where labels guide the model, K-Means finds structure on its own by exploiting the distance relationships you already understand from working with vectors in R^n and metric spaces.

The algorithm follows a beautifully simple two-step loop. First, **assign** every data point to the nearest centroid using a distance metric (typically Euclidean distance). Second, **update** each centroid by computing the mean position of all points assigned to it. These two steps repeat until the assignments stop changing — that is, the algorithm has **converged**. You can think of it as an optimization problem: K-Means minimizes the total within-cluster sum of squared distances (the "inertia"), which connects directly to the optimization concepts you have studied. Each iteration is guaranteed to reduce or maintain this objective, so the algorithm always terminates.

The critical design choice is the value of *k* — how many clusters to look for. Since K-Means does not determine this automatically, you need heuristics. The **elbow method** runs K-Means for several values of *k*, plots inertia against *k*, and looks for the "elbow" where adding more clusters yields diminishing returns. **Silhouette scores** measure how similar each point is to its own cluster versus the nearest neighboring cluster, giving a more nuanced quality measure. Neither method is foolproof, but together they provide reasonable guidance.

K-Means has important limitations worth understanding upfront. Because it uses Euclidean distance and computes means, it implicitly assumes clusters are roughly **spherical and equally sized** — elongated, irregular, or overlapping clusters will be poorly captured. The algorithm is also sensitive to **initialization**: different random starting centroids can produce different final clusterings. The widely used **K-Means++** initialization selects initial centroids that are spread apart, dramatically improving consistency. Despite these limitations, K-Means remains one of the most widely used clustering algorithms because it scales efficiently to large datasets — each iteration is O(n·k·d) for n points in d dimensions — and its simplicity makes it an excellent first tool for exploratory data analysis before moving to more complex methods.
