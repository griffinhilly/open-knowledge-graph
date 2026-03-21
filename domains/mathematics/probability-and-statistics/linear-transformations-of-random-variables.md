---
id: linear-transformations-of-random-variables
title: Linear Transformations of Random Variables
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: expected-value
  type: hard
- id: variance-of-random-variables
  type: hard
builds-toward:
- sampling-distributions
- confidence-intervals-means
tags:
- transformations
- random-variables
- probability
stage: formal-systems
status: draft
---

# Linear Transformations of Random Variables

## Core Idea
Linear transformations are the workhorses of probability. If Y = aX + b, then E[Y] = aE[X] + b and Var(Y) = a²Var(X)—expectation is linear while variance scales quadratically and is unaffected by shifts. For sums of random variables, E[X + Y] = E[X] + E[Y] always holds, but Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y), so independence simplifies the variance formula. These properties underpin standardization (converting any distribution to mean 0 and variance 1), the construction of confidence intervals, and the derivation of sampling distributions used throughout statistical inference.

## How It's Best Learned
Derive the rules algebraically from the definition of expectation, then verify them numerically with a simple example: roll a die, let X be the result, compute E[3X + 2] and Var(3X + 2) both by formula and by enumerating all outcomes.

## Common Misconceptions
Students frequently forget the squared coefficient in Var(aX) = a²Var(X) and write aVar(X) instead. Another common error is assuming Var(X + Y) = Var(X) + Var(Y) without checking independence—the covariance term is only zero when X and Y are uncorrelated.

## Questions

```yaml
- question: "Random variable X has mean μ = 4 and standard deviation σ = 3. What are the mean and standard deviation of Y = 2X + 7?"
  type: multiple-choice
  options:
    - "Mean = 15, Standard deviation = 13"
    - "Mean = 15, Standard deviation = 6"
    - "Mean = 8, Standard deviation = 6"
    - "Mean = 15, Standard deviation = 36"
  answer: 1
  explanation: "E[Y] = 2·E[X] + 7 = 2(4) + 7 = 15. For the standard deviation: Var(Y) = 2²·Var(X) = 4·9 = 36, so SD(Y) = √36 = 6. The constant shift (+7) moves the mean but has no effect on spread. Option A (SD = 13) is wrong because it applies the linear formula to standard deviation; option D gives the variance (36) not the standard deviation."

- question: "Two random variables X and Y have Var(X) = 5 and Var(Y) = 8. A student computes Var(X + Y) = 13. When is this calculation guaranteed to be correct?"
  type: multiple-choice
  options:
    - "Always — variance of a sum always equals the sum of the variances"
    - "Only when X and Y have the same distribution"
    - "Only when X and Y are independent (or at least uncorrelated, so that Cov(X,Y) = 0)"
    - "Only when both X and Y have mean zero"
  answer: 2
  explanation: "The full formula is Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y). The sum-of-variances shortcut is only valid when Cov(X, Y) = 0, which holds when X and Y are independent (independence implies zero covariance, though the converse is not always true). If X and Y are positively correlated, the true variance exceeds 13; if negatively correlated, it is less than 13."

- question: "If Y = X + 10, then Var(Y) = Var(X) + 100."
  type: true-false
  answer: false
  explanation: "Adding a constant shifts the distribution without changing its spread. Formally, Var(aX + b) = a²Var(X) — the constant b disappears entirely. With a = 1 and b = 10: Var(Y) = 1²·Var(X) = Var(X). This makes intuitive sense: every value of X is shifted up by 10, so every deviation from the new mean is identical to the corresponding deviation from the old mean. The spread is unchanged."

- question: "For any two random variables X and Y — whether independent or not — E[X + Y] = E[X] + E[Y]."
  type: true-false
  answer: true
  explanation: "Linearity of expectation holds unconditionally, with no independence requirement. This is one of the most powerful and frequently used properties in probability. Variance, by contrast, does require independence (or zero covariance) for the simple additive formula. The asymmetry is worth remembering: expectation is always linear; variance is only additive under independence."

- question: "Why does variance scale with the square of the multiplier (a²) rather than linearly with a, when computing Var(aX)?"
  type: short-answer
  answer: "Variance is defined as the expected squared deviation from the mean: Var(X) = E[(X − μ)²]. When X is scaled by a, the new mean is aμ and each deviation scales by a as well: (aX − aμ) = a(X − μ). Squaring that gives a²(X − μ)², so the expected value is a²E[(X − μ)²] = a²Var(X). The squaring happens because variance is inherently a squared quantity — it measures spread in squared units. Standard deviation, which takes the square root, then scales linearly: SD(aX) = |a|·SD(X)."
  explanation: "This is why multiplying a distribution by 2 doubles the standard deviation but quadruples the variance. The distinction matters practically: when standardizing (subtracting the mean and dividing by SD), you use the linear scaling of SD, not the quadratic scaling of variance. Understanding the derivation prevents the common error of writing Var(aX) = aVar(X), which is dimensionally incorrect."
```

