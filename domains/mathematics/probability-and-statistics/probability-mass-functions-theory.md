---
id: probability-mass-functions-theory
title: Probability Mass Functions and Discrete Distributions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: random-variables-definition-types
  type: hard
builds-toward:
- expected-value
- variance-of-random-variables
tags:
- pmf
- discrete
stage: formal-systems
status: validated
---

# Probability Mass Functions and Discrete Distributions

## Core Idea
The PMF p(x)=P(X=x) of a discrete random variable assigns probability to each value in its range. Valid PMFs satisfy p(x)≥0 and ∑p(x)=1. The PMF completely characterizes the distribution and enables computing probabilities of events as sums of point probabilities.

## Questions

```yaml
- question: "A discrete random variable X has PMF: p(1) = 0.2, p(2) = 0.3, p(3) = 0.4, p(4) = 0.1. What is P(X ≥ 3)?"
  type: multiple-choice
  options:
    - "0.4"
    - "0.5"
    - "0.6"
    - "0.9"
  answer: 1
  explanation: "P(X ≥ 3) = p(3) + p(4) = 0.4 + 0.1 = 0.5. This is computed by summing the PMF values at all outcomes in the event — the defining operation for discrete distributions. Option A (0.4) is p(3) alone, a classic off-by-one error from misreading 'at least 3' as 'exactly 3.'"

- question: "For a continuous random variable Y and a discrete random variable X, both describing the same phenomenon, which statement is always true?"
  type: multiple-choice
  options:
    - "P(X = 5) can be positive; P(Y = 5) must equal zero"
    - "P(X = 5) and P(Y = 5) are both positive if 5 is the most likely value"
    - "P(X = 5) = 0 because individual points have no width"
    - "Both P(X = 5) and P(Y = 5) must equal zero for the distributions to integrate to 1"
  answer: 0
  explanation: "The key distinction between discrete and continuous distributions: a discrete random variable can assign positive probability to individual values — P(X = 5) > 0 is perfectly valid and is exactly what the PMF specifies. For a continuous random variable, every single point has probability zero; probability only accumulates over intervals. Option B is a common misconception — the most likely value in a continuous distribution still has probability zero."

- question: "A PMF can validly assign probability 0 to some values in the random variable's range, as long as all probabilities are nonnegative and sum to 1."
  type: true-false
  answer: true
  explanation: "True. The two validity conditions for a PMF are p(x) ≥ 0 for all x and ∑p(x) = 1. Assigning p(x) = 0 to some values satisfies both conditions — a zero probability just means that outcome never occurs. For example, a die that never lands on 6 would have p(6) = 0 while still being a valid PMF."

- question: "For a discrete random variable, all PMF values must be equal — each outcome gets the same share of the probability budget."
  type: true-false
  answer: false
  explanation: "False. Equal probabilities (a uniform distribution) are a special case, not a requirement. A valid PMF only requires nonnegativity and that all values sum to 1. A loaded die, for example, might have p(6) = 0.5 and p(1) = p(2) = p(3) = p(4) = p(5) = 0.1 — a completely valid PMF where outcomes have unequal probabilities."

- question: "Why can a continuous random variable not have a probability mass function, and why does this distinction matter for computing event probabilities?"
  type: short-answer
  answer: "A continuous random variable takes values on an uncountable range (e.g., all real numbers in an interval). If we tried to assign positive probability to each of uncountably many points, even tiny values would sum to infinity, violating the normalization condition. For continuous variables, probability accumulates over intervals, not points — P(a ≤ Y ≤ b) > 0 even when P(Y = a) = 0. For a discrete variable, event probabilities are computed by summing PMF values, which works because there are only countably many possible outcomes."
  explanation: "This distinction drives the entire difference in mathematical machinery: PMFs and sums for discrete distributions, probability density functions and integrals for continuous ones. Understanding that individual points carry zero probability in the continuous case prevents the common error of trying to compute P(Y = 5) for a normally distributed variable."
```

## Explainer

You already know that a **random variable** is a function that maps outcomes of an experiment to numbers. A **probability mass function** (PMF) is simply the rule that tells you how much probability weight each number in the range receives. Think of it as a probability budget: you have a total of 1.0 to spend, and the PMF specifies exactly how much goes to each possible outcome.

Consider a fair six-sided die. The random variable X gives the number rolled. The PMF is p(1) = p(2) = p(3) = p(4) = p(5) = p(6) = 1/6. Each value gets an equal share of the budget, and the shares sum to exactly 1. The key insight distinguishing discrete distributions from continuous ones is that here each individual value carries nonzero probability — you can meaningfully ask "what is P(X = 3)?" and get a real answer, 1/6. With a continuous random variable, any single point has probability zero.

The two validity conditions — **nonnegativity** (p(x) ≥ 0 for all x) and **normalization** (∑p(x) = 1 over all x in the range) — are the only constraints a PMF must satisfy. These mirror the axioms of probability you've already internalized: probabilities can't be negative, and the total probability of all outcomes is 1. A PMF is just a concrete bookkeeping device that encodes those axioms for a specific discrete random variable.

Once you have the PMF, computing event probabilities is mechanical: just add up the point probabilities of all outcomes in the event. For example, if p(1) = 0.1, p(2) = 0.3, p(3) = 0.4, p(4) = 0.2, then P(X ≤ 2) = p(1) + p(2) = 0.4. This additive structure is what makes discrete distributions tractable. The PMF is also the foundation for the two quantities you'll study next: the **expected value** (a weighted average of the values, weighted by their probabilities) and the **variance** (a weighted average of the squared deviations from the mean). Both reduce to sums over the PMF, so a thorough understanding of the PMF now pays dividends immediately.
