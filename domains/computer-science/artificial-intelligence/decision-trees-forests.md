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

## Questions

```yaml
- question: "A single deep decision tree achieves 100% accuracy on training data but only 70% on a held-out test set. A random forest of 500 trees achieves 93% training accuracy and 89% test accuracy. What best explains why the forest outperforms the single tree on test data?"
  type: multiple-choice
  options:
    - "The forest uses more training data because each tree sees a bootstrap sample larger than the original dataset"
    - "Each tree in the forest is shallower and therefore has higher bias, which generalizes better"
    - "The forest averages many high-variance, decorrelated trees, reducing overall variance while preserving low bias"
    - "The forest eliminates all irrelevant features, leaving only the most predictive ones"
  answer: 2
  explanation: "The single tree has high variance — it memorized the training data, including noise. Random forests reduce variance by averaging many trees whose errors are not correlated (each tree makes different mistakes due to random feature subsets and bootstrap sampling). When uncorrelated errors are averaged, they cancel out; coherent signal is preserved. Option A is wrong — bootstrap samples are the same size as the original data. Option B is wrong — deep trees still have low bias in a forest; the gain comes from variance reduction, not bias increase. Option D is a side effect, not the core mechanism."

- question: "What is the primary purpose of selecting only a random subset of features at each split in a random forest, rather than considering all features?"
  type: multiple-choice
  options:
    - "It speeds up training by reducing computation at each node"
    - "It forces each tree to use every feature at least once, ensuring full coverage"
    - "It decorrelates the trees so that their errors are independent and cancel when averaged"
    - "It prevents any single tree from overfitting by limiting its information access"
  answer: 2
  explanation: "The key insight is decorrelation. If all trees were trained on the same features (even on different bootstrap samples), strong predictors would dominate every tree's first split, making the trees highly correlated — they would make the same mistakes on the same examples, and averaging would not help. By randomly restricting features at each split, some trees are forced to build their first split around secondary predictors, creating diverse, decorrelated trees whose errors are partially independent. When averaged, independent errors cancel while signal accumulates. Speed (option A) is a true side effect, but not the primary purpose."

- question: "Adding more trees to a random forest will eventually cause it to overfit the training data, just as a single deep tree does."
  type: true-false
  answer: false
  explanation: "False. This is a common misapplication of the intuition that 'more complexity = more overfitting.' In a random forest, each additional tree is an independent high-variance estimator, and averaging them reduces variance monotonically — adding trees cannot increase variance (and thus cannot cause overfitting). The training accuracy may stay high, but test accuracy plateaus rather than declining. This is in sharp contrast to a single tree, where more depth directly increases complexity and overfitting. The practical consequence is that the 'number of trees' hyperparameter is safe to set large; you never need to worry about 'too many.'"

- question: "Random forests preserve interpretability because you can inspect the individual trees and trace the decision path for any prediction."
  type: true-false
  answer: false
  explanation: "False. A single decision tree is interpretable — you can follow the sequence of splits from root to leaf for any input. But a random forest aggregates hundreds or thousands of trees; no single decision path explains a prediction, and the ensemble vote is a black box. Feature importance scores (measuring average impurity reduction per feature across all trees) partially recover a sense of variable importance, but this is a summary statistic, not an explanation of individual predictions. This interpretability tradeoff is one of the main practical reasons to choose a single tree over a forest when transparency is required."

- question: "Explain why averaging many decision trees reduces prediction error. What role does the 'random feature subset' step play, and what would happen if it were removed?"
  type: short-answer
  answer: "Each individual tree has high variance — small changes in training data produce very different trees. When many high-variance estimators whose errors are uncorrelated are averaged, variance decreases (errors cancel) while bias is unchanged. The random feature subset step is what creates the decorrelation: without it, all trees would tend to put the strongest predictors at their root, producing highly correlated trees that make the same errors and gain little from averaging. With random feature subsets, trees are forced to differ structurally, making their errors more independent and the averaging more effective at noise reduction."
  explanation: "The statistical principle is that the variance of an average of n independent random variables with variance σ² is σ²/n, while the average of n perfectly correlated variables has the same variance σ². Real random forest trees are neither perfectly independent nor perfectly correlated — they fall somewhere in between, so variance reduction is real but not as large as if trees were independent. The random feature subset step pushes trees toward lower correlation by preventing any single dominant feature from structuring all trees identically."
```

## Explainer

A **decision tree** works exactly like a flowchart of yes/no questions. At each internal node, the algorithm asks a question about one feature — "Is income > $50,000?" or "Is age ≤ 30?" — and splits the data into two branches based on the answer. This splitting continues recursively until the leaves contain data points that are sufficiently homogeneous (mostly one class for classification, or similar values for regression). The result is a partition of the entire feature space into rectangular regions, each assigned a prediction.

The critical question is: which feature and which threshold should each split use? The algorithm tries every possible split and selects the one that produces the most **information gain** — the greatest reduction in impurity or uncertainty. For classification, impurity is typically measured by **entropy** (from information theory) or the **Gini index** (the probability that two randomly chosen examples from the node would have different labels). A split that separates cats from dogs perfectly has zero impurity in both children; a split that leaves both children as mixed as the parent gains nothing. The algorithm greedily picks the best split at each node, building the tree top-down. Because you know probability axioms, you can see that these splitting criteria are just measuring how far the class distribution at a node is from uniform (maximum uncertainty) or from pure (zero uncertainty).

A single decision tree is interpretable and fast but has a serious problem: **overfitting**. A deep tree can memorize the training data perfectly, creating tiny leaf nodes that capture noise rather than real patterns. Pruning (removing branches that don't improve validation performance) helps, but a more powerful solution is to build many trees and combine them. A **random forest** creates hundreds or thousands of trees, each trained on a different **bootstrap sample** (random sample with replacement) of the training data. At each split, only a random subset of features is considered, which **decorrelates** the trees — they make different errors on different examples. The final prediction is the majority vote (classification) or average (regression) across all trees.

Why does averaging decorrelated trees work so well? Each individual tree has high variance — small changes in the training data produce very different trees. But when you average many high-variance, low-bias estimators whose errors are not correlated, the variance decreases while the low bias is preserved. This is the statistical insight behind all ensemble methods. Random forests are remarkably robust in practice: they handle mixed feature types, missing data, and high-dimensional inputs with minimal tuning, and they rarely overfit even with very large numbers of trees. The main tradeoff is interpretability — a single tree is transparent, but a forest of 500 trees is a black box, though **feature importance** scores (measuring how much each feature reduces impurity across all trees) partially recover interpretability.
