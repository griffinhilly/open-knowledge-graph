---
id: condition-number
title: Condition Number of a Problem
domain: mathematics
course: numerical-analysis
prerequisites:
- id: numerical-stability
  type: hard
- id: mean-value-theorem
  type: soft
builds-toward:
- condition-number-of-matrix
tags:
- condition-number
- conditioning
- sensitivity
stage: abstract-reasoning
status: draft
---

# Condition Number of a Problem

## Core Idea
The condition number measures how much the solution changes relative to changes in input data. A large condition number indicates an ill-conditioned problem where small input perturbations cause large output changes. The relative condition number κ(x) = |x f'(x) / f(x)| quantifies this sensitivity for a general function f.
