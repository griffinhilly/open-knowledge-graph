---
id: marginal-distributions-from-joint
title: Marginal Distributions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: joint-probability-distributions
  type: hard
builds-toward:
- conditional-distributions-of-random-variables
tags:
- marginal-distributions
- multivariate
- probability
stage: formal-systems
status: draft
---

# Marginal Distributions

## Core Idea
The marginal distribution of one variable is obtained by summing/integrating the joint distribution over the other variables. For bivariate: P(X=x) = Σ_y P(X=x, Y=y). Marginal distributions describe individual variables while ignoring others.

## How It's Best Learned
Start with joint probability tables and compute marginals by summing rows or columns. For continuous distributions, practice computing marginals via integration. Recognize marginals in frequency tables.
