---
id: naive-bayes-classifier
title: Naive Bayes Classifier
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: supervised-learning-intro
  type: hard
- id: bayes-theorem
  type: soft
- id: conditional-probability
  type: soft
- id: probability-axioms
  type: soft
tags:
- classification
- probabilistic-models
- bayes-theorem
- conditional-independence
stage: advanced
status: draft
---

# Naive Bayes Classifier

## Core Idea
The naive Bayes classifier uses Bayes' theorem with a strong conditional independence assumption: all features are conditionally independent given the class label. Despite this oversimplification, naive Bayes is surprisingly effective for text classification, spam detection, and other domains where features are weakly dependent; it is fast to train and requires little data.

## How It's Best Learned
Implement naive Bayes for text classification and examine learned probabilities to understand which features are most predictive of each class.

## Explainer

You already know Bayes' theorem: P(C|X) = P(X|C) · P(C) / P(X), where C is a class label and X is observed evidence. A Bayesian classifier uses this directly — compute the posterior probability of each class given the features and pick the most probable one. The challenge is estimating P(X|C), the likelihood of seeing a particular combination of features given the class. If X consists of hundreds of features, the joint distribution P(X₁, X₂, ..., Xₙ|C) has an astronomically large number of parameters. With realistic training set sizes, you will never observe most feature combinations, making direct estimation impossible.

The **naive Bayes assumption** cuts through this problem with a single bold simplification: all features are conditionally independent given the class label. This means P(X₁, X₂, ..., Xₙ|C) = P(X₁|C) · P(X₂|C) · ... · P(Xₙ|C). Instead of estimating one enormous joint distribution, you estimate n small univariate distributions — each requiring only enough data to count how often each feature value appears within each class. For text classification, this means counting word frequencies per class, which is trivially fast even for vocabularies of hundreds of thousands of words. Training reduces to counting, which is why naive Bayes is one of the fastest classifiers to fit.

The independence assumption is almost always wrong in practice. In a spam classifier, the words "free" and "click" are not independent given that the email is spam — they co-occur far more often than chance would predict. Yet naive Bayes still works remarkably well. The reason is that classification only requires getting the *ranking* of class probabilities right, not their exact values. Even when the estimated probabilities are poorly calibrated (and they typically are), the correct class often still receives the highest score. The classifier does not need the joint distribution to be accurate — it only needs the product of marginals to preserve the ordering of classes. This is why naive Bayes is called a good classifier but a bad estimator.

In practice, you need to handle two technical issues. First, **smoothing**: if a feature value never appears with a particular class in training data, the likelihood term is zero, which zeroes out the entire product regardless of all other evidence. **Laplace smoothing** (adding a small count to every feature-class combination) prevents this. Second, working in **log space**: multiplying many small probabilities together causes numerical underflow, so implementations sum log-probabilities instead. The classification decision becomes argmax over sums of log-likelihoods plus the log-prior — simple, fast, and numerically stable. Different variants of naive Bayes handle different feature types: **multinomial** naive Bayes models word counts, **Bernoulli** naive Bayes models binary word presence, and **Gaussian** naive Bayes models continuous features by fitting a normal distribution per feature per class.
