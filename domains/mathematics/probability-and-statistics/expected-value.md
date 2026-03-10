---
id: expected-value
title: Expected Value
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: random-variables-intro
  type: hard
- id: sigma-notation
  type: hard
builds-toward:
- variance-of-random-variables
- binomial-distribution
- poisson-distribution
- sampling-distributions
tags:
- expected-value
- mean
- expectation
- long-run-average
- weighted-average
stage: formal-systems
status: draft
---

# Expected Value

## Core Idea
The expected value E(X) = Σ x · P(X = x) is the long-run average value of a random variable over many repetitions of the experiment. It is a weighted average of all possible values, where each weight is the corresponding probability. E(X) need not be a value the variable can actually take — for a fair die, E(X) = 3.5. Key properties: E(aX + b) = aE(X) + b, and for independent variables, E(X + Y) = E(X) + E(Y).

## How It's Best Learned
Games of chance (lotteries, casino games) make expected value immediately meaningful. Have students compute expected payoffs to determine whether a game is fair. Then connect to the long-run frequency interpretation with simulations.

## Common Misconceptions
- Thinking the expected value will actually occur on a single trial.
- Forgetting to multiply each outcome by its probability — treating it as a simple average.
- Not recognizing that E(X + Y) = E(X) + E(Y) holds even when X and Y are dependent.
