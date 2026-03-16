---
id: expected-value-theory
title: 'Expected Value: Theory and Properties'
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: probability-mass-functions-theory
  type: hard
builds-toward:
- variance-of-random-variables
- covariance-between-random-variables
tags:
- expected-value
- mean
stage: formal-systems
status: draft
---

# Expected Value: Theory and Properties

## Core Idea
Expected value E[X]=∑xp(x) (discrete) or E[X]=∫xf(x)dx (continuous) is the long-run average. Linearity of expectation: E[aX+b]=aE[X]+b. For independent variables, E[XY]=E[X]E[Y]. Expected value is the center of a distribution.

## Questions

```yaml
- question: "A fair six-sided die has expected value E[X] = 3.5. Which best explains why 3.5 is the expected value even though a die can never actually land on 3.5?"
  type: multiple-choice
  options:
    - "It is a rounding artifact of the calculation"
    - "Expected value is the long-run average over many rolls, not a value the variable must be able to take"
    - "3.5 is the median of the outcomes 1 through 6"
    - "Expected value always equals the midpoint between the minimum and maximum"
  answer: 1
  explanation: "Expected value is a weighted average of all possible outcomes — it describes the center of the distribution in the long run. It need not be a value the random variable can actually take. The median of {1,2,3,4,5,6} is also 3.5 here, but that's a coincidence — for asymmetric distributions, mean and median differ."

- question: "The expected value of the sum of two random variables always equals the sum of their individual expected values, even when the variables are not independent."
  type: true-false
  answer: true
  explanation: "Linearity of expectation holds unconditionally: E[X + Y] = E[X] + E[Y] for any X and Y, regardless of dependence. Independence is only required for the stronger property E[XY] = E[X]E[Y]. This makes linearity an unusually powerful tool — you can decompose complicated sums without worrying about dependence."

- question: "If X is a random variable with E[X] = 5, what is E[3X − 2]?"
  type: short-answer
  answer: "13"
  explanation: "By linearity of expectation, E[aX + b] = aE[X] + b. Substituting a = 3, b = -2, and E[X] = 5: E[3X − 2] = 3(5) − 2 = 13. This works because expectation is a linear operator — it distributes over addition and pulls constants through."
```

## Explainer

Expected value formalizes a simple intuition: if you repeat an experiment many times, what value will the outcomes average to? You already know, from probability mass functions, that a random variable assigns a probability to each possible outcome. Expected value weights each outcome by its probability and sums the results: E[X] = ∑ x · p(x). For a fair six-sided die, that is (1)(1/6) + (2)(1/6) + ... + (6)(1/6) = 3.5. Notice that 3.5 is not a possible outcome — expected value is a property of the distribution, not a prediction about any single trial.

The most important property of expected value is linearity. If you scale a random variable by a constant a and shift it by b, the expected value scales and shifts the same way: E[aX + b] = aE[X] + b. More powerfully, E[X + Y] = E[X] + E[Y] for *any* X and Y — no independence assumption required. This lets you decompose complicated sums into manageable pieces. For example, the expected number of heads in 10 fair coin flips can be computed as the sum of 10 simple expectations (each 1/2), giving E = 5, without reasoning about the joint distribution at all.

Independence matters for products, not sums. The product rule E[XY] = E[X]E[Y] holds only when X and Y are independent. If they are correlated — say X is the temperature and Y is ice cream sales — then the product expectation will differ from the product of the expectations. Distinguishing where independence is required versus where it is not is a recurring source of errors.

Expected value is the first moment of a distribution and represents its center of mass. It is closely related to variance (the second central moment), which measures spread around the expected value. Understanding expected value deeply — especially linearity — is the foundation for almost everything in probability theory, statistics, and decision-making under uncertainty.

