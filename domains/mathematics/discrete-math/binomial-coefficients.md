---
id: binomial-coefficients
title: Binomial Coefficients and Pascal's Triangle
domain: mathematics
course: discrete-math
prerequisites:
- id: combinations-and-selections
  type: hard
builds-toward:
- binomial-theorem
- multinomial-theorem
tags:
- combinatorics
- binomial
stage: formal-systems
status: draft
---

# Binomial Coefficients and Pascal's Triangle

## Core Idea
Binomial coefficients C(n,k) = n!/(k!(n-k)!) count the ways to choose k items from n items. These coefficients appear as entries in Pascal's triangle and satisfy the recursive property C(n,k) = C(n-1,k-1) + C(n-1,k). They also form the coefficients in the expansion of (a+b)^n.
