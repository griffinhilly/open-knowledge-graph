---
id: cumulative-distribution-functions-theory
title: Cumulative Distribution Functions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: probability-mass-functions-theory
  type: soft
- id: probability-density-functions-theory
  type: soft
builds-toward:
- standard-normal-and-z-scores
tags:
- cdf
stage: formal-systems
status: draft
---

# Cumulative Distribution Functions

## Core Idea
The cumulative distribution function F(x) = P(X ≤ x) gives the probability that a random variable takes a value at or below x. Every CDF is non-decreasing, right-continuous, with F(−∞) = 0 and F(∞) = 1. For continuous random variables, the PDF is the derivative of the CDF: f(x) = F'(x). For discrete variables, the CDF is a step function with jumps at each possible value. CDFs provide a unified framework for computing tail probabilities, quantiles, and comparing distributions regardless of whether the variable is discrete, continuous, or mixed.

## How It's Best Learned
Plot CDFs for familiar distributions (uniform, normal, geometric) side by side. Practice reading probabilities as vertical differences: P(a < X ≤ b) = F(b) − F(a). This graphical approach builds stronger intuition than formulas alone.

## Common Misconceptions
Students often confuse F(x) with f(x), treating the CDF as a density. The CDF gives cumulative probability, not probability at a point. Also, P(X = x) is not always F(x) − F(x⁻) for continuous variables—it is zero.

