---
id: multivariable-limits-definition
title: Limits of Multivariable Functions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: multivariable-functions-intro-domain
  type: hard
- id: epsilon-delta-continuity
  type: soft
builds-toward:
- continuity-multivariable
- partial-derivatives
tags:
- limits
- multivariable
- epsilon-delta
stage: formal-systems
status: draft
---

# Limits of Multivariable Functions

## Core Idea
We say lim_{(x,y)→(a,b)} f(x, y) = L if for every ε > 0 there exists δ > 0 such that |f(x, y) − L| < ε whenever 0 < √((x−a)² + (y−b)²) < δ. The limit must be the same along all paths approaching (a, b).
