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

## Questions

```yaml
- question: "A spam classifier computes P(spam | features) = 0.000003 and P(not spam | features) = 0.000001 for a particular email. The classifier marks the email as spam. Despite the probabilities being wildly inaccurate (the true spam probability is 0.97), this classification is correct. Why?"
  type: multiple-choice
  options:
    - "Laplace smoothing corrected the probability estimates before classification"
    - "Classification only requires the correct class to have the highest score — even poorly calibrated probabilities preserve the correct ordering"
    - "Working in log space normalizes the probabilities before the decision is made"
    - "The naive Bayes assumption ensures probability estimates are accurate enough for practical classification"
  answer: 1
  explanation: "This is the key reason naive Bayes works despite its violated independence assumption. Classification is an argmax operation: pick the class with the highest posterior probability. Even if all probabilities are orders of magnitude wrong, the *ranking* of class posteriors is often preserved. As long as the spam class gets the highest score (even if that score is 0.000003 vs 0.000001), the decision is correct. This is why naive Bayes is called a 'good classifier but bad estimator' — it gets decisions right far more often than its probability estimates would suggest."

- question: "A text classifier uses naive Bayes with a vocabulary of 50,000 words and 10 class labels. How many likelihood parameters must be estimated for the class-conditional distributions P(feature | class)?"
  type: multiple-choice
  options:
    - "50,000 — one probability per word regardless of class"
    - "500,000 — one probability per word-class combination"
    - "50,000^10 — the full joint distribution across all words for each class"
    - "10 — one class-conditional distribution treated as a single parameter"
  answer: 1
  explanation: "With the naive Bayes independence assumption, P(X₁, X₂, ..., Xₙ | C) = P(X₁|C) · P(X₂|C) · ... · Pₙ(Xₙ|C). So we need one P(word_i | class_j) for each of the 50,000 words × 10 classes = 500,000 parameters. Without the independence assumption, estimating the full joint distribution P(X₁, X₂, ..., X₅₀,₀₀₀ | C) would require an astronomically large number of parameters — effectively impossible with any realistic training set. The independence assumption reduces an intractable estimation problem to a tractable one."

- question: "Naive Bayes requires that its conditional independence assumption holds approximately in the data for it to achieve good classification accuracy."
  type: true-false
  answer: false
  explanation: "This is the central misconception about naive Bayes. The independence assumption is routinely and often dramatically violated in practice. In spam classification, words like 'free,' 'click,' and 'offer' co-occur far more than independence would predict. Yet naive Bayes still achieves competitive classification accuracy. The reason: classification is an argmax, not a probability estimate. As long as the independence violations don't flip which class receives the highest score — and empirically they often don't — the classifier gets the decision right. Accuracy and calibration are distinct: naive Bayes is poorly calibrated but often correctly ranked."

- question: "Without Laplace smoothing, a single word that appears in training data for class A but never for class B will cause naive Bayes to assign zero probability to class B for any document containing that word, regardless of all other evidence."
  type: true-false
  answer: true
  explanation: "This is the zero-frequency (or zero-count) problem. Without smoothing, P(word | class B) = 0/n = 0. Since naive Bayes multiplies likelihoods together, one zero factor zeros out the entire product: P(word₁|B) · 0 · P(word₃|B) · ... = 0. No matter how strongly all other words favor class B, this single unseen word makes P(B|document) = 0. Laplace smoothing (adding a small count, typically 1, to every feature-class combination) ensures no probability is exactly zero, so evidence from all features can contribute to the final decision."

- question: "Explain why naive Bayes is described as a 'good classifier but bad estimator.' What does this mean, and why does the independence assumption's violation not necessarily impair classification performance?"
  type: short-answer
  answer: "Naive Bayes is a 'good classifier' because it frequently assigns the highest posterior probability to the correct class, leading to correct decisions. It is a 'bad estimator' because the actual probability values it produces are often wildly miscalibrated — the true probability might be 0.97 but naive Bayes estimates 0.00003. The reason violation of the independence assumption doesn't always impair classification: argmax only requires that the correct class ranks first, not that probabilities are accurate. Even when feature co-occurrences violate independence (causing probability estimates to be wrong), the relative ordering of class posteriors is often still correct. Where the assumption fails enough to flip rankings, accuracy does degrade — but in many practical domains, particularly text, the ranking is robust to the violated assumption."
  explanation: "This distinction between classification accuracy and probability calibration is fundamental in machine learning. When you need well-calibrated probabilities (e.g., for risk scoring or cost-sensitive decisions), naive Bayes is insufficient and isotonic regression or Platt scaling is used to post-process its outputs. But for pure classification tasks, naive Bayes remains competitive and is often the right choice due to its speed and data efficiency."
```

## Explainer

You already know Bayes' theorem: P(C|X) = P(X|C) · P(C) / P(X), where C is a class label and X is observed evidence. A Bayesian classifier uses this directly — compute the posterior probability of each class given the features and pick the most probable one. The challenge is estimating P(X|C), the likelihood of seeing a particular combination of features given the class. If X consists of hundreds of features, the joint distribution P(X₁, X₂, ..., Xₙ|C) has an astronomically large number of parameters. With realistic training set sizes, you will never observe most feature combinations, making direct estimation impossible.

The **naive Bayes assumption** cuts through this problem with a single bold simplification: all features are conditionally independent given the class label. This means P(X₁, X₂, ..., Xₙ|C) = P(X₁|C) · P(X₂|C) · ... · P(Xₙ|C). Instead of estimating one enormous joint distribution, you estimate n small univariate distributions — each requiring only enough data to count how often each feature value appears within each class. For text classification, this means counting word frequencies per class, which is trivially fast even for vocabularies of hundreds of thousands of words. Training reduces to counting, which is why naive Bayes is one of the fastest classifiers to fit.

The independence assumption is almost always wrong in practice. In a spam classifier, the words "free" and "click" are not independent given that the email is spam — they co-occur far more often than chance would predict. Yet naive Bayes still works remarkably well. The reason is that classification only requires getting the *ranking* of class probabilities right, not their exact values. Even when the estimated probabilities are poorly calibrated (and they typically are), the correct class often still receives the highest score. The classifier does not need the joint distribution to be accurate — it only needs the product of marginals to preserve the ordering of classes. This is why naive Bayes is called a good classifier but a bad estimator.

In practice, you need to handle two technical issues. First, **smoothing**: if a feature value never appears with a particular class in training data, the likelihood term is zero, which zeroes out the entire product regardless of all other evidence. **Laplace smoothing** (adding a small count to every feature-class combination) prevents this. Second, working in **log space**: multiplying many small probabilities together causes numerical underflow, so implementations sum log-probabilities instead. The classification decision becomes argmax over sums of log-likelihoods plus the log-prior — simple, fast, and numerically stable. Different variants of naive Bayes handle different feature types: **multinomial** naive Bayes models word counts, **Bernoulli** naive Bayes models binary word presence, and **Gaussian** naive Bayes models continuous features by fitting a normal distribution per feature per class.
