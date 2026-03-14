---
id: logarithms-intro
title: Logarithms Introduction
domain: mathematics
course: algebra-2
prerequisites:
  - id: exponential-functions-and-graphs
    type: hard
  - id: inverse-functions
    type: hard
builds-toward:
  - logarithm-properties
  - solving-logarithmic-equations
  - natural-logarithm-and-e
tags: [logarithms, inverse, exponential, definition]
stage: abstract-reasoning
status: validated
---

# Logarithms Introduction

## Core Idea
A logarithm answers the question: "To what exponent must we raise the base to get this number?" Formally, log_b(x) = y means b^y = x. The logarithm function is the inverse of the exponential function. Key values: log_b(1) = 0, log_b(b) = 1, log_b(b^n) = n. Common logarithm: log(x) = log_10(x). Natural logarithm: ln(x) = log_e(x). The domain of log_b(x) is x > 0.

## How It's Best Learned
Start with the conversion between exponential and logarithmic forms: 2^3 = 8 means log_2(8) = 3. Practice converting in both directions. Evaluate logarithms by asking "what exponent gives me this?" Graph y = log_b(x) as the reflection of y = b^x over y = x. Emphasize that log is undefined for zero and negative numbers.

## Common Misconceptions
- Thinking log_b(0) is defined (it is not; you cannot raise a positive base to any power and get 0).
- Confusing log_b(x) with b*x or x/b (log is an exponent, not multiplication or division).
- Not recognizing that log and ln are the same concept with different bases.
- Thinking log(a + b) = log(a) + log(b) (this is wrong; the product rule is log(a*b) = log(a) + log(b)).
