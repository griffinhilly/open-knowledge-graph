---
id: maclaurin-series
title: Maclaurin Series
domain: mathematics
course: calculus-2
prerequisites:
  - id: taylor-series
    type: hard
builds-toward:
  - taylor-series-common-functions
tags: [series, Maclaurin, Taylor, special-case]
stage: formal-systems
status: draft
---

# Maclaurin Series

## Core Idea
A Maclaurin series is a Taylor series centered at a = 0: sum from n=0 to infinity of f^(n)(0)/n! * x^n. It is not a separate concept from Taylor series but a special case that is used so frequently it has its own name. The most important Maclaurin series (e^x, sin(x), cos(x), 1/(1-x), ln(1+x), arctan(x)) should be memorized because they are used to derive many other series.

## How It's Best Learned
Derive the standard Maclaurin series from the definition. Memorize the key ones. Practice using them to find series for related functions: e^(-x^2) from e^x, sin(x^2) from sin(x), etc. Show how known series can be added, multiplied, substituted, differentiated, and integrated.

## Common Misconceptions
- Believing Maclaurin series and Taylor series are fundamentally different concepts (Maclaurin is just Taylor at 0).
- Not memorizing the standard series and rederiving from scratch every time (inefficient).
- Forgetting the radius of convergence of the manipulated series.
