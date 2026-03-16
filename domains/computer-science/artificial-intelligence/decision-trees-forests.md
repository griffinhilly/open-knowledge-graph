---
id: decision-trees-forests
title: Decision Trees and Random Forests
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: algorithm-design-basics
  type: soft
- id: probability-axioms
  type: soft
tags:
- supervised-learning
- tree-models
- ensemble
stage: advanced
status: draft
---

# Decision Trees and Random Forests

## Core Idea
Decision trees partition feature space recursively using splitting criteria like information gain. Random forests reduce overfitting by averaging predictions from trees trained on random data/feature subsets, creating decorrelated learners robust to variance.

## Explainer

A **decision tree** works exactly like a flowchart of yes/no questions. At each internal node, the algorithm asks a question about one feature — "Is income > $50,000?" or "Is age ≤ 30?" — and splits the data into two branches based on the answer. This splitting continues recursively until the leaves contain data points that are sufficiently homogeneous (mostly one class for classification, or similar values for regression). The result is a partition of the entire feature space into rectangular regions, each assigned a prediction.

The critical question is: which feature and which threshold should each split use? The algorithm tries every possible split and selects the one that produces the most **information gain** — the greatest reduction in impurity or uncertainty. For classification, impurity is typically measured by **entropy** (from information theory) or the **Gini index** (the probability that two randomly chosen examples from the node would have different labels). A split that separates cats from dogs perfectly has zero impurity in both children; a split that leaves both children as mixed as the parent gains nothing. The algorithm greedily picks the best split at each node, building the tree top-down. Because you know probability axioms, you can see that these splitting criteria are just measuring how far the class distribution at a node is from uniform (maximum uncertainty) or from pure (zero uncertainty).

A single decision tree is interpretable and fast but has a serious problem: **overfitting**. A deep tree can memorize the training data perfectly, creating tiny leaf nodes that capture noise rather than real patterns. Pruning (removing branches that don't improve validation performance) helps, but a more powerful solution is to build many trees and combine them. A **random forest** creates hundreds or thousands of trees, each trained on a different **bootstrap sample** (random sample with replacement) of the training data. At each split, only a random subset of features is considered, which **decorrelates** the trees — they make different errors on different examples. The final prediction is the majority vote (classification) or average (regression) across all trees.

Why does averaging decorrelated trees work so well? Each individual tree has high variance — small changes in the training data produce very different trees. But when you average many high-variance, low-bias estimators whose errors are not correlated, the variance decreases while the low bias is preserved. This is the statistical insight behind all ensemble methods. Random forests are remarkably robust in practice: they handle mixed feature types, missing data, and high-dimensional inputs with minimal tuning, and they rarely overfit even with very large numbers of trees. The main tradeoff is interpretability — a single tree is transparent, but a forest of 500 trees is a black box, though **feature importance** scores (measuring how much each feature reduces impurity across all trees) partially recover interpretability.
