---
id: geometric-distribution-properties
title: 'Geometric Distribution: Waiting Times'
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: geometric-distribution
  type: soft
builds-toward:
- exponential-distribution-theory
tags:
- geometric
- waiting-time
stage: formal-systems
status: validated
---

# Geometric Distribution: Waiting Times

## Core Idea
Geometric(p): number of trials until first success with probability p. PMF: P(X=k)=(1−p)^{k-1}p. E[X]=1/p, Var(X)=(1−p)/p². Only discrete distribution with memoryless property: P(X>n+m|X>n)=P(X>m).

## Questions

```yaml
- question: "You roll a fair die 30 times without rolling a six (p = 1/6). What does the memoryless property tell you about your remaining wait?"
  type: multiple-choice
  options:
    - "You are now overdue — the probability of rolling a six on the next roll is higher than 1/6"
    - "Your remaining wait follows Geometric(1/6) — exactly the same distribution as if you had just started"
    - "The expected additional wait is now shorter because some of the 'probability mass' has been used up"
    - "You need fewer than 6 expected additional rolls because past failures shift the distribution leftward"
  answer: 1
  explanation: "The memoryless property states P(X > n+m | X > n) = P(X > m). Given that you have already waited 30 trials, the conditional distribution of additional waiting time is still Geometric(1/6), with expected value 6. Past failures carry no information because each trial is independent. Options A, C, and D all reflect the gambler's fallacy — the intuition that past failures make future success 'due,' which independence directly refutes."

- question: "Among all discrete probability distributions, what is special about the geometric distribution regarding the memoryless property?"
  type: multiple-choice
  options:
    - "It is one of several discrete distributions that have the memoryless property"
    - "It is the only discrete distribution with the memoryless property"
    - "It shares the memoryless property with the binomial and Poisson distributions"
    - "All discrete distributions derived from Bernoulli trials have the memoryless property"
  answer: 1
  explanation: "The geometric distribution is the unique discrete distribution with the memoryless property. This can be proven: any discrete distribution with the memoryless property must satisfy P(X = k) = (1-p)^{k-1}p for some p, which is exactly the geometric PMF. The Poisson, binomial, and negative binomial distributions do not have this property. This uniqueness is what makes the geometric distribution the discrete analog of the exponential."

- question: "After failing 15 consecutive times on a Geometric(0.2) experiment, the probability of success on the next trial is greater than 0.2 because a success is now 'overdue.'"
  type: true-false
  answer: false
  explanation: "This is the gambler's fallacy applied to the geometric distribution. Each trial is an independent Bernoulli trial with probability p = 0.2. Past failures carry no information about future outcomes — the probability on any single trial is always exactly 0.2. The memoryless property formalizes this: P(X > 16 | X > 15) = P(X > 1) = 1 - p = 0.8, exactly as before."

- question: "The continuous analog of the geometric distribution — the exponential distribution — also has the memoryless property."
  type: true-false
  answer: true
  explanation: "Just as the geometric is the only memoryless discrete distribution, the exponential is the only memoryless continuous distribution. This is not a coincidence — the exponential distribution is the continuous limit of the geometric as p → 0 and the trial rate grows, with λ = p × (trials per unit time) held constant. The memoryless property is what unifies the geometric and exponential as the fundamental waiting-time distributions in their respective settings."

- question: "In your own words, what does the memoryless property mean for the geometric distribution, and why does it follow directly from the independence of trials?"
  type: short-answer
  answer: "The memoryless property means that if you have already waited n trials without success, the conditional distribution of your remaining wait is identical to the original distribution — as if the n failures never happened. It follows from independence because each trial is a fresh Bernoulli(p) experiment with no connection to past outcomes. There is no accumulated 'pressure' toward success; the probability p on the next trial is always the same, regardless of history."
  explanation: "The memoryless property is a consequence of independence, not an additional assumption. Because trials are independent, conditioning on past failures gives no information about future trials. This is what separates geometric waiting from processes with 'wear' or 'aging' — a light bulb that physically degrades over time is not memoryless, but a process of independent coin flips is."
```

## Explainer

The geometric distribution models the simplest waiting time scenario: you repeatedly perform independent Bernoulli trials (each succeeds with probability p), and X counts how many trials you need until the first success. From your study of the **geometric distribution** basics, you know the PMF is P(X = k) = (1 − p)^{k−1} · p. The factor (1 − p)^{k−1} is the probability of failing k − 1 times in a row; the final factor p is the probability of succeeding on trial k. The trials are independent, so these multiply.

The mean E[X] = 1/p has a clean intuition: if each trial succeeds with probability p, you need on average 1/p trials. With p = 0.1 (a 10% success rate), expect 10 trials. With p = 0.5, expect 2. This can be derived by summing the series Σ k(1−p)^{k−1}p from k = 1 to ∞, or more elegantly by a first-step argument: on the first trial, you either succeed (probability p) or fail and restart (probability 1−p), giving E[X] = p · 1 + (1−p)(1 + E[X]), which solves to E[X] = 1/p. The variance Var(X) = (1−p)/p² captures how spread out the waiting time is — when p is small, waits are long and highly variable.

The **memoryless property** is the geometric distribution's most important characteristic, and the only discrete distribution that has it. It states: P(X > n + m | X > n) = P(X > m). In plain language: if you have already waited n trials without success, the conditional distribution of additional waiting time is exactly the same as the original distribution — as if the n failed trials never happened. Each trial truly starts fresh. A concrete example: you're rolling a die waiting for a six (p = 1/6). After rolling 20 times without a six, your expected additional wait is still 6 more rolls — not 6 minus 20. Past failures give you no information about future trials when each trial is independent.

The memoryless property is what connects the geometric distribution to its continuous analog: the **exponential distribution** builds exactly on this concept, replacing discrete trial counts with continuous time. Just as Geometric(p) is the only memoryless discrete distribution, Exponential(λ) is the only memoryless continuous distribution. The exponential distribution is the continuous limit of the geometric as p → 0 and the number of trials per unit time grows, with λ = p · (trials per unit time) held constant. Understanding the geometric distribution's waiting-time interpretation and memoryless property is therefore the discrete foundation for all of continuous-time probability theory.
