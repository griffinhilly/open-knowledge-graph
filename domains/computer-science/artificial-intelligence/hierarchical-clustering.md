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
status: validated
---

# Hierarchical Clustering

## Core Idea
Hierarchical clustering builds a tree (dendrogram) of nested clusters using agglomerative (bottom-up, starting with individual points) or divisive (top-down) methods. Linkage criteria (single, complete, average, Ward) define inter-cluster distance; dendrograms allow analysis at multiple scales without fixing the number of clusters a priori.

## How It's Best Learned
Perform hierarchical clustering on a dataset and visualize the dendrogram, then experiment with different linkage criteria to understand how they produce different clustering structures.

## Questions

```yaml
- question: "A data scientist wants clusters that are compact and roughly spherical. Which linkage criterion should they prefer for agglomerative hierarchical clustering?"
  type: multiple-choice
  options:
    - "Single linkage, because it minimizes the distance between the nearest points in each cluster pair"
    - "Complete linkage, because using the maximum pairwise distance to define inter-cluster distance tends to produce compact, bounded clusters"
    - "Any linkage criterion produces identical cluster shapes for spherical data"
    - "Ward's method cannot be used here because it assumes clusters are normally distributed"
  answer: 1
  explanation: "Single linkage uses the closest pair of points between clusters, which causes 'chaining' — elongated, snake-like clusters that keep merging because a single nearby point bridges them. Complete linkage requires that the farthest points in two clusters are close before merging, which compresses clusters into compact forms. Ward's method (minimizing within-cluster variance increase) also tends to produce compact, evenly sized clusters and is often the best default. Single linkage is appropriate for detecting elongated or irregularly shaped clusters, not compact spherical ones."

- question: "A colleague claims: 'Hierarchical clustering is strictly better than K-means because it automatically determines the correct number of clusters.' What is the most accurate assessment of this claim?"
  type: multiple-choice
  options:
    - "Fully correct — hierarchical clustering objectively determines K from the dendrogram structure"
    - "Partially correct — hierarchical clustering avoids specifying K during computation, but a human must still choose where to cut the dendrogram, which is its own subjective decision"
    - "Incorrect — both methods require you to specify K before running"
    - "Incorrect — K-means also builds a hierarchical structure if you run it with multiple values of K"
  answer: 1
  explanation: "Hierarchical clustering builds a complete tree so you don't need to commit to K before running the algorithm. But reading the 'right' K from a dendrogram still requires human judgment: you look for large gaps between merge heights and decide where to draw a horizontal cut. In practice, different analysts may choose different cuts from the same dendrogram. The advantage over K-means is that you can explore many values of K from a single computation, not that K is determined objectively."

- question: "Hierarchical clustering can reveal whether a dataset has two clear clusters, five, or a continuum — information that a flat K-means analysis cannot easily provide from a single run."
  type: true-false
  answer: true
  explanation: "This is the key qualitative advantage of hierarchical clustering. A dendrogram visualizes the full nested structure: large vertical gaps between merges indicate natural cluster boundaries at that scale; uniformly small gaps suggest a continuum with no clear structure. A K-means analysis with a fixed K gives you K clusters but tells you nothing about what happens at other values of K. To get equivalent information from K-means, you would need to run it many times with different K values and compare."

- question: "Single linkage hierarchical clustering produces the most compact, evenly sized clusters and is the best default choice for general-purpose clustering tasks."
  type: true-false
  answer: false
  explanation: "Single linkage is notoriously prone to 'chaining': because it merges clusters whenever any single pair of points is close, it tends to produce elongated clusters that spread across long chains of nearby points rather than compact groups. Ward's method — which merges the pair of clusters whose union minimizes the increase in total within-cluster variance — typically produces the most compact, evenly sized clusters and is usually the recommended default. Single linkage has specific use cases (detecting elongated shapes, finding the minimum spanning tree) but is not a general-purpose default."

- question: "You have a dataset of 50,000 observations and want to explore its cluster structure. Why might agglomerative hierarchical clustering be impractical, and what would you do instead?"
  type: short-answer
  answer: "Agglomerative hierarchical clustering requires maintaining and updating a pairwise distance matrix, which runs in O(n³) time and O(n²) space. For n = 50,000, that means tracking 2.5 billion pairwise distances — likely exceeding available memory and taking prohibitively long. A practical alternative would be to first cluster with K-means (O(nKt), far cheaper) to obtain a manageable number of representative centroids, then run hierarchical clustering on those centroids to explore multi-scale structure. Alternatively, approximate methods or subsampling strategies can bring hierarchical clustering within reach."
  explanation: "The O(n³)/O(n²) cost is the main practical limitation of hierarchical clustering. The tradeoff with K-means is real: K-means scales to millions of points but requires pre-specifying K and finds only flat partitions. Hierarchical clustering is most valuable when n is small enough to afford it — typically thousands of points, not hundreds of thousands."
```

## Explainer

From K-means, you know the basic clustering setup: group data points so that similar points end up together and dissimilar points end up apart. But K-means has a hard constraint — you must specify the number of clusters K in advance, and every point gets a flat assignment to exactly one cluster. **Hierarchical clustering** removes this limitation by producing a complete hierarchy of nested clusters, from individual points at the bottom to a single cluster containing everything at the top. You can then choose any level of granularity after the fact.

The most common approach is **agglomerative (bottom-up) clustering**. The algorithm starts with each data point as its own singleton cluster. At each step, it merges the two closest clusters into one, reducing the total number of clusters by one. This continues until all points belong to a single cluster. The result is a binary tree called a **dendrogram**, where the height of each merge indicates the distance at which those clusters were joined. To obtain a specific number of clusters, you simply cut the dendrogram at the desired height — a horizontal line through the tree. Points in the same subtree below the cut belong to the same cluster. This is powerful because you can explore multiple clustering solutions from a single computation by varying the cut height.

The definition of "distance between two clusters" is where things get interesting, and this is controlled by the **linkage criterion**. You know about distances between individual points from your metric spaces prerequisite — but once points are grouped into clusters, you need to define distance between sets of points. **Single linkage** uses the minimum distance between any pair of points in the two clusters; it tends to produce elongated, chain-like clusters and is sensitive to noise. **Complete linkage** uses the maximum distance, producing compact, roughly spherical clusters. **Average linkage** takes the mean of all pairwise distances, offering a balance. **Ward's method** merges the pair of clusters that produces the smallest increase in total within-cluster variance — it tends to produce the most evenly sized, compact clusters and is often the default choice for many applications.

The main tradeoff compared to K-means is computational cost. Naive agglomerative clustering requires computing and maintaining a distance matrix between all pairs of clusters, running in O(n³) time and O(n²) space. This makes it impractical for very large datasets — K-means at O(nKt) is far cheaper. However, hierarchical clustering offers things K-means cannot: a multi-scale view of cluster structure, no need to prespecify K, and the ability to capture non-spherical cluster shapes (especially with single linkage). In practice, the dendrogram itself is often the most valuable output, revealing the natural grouping structure of the data — whether there are two clear clusters, five, or a continuum with no sharp boundaries.
