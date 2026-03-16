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
status: draft
---

# Probability Mass Functions and Discrete Distributions

## Core Idea
The PMF p(x)=P(X=x) of a discrete random variable assigns probability to each value in its range. Valid PMFs satisfy p(x)≥0 and ∑p(x)=1. The PMF completely characterizes the distribution and enables computing probabilities of events as sums of point probabilities.

## Explainer

You already know that a **random variable** is a function that maps outcomes of an experiment to numbers. A **probability mass function** (PMF) is simply the rule that tells you how much probability weight each number in the range receives. Think of it as a probability budget: you have a total of 1.0 to spend, and the PMF specifies exactly how much goes to each possible outcome.

Consider a fair six-sided die. The random variable X gives the number rolled. The PMF is p(1) = p(2) = p(3) = p(4) = p(5) = p(6) = 1/6. Each value gets an equal share of the budget, and the shares sum to exactly 1. The key insight distinguishing discrete distributions from continuous ones is that here each individual value carries nonzero probability — you can meaningfully ask "what is P(X = 3)?" and get a real answer, 1/6. With a continuous random variable, any single point has probability zero.

The two validity conditions — **nonnegativity** (p(x) ≥ 0 for all x) and **normalization** (∑p(x) = 1 over all x in the range) — are the only constraints a PMF must satisfy. These mirror the axioms of probability you've already internalized: probabilities can't be negative, and the total probability of all outcomes is 1. A PMF is just a concrete bookkeeping device that encodes those axioms for a specific discrete random variable.

Once you have the PMF, computing event probabilities is mechanical: just add up the point probabilities of all outcomes in the event. For example, if p(1) = 0.1, p(2) = 0.3, p(3) = 0.4, p(4) = 0.2, then P(X ≤ 2) = p(1) + p(2) = 0.4. This additive structure is what makes discrete distributions tractable. The PMF is also the foundation for the two quantities you'll study next: the **expected value** (a weighted average of the values, weighted by their probabilities) and the **variance** (a weighted average of the squared deviations from the mean). Both reduce to sums over the PMF, so a thorough understanding of the PMF now pays dividends immediately.
