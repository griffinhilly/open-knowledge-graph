---
id: joint-marginal-distributions
title: Joint and Marginal Distributions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: random-variables-definition-types
  type: hard
builds-toward:
- conditional-distributions-of-random-variables
- covariance-between-random-variables
tags:
- joint-distribution
- marginal
stage: formal-systems
status: draft
---

# Joint and Marginal Distributions

## Core Idea
Joint PMF/PDF p(x,y) or f(x,y) specifies the probability of pairs. Marginal distributions sum or integrate out the other variable: p_X(x)=∑_y p(x,y). Two variables are independent iff joint factors into marginals: p(x,y)=p_X(x)p_Y(y).

## Explainer

When you studied random variables, each variable described the uncertainty about a single quantity — the outcome of one die roll, one measurement, one coin flip. But most real situations involve multiple uncertain quantities at once: the height and weight of a randomly chosen person, the price and volume of a stock, the test scores of two students. Joint distributions are the framework for handling multiple random variables simultaneously.

The **joint PMF** (for discrete variables) p(x, y) = P(X = x and Y = y) assigns a probability to every pair of values. It's a complete description of the relationship between X and Y — not just what each variable does on its own, but how they interact. Think of it as a table (for finite discrete variables): each cell (x, y) holds the probability of that particular combination. All cells must be non-negative, and they must sum to 1. From this table, you can answer any probability question about X and Y together.

**Marginal distributions** recover the individual behavior of each variable from the joint. To find P(X = x), just sum p(x, y) over all possible values of y — you're "summing out" Y, which is equivalent to asking what X is doing regardless of Y's value. Geometrically, if you imagine the joint distribution as a surface over a grid, the marginal of X is the "shadow" of that surface projected onto the x-axis. For continuous variables, summation becomes integration: f_X(x) = ∫ f(x, y) dy. The marginals tell you each variable's individual distribution, but they don't tell you the relationship *between* them.

**Independence** is the key structural condition. X and Y are independent if and only if the joint distribution factors: p(x, y) = p_X(x) · p_Y(y) for all pairs (x, y). In words: knowing X gives you no information about Y, and vice versa. Equivalently, the joint table looks like the "outer product" of the two marginals — every row is a scalar multiple of every other row. Independence is a very strong condition; most interesting pairs of variables are *not* independent, because they tend to be correlated (height and weight, income and education, etc.).

The payoff of understanding joint and marginal distributions is that they enable everything downstream: conditional distributions (what's the distribution of Y given that X = x?), covariance and correlation (how much do X and Y move together?), and the joint behavior of sums and transformations. When you encounter bivariate Normal distributions, regression models, or multivariate statistics, the joint distribution is always the starting point. The marginals describe what each variable does alone; the joint describes what they do together; the gap between those two descriptions is exactly the information carried by their statistical relationship.
