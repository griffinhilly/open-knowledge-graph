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
status: validated
---

# Discrete Random Variables

## Core Idea
A discrete random variable takes on a countable (often finite) set of values. Its distribution is described by the probability mass function (PMF), p(x) = P(X = x), which specifies the probability of each possible value. The PMF must be non-negative and sum to 1. Discrete random variables model count data and outcomes from experiments with finitely many possibilities.

## Questions

```yaml
- question: "Which of the following could be a valid PMF for a random variable taking values {1, 2, 3}?"
  type: multiple-choice
  options:
    - "p(1) = 0.5, p(2) = 0.4, p(3) = 0.2"
    - "p(1) = 0.1, p(2) = -0.1, p(3) = 1.0"
    - "p(1) = 0.3, p(2) = 0.5, p(3) = 0.2"
    - "p(1) = 0.4, p(2) = 0.4, p(3) = 0.4"
  answer: 2
  explanation: "Option C is the only valid PMF: all values are non-negative and they sum to exactly 1 (0.3 + 0.5 + 0.2 = 1.0). Option A fails because the probabilities sum to 1.1. Option B fails because p(2) = -0.1 is negative — probabilities can never be negative. Option D fails because the probabilities sum to 1.2. Both conditions — non-negativity AND summing to 1 — are required; either alone is not sufficient."

- question: "A discrete random variable X has PMF: p(0) = 0.1, p(1) = 0.4, p(2) = 0.3, p(3) = 0.2. What is P(1 ≤ X < 3)?"
  type: multiple-choice
  options:
    - "0.4 — only p(1), since X=1 is the left endpoint"
    - "0.7 — summing p(1) + p(2) = 0.4 + 0.3"
    - "0.9 — summing p(1) + p(2) + p(3) = 0.4 + 0.3 + 0.2"
    - "0.6 — summing p(2) + p(3) = 0.3 + 0.2"
  answer: 1
  explanation: "The event 1 ≤ X < 3 means X can equal 1 or 2 (since X is discrete and integer-valued, 'X < 3' means X ≤ 2). For discrete random variables, event probabilities are found by summing the PMF over all values in the event: p(1) + p(2) = 0.4 + 0.3 = 0.7. Option C is the classic error of treating the strict inequality as inclusive — X = 3 is excluded because 3 < 3 is false."

- question: "A discrete random variable can only take on a finite number of distinct values."
  type: true-false
  answer: false
  explanation: "False. A discrete random variable can take on countably infinitely many values. The standard example is the number of coin flips until the first heads: the possible values are {1, 2, 3, 4, …} with no upper bound, yet the values are still discrete (isolated, listable). 'Discrete' means the values form a countable set — not that the set must be finite."

- question: "For a discrete random variable, the probability that X falls in a range [a, b] is found by summing p(x) over all values x satisfying a ≤ x ≤ b."
  type: true-false
  answer: true
  explanation: "True. This is exactly how event probabilities work for discrete distributions. The PMF assigns a specific probability to each individual value, and any event is a union of those individual outcomes. Summing p(x) over the relevant values uses the additivity of probability for disjoint events. This is fundamentally different from continuous distributions, where you integrate a probability density function — for discrete variables, integration is replaced by summation."

- question: "Explain what the two required properties of a probability mass function are, and why each property is necessary."
  type: short-answer
  answer: "The two required properties are: (1) non-negativity — p(x) ≥ 0 for every value x — because probabilities cannot be negative; and (2) normalization — the sum of p(x) over all possible values equals exactly 1 — because the random variable must take on some value with certainty (total probability = 1). Non-negativity ensures p(x) is interpretable as a probability at each point. Normalization ensures the probabilities form a coherent model of a complete experiment where exactly one outcome occurs."
  explanation: "Together these two properties are necessary and sufficient: any non-negative function on a countable set that sums to 1 is a valid PMF and defines a legitimate discrete random variable. If either property fails — say, a value has probability -0.1, or all values sum to 0.8 — the function cannot represent a genuine probability distribution."
```

## Explainer

From your introduction to random variables, you know that a random variable is a function that assigns a numerical value to each outcome of a random experiment. A **discrete random variable** is one where those values form a countable set — meaning you can list them as x₁, x₂, x₃, … (possibly with finitely many or countably infinitely many entries). Rolling a die gives a discrete random variable taking values {1, 2, 3, 4, 5, 6}. Counting the number of emails you receive in an hour gives a discrete random variable taking values {0, 1, 2, 3, …}. The defining feature is that the values are isolated: there is no value between 3 and 4 emails.

The complete description of a discrete random variable's behavior is its **probability mass function** (PMF). Written p(x) or P(X = x), it assigns a probability to each possible value. For a fair die, p(1) = p(2) = … = p(6) = 1/6. The two requirements on any PMF are (1) p(x) ≥ 0 for all x (probabilities are non-negative) and (2) the sum of p(x) over all possible values equals 1 (something must happen). These two properties are necessary and sufficient: any non-negative function on a countable set that sums to 1 is a valid PMF, and therefore defines a valid random variable. A common way to display a PMF is a table of values and their probabilities, or a bar chart where bar height equals probability.

Once you have a PMF, you can compute probabilities of more complex events by summing. For example, P(X ≤ 3) for a die is p(1) + p(2) + p(3) = 1/2. This accumulation is exactly the **cumulative distribution function** (CDF), F(x) = P(X ≤ x) = Σ_{k ≤ x} p(k). The CDF is a step function that jumps by p(x) at each value x. For discrete random variables, the CDF and PMF carry exactly the same information — you can recover one from the other — but different questions are easier to answer with each form.

The PMF is also the foundation for computing summaries of the distribution. The **expected value** E[X] = Σ x · p(x) is the probability-weighted average of all possible values — you'll study this thoroughly in the next topic. The **variance** Var(X) = E[(X − E[X])²] measures how spread out the distribution is. Most named discrete distributions — Binomial, Geometric, Poisson, Negative Binomial — are simply families of PMFs parameterized by one or two numbers, each arising as a natural model for a different type of counting experiment. The structure you are learning now — PMF, CDF, expectation, variance — applies identically to all of them.
