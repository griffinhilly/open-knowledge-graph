---
id: binomial-distribution
title: Binomial Distribution
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: discrete-random-variables
  type: hard
- id: independence-and-multiplication-rule
  type: hard
builds-toward:
- normal-distribution
- sampling-distributions
tags:
- binomial
- discrete-distribution
- bernoulli
- trials
stage: formal-systems
status: draft
---

# Binomial Distribution

## Core Idea
The binomial distribution models the number of successes in n independent Bernoulli trials, each with success probability p. Its PMF is P(X = k) = C(n,k) × p^k × (1-p)^(n-k), where C(n,k) is the binomial coefficient. The mean is np and variance is np(1-p). Binomial distributions arise whenever we count successes in a fixed number of identical, independent trials.

## How It's Best Learned
Derive the binomial formula from first principles using counting and independence. Explore how the distribution changes with n and p using simulation or calculation.

## Common Misconceptions
Assuming binomial applies without independent trials or equal p. Confusing binomial coefficients with probabilities. Misremembering whether variance is np or np(1-p).

## Explainer

You already know what a **discrete random variable** is — a variable that takes specific countable values, each with a defined probability — and you understand the **multiplication rule for independent events**. The binomial distribution is what emerges when you combine those two ideas in the most natural setting: repeated independent trials with the same outcome structure each time.

A single trial with two outcomes (success with probability p, failure with probability 1 − p) is called a **Bernoulli trial**. The binomial distribution counts successes across n such trials performed independently. To derive the PMF, ask: what is the probability of exactly k successes in n trials? One specific sequence with k successes and (n − k) failures has probability p^k · (1 − p)^(n − k) by the multiplication rule for independent events. But there are **C(n, k)** ways to arrange k successes among n positions (the binomial coefficient, "n choose k"), and each arrangement has the same probability. So P(X = k) = C(n, k) · p^k · (1 − p)^(n − k). The formula is not handed down from above — it follows directly from counting arrangements and multiplying independent probabilities.

The **mean** E[X] = np has a clean intuition: if each trial succeeds with probability p, you expect np successes out of n. To see this formally, write X = X₁ + X₂ + ... + Xₙ where each Xᵢ is a Bernoulli(p) indicator variable. Since E[Xᵢ] = p for each i, linearity of expectation gives E[X] = np. The **variance** Var(X) = np(1 − p) follows similarly from the independence of the Xᵢ's: variances add for independent variables, and Var(Xᵢ) = p(1 − p) for each Bernoulli trial. Notice that variance is largest when p = 1/2 (maximum uncertainty) and shrinks toward zero as p approaches 0 or 1 (near certainty).

Two conditions must hold for the binomial to be appropriate: **fixed n** (the number of trials is set in advance) and **constant, independent p** (each trial has the same success probability and the trials do not influence each other). Drawing without replacement from a small population violates independence; trials where the probability of success shifts over time violate the constant-p condition. When these conditions hold — flipping a fair coin 20 times, testing whether each of 100 components is defective, counting how many of 50 email recipients click a link — the binomial distribution is the exact model. As n grows large, the binomial distribution approaches the normal distribution, which is why the normal appears as a limit for sums of independent random variables and why the binomial is your bridge to that next major topic.
