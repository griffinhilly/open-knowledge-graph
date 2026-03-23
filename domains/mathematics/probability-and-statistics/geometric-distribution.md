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
status: validated
---

# Geometric Distribution

## Core Idea
The geometric distribution models the number of trials needed to achieve the first success in a sequence of independent Bernoulli trials with success probability p. Its PMF is P(X = k) = (1-p)^(k-1) × p for k = 1, 2, 3, ... Mean is 1/p and variance is (1-p)/p². This distribution is memoryless: the probability of success on the next trial doesn't depend on how many failures have occurred.

## How It's Best Learned
Compare with binomial by noting geometric counts until first success, while binomial counts successes in fixed trials. Demonstrate memorylessness with examples.

## Common Misconceptions
Confusing when to use geometric vs. binomial. Different conventions for support (some start at 0, others at 1).

## Questions

```yaml
- question: "A fair coin is flipped repeatedly. After 10 consecutive tails, what is the probability that the next flip is heads?"
  type: multiple-choice
  options:
    - "Greater than 1/2 — the coin is 'due' for heads after so many tails."
    - "Less than 1/2 — a long tails streak suggests the coin may be biased."
    - "Exactly 1/2 — each flip is independent, so past results carry no information."
    - "Exactly (1/2)^11 — the probability of heads after 10 tails is the probability of that whole sequence."
  answer: 2
  explanation: "This is the memorylessness property in action. Each flip is an independent Bernoulli trial with P(heads) = 1/2. The geometric distribution's memorylessness states P(X > m+1 | X > m) = P(X > 1) = 1/2 — the conditional probability of needing one more trial is identical to the unconditional probability. Option A is the gambler's fallacy: random processes do not 'correct' for streaks. Option D confuses the probability of a specific sequence of 11 flips with the conditional probability of the next flip given the previous 10."

- question: "A quality inspector checks items from an assembly line where each item independently has a 5% defect rate. What is the expected number of items she must inspect to find the first defect?"
  type: multiple-choice
  options:
    - "5 items — because 5% of 100 is 5 defects per 100 items."
    - "20 items — because E[X] = 1/p = 1/0.05 = 20."
    - "0.05 items — because the probability of a defect on any one item is 0.05."
    - "95 items — because the probability of a non-defect is 0.95."
  answer: 1
  explanation: "For a geometric distribution with success probability p, E[X] = 1/p. With p = 0.05, E[X] = 20. Intuitively: if each item has a 1-in-20 chance of being defective, you expect to check about 20 items before finding one. Option A confuses the rate (5%) with a count per batch; option C takes p literally as a number of items; option D has no basis in the formula. The mean 1/p also implies that rarer events require more trials on average — lower p means longer expected wait."

- question: "The memorylessness property of the geometric distribution is a direct consequence of the independence of Bernoulli trials."
  type: true-false
  answer: true
  explanation: "Memorylessness — P(X > m+n | X > m) = P(X > n) — follows algebraically from independence. P(X > m) = (1−p)^m is just the probability that m independent trials all fail. Conditional probability gives P(X > m+n | X > m) = (1−p)^(m+n) / (1−p)^m = (1−p)^n = P(X > n). Every step in this derivation relies on independence: the probability of a sequence of failures multiplies because trials are independent. If outcomes were correlated, the distribution would not be memoryless."

- question: "Having already failed 10 times in a geometric trial sequence, the expected number of additional trials needed before the first success is less than 1/p, because you have 'used up' some of your expected waiting time."
  type: true-false
  answer: false
  explanation: "This is the gambler's fallacy expressed in expectation form. The geometric distribution is memoryless: given that you have failed 10 times, the expected number of additional trials is still exactly 1/p — as if you were starting from scratch. The failures are irrelevant because each trial is independent. The mechanism (a coin, a manufacturing defect rate) has not changed. Past outcomes contain no information about future outcomes, so the remaining expected wait is always 1/p regardless of accumulated failures."

- question: "Explain in plain language what the memorylessness property means for the geometric distribution, and why it holds."
  type: short-answer
  answer: "Memorylessness means the distribution of remaining wait time is the same regardless of how long you have already waited. If you flip a coin until heads and have seen 20 tails, the expected number of additional flips is still 1/p — identical to starting fresh. This holds because each flip is an independent Bernoulli trial: the coin has no memory of past results, and past results provide no information about future outcomes. The underlying success probability p is unchanged by any number of failures."
  explanation: "Formally: P(X > m+n | X > m) = P(X > n), which follows directly from independence. This is why the geometric distribution is the discrete analogue of the exponential distribution — the only continuous distribution with the same property. Memorylessness has practical implications: if you are waiting for a bus that arrives with probability p each minute, knowing you've waited 20 minutes does not change the expected additional wait. The wait distribution resets with each passing minute."
```

## Explainer

You know from discrete random variables that a **Bernoulli trial** is a single experiment with two outcomes: success (probability p) and failure (probability 1−p). The geometric distribution answers a natural question: if I keep running independent Bernoulli trials, how many trials will I need before I see the first success? Unlike the binomial, which asks "how many successes in n fixed trials?", the geometric lets the number of trials vary and stops when the experiment succeeds.

The PMF follows directly from the independence and multiplication rules you already know. To get the first success on trial k, you need exactly k−1 failures followed by 1 success. Since each trial is independent, multiply the probabilities: P(X=k) = (1−p)^(k−1) · p. This is the PMF for k = 1, 2, 3, .... Check that it sums to 1: Σₖ₌₁^∞ (1−p)^(k−1)p = p · 1/(1−(1−p)) = 1 by the geometric series formula — which is exactly where the distribution gets its name.

The mean E[X] = 1/p has clear intuitive content. If each trial has a 1-in-5 chance of success, you expect to need 5 trials on average. If success probability is 1%, expect 100 trials. More precisely: E[X] = 1/p and Var(X) = (1−p)/p². Both scale with 1/p — lower success probability means both more trials on average and greater uncertainty about how many you'll need.

The **memorylessness** property is the geometric distribution's most striking feature: P(X > m+n | X > m) = P(X > n). In English, given that you have already failed m times, the probability of needing at least n more trials is identical to the probability of needing at least n trials if you were starting from scratch. Past failures contain no information about future success — because each trial is independent. This makes the geometric distribution the discrete analogue of the exponential distribution. You can verify it directly: P(X > m) = (1−p)^m, so P(X > m+n | X > m) = (1−p)^(m+n)/(1−p)^m = (1−p)^n = P(X > n). The independence assumption is doing all the work.
