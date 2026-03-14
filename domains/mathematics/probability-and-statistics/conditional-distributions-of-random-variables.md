---
id: conditional-distributions-of-random-variables
title: Conditional Distributions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: marginal-distributions-from-joint
  type: hard
- id: conditional-probability
  type: hard
builds-toward:
- conditional-expectation
- bivariate-normal-distribution
tags:
- conditional-distributions
- multivariate
- probability
stage: formal-systems
status: draft
---

# Conditional Distributions

## Core Idea
The conditional distribution of X given Y=y is the distribution of X when Y is fixed: P(X=x|Y=y) = P(X=x,Y=y)/P(Y=y). Conditional distributions capture how one variable's distribution depends on another's value.

## How It's Best Learned
From a joint distribution table, select a column or row and normalize it to sum to 1. For continuous distributions, condition by dividing joint PDF by marginal PDF. Compare conditional distributions for different values.
