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

## Questions

```yaml
- question: "A student calculates a PDF for a continuous random variable and finds f(1.5) = 2.5. The student concludes the probability P(X = 1.5) = 2.5, which is impossible since probabilities can't exceed 1. What went wrong in their reasoning?"
  type: multiple-choice
  options:
    - "The student made an arithmetic error; a valid PDF value can never exceed 1"
    - "f(x) is a density, not a probability; it can legitimately exceed 1, and probability requires integration over an interval"
    - "The variable must be discrete, not continuous, since the PDF exceeds 1"
    - "The student should have used the CDF instead, since PDFs only apply to symmetric distributions"
  answer: 1
  explanation: "f(x) is a probability density, not a probability. The PDF can exceed 1 — for example, a Uniform distribution on [0, 0.5] has f(x) = 2. What matters is that the PDF integrates to 1 over its entire domain. To find any probability, you must integrate: P(a ≤ X ≤ b) = ∫ₐᵇ f(x) dx. Reading probability directly off the y-axis is the defining misconception when moving from discrete to continuous distributions."

- question: "For a continuous random variable X with PDF f(x), what is the exact value of P(X = 3.0)?"
  type: multiple-choice
  options:
    - "f(3.0) — the PDF value at that point"
    - "F(3.0) — the CDF evaluated at 3.0"
    - "0, because the probability of any single exact value is zero for a continuous distribution"
    - "Undefined, because continuous distributions have no probability assigned to individual points"
  answer: 2
  explanation: "For any continuous random variable, P(X = c) = ∫_c^c f(x) dx = 0, regardless of how high f(c) is. This is not undefined — it is exactly zero. There are infinitely many possible values, so no single point can hold positive probability. This is why option D is wrong: the probability exists, it's just 0. This also explains why P(a < X < b) = P(a ≤ X ≤ b) for continuous variables — the endpoints contribute nothing."

- question: "If f(5) > f(3) for some PDF, then the probability of getting exactly X = 5 is greater than the probability of getting exactly X = 3."
  type: true-false
  answer: false
  explanation: "Both P(X = 5) and P(X = 3) are exactly 0 for any continuous random variable, regardless of the PDF values. A higher PDF value at x = 5 means probability is more densely concentrated near 5 — you are more likely to fall in a small interval around 5 than an equally-sized interval around 3 — but you cannot read probability from individual PDF values. Probability requires integration over an interval."

- question: "A valid probability density function must be non-negative everywhere and must integrate to 1 over its entire domain."
  type: true-false
  answer: true
  explanation: "These are the two necessary and sufficient conditions for a valid PDF. Non-negativity ensures that no region has 'negative probability.' Integrating to 1 ensures that the total probability across all possible outcomes equals 1, consistent with certainty that the random variable takes some value. Note that f(x) can exceed 1 at individual points — only the total area is constrained to equal 1."

- question: "Explain why you cannot calculate the probability that a continuous random variable equals exactly 3.7 by reading the value f(3.7) from the PDF."
  type: short-answer
  answer: "f(3.7) is a probability density, not a probability. For continuous variables, probability is defined as area under the curve, not height. Since a single point has zero width, the area above any single point is zero — so P(X = 3.7) = 0, regardless of how large f(3.7) is. To find probability, you must integrate f(x) over an interval."
  explanation: "The density analogy helps here: f(x) describes how thick the pile of probability is at each point, like sand on a table. The height of the pile at one spot tells you relative concentration, but the amount of sand in a single geometric point (no width) is zero. Probability requires a region with positive width. This is the fundamental shift from discrete to continuous probability — from summing function values to integrating them."
```

## Explainer

You already know what a continuous random variable is: a quantity that can take any value in an interval, like the exact height of a randomly chosen person or the precise time until a radioactive atom decays. The challenge is that for continuous variables, the probability of landing on any *single* exact value — say, exactly 1.7320508... meters — is zero. There are infinitely many possible values, so none has positive probability on its own. This is where the **probability density function** comes in: instead of assigning probability to individual points, it assigns probability to *intervals*, via integration.

Think of f(x) as describing how probability is *spread* over the number line — like a pile of sand distributed along a table. The total amount of sand is 1 (the PDF integrates to 1 over its entire domain), but in any specific region, the sand is thicker or thinner depending on f(x). The probability that X falls in the interval [a, b] is the area of sand between a and b — formally, P(a ≤ X ≤ b) = ∫ₐᵇ f(x) dx. The height of the pile at a single point tells you *relative likelihood* — where probability is concentrated — but not probability itself. You can't read probability off the y-axis; you must integrate.

This is the crucial distinction from a discrete PMF, where you *can* read probabilities directly from the function value. For PDFs, f(x) is a *density*, not a probability. In fact, f(x) can exceed 1 — a uniform distribution on [0, 0.5] has f(x) = 2, since the area under the curve must still equal 1. Two requirements constrain any valid PDF: f(x) ≥ 0 everywhere (probability can't be negative, and neither can density), and ∫₋∞^∞ f(x) dx = 1 (the total probability across all outcomes is 1).

From your prerequisite on definite integrals, you know that integration measures signed area under a curve. Applying that here: P(X ≤ b) is the area under f from −∞ to b. This accumulated probability — the area to the left of a threshold — is the **cumulative distribution function** (CDF), which you will study next. The CDF F(b) = P(X ≤ b) = ∫₋∞ᵇ f(x) dx summarizes everything about the distribution's behavior. The PDF and CDF are related by differentiation: f(x) = F′(x) wherever F is differentiable. So the PDF is the *rate* at which accumulated probability grows — tall peaks in f(x) correspond to steep rises in the CDF, indicating regions where the variable concentrates.

