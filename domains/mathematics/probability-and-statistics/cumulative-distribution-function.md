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

## Explainer

The **cumulative distribution function** unifies discrete and continuous random variables under one umbrella. You already know the PMF, which assigns probabilities to individual values, and the PDF, which gives probability density. The CDF F(x) = P(X ≤ x) works for both: it accumulates all the probability to the left of and including x. Think of it as a running total — starting at 0 on the far left, climbing as x increases, and reaching 1 on the far right.

For a discrete variable — say a fair die with values 1 through 6 — F(3) = P(X ≤ 3) = 1/2, the sum of PMF values at x = 1, 2, 3. The CDF of a discrete variable is a **staircase function**: flat between the support values, with an upward jump at each support point. The jump height at each point equals exactly the PMF value there — the probability of that specific outcome. For a continuous variable — say a uniform distribution on [0, 1] — F(x) = x for 0 ≤ x ≤ 1, a smooth ramp. The relationship F'(x) = f(x) recovers the PDF as the derivative of the CDF.

The CDF is the right tool for computing interval probabilities: P(a < X ≤ b) = F(b) − F(a) for any distribution, discrete or continuous. The careful use of strict vs. non-strict inequalities matters for discrete distributions. P(X < b) = F(b⁻) (the left-hand limit of F at b), while P(X ≤ b) = F(b). The difference is P(X = b), the PMF value at b. For continuous distributions, this distinction disappears since P(X = b) = 0 for any single point — the CDF has no jumps, and left and right limits agree everywhere.

The CDF also enables the **quantile function** (the inverse CDF), which builds toward your next topic. The p-th quantile is the smallest x with F(x) ≥ p — for example, the median is the 0.5 quantile. For continuous, strictly increasing CDFs this is simply F⁻¹(p). This inverse relationship powers **inverse transform sampling**: to generate a random sample from any distribution with known CDF, generate U ~ Uniform(0,1) and return F⁻¹(U). The resulting variable has the correct distribution, since P(F⁻¹(U) ≤ x) = P(U ≤ F(x)) = F(x). The CDF thus sits at the center of probability theory — it characterizes the distribution, computes probabilities, connects discrete and continuous cases, and generates random samples.
