---
id: probability-density-functions
title: Probability Density Functions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: continuous-random-variables-basics
  type: hard
- id: definite-integral-definition
  type: soft
builds-toward:
- expected-value
- variance-of-random-variables
- cumulative-distribution-function
tags:
- pdf
- continuous-distributions
- probability
stage: formal-systems
status: draft
---

# Probability Density Functions

## Core Idea
The probability density function (PDF), denoted f(x), describes the relative likelihood of a continuous random variable taking values near x. Probabilities are found by integrating: P(a ≤ X ≤ b) = ∫ₐᵇ f(x)dx. The PDF is always non-negative and integrates to 1.

## How It's Best Learned
Sketch PDFs and visualize integration as areas under curves. Compare PDFs of different distributions. Practice finding probabilities by integration. Use properties of PDFs to identify valid densities.

## Common Misconceptions
Thinking f(x) is a probability (it's a density, not probability). Reading probability directly from PDF height. Forgetting to integrate to find probabilities. Confusing PDF with PMF.

## Explainer

You already know what a continuous random variable is: a quantity that can take any value in an interval, like the exact height of a randomly chosen person or the precise time until a radioactive atom decays. The challenge is that for continuous variables, the probability of landing on any *single* exact value — say, exactly 1.7320508... meters — is zero. There are infinitely many possible values, so none has positive probability on its own. This is where the **probability density function** comes in: instead of assigning probability to individual points, it assigns probability to *intervals*, via integration.

Think of f(x) as describing how probability is *spread* over the number line — like a pile of sand distributed along a table. The total amount of sand is 1 (the PDF integrates to 1 over its entire domain), but in any specific region, the sand is thicker or thinner depending on f(x). The probability that X falls in the interval [a, b] is the area of sand between a and b — formally, P(a ≤ X ≤ b) = ∫ₐᵇ f(x) dx. The height of the pile at a single point tells you *relative likelihood* — where probability is concentrated — but not probability itself. You can't read probability off the y-axis; you must integrate.

This is the crucial distinction from a discrete PMF, where you *can* read probabilities directly from the function value. For PDFs, f(x) is a *density*, not a probability. In fact, f(x) can exceed 1 — a uniform distribution on [0, 0.5] has f(x) = 2, since the area under the curve must still equal 1. Two requirements constrain any valid PDF: f(x) ≥ 0 everywhere (probability can't be negative, and neither can density), and ∫₋∞^∞ f(x) dx = 1 (the total probability across all outcomes is 1).

From your prerequisite on definite integrals, you know that integration measures signed area under a curve. Applying that here: P(X ≤ b) is the area under f from −∞ to b. This accumulated probability — the area to the left of a threshold — is the **cumulative distribution function** (CDF), which you will study next. The CDF F(b) = P(X ≤ b) = ∫₋∞ᵇ f(x) dx summarizes everything about the distribution's behavior. The PDF and CDF are related by differentiation: f(x) = F′(x) wherever F is differentiable. So the PDF is the *rate* at which accumulated probability grows — tall peaks in f(x) correspond to steep rises in the CDF, indicating regions where the variable concentrates.

