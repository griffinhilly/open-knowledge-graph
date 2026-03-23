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
status: validated
---

# K-Means Clustering

## Core Idea
K-Means partitions data into k clusters by iteratively assigning points to nearest centroids and updating centroids. Fast and scalable but sensitive to initialization and assumes spherical clusters. Selecting k requires elbow method or silhouette scores.

## Questions

```yaml
- question: "K-Means is run twice on the same dataset with different random initializations and produces two different final cluster assignments. What does this most likely indicate?"
  type: multiple-choice
  options:
    - "The data contains no meaningful cluster structure, so K-Means returns arbitrary results"
    - "K-Means has converged to different local minima of the within-cluster sum of squared distances"
    - "The value of k is incorrect and should be adjusted"
    - "K-Means always produces random output and cannot be trusted for analysis"
  answer: 1
  explanation: "K-Means minimizes a non-convex objective (total within-cluster inertia) that can have multiple local minima. Different initializations can lead the iterative algorithm to converge at different local optima — each is a valid solution to the algorithm, but none is guaranteed to be the global minimum. This sensitivity to initialization is why K-Means++ initializes centroids spread far apart to improve consistency, and why running K-Means multiple times and keeping the best result is standard practice."

- question: "A dataset contains two elongated, crescent-shaped clusters that curve around each other. K-Means with k=2 consistently fails to separate them, instead splitting each crescent roughly in half. What is the fundamental reason for this failure?"
  type: multiple-choice
  options:
    - "K-Means needs more iterations to discover curved cluster boundaries"
    - "The features require standardization before K-Means can handle non-circular shapes"
    - "K-Means assigns points to the nearest centroid using Euclidean distance, implicitly assuming spherical clusters — curved or irregular shapes violate this assumption"
    - "k=2 is too small; increasing k would resolve the problem"
  answer: 2
  explanation: "K-Means defines clusters by proximity to centroids using Euclidean distance, which creates spherical (Voronoi) decision boundaries. Any cluster shape that is not roughly spherical and convex will be poorly captured — elongated, crescent, ring, or interleaved clusters all violate the assumption. This is a fundamental geometric limitation, not a parameter-tuning issue. Algorithms like DBSCAN or spectral clustering handle arbitrary shapes by defining clusters through local density or connectivity rather than centroid distance."

- question: "Each iteration of the K-Means algorithm is guaranteed to reduce or maintain the total within-cluster sum of squared distances."
  type: true-false
  answer: true
  explanation: "Both the assignment step and the update step are non-increasing with respect to inertia. The assignment step reduces inertia (or keeps it the same) by reassigning each point to its nearest centroid. The update step moves each centroid to the mean of its assigned points, which by definition minimizes the sum of squared distances from those points to any single location. Because inertia is bounded below by zero and decreases monotonically, convergence is guaranteed — though the solution may be a local minimum."

- question: "The elbow method identifies the optimal value of k by selecting the k that produces the lowest inertia."
  type: true-false
  answer: false
  explanation: "Inertia always decreases as k increases — at k=n (one cluster per point), inertia is exactly zero. Selecting the minimum inertia would always yield k=n, which is meaningless. The elbow method instead looks for the point of diminishing returns: the 'elbow' where each additional cluster provides a much smaller reduction in inertia than before. Beyond the true number of clusters, additional centroids merely subdivide genuine clusters, yielding only marginal improvement. In practice, the elbow is often ambiguous, which is why silhouette scores provide a complementary criterion."

- question: "Why does K-Means++ improve on random initialization, and what property of the initial centroids does it aim to achieve?"
  type: short-answer
  answer: "K-Means++ selects initial centroids that are spread far apart rather than placed randomly. It chooses the first centroid uniformly at random, then selects each subsequent centroid with probability proportional to its squared distance from the nearest already-chosen centroid. This ensures the initial centroids broadly cover the data space and are unlikely to cluster inside the same true group. The goal is to avoid degenerate starting configurations — such as multiple initial centroids inside one true cluster — that force K-Means to waste iterations recovering and risk converging to a poor local minimum."
  explanation: "K-Means++ provides a theoretical guarantee: in expectation, its initial cost is within O(log k) of the optimal cost, whereas random initialization offers no such guarantee. In practice it dramatically reduces both variance across runs and the number of iterations needed to converge, making it the default initialization strategy in most K-Means implementations."
```

## Explainer

Imagine you have a room full of unlabeled data points scattered across a space — customer purchase histories, sensor readings, or pixel colors in an image — and you want to discover natural groupings. **K-Means clustering** is an unsupervised algorithm that partitions these points into exactly *k* groups, where each group is defined by its center of mass, called a **centroid**. Unlike supervised learning where labels guide the model, K-Means finds structure on its own by exploiting the distance relationships you already understand from working with vectors in R^n and metric spaces.

The algorithm follows a beautifully simple two-step loop. First, **assign** every data point to the nearest centroid using a distance metric (typically Euclidean distance). Second, **update** each centroid by computing the mean position of all points assigned to it. These two steps repeat until the assignments stop changing — that is, the algorithm has **converged**. You can think of it as an optimization problem: K-Means minimizes the total within-cluster sum of squared distances (the "inertia"), which connects directly to the optimization concepts you have studied. Each iteration is guaranteed to reduce or maintain this objective, so the algorithm always terminates.

The critical design choice is the value of *k* — how many clusters to look for. Since K-Means does not determine this automatically, you need heuristics. The **elbow method** runs K-Means for several values of *k*, plots inertia against *k*, and looks for the "elbow" where adding more clusters yields diminishing returns. **Silhouette scores** measure how similar each point is to its own cluster versus the nearest neighboring cluster, giving a more nuanced quality measure. Neither method is foolproof, but together they provide reasonable guidance.

K-Means has important limitations worth understanding upfront. Because it uses Euclidean distance and computes means, it implicitly assumes clusters are roughly **spherical and equally sized** — elongated, irregular, or overlapping clusters will be poorly captured. The algorithm is also sensitive to **initialization**: different random starting centroids can produce different final clusterings. The widely used **K-Means++** initialization selects initial centroids that are spread apart, dramatically improving consistency. Despite these limitations, K-Means remains one of the most widely used clustering algorithms because it scales efficiently to large datasets — each iteration is O(n·k·d) for n points in d dimensions — and its simplicity makes it an excellent first tool for exploratory data analysis before moving to more complex methods.
