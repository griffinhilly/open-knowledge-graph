---
id: joint-probability-distributions
title: Joint Probability Distributions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: probability-mass-functions
  type: soft
- id: probability-density-functions
  type: soft
builds-toward:
- marginal-distributions-from-joint
- conditional-distributions-of-random-variables
tags:
- joint-distributions
- multivariate
- probability
stage: formal-systems
status: draft
---

# Joint Probability Distributions

## Core Idea
The joint distribution of multiple random variables describes their probabilities together. For discrete: P(X=x, Y=y) sums to 1. For continuous: f(x,y) integrates to 1. Joint distributions reveal dependence structure between variables.

## How It's Best Learned
Create joint probability tables for simple two-variable scenarios. Integrate joint PDFs over regions. Recognize that knowing joint distributions allows computing all other probabilistic quantities.

## Common Misconceptions
Assuming variables are independent without checking. Confusing joint probability with conditional probability. Not recognizing that joint distributions contain complete information about the system.

## Explainer

When you studied probability mass functions (PMFs) and probability density functions (PDFs), you were describing a single random variable in isolation — P(X = x) or f_X(x). A **joint distribution** extends this to two or more variables simultaneously, capturing not just how each behaves alone, but how they relate to each other. The joint distribution is the complete description of a random system: everything you might want to know about the variables can be derived from it.

For two discrete random variables X and Y, the **joint PMF** is P(X = x, Y = y) — the probability that X takes value x *and* Y takes value y at the same time. The full collection of these probabilities is often arranged in a table where rows index values of X and columns index values of Y. The entries must sum to 1 over all pairs (x, y). From this table, you can read off everything: P(X = x, Y = 3) sums the column for Y = 3 at row x; P(X ≤ 2) sums all entries where x ≤ 2. For continuous variables, the **joint PDF** f(x, y) works the same way but sums become integrals: probabilities are volumes under the joint density surface over regions in the xy-plane.

The most important operation on joint distributions is **marginalization**: recovering the distribution of one variable by summing (or integrating) over all values of the other. The **marginal PMF** of X is P(X = x) = Σ_y P(X = x, Y = y) — you sum across each row of the joint table. This collapses the two-variable picture back to a one-variable picture. The marginals tell you about each variable separately, but they do not tell you about the relationship between them. Two very different joint distributions can have identical marginals.

**Independence** is the special case where the joint distribution factors: P(X = x, Y = y) = P(X = x) · P(Y = y) for all pairs, or equivalently f(x, y) = f_X(x) · f_Y(y). Independence means knowing X gives you no information about Y. You should never assume independence without justification — it is a strong claim. For example, a student's score on exam 1 and their score on exam 2 probably have positive dependence (students who do well on one tend to do well on the other); the joint distribution will not factor into the product of the marginals. Joint distributions are the foundation for understanding **conditional distributions**, **covariance**, and **correlation** — concepts that precisely quantify how much and in what direction variables influence each other.
