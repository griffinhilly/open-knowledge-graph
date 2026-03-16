---
id: machine-learning-social-science
title: Machine Learning Applications in Social Science
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: computational-social-science-intro
  type: hard
- id: probability-and-statistics
  type: hard
- id: eigenvalues-eigenvectors
  type: hard
- id: optimization-multivariable-basics
  type: hard
- id: matrix-operations
  type: hard
- id: matrices-intro
  type: soft
- id: algorithm-complexity
  type: soft
- id: eigenvalues-and-eigenvectors
  type: soft
- id: linear-algebra-basics
  type: soft
builds-toward:
- interpretable-machine-learning
- fairness-bias-ml
tags:
- machine-learning
- prediction
- algorithmic
- computational
stage: advanced
status: draft
---

# Machine Learning Applications in Social Science

## Core Idea
Machine learning algorithms (classification, regression, clustering, dimensionality reduction) scale to large datasets and detect non-linear patterns. In social science, supervised methods predict outcomes (e.g., recidivism, protest participation); unsupervised methods find latent structure (e.g., ideological blocs, ethnic groupings). Challenges include interpretability (why did the algorithm decide?), fairness (does it discriminate?), and causality (prediction ≠ understanding mechanisms). ML is a tool for pattern discovery, not causal inference.

## Explainer

Your prerequisites in probability, linear algebra, and optimization are the machinery that machine learning runs on. A linear regression you already know minimizes squared prediction error by finding the weights for each feature. ML algorithms extend this logic aggressively: instead of a linear function, they can learn decision trees, neural networks, kernel functions — any structure that fits the training data well. The key idea that unifies them is **supervised learning**: you provide labeled examples (inputs paired with known outputs), and the algorithm learns a function that maps inputs to outputs well enough to generalize to new, unseen cases. Classification predicts discrete categories (will this person vote?); regression predicts continuous values (what wage will this worker earn?). Your matrix operations knowledge is directly relevant — most of these algorithms are best understood as operations on data matrices, where rows are observations and columns are features.

**Unsupervised learning** has no labels — the algorithm finds structure the analyst did not pre-specify. **Clustering** (k-means, hierarchical clustering) groups observations by similarity; it might reveal that survey respondents cluster into three ideological types you didn't know to look for. **Dimensionality reduction** (PCA, t-SNE) compresses many features into fewer dimensions — your eigenvalue/eigenvector background directly explains PCA: the first principal component is the eigenvector of the covariance matrix corresponding to the largest eigenvalue, capturing the direction of maximum variance. In social science, these tools are used to find latent structure in large corpora (text, social networks, behavioral data) that would be invisible to traditional variable-by-variable analysis.

The most important distinction in social science applications is **prediction versus causal inference**. ML excels at prediction: given a new person's characteristics, what is the probability they will be arrested again? But this says nothing about what *causes* recidivism. If the model learns that race predicts recidivism, it is capturing historical patterns of policing and sentencing, not any causal mechanism. Using an ML prediction for policy intervention — arresting people based on predicted risk — embeds those historical patterns in future decisions, a form of **algorithmic discrimination**. Your probability prerequisites help here: a model that is accurate on average (high overall accuracy) can still be systematically wrong for specific subgroups, violating fairness criteria like equal false positive rates across demographic groups.

**Interpretability** is the third challenge. Traditional regression gives you coefficients you can read as marginal effects. A deep neural network with millions of parameters gives you a prediction but no interpretable story about how it arrived there. This "black box" problem is a fundamental tension in social science: we want to understand *why* and *how*, not just predict. Modern interpretability methods (SHAP values, LIME, partial dependence plots) decompose predictions into feature contributions, but these are approximations — they describe the model's behavior, not the underlying social mechanism. ML's proper role in social science is pattern discovery and prediction at scale, not theory testing or causal explanation. Treat it as a powerful first-pass tool that can tell you *where* to look, but not *why* something is happening.
