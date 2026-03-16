---
id: expected-value-and-variance
title: Expected Value and Variance
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: discrete-random-variables
  type: hard
builds-toward:
- continuous-random-variables
- binomial-distribution
- normal-distribution
tags:
- expected-value
- mean
- variance
- standard-deviation
stage: formal-systems
status: draft
---

# Expected Value and Variance

## Core Idea
The expected value E[X] = Σ x × p(x) is the long-run average value of a random variable, representing its center. Variance Var(X) = E[(X - E[X])²] measures the spread of the distribution around its mean. Standard deviation σ = √Var(X) is variance expressed in the original units. These moments summarize key features of a distribution's shape and behavior.

## How It's Best Learned
Compute expected value and variance for simple distributions (fair die, coin flip). Verify that variance increases when probability mass spreads away from the mean.

## Common Misconceptions
Thinking E[X] is always the most likely value. Confusing variance with standard deviation in interpretation. Misunderstanding that E[aX + b] = aE[X] + b but Var(aX + b) = a²Var(X).

## Questions

```yaml
- question: "If X has E[X] = 5 and Var(X) = 4, what are E[2X + 3] and Var(2X + 3)?"
  type: multiple-choice
  options: ["E = 13, Var = 11", "E = 13, Var = 16", "E = 13, Var = 8", "E = 10, Var = 16"]
  answer: 1
  explanation: "E[2X + 3] = 2·E[X] + 3 = 2(5) + 3 = 13. Var(2X + 3) = 2²·Var(X) = 4·4 = 16. The constant +3 shifts the distribution without changing spread (variance unaffected), while scaling by 2 multiplies all distances from the mean by 2, so squared distances (variance) multiply by 4."

- question: "The expected value E[X] of a discrete random variable is always the value X is most likely to take."
  type: true-false
  answer: false
  explanation: "E[X] is the long-run average (weighted mean), not the mode (most likely value). For example, if X = 0 with probability 0.9 and X = 100 with probability 0.1, then E[X] = 10 — but X is most likely to equal 0. The expected value can even be a value X never actually takes (like E[die roll] = 3.5)."

- question: "A fair six-sided die is rolled. What is E[X]? What does this value mean if the die is rolled many times?"
  type: short-answer
  answer: "E[X] = (1+2+3+4+5+6)/6 = 3.5. If the die is rolled a large number of times, the average of all outcomes will converge to 3.5."
  explanation: "Expected value is the long-run average. Even though 3.5 is never rolled, averaging thousands of rolls will produce a value very close to 3.5 by the law of large numbers. The formula weights each outcome by its probability: E[X] = Σ x·p(x) = Σ x·(1/6) = 21/6 = 3.5."
```

## Explainer

The expected value E[X] is the mathematical formalization of "long-run average." If you roll a fair die thousands of times and track the running average, that average will converge toward 3.5 — even though 3.5 is never actually rolled. The formula E[X] = Σ x · p(x) weights each possible outcome by its probability and sums the products. Geometrically, the expected value is the balance point, or center of mass, of the probability distribution: if you placed physical weights proportional to each probability on a number line, the distribution would balance at E[X].

A critical misconception: the expected value is not the most likely value. The most likely value is the mode. For symmetric distributions these coincide, but for skewed distributions they can be far apart. If X takes value 0 with probability 0.9 and value 100 with probability 0.1, then E[X] = 10 — yet the most common outcome is 0. Income distributions are a real-world example: average income is pulled upward by high earners, while median and modal income are much lower. The expected value can even be a value that X can never take (3.5 for a die; 10 in the example above).

Variance Var(X) = E[(X − E[X])²] measures spread. It asks: on average, how far does X deviate from its mean, in squared terms? Squaring the deviation serves two purposes: it makes all deviations positive (so negative and positive deviations don't cancel), and it penalizes large deviations more heavily than small ones. The standard deviation σ = √Var(X) brings the units back in line with X, making it more interpretable as "typical distance from the mean."

The transformation rules for mean and variance capture something deep. For E[aX + b] = aE[X] + b: shifting every outcome by b shifts the average by b, and scaling by a scales the average by a. For variance: Var(aX + b) = a²Var(X). Adding a constant b moves every value by the same amount, so all deviations from the mean are unchanged — variance is unaffected. Multiplying by a scales every value and every deviation by a, so squared deviations scale by a². This asymmetry — E scales linearly but Var scales by the square — is a common source of errors and is essential to remember.

These two moments — mean and variance — do not fully characterize a distribution (you need the full density for that), but they capture the two most important features: where it is centered and how spread out it is. Nearly all of statistical inference builds on them. When you study the normal distribution, the binomial, and eventually the central limit theorem, you will use E[X] and Var(X) constantly — both to characterize distributions directly and to describe how statistics computed from samples behave.
