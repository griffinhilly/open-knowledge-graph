---
id: probability-mass-functions
title: Probability Mass Functions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: discrete-random-variables
  type: hard
builds-toward:
- expected-value
- variance-of-random-variables
- moment-generating-functions
tags:
- pmf
- discrete-distributions
- probability
stage: formal-systems
status: validated
---

# Probability Mass Functions

## Core Idea
The probability mass function (PMF) gives P(X = x) for each possible value x of a discrete random variable X. The PMF satisfies: all probabilities are non-negative and sum to 1. It completely describes the probability distribution.

## How It's Best Learned
Write out PMFs for simple discrete variables (die rolls, coin flips, counting successes). Verify that probabilities sum to 1. Practice calculating probabilities from PMFs by summing over appropriate values.

## Common Misconceptions
Confusing PMF with PDF (PMF applies to discrete, PDF to continuous). Thinking probabilities can be read from a single bar height (PMFs are discrete). Using PMF methods on continuous data.

## Questions

```yaml
- question: "A fair six-sided die has PMF p(x) = 1/6 for x ∈ {1,2,3,4,5,6}. What is P(X ≥ 5)?"
  type: multiple-choice
  options: ["1/6", "1/3", "1/2", "5/6"]
  answer: 1
  explanation: "P(X ≥ 5) = P(X = 5) + P(X = 6) = 1/6 + 1/6 = 2/6 = 1/3. For discrete variables, probabilities of ranges are computed by summing the PMF over the relevant values — unlike continuous distributions where you integrate a density."

- question: "For a continuous random variable (like human height), the probability mass function gives the probability that the variable equals exactly any specific value."
  type: true-false
  answer: false
  explanation: "PMFs only apply to discrete random variables — those that take countable values. Continuous random variables use a probability density function (PDF), where P(X = any exact value) = 0. The PDF gives density, not probability; you must integrate over an interval to get a probability."

- question: "A PMF assigns probability 0.4 to x = 0, probability 0.35 to x = 1, and probability 0.25 to x = 2. Explain why this is a valid PMF."
  type: short-answer
  answer: "It is valid because all values are non-negative (0.4, 0.35, 0.25 ≥ 0) and they sum to exactly 1 (0.4 + 0.35 + 0.25 = 1.00). These are the two requirements for any valid PMF."
  explanation: "The two axioms of a PMF mirror the probability axioms: probabilities cannot be negative, and the total probability across all possible outcomes must equal 1. Any function satisfying these two conditions over a discrete domain is a valid PMF."
```

## Explainer

When you first encountered discrete random variables, you described them informally — a die roll, a coin flip count, a number of defects on an assembly line. A **probability mass function** is the formal tool that completely describes such a variable: it tells you the exact probability that the variable equals each of its possible values.

For a discrete random variable X, the PMF is the function p(x) = P(X = x). For a fair die, p(1) = p(2) = … = p(6) = 1/6. For a biased coin that lands heads 70% of the time, the number of heads in one flip has PMF p(0) = 0.3 and p(1) = 0.7. Any valid PMF must satisfy two conditions: (1) every probability is non-negative, p(x) ≥ 0 for all x, and (2) the probabilities sum to exactly 1 across all possible values. These mirror the axioms of probability you have already studied.

The power of the PMF is that once you have it, you can compute any probability about X by summing. Want P(X > 3) for a die? Add p(4) + p(5) + p(6) = 3/6 = 1/2. Want P(2 ≤ X ≤ 4)? Add p(2) + p(3) + p(4). This "sum over the range" approach is the discrete analogue of integrating a PDF for continuous variables — and understanding the distinction is crucial. A PMF assigns genuine probability to each individual point; a PDF does not (it gives density, and you must integrate over an interval).

The PMF also serves as the foundation for everything you will compute next: the expected value (weighted average of outcomes) and variance (spread of outcomes) are both defined as sums involving the PMF. Any time you see E[X] = Σ x·p(x) or Var(X) = Σ (x - μ)²·p(x), you are applying the PMF directly. Getting comfortable reading and constructing PMFs for simple cases — dice, coins, small finite sample spaces — prepares you for the named distributions (Binomial, Poisson, Geometric) where the PMF has a closed algebraic form.
