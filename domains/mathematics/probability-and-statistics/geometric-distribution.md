---
id: geometric-distribution
title: Geometric Distribution
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: discrete-random-variables
  type: hard
- id: independence-and-multiplication-rule
  type: hard
tags:
- geometric
- waiting-time
- first-success
stage: formal-systems
status: draft
---

# Geometric Distribution

## Core Idea
The geometric distribution models the number of trials needed to achieve the first success in a sequence of independent Bernoulli trials with success probability p. Its PMF is P(X = k) = (1-p)^(k-1) × p for k = 1, 2, 3, ... Mean is 1/p and variance is (1-p)/p². This distribution is memoryless: the probability of success on the next trial doesn't depend on how many failures have occurred.

## How It's Best Learned
Compare with binomial by noting geometric counts until first success, while binomial counts successes in fixed trials. Demonstrate memorylessness with examples.

## Common Misconceptions
Confusing when to use geometric vs. binomial. Different conventions for support (some start at 0, others at 1).

## Explainer

You know from discrete random variables that a **Bernoulli trial** is a single experiment with two outcomes: success (probability p) and failure (probability 1−p). The geometric distribution answers a natural question: if I keep running independent Bernoulli trials, how many trials will I need before I see the first success? Unlike the binomial, which asks "how many successes in n fixed trials?", the geometric lets the number of trials vary and stops when the experiment succeeds.

The PMF follows directly from the independence and multiplication rules you already know. To get the first success on trial k, you need exactly k−1 failures followed by 1 success. Since each trial is independent, multiply the probabilities: P(X=k) = (1−p)^(k−1) · p. This is the PMF for k = 1, 2, 3, .... Check that it sums to 1: Σₖ₌₁^∞ (1−p)^(k−1)p = p · 1/(1−(1−p)) = 1 by the geometric series formula — which is exactly where the distribution gets its name.

The mean E[X] = 1/p has clear intuitive content. If each trial has a 1-in-5 chance of success, you expect to need 5 trials on average. If success probability is 1%, expect 100 trials. More precisely: E[X] = 1/p and Var(X) = (1−p)/p². Both scale with 1/p — lower success probability means both more trials on average and greater uncertainty about how many you'll need.

The **memorylessness** property is the geometric distribution's most striking feature: P(X > m+n | X > m) = P(X > n). In English, given that you have already failed m times, the probability of needing at least n more trials is identical to the probability of needing at least n trials if you were starting from scratch. Past failures contain no information about future success — because each trial is independent. This makes the geometric distribution the discrete analogue of the exponential distribution. You can verify it directly: P(X > m) = (1−p)^m, so P(X > m+n | X > m) = (1−p)^(m+n)/(1−p)^m = (1−p)^n = P(X > n). The independence assumption is doing all the work.
