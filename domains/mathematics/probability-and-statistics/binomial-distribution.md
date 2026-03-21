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

## Questions

```yaml
- question: "A bag contains 5 red and 5 blue marbles. You draw 3 marbles one at a time without replacement. Can the binomial distribution model the number of red marbles you draw?"
  type: multiple-choice
  options:
    - "Yes — there are a fixed number of trials (3) and two outcomes (red or not red) per draw"
    - "No — drawing without replacement changes the probability of success on each trial, violating the independence requirement"
    - "Yes — as long as you count only two outcomes per trial, binomial applies"
    - "No — binomial requires more than 3 trials to produce a valid distribution"
  answer: 1
  explanation: "The binomial distribution requires both a fixed number of trials AND independent trials with constant success probability p. Drawing without replacement violates both of these last conditions: the probability of drawing red changes with each draw (after drawing one red, there are only 4 red of 9 remaining), and the draws are not independent. The correct model for sampling without replacement from a finite population is the hypergeometric distribution. This is one of the most common errors in applying the binomial: the setup looks right (binary outcomes, fixed draws) but the dependence created by sampling without replacement disqualifies it."

- question: "In the binomial PMF, P(X = k) = C(n,k) × p^k × (1−p)^(n−k), what does the binomial coefficient C(n,k) count?"
  type: multiple-choice
  options:
    - "The probability that the first k trials all succeed"
    - "The number of distinct arrangements of k successes among n trials"
    - "The expected number of successes in n trials with probability p"
    - "The ratio of the probability of k successes to the probability of k failures"
  answer: 1
  explanation: "C(n,k) — 'n choose k' — counts the number of distinct ways to arrange k successes among n positions. Each specific sequence of k successes and (n−k) failures has probability p^k × (1−p)^(n−k) by the multiplication rule for independent events. Since there are C(n,k) such sequences and each has the same probability (because trials are independent and identically distributed), we multiply. C(n,k) is not a probability itself — it is a count of equally likely arrangements. Understanding why C(n,k) appears is the key to deriving the formula from first principles rather than memorizing it."

- question: "The variance of a binomial distribution with parameters n and p is largest when p = 0.5."
  type: true-false
  answer: true
  explanation: "The binomial variance is np(1−p). For fixed n, this is maximized by maximizing p(1−p). Taking the derivative with respect to p and setting to zero gives p = 0.5. Intuitively, this makes sense: when p is near 0 or 1, you are nearly certain of the outcome on each trial (almost always failure or almost always success), so there is little uncertainty and thus low variance. When p = 0.5, each trial is maximally uncertain, and the distribution of successes is most spread out. This is also why the Bernoulli distribution has maximum variance at p = 0.5."

- question: "The variance of a binomial distribution with n trials and success probability p equals np."
  type: true-false
  answer: false
  explanation: "The variance is np(1−p), not np. np alone is the mean. Students often confuse these because both involve n and p. The (1−p) factor reflects that variance is reduced when outcomes are more predictable: as p approaches 0 or 1, (1−p) shrinks toward 0 and so does the variance. The mean np grows with p (more likely successes means more expected successes), but the variance peaks at p = 0.5 and falls to zero at both extremes. A useful check: at p = 1, every trial succeeds with certainty, so variance must be 0. np = n at p = 1, which is wrong; np(1−p) = 0 at p = 1, which is correct."

- question: "Why must trials be independent for the binomial distribution to apply, and what happens to the probability calculation if they are not?"
  type: short-answer
  answer: "Independence is required because the binomial PMF is derived by multiplying probabilities across trials: the probability of a specific sequence of k successes is p^k × (1−p)^(n−k) only if each trial's outcome does not affect the others. If trials are dependent, the probability of each trial's outcome changes based on previous outcomes, and you cannot simply multiply p and (1−p) fixed values — you would need conditional probabilities that differ for each trial. The formula breaks down and the resulting probability is incorrect. Sampling without replacement is the canonical case: each draw changes the composition of the population, so subsequent probabilities shift, and the hypergeometric distribution applies instead."
  explanation: "The mathematical derivation makes the requirement explicit: we write P(X = k) = C(n,k) × p^k × (1−p)^(n−k) by multiplying C(n,k) sequences each with probability p^k × (1−p)^(n−k). This multiplication step assumes independent events. When trials are dependent, the joint probability of a sequence is not the product of the marginals, and the entire counting argument collapses. Always verify independence (and constant p) before applying the binomial."
```

## Explainer

You already know what a **discrete random variable** is — a variable that takes specific countable values, each with a defined probability — and you understand the **multiplication rule for independent events**. The binomial distribution is what emerges when you combine those two ideas in the most natural setting: repeated independent trials with the same outcome structure each time.

A single trial with two outcomes (success with probability p, failure with probability 1 − p) is called a **Bernoulli trial**. The binomial distribution counts successes across n such trials performed independently. To derive the PMF, ask: what is the probability of exactly k successes in n trials? One specific sequence with k successes and (n − k) failures has probability p^k · (1 − p)^(n − k) by the multiplication rule for independent events. But there are **C(n, k)** ways to arrange k successes among n positions (the binomial coefficient, "n choose k"), and each arrangement has the same probability. So P(X = k) = C(n, k) · p^k · (1 − p)^(n − k). The formula is not handed down from above — it follows directly from counting arrangements and multiplying independent probabilities.

The **mean** E[X] = np has a clean intuition: if each trial succeeds with probability p, you expect np successes out of n. To see this formally, write X = X₁ + X₂ + ... + Xₙ where each Xᵢ is a Bernoulli(p) indicator variable. Since E[Xᵢ] = p for each i, linearity of expectation gives E[X] = np. The **variance** Var(X) = np(1 − p) follows similarly from the independence of the Xᵢ's: variances add for independent variables, and Var(Xᵢ) = p(1 − p) for each Bernoulli trial. Notice that variance is largest when p = 1/2 (maximum uncertainty) and shrinks toward zero as p approaches 0 or 1 (near certainty).

Two conditions must hold for the binomial to be appropriate: **fixed n** (the number of trials is set in advance) and **constant, independent p** (each trial has the same success probability and the trials do not influence each other). Drawing without replacement from a small population violates independence; trials where the probability of success shifts over time violate the constant-p condition. When these conditions hold — flipping a fair coin 20 times, testing whether each of 100 components is defective, counting how many of 50 email recipients click a link — the binomial distribution is the exact model. As n grows large, the binomial distribution approaches the normal distribution, which is why the normal appears as a limit for sums of independent random variables and why the binomial is your bridge to that next major topic.
