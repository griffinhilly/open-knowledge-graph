---
id: limits-continuity-multivariable
title: Limits and Continuity in Multivariable Functions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: functions-of-several-variables
  type: hard
- id: limit-definition-intuitive
  type: hard
builds-toward:
- partial-derivatives
- differentiability-multivariate
tags:
- limits
- continuity
- epsilon-delta
stage: formal-systems
status: draft
---

# Limits and Continuity in Multivariable Functions

## Core Idea
For a multivariable function, lim_(x,y)→(a,b) f(x,y) = L if for every ε > 0 there exists δ > 0 such that |f(x,y) − L| < ε whenever 0 < √[(x−a)² + (y−b)²] < δ. Continuity requires the limit to exist and equal f(a, b). Multiple paths to a point complicate convergence analysis.
