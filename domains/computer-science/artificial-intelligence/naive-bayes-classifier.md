---
id: naive-bayes-classifier
title: Naive Bayes Classifier
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: supervised-learning-intro
  type: hard
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
