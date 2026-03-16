---
id: discrete-random-variables
title: Discrete Random Variables
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: random-variables-intro
  type: hard
builds-toward:
- expected-value-and-variance
- binomial-distribution
- geometric-distribution
- poisson-distribution
tags:
- discrete
- probability-mass-function
- pmf
stage: formal-systems
status: draft
---

# Discrete Random Variables

## Core Idea
A discrete random variable takes on a countable (often finite) set of values. Its distribution is described by the probability mass function (PMF), p(x) = P(X = x), which specifies the probability of each possible value. The PMF must be non-negative and sum to 1. Discrete random variables model count data and outcomes from experiments with finitely many possibilities.

## Explainer

From your introduction to random variables, you know that a random variable is a function that assigns a numerical value to each outcome of a random experiment. A **discrete random variable** is one where those values form a countable set — meaning you can list them as x₁, x₂, x₃, … (possibly with finitely many or countably infinitely many entries). Rolling a die gives a discrete random variable taking values {1, 2, 3, 4, 5, 6}. Counting the number of emails you receive in an hour gives a discrete random variable taking values {0, 1, 2, 3, …}. The defining feature is that the values are isolated: there is no value between 3 and 4 emails.

The complete description of a discrete random variable's behavior is its **probability mass function** (PMF). Written p(x) or P(X = x), it assigns a probability to each possible value. For a fair die, p(1) = p(2) = … = p(6) = 1/6. The two requirements on any PMF are (1) p(x) ≥ 0 for all x (probabilities are non-negative) and (2) the sum of p(x) over all possible values equals 1 (something must happen). These two properties are necessary and sufficient: any non-negative function on a countable set that sums to 1 is a valid PMF, and therefore defines a valid random variable. A common way to display a PMF is a table of values and their probabilities, or a bar chart where bar height equals probability.

Once you have a PMF, you can compute probabilities of more complex events by summing. For example, P(X ≤ 3) for a die is p(1) + p(2) + p(3) = 1/2. This accumulation is exactly the **cumulative distribution function** (CDF), F(x) = P(X ≤ x) = Σ_{k ≤ x} p(k). The CDF is a step function that jumps by p(x) at each value x. For discrete random variables, the CDF and PMF carry exactly the same information — you can recover one from the other — but different questions are easier to answer with each form.

The PMF is also the foundation for computing summaries of the distribution. The **expected value** E[X] = Σ x · p(x) is the probability-weighted average of all possible values — you'll study this thoroughly in the next topic. The **variance** Var(X) = E[(X − E[X])²] measures how spread out the distribution is. Most named discrete distributions — Binomial, Geometric, Poisson, Negative Binomial — are simply families of PMFs parameterized by one or two numbers, each arising as a natural model for a different type of counting experiment. The structure you are learning now — PMF, CDF, expectation, variance — applies identically to all of them.
