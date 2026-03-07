---
id: radius-and-interval-of-convergence
title: Radius and Interval of Convergence
domain: mathematics
course: calculus-2
prerequisites:
  - id: power-series
    type: hard
  - id: ratio-test
    type: hard
  - id: root-test
    type: soft
builds-toward:
  - taylor-series
tags: [series, power-series, convergence, radius]
stage: formal-systems
status: draft
---

# Radius and Interval of Convergence

## Core Idea
Every power series sum of c_n * (x - a)^n has a radius of convergence R such that the series converges absolutely for |x - a| < R and diverges for |x - a| > R. The interval of convergence is (a - R, a + R) with the endpoints requiring separate testing. R is found using the ratio test or root test applied to the general term. R can be 0 (converges only at a), infinity (converges everywhere), or any positive number.

## How It's Best Learned
Apply the ratio test to |c_n (x - a)^n| and solve for the values of x where the resulting limit is less than 1. This gives R. Then test each endpoint individually using known series tests (p-series, alternating series, etc.). Practice until the three-step process (find R, determine interval, test endpoints) is systematic.

## Common Misconceptions
- Forgetting to test the endpoints (the ratio/root test is inconclusive at |x - a| = R).
- Believing the radius of convergence determines the interval completely (endpoints must be checked separately).
- Confusing radius of convergence with interval of convergence (R is a number, the interval is a set).
