---
id: variance-of-random-variables
title: Variance and Standard Deviation of Random Variables
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: expected-value
  type: hard
- id: measures-of-spread
  type: soft
builds-toward:
- sampling-distributions
- binomial-distribution
tags:
- variance
- standard-deviation
- random-variable
- spread
stage: formal-systems
status: validated
---

# Variance and Standard Deviation of Random Variables

## Core Idea
The variance of a random variable X is Var(X) = E[(X − μ)²] = E(X²) − [E(X)]², measuring expected squared deviation from the mean. The standard deviation σ = √Var(X) restores original units. Key rules: Var(aX + b) = a²Var(X) (adding a constant doesn't change spread; scaling multiplies variance by the square of the scale factor). For independent variables, Var(X + Y) = Var(X) + Var(Y) — variances add for independent random variables, but standard deviations do not.

## How It's Best Learned
Use the shortcut formula E(X²) − μ² in practice, but derive Var(X) = E[(X − μ)²] conceptually first. Emphasize the independence requirement for adding variances — this is a common source of errors.

## Common Misconceptions
- Adding standard deviations directly instead of adding variances first.
- Thinking Var(X + Y) = Var(X) + Var(Y) holds without independence.
- Forgetting that the ±b shift in aX + b has no effect on variance.

## Questions

```yaml
- question: "A random variable X has variance 9. You define Y = 3X + 7. What is Var(Y)?"
  type: multiple-choice
  options:
    - "27"
    - "81"
    - "34"
    - "9"
  answer: 1
  explanation: "Var(aX + b) = a²·Var(X). Here a = 3 and b = 7, so Var(Y) = 3²·9 = 9·9 = 81. The constant +7 shifts every outcome equally without changing spread, so it contributes nothing. A common error is multiplying by a instead of a² (giving 27), or adding 7 to the result (giving 34)."

- question: "If X and Y are independent random variables with standard deviations 3 and 4 respectively, then the standard deviation of X + Y is 7."
  type: true-false
  answer: false
  explanation: "Standard deviations do not add — variances do (for independent variables). Var(X + Y) = Var(X) + Var(Y) = 9 + 16 = 25, so SD(X + Y) = √25 = 5, not 3 + 4 = 7. This is the 3-4-5 right triangle appearing in probability: standard deviations combine like sides of a right triangle, not like collinear lengths."

- question: "Why is variance defined using squared deviations E[(X − μ)²] rather than the simpler expected absolute deviation E[|X − μ|]?"
  type: short-answer
  answer: "Squared deviations are algebraically tractable: they yield the clean rules Var(aX + b) = a²Var(X) and Var(X + Y) = Var(X) + Var(Y) for independent variables. Absolute value is not differentiable at zero and does not obey these addition rules."
  explanation: "E[|X − μ|] (mean absolute deviation) is more interpretable in isolation but breaks down algebraically. The squaring operation is what gives variance its composition rules — the ones that power almost all of statistical theory. Standard deviation σ = √Var(X) then restores interpretable units while retaining the algebraic tractability inherited from variance."
```

## Explainer

You learned that the expected value E(X) gives the long-run average of a random variable. But two very different distributions can share the same mean — knowing the average tells you nothing about how spread out the outcomes are. Variance measures that spread: it asks, on average, how far from the mean does X land?

The formula Var(X) = E[(X − μ)²] says: for each possible outcome of X, compute its squared distance from the mean μ, then average those squared distances. Squaring serves two purposes: it makes all deviations positive (no cancellation between outcomes above and below the mean), and it heavily penalizes large deviations, making variance more sensitive to outliers than the mean absolute deviation. In practice, the equivalent shortcut formula Var(X) = E(X²) − [E(X)]² is faster to compute and avoids calculating each deviation individually. The standard deviation σ = √Var(X) simply restores the original units — if X is measured in dollars, variance is in dollars-squared and standard deviation is in dollars.

The two scaling rules are essential. First, adding a constant b to X shifts every outcome by the same amount, so the shape of the distribution doesn't change and neither does its spread: Var(X + b) = Var(X). Second, multiplying X by a stretches each deviation by a factor of a, so squared deviations grow by a²: Var(aX) = a²Var(X). Combined: Var(aX + b) = a²Var(X). The corresponding rule for standard deviation follows: SD(aX + b) = |a|·SD(X). Note that the constant b vanishes entirely.

The independence rule is where students most often stumble: for independent X and Y, Var(X + Y) = Var(X) + Var(Y). This looks obvious but conceals a trap — **standard deviations do not add**. If σ_X = 3 and σ_Y = 4, then σ_{X+Y} = √(9 + 16) = √25 = 5, not 7. The 3-4-5 right triangle is appearing: standard deviations combine like perpendicular vectors, not like collinear ones. Without independence, the formula becomes Var(X + Y) = Var(X) + 2Cov(X, Y) + Var(Y), where the covariance term captures the dependence between X and Y. The independence rule is the special case where that covariance is zero.
