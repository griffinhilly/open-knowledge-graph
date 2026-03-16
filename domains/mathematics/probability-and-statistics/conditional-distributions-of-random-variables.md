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

## Explainer

You know how to work with joint distributions — probability tables or density functions describing two random variables simultaneously — and you know conditional probability: P(A|B) = P(A∩B)/P(B). Conditional distributions combine these ideas. Instead of asking for the probability of a single event given another event, you ask: what does the entire distribution of X look like when Y is fixed at a specific value?

In the discrete case, the idea is concrete. Suppose (X, Y) has a joint probability table. Fix a particular value y for Y. The **conditional distribution of X given Y = y** is the distribution you get by looking only at the column (or row) of the table where Y = y, then rescaling so the values sum to 1. Formally: P(X = x | Y = y) = P(X = x, Y = y) / P(Y = y). The denominator P(Y = y) is the **marginal probability** of that value of Y, obtained by summing the column — exactly the marginal distribution you know how to compute. Dividing by this sum is the normalization step: you zoom in on the subpopulation where Y = y and rescale to form a valid probability distribution for X within that subpopulation.

In the continuous case, individual values have probability zero, so the formula P(X = x | Y = y) / P(Y = y) would be 0/0. Instead, the **conditional density** is defined as the ratio of densities: f_{X|Y}(x|y) = f_{X,Y}(x, y) / f_Y(y). This is the same logical structure — numerator is joint, denominator is marginal — just expressed in terms of density functions rather than probabilities. To verify it is a valid density: integrate over x, getting ∫ f_{X,Y}(x,y) dx / f_Y(y) = f_Y(y) / f_Y(y) = 1. The normalization works out automatically from the definition of the marginal.

Conditional distributions reveal the **dependence structure** between variables. If X and Y are independent, the conditional distribution of X given Y = y is identical to the marginal distribution of X — knowing Y tells you nothing about X, and every column of the joint table looks the same after normalization. If they are dependent, the shape of the conditional distribution changes as y varies. Comparing f_{X|Y}(x|y) for several values of y shows exactly how Y "informs" X: which values of X become more or less likely as Y shifts. This comparison is the right way to think about dependence, and it directly motivates conditional expectation — the expected value of X given Y = y, which averages the conditional distribution and becomes the central tool in regression and Bayesian inference.
