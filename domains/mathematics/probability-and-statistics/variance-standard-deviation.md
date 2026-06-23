---
id: variance-standard-deviation
title: Variance and Standard Deviation
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: expected-value-theory
  type: hard
builds-toward:
- covariance-between-random-variables
tags:
- variance
- spread
stage: formal-systems
status: validated
---

# Variance and Standard Deviation

## Core Idea
Variance σ²=Var(X)=E[(X−μ)²]=E[X²]−μ² measures spread. Standard deviation σ=√Var(X) is in original units. Var(aX+b)=a²Var(X). For independent variables, Var(X+Y)=Var(X)+Var(Y). Variance characterizes dispersion around the mean.

## Questions

```yaml
- question: "A dataset has mean 70 and standard deviation 10. Every value is increased by 5 points. What happens to the variance?"
  type: multiple-choice
  options:
    - "Variance increases by 25, because 5² = 25"
    - "Variance increases by 5, matching the shift"
    - "Variance is unchanged"
    - "Variance decreases because scores are now closer to the new mean"
  answer: 2
  explanation: "Adding a constant b to every value shifts the entire distribution without changing its spread. Formally, Var(X + b) = Var(X) — the b appears in every term of E[(X + b − (μ + b))²] = E[(X − μ)²] = Var(X), and cancels exactly. The mean shifts to 75, but every deviation from the new mean is identical to the old deviation from the old mean. Variance measures spread around the mean, so a pure location shift leaves it untouched. Option D contains a subtle logic error — the scores are not 'closer together'; each score moved by the same amount."

- question: "X and Y are independent random variables with Var(X) = 9 and Var(Y) = 16. What is Var(X + Y)?"
  type: multiple-choice
  options:
    - "5, by analogy with the rule for standard deviations"
    - "7, averaging the two variances"
    - "25, summing the variances"
    - "12, taking the geometric mean"
  answer: 2
  explanation: "For independent random variables, Var(X + Y) = Var(X) + Var(Y) = 9 + 16 = 25. Note that the standard deviation of X + Y is √25 = 5, which happens to equal σ_X + σ_Y = 3 + 4 in this case — but that's a coincidence of this specific example. In general, σ(X+Y) = √(σ_X² + σ_Y²) ≠ σ_X + σ_Y. This is precisely why variance (not standard deviation) is the fundamental object: it has the clean additivity property for independent variables."

- question: "Squaring the deviations before averaging them — rather than taking the average of absolute deviations — means that large deviations from the mean are penalized proportionally more than small ones."
  type: true-false
  answer: true
  explanation: "Squaring is superlinear: a deviation of 10 contributes 100, while a deviation of 2 contributes only 4 — a 5-fold difference in raw deviation becomes a 25-fold difference after squaring. This means variance is especially sensitive to outliers and extreme values. This property, combined with the mathematical convenience that differentiating squared terms is clean (leading to the normal equations, least squares, etc.), is why squaring is the canonical choice for measuring spread."

- question: "If Var(X) = 4 and Var(Y) = 9 and X, Y are independent, then the standard deviation of X + Y equals σ_X + σ_Y = 2 + 3 = 5."
  type: true-false
  answer: false
  explanation: "Standard deviations do not add. σ(X+Y) = √(Var(X) + Var(Y)) = √(4 + 9) = √13 ≈ 3.61, not 5. The variance additivity property (Var(X+Y) = Var(X) + Var(Y)) holds for independent variables, but taking the square root of a sum is not the same as the sum of square roots: √(a² + b²) ≠ a + b except in degenerate cases. This is a crucial reason why variance, not standard deviation, is the object that appears in most statistical formulas."

- question: "Why is variance defined using squared deviations from the mean rather than simply averaging the absolute deviations |X − μ|? What mathematical advantages does squaring provide?"
  type: short-answer
  answer: "Squaring has two key advantages: (1) it eliminates the sign problem — without squaring, positive and negative deviations would cancel, and the average deviation would be zero for any symmetric distribution. (2) It produces mathematically tractable formulas — squared expressions are differentiable and lead cleanly to the additivity property Var(X+Y) = Var(X)+Var(Y) for independent variables, which absolute values do not satisfy. The mean absolute deviation is a valid measure of spread but loses these properties."
  explanation: "A third advantage of squaring is that it naturally emphasizes outliers more than absolute value does, which is often desirable. The tradeoff is that variance is in squared units (dollars² if X is in dollars), requiring the square root to restore interpretability as standard deviation. Mean absolute deviation (MAD) is more robust to outliers and interpretable directly, but it lacks the additivity and differentiability that make variance so useful in probability theory, estimation, and linear algebra."
```

## Explainer

You already know that the **expected value** E[X] = μ is the probability-weighted average of a random variable — the center of mass of the distribution. But two distributions can share the same mean yet behave very differently. A coin that pays $1 with certainty has the same expected value as a coin that pays $0 or $2 with equal probability, but the second one is riskier. **Variance** is the tool that quantifies that spread.

Variance is defined as Var(X) = E[(X − μ)²]. The logic: subtract the mean from each outcome to get the deviation, square it so negatives don't cancel positives, then take the expectation. Squaring is the canonical choice — it penalizes large deviations quadratically and produces a mathematically clean theory. The computational shortcut E[X²] − μ² follows directly from expanding the square: E[(X−μ)²] = E[X² − 2μX + μ²] = E[X²] − 2μ² + μ² = E[X²] − μ². Use whichever form is easier for a given distribution.

The squaring introduces a units problem: if X is in dollars, variance is in dollars-squared. **Standard deviation** σ = √Var(X) restores original units and is typically what you report. But variance is what you use in formulas, because it has the crucial additivity property: for *independent* random variables, Var(X + Y) = Var(X) + Var(Y). This property doesn't hold for standard deviation (√(σ_X² + σ_Y²) ≠ σ_X + σ_Y), which is why variance is the fundamental object even if standard deviation is more interpretable.

The scaling rule Var(aX + b) = a²Var(X) is worth internalizing. Shifting a distribution by a constant b doesn't change its spread — variance ignores location. Scaling by a factor a stretches all deviations by a, so squared deviations scale by a². This means if you double the measurement scale of a variable, its variance quadruples. This rule is essential for standardizing random variables: if you form Z = (X − μ)/σ, then Var(Z) = (1/σ²)·Var(X) = (1/σ²)·σ² = 1. Standard deviation is the natural unit of spread, and standardization sets it to 1.

Variance connects to everything downstream. The Chebyshev inequality (which you'll study next) uses variance to bound how much probability can lie far from the mean — a distribution with small variance can't put much probability far from its center. Covariance, which measures joint spread of two variables, is the generalization of variance to pairs: Cov(X, X) = Var(X). Understanding variance as squared expected deviation from the mean is the conceptual foundation for all of these extensions.
