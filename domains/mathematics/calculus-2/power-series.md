---
id: power-series
title: Power Series
domain: mathematics
course: calculus-2
prerequisites:
- id: geometric-series
  type: hard
- id: absolute-vs-conditional-convergence
  type: hard
- id: binomial-theorem-expansion
  type: soft
builds-toward:
- radius-and-interval-of-convergence
- taylor-polynomials
tags:
- series
- power-series
- functions
stage: formal-systems
status: validated
---
# Power Series

## Core Idea
A power series centered at a is sum from n=0 to infinity of c_n * (x - a)^n, where c_n are the coefficients and x is the variable. It is a "polynomial of infinite degree" that defines a function of x on whatever interval it converges. Within its interval of convergence, a power series can be differentiated and integrated term by term. Power series are the bridge between series and functions, culminating in Taylor series representations.

## How It's Best Learned
Start with the geometric series 1/(1 - x) = sum of x^n for |x| < 1 as the prototype power series. Manipulate it (substitute, differentiate, integrate) to generate new power series. Introduce the concept of radius of convergence. Emphasize that the power series defines a function whose domain is determined by convergence.

## Common Misconceptions
- Treating a power series as valid for all x (it converges only within its radius of convergence).
- Forgetting that term-by-term differentiation and integration are only valid inside the interval of convergence.
- Confusing the coefficients c_n with the partial sums.
