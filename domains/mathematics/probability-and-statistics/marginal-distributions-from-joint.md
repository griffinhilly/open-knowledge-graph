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

## Explainer

A **joint distribution** captures the full probabilistic relationship between two (or more) random variables at once — it tells you how likely every combination of values is. But often you only care about one variable at a time. The **marginal distribution** is how you recover the single-variable picture from the joint one by systematically "collapsing" the other variable out of the picture.

The mechanism is straightforward and follows directly from the total probability law you already know. For discrete variables, imagine a joint probability table where rows represent values of X and columns represent values of Y. The cell at row x, column y holds P(X=x, Y=y). To get the marginal P(X=x) — the probability that X equals x, regardless of what Y does — you sum across the entire row: P(X=x) = Σ_y P(X=x, Y=y). You're averaging over all possible Y values, weighted by their probabilities. Literally: add up each column entry in row x. The resulting row-sums form the marginal distribution of X; the column-sums form the marginal of Y. This is where the term "marginal" comes from — historically, these sums were written in the margins of the table.

For continuous joint distributions f(x, y), the logic is identical but summation becomes integration: f_X(x) = ∫ f(x, y) dy. You fix x and integrate out y over its entire range, leaving a function of x alone. The resulting f_X is a valid probability density — it integrates to 1 — and it describes X's behavior irrespective of Y. The key insight is that **marginalization discards information about the relationship between variables** without discarding information about each variable individually. The joint distribution contains everything; the marginals contain only each variable's behavior in isolation.

One critical implication: you cannot generally recover the joint distribution from the marginals alone. Two pairs of variables can share identical marginals yet have completely different joint distributions — one pair might be independent, another strongly correlated. Independence is the special case where the joint factors into the product of the marginals: P(X=x, Y=y) = P(X=x) · P(Y=y) for all x, y. When that factorization fails, the variables are dependent and the marginals fail to capture the relationship. This asymmetry — joint implies marginals, but marginals don't imply joint — is one of the foundational lessons of multivariate probability.
