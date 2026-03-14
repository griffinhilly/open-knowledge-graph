---
id: cumulative-distribution-function
title: Cumulative Distribution Functions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: probability-mass-functions
  type: soft
- id: probability-density-functions
  type: soft
builds-toward:
- quantile-functions
tags:
- cdf
- probability
- distributions
stage: formal-systems
status: draft
---

# Cumulative Distribution Functions

## Core Idea
The cumulative distribution function (CDF), F(x) = P(X ≤ x), gives the probability that a random variable is at most x. The CDF is always non-decreasing, approaches 0 as x → -∞ and 1 as x → +∞. For continuous variables, the PDF is the derivative of the CDF.

## How It's Best Learned
Sketch CDFs and relate them to PMFs/PDFs. Note that CDF is always increasing. Calculate probabilities using the CDF: P(a < X ≤ b) = F(b) - F(a). Compare the CDF to histograms of empirical data.

## Common Misconceptions
Confusing CDF with PDF (CDF is cumulative, always increasing). Thinking F(x) = f(x) for continuous variables (F'(x) = f(x)). Not recognizing that CDF works for both discrete and continuous variables.
