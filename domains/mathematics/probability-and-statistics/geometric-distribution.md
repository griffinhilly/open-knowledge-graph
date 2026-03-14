---
id: geometric-distribution
title: The Geometric Distribution
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: independence-and-multiplication-rule
  type: hard
- id: binomial-distribution
  type: soft
tags:
- geometric-distribution
- waiting-time
- first-success
- memoryless
stage: formal-systems
status: validated
---

# The Geometric Distribution

## Core Idea
The geometric distribution models the number of independent Bernoulli trials until the first success, with P(X = k) = (1−p)^(k−1) · p. The mean is 1/p — on average, you need 1/p trials to see the first success — and the variance is (1−p)/p². Its defining property is memorylessness: having already failed k times does not change the probability distribution for future trials.

## How It's Best Learned
Use physical simulations: roll a die until you get a 6 and record how many rolls it took. Repeat many times to build an empirical distribution and compare to the theoretical geometric. Contrast with binomial by asking: binomial fixes n and asks about k; geometric fixes one success and asks when.

## Common Misconceptions
- Thinking previous failures make future success 'more likely' — the memoryless property directly contradicts this.
- Confusion over whether the first success is included in the count (X = number of trials including success vs. number of failures before success — two common conventions).
