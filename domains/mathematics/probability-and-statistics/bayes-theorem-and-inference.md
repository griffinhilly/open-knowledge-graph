---
id: bayes-theorem-and-inference
title: Bayes' Theorem and Statistical Inference
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: conditional-probability-fundamentals
  type: hard
- id: law-of-total-probability
  type: hard
builds-toward:
- bayesian-inference-intro
- maximum-likelihood-estimation-theory
tags:
- bayes
- inference
stage: formal-systems
status: draft
---

# Bayes' Theorem and Statistical Inference

## Core Idea
Bayes' theorem: P(B_i|A)=P(A|B_i)P(B_i)/∑P(A|B_j)P(B_j). It enables updating prior beliefs P(B_i) to posterior beliefs P(B_i|A) given evidence A. This formula is foundational for statistical inference, machine learning, and decision-making under uncertainty.
