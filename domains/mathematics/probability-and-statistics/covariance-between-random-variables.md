---
id: covariance-between-random-variables
title: Covariance and Correlation of Random Variables
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: expected-value
  type: hard
- id: variance-of-random-variables
  type: hard
builds-toward:
- joint-probability-distributions
- linear-regression
tags:
- dependence
- covariance
- correlation
stage: formal-systems
status: validated
---

# Covariance and Correlation of Random Variables

## Core Idea
Covariance measures how two random variables vary together: Cov(X,Y) = E[(X-μ_X)(Y-μ_Y)]. Correlation ρ = Cov(X,Y)/(σ_X σ_Y) scales covariance to [-1,1]. Correlation measures linear association; covariance incorporates both direction and scale.

## How It's Best Learned
Calculate covariance and correlation from bivariate data. Visualize relationships with scatterplots. Understand that correlation ≠ causation. Examine how transformations affect covariance.

## Common Misconceptions
Assuming zero correlation means independence. Thinking high covariance means strong relationship (it depends on variable scales). Interpreting correlation causally. Forgetting that covariance and correlation only measure linear association.

## Questions

```yaml
- question: "Let X be uniformly distributed on [−1, 1] and let Y = X². What is Cov(X, Y)?"
  type: multiple-choice
  options:
    - "Positive — because when X is large, Y = X² is also large"
    - "Negative — because Y = X² is a decreasing function of X when X < 0"
    - "Zero — despite Y being completely determined by X"
    - "Undefined — covariance requires both variables to have variance greater than zero"
  answer: 2
  explanation: "Cov(X, Y) = E[XY] − E[X]E[X²] = E[X³] − 0 · E[X²] = 0, because X is symmetric around 0, so E[X³] = 0. Yet Y = X² is completely determined by X — perfect nonlinear dependence. This is the key illustration that zero covariance (and zero correlation) does NOT imply independence. Covariance only measures linear association; the relationship between X and X² is purely nonlinear (a parabola), which is invisible to covariance. Option A and B are both tempting because the relationship between X and X² is real — covariance just can't see it."

- question: "A dataset shows Cov(height_cm, weight_kg) = 450 and Cov(height_m, weight_kg) = 4.5. What does this comparison illustrate?"
  type: multiple-choice
  options:
    - "The relationship between height and weight is 100 times stronger when measured in centimeters"
    - "Covariance depends on the units of measurement, so its magnitude alone cannot indicate the strength of a relationship"
    - "The correlation between height and weight is also 100 times larger when using centimeters"
    - "The dataset with higher covariance has measurement error — both should give the same covariance"
  answer: 1
  explanation: "Covariance is not scale-free: Cov(aX, Y) = a · Cov(X, Y). Converting height from meters to centimeters multiplies by 100, which multiplies the covariance by 100 — but the underlying relationship between height and weight hasn't changed. This is exactly why correlation was invented: ρ = Cov(X,Y)/(σ_X σ_Y) normalizes by the standard deviations, producing a dimensionless measure in [−1, 1] that doesn't change when you rescale either variable. Option C is wrong: correlation is unit-free, so it remains the same regardless of whether height is in meters or centimeters."

- question: "If X and Y are independent random variables, then Cov(X, Y) = 0."
  type: true-false
  answer: true
  explanation: "Independence means E[XY] = E[X]E[Y], which directly gives Cov(X, Y) = E[XY] − E[X]E[Y] = 0. This direction is always true. Independence implies zero covariance. The practical consequence is that Var(X + Y) = Var(X) + Var(Y) when X and Y are independent — the covariance cross-term vanishes. This is the result used constantly in probability theory, statistics, and portfolio theory."

- question: "If Cov(X, Y) = 0, then X and Y are independent."
  type: true-false
  answer: false
  explanation: "Zero covariance does not imply independence — this is the most important misconception about covariance. The converse of 'independence ⟹ zero covariance' does not hold. The canonical counterexample: X uniform on [−1, 1], Y = X². Here Cov(X, Y) = 0, but Y is a deterministic function of X — perfect dependence. Covariance only measures linear association, so any nonlinear relationship (quadratic, circular, etc.) can produce zero covariance while X and Y remain completely dependent."

- question: "Explain why zero correlation between two random variables does not imply that they are independent, and give an example."
  type: short-answer
  answer: "Correlation measures only linear association — how much X and Y vary together in a straight-line pattern. A relationship that is nonlinear can produce zero correlation even when one variable completely determines the other. For example, let X ~ Uniform(−1, 1) and Y = X². Then Cor(X, Y) = 0 because the relationship is symmetric (X = 1 and X = −1 both give Y = 1, so positive and negative deviations of X cancel in the covariance), yet Y is a deterministic function of X — knowing X tells you Y exactly."
  explanation: "The independence condition requires E[f(X)g(Y)] = E[f(X)]E[g(Y)] for all functions f and g. Correlation only checks this for the specific functions f(x) = x and g(y) = y. All the other function pairs are ignored. If the dependence between X and Y is captured by a nonlinear relationship, it won't appear in the covariance or correlation at all."
```

## Explainer

From expected value, you know E[X] is the "center of mass" of a random variable — the long-run average. From variance, you know Var(X) = E[(X − μ_X)²] measures how spread out X is around its mean, by averaging squared deviations. **Covariance** extends this idea from one variable to two: Cov(X, Y) = E[(X − μ_X)(Y − μ_Y)] averages the *product* of deviations. When X is above its mean and Y is simultaneously above its mean, the product (X − μ_X)(Y − μ_Y) is positive. When they move in opposite directions, the product is negative. The expected value of these products captures the overall tendency.

A practical computing formula is Cov(X, Y) = E[XY] − E[X]E[Y]. This is analogous to Var(X) = E[X²] − (E[X])², and it is often easier to apply. Notice that Cov(X, X) = Var(X) — variance is just covariance of a variable with itself. Covariance is **bilinear**: Cov(aX + b, cY + d) = ac · Cov(X, Y), meaning constants and shifts affect covariance multiplicatively. This bilinearity makes covariance central to the variance of sums: Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y). When X and Y are independent, the covariance term vanishes, giving the familiar Var(X + Y) = Var(X) + Var(Y).

The problem with raw covariance is that it depends on the units of X and Y. If X is measured in centimeters rather than meters, Cov(X, Y) scales by 100. To get a unit-free measure, **normalize** by dividing by the standard deviations: ρ = Cov(X, Y) / (σ_X σ_Y). This is the **correlation coefficient**, guaranteed to lie in [−1, 1]. Values near ±1 indicate a near-perfect linear relationship; values near 0 indicate little linear relationship. The Cauchy-Schwarz inequality is what constrains ρ to this range.

The most important subtlety is the gap between correlation and independence. If X and Y are independent, then E[XY] = E[X]E[Y], so Cov(X, Y) = 0 and ρ = 0. But the converse fails: zero correlation does not imply independence. A classic example: let X be uniform on [−1, 1] and Y = X². Then Cov(X, Y) = E[X³] − E[X]E[X²] = 0 − 0 = 0, yet Y is completely determined by X — perfect dependence, but nonlinear. Correlation only detects *linear* association; any purely nonlinear relationship can be invisible to it.
