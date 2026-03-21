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

## Questions

```yaml
- question: "For a discrete random variable, a student observes the CDF and interprets F(3) as 'the probability that X equals exactly 3.' What does F(3) actually represent?"
  type: multiple-choice
  options:
    - "The probability that X equals 3, equivalent to the PMF value f(3)"
    - "The total accumulated probability that X is 3 or less: P(X ≤ 3)"
    - "The probability density at x = 3 (valid for continuous distributions)"
    - "The probability that X is greater than 3"
  answer: 1
  explanation: "F(3) = P(X ≤ 3), the sum of all probability mass at or below 3. The PMF f(3) gives only P(X = 3). The CDF is a running total — the jump at x = 3 equals f(3), but F(3) itself includes all probability mass at x ≤ 3. Conflating the CDF with the PMF is the most common error in working with distributions."

- question: "The CDF of a continuous random variable is F(x) = x² for 0 ≤ x ≤ 1. What is the probability density function f(x) on this interval?"
  type: multiple-choice
  options:
    - "f(x) = x² (the CDF and PDF are the same function)"
    - "f(x) = 2x (the derivative of the CDF)"
    - "f(x) = √x (the square root of the CDF)"
    - "f(x) = 1/(2x) (the reciprocal of the derivative)"
  answer: 1
  explanation: "For a continuous random variable, f(x) = F'(x). Differentiating x² gives 2x. This relationship — the PDF is the derivative of the CDF, or equivalently the CDF is the antiderivative of the PDF — is the key connection between the two representations and means you can convert in either direction."

- question: "The CDF can decrease as x increases, since probability accumulated earlier can be 'redistributed' to later regions."
  type: true-false
  answer: false
  explanation: "The CDF F(x) = P(X ≤ x) is always non-decreasing. As x increases, more values fall at or below x, so the accumulated probability can only stay the same or increase. A decreasing CDF would imply negative probability, which is impossible. The CDF must go from 0 at −∞ to 1 at +∞ monotonically."

- question: "For any random variable — whether discrete or continuous — the probability P(a < X ≤ b) can be computed as F(b) − F(a)."
  type: true-false
  answer: true
  explanation: "This is one of the most useful properties of the CDF. P(a < X ≤ b) = P(X ≤ b) − P(X ≤ a) = F(b) − F(a). This works for both discrete and continuous distributions. For discrete variables, care is needed with strict vs. non-strict inequalities at isolated points, but the formula P(a < X ≤ b) = F(b) − F(a) holds exactly as written."

- question: "Explain why the CDF of a discrete random variable forms a staircase shape, and what determines the height of each jump."
  type: short-answer
  answer: "The CDF is flat between support values because no new probability accumulates there, and jumps at each support value by exactly P(X = x) — the PMF value at that point."
  explanation: "Between the discrete values where X can take on mass, F(x) = P(X ≤ x) does not change since no additional probability is accumulated. At each support point x₀, the CDF jumps up by f(x₀) = P(X = x₀), which is the probability mass at that value. This is why the jump sizes encode the PMF, and summing all jumps gives a total of 1."
```

## Explainer

The **cumulative distribution function** unifies discrete and continuous random variables under one umbrella. You already know the PMF, which assigns probabilities to individual values, and the PDF, which gives probability density. The CDF F(x) = P(X ≤ x) works for both: it accumulates all the probability to the left of and including x. Think of it as a running total — starting at 0 on the far left, climbing as x increases, and reaching 1 on the far right.

For a discrete variable — say a fair die with values 1 through 6 — F(3) = P(X ≤ 3) = 1/2, the sum of PMF values at x = 1, 2, 3. The CDF of a discrete variable is a **staircase function**: flat between the support values, with an upward jump at each support point. The jump height at each point equals exactly the PMF value there — the probability of that specific outcome. For a continuous variable — say a uniform distribution on [0, 1] — F(x) = x for 0 ≤ x ≤ 1, a smooth ramp. The relationship F'(x) = f(x) recovers the PDF as the derivative of the CDF.

The CDF is the right tool for computing interval probabilities: P(a < X ≤ b) = F(b) − F(a) for any distribution, discrete or continuous. The careful use of strict vs. non-strict inequalities matters for discrete distributions. P(X < b) = F(b⁻) (the left-hand limit of F at b), while P(X ≤ b) = F(b). The difference is P(X = b), the PMF value at b. For continuous distributions, this distinction disappears since P(X = b) = 0 for any single point — the CDF has no jumps, and left and right limits agree everywhere.

The CDF also enables the **quantile function** (the inverse CDF), which builds toward your next topic. The p-th quantile is the smallest x with F(x) ≥ p — for example, the median is the 0.5 quantile. For continuous, strictly increasing CDFs this is simply F⁻¹(p). This inverse relationship powers **inverse transform sampling**: to generate a random sample from any distribution with known CDF, generate U ~ Uniform(0,1) and return F⁻¹(U). The resulting variable has the correct distribution, since P(F⁻¹(U) ≤ x) = P(U ≤ F(x)) = F(x). The CDF thus sits at the center of probability theory — it characterizes the distribution, computes probabilities, connects discrete and continuous cases, and generates random samples.
