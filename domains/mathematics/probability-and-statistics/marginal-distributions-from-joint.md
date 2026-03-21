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

## Questions

```yaml
- question: "A joint distribution has X and Y each taking values {1, 2}. Two students construct different joint distributions that both give X and Y the same marginals (X and Y each uniform on {1,2}). Student A makes X and Y independent; Student B makes X = Y with probability 1. What does this demonstrate?"
  type: multiple-choice
  options:
    - "The two students must have made an error, since identical marginals force the same joint distribution"
    - "Different joint distributions can share identical marginals — the marginals do not determine the joint, because they contain no information about the relationship between variables"
    - "The marginals are incorrect, because X = Y with probability 1 contradicts a uniform marginal for X"
    - "This situation is impossible; joint distributions with the same marginals must be identical"
  answer: 1
  explanation: "Both constructions are valid. In Student A's version, P(X=1,Y=1) = P(X=1,Y=2) = P(X=2,Y=1) = P(X=2,Y=2) = 1/4. In Student B's version, P(X=1,Y=1) = P(X=2,Y=2) = 1/2 and cross terms = 0. Both have the same marginals: P(X=1) = P(X=2) = P(Y=1) = P(Y=2) = 1/2. Yet one has perfectly correlated variables and the other has independent variables. The joint distribution contains strictly more information than either marginal."

- question: "Given a continuous joint density f(x, y), how do you compute the marginal density f_X(x)?"
  type: multiple-choice
  options:
    - "Set y = 0 and evaluate: f_X(x) = f(x, 0)"
    - "Divide by the marginal of Y: f_X(x) = f(x, y) / f_Y(y)"
    - "Integrate over all values of y: f_X(x) = ∫ f(x, y) dy"
    - "Average over the range of x: f_X(x) = (1/(b−a)) ∫ₐᵇ f(x, y) dx"
  answer: 2
  explanation: "Marginalization works by 'integrating out' the variable you don't care about. You fix x and integrate over all possible y values, weighting each by how likely that y value is — but since f(x,y) already encodes this, you simply integrate over y. The result is a function of x alone that sums up all the probability at x regardless of what y does. Setting y = 0 (option A) would give the density only along the x-axis, not the marginal. Option D is circular."

- question: "If you know the marginal distributions of X and Y separately, you cannot in general reconstruct their joint distribution."
  type: true-false
  answer: true
  explanation: "The joint distribution encodes the full relationship between X and Y, including any dependencies. The marginals discard this relational information, keeping only each variable's individual behavior. Knowing that X is uniform on [0,1] and Y is uniform on [0,1] is consistent with X and Y being independent, perfectly correlated, negatively correlated, or related in any number of other ways. Recovery of the joint is only possible if you additionally know the dependency structure — for example, that X and Y are independent, which allows the factorization P(X,Y) = P(X)·P(Y)."

- question: "Two random variables are independent if and only if their joint distribution equals the product of their marginal distributions at every point."
  type: true-false
  answer: true
  explanation: "This is the formal definition of independence for random variables. Independence means that knowing the value of X gives no information about Y (and vice versa). Mathematically, this is equivalent to the factorization P(X=x, Y=y) = P(X=x)·P(Y=y) for all x and y (discrete case), or f(x,y) = f_X(x)·f_Y(y) for all x and y (continuous case). When this factorization fails, the variables are dependent, and the joint contains information not present in either marginal."

- question: "Why does knowing both marginal distributions of X and Y not tell you whether X and Y are positively correlated, negatively correlated, or independent?"
  type: short-answer
  answer: "The marginal distributions describe each variable in isolation by summing/integrating out the other. This process discards all information about how X and Y co-vary. Correlation and dependence live in the joint distribution — specifically in whether the probability of a (x, y) pair differs from the product of the individual probabilities. Two completely different joint distributions can produce identical marginals, so the marginals are insufficient to determine any aspect of the relationship between the variables."
  explanation: "A helpful analogy: the marginal of X is like the row-sums of a probability table, and the marginal of Y is the column-sums. Many different tables can have the same row-sums and column-sums. The structure *inside* the table — which cells have high or low probability — is exactly what encodes correlation and dependence. The marginals see only the totals, not the interior."
```

## Explainer

A **joint distribution** captures the full probabilistic relationship between two (or more) random variables at once — it tells you how likely every combination of values is. But often you only care about one variable at a time. The **marginal distribution** is how you recover the single-variable picture from the joint one by systematically "collapsing" the other variable out of the picture.

The mechanism is straightforward and follows directly from the total probability law you already know. For discrete variables, imagine a joint probability table where rows represent values of X and columns represent values of Y. The cell at row x, column y holds P(X=x, Y=y). To get the marginal P(X=x) — the probability that X equals x, regardless of what Y does — you sum across the entire row: P(X=x) = Σ_y P(X=x, Y=y). You're averaging over all possible Y values, weighted by their probabilities. Literally: add up each column entry in row x. The resulting row-sums form the marginal distribution of X; the column-sums form the marginal of Y. This is where the term "marginal" comes from — historically, these sums were written in the margins of the table.

For continuous joint distributions f(x, y), the logic is identical but summation becomes integration: f_X(x) = ∫ f(x, y) dy. You fix x and integrate out y over its entire range, leaving a function of x alone. The resulting f_X is a valid probability density — it integrates to 1 — and it describes X's behavior irrespective of Y. The key insight is that **marginalization discards information about the relationship between variables** without discarding information about each variable individually. The joint distribution contains everything; the marginals contain only each variable's behavior in isolation.

One critical implication: you cannot generally recover the joint distribution from the marginals alone. Two pairs of variables can share identical marginals yet have completely different joint distributions — one pair might be independent, another strongly correlated. Independence is the special case where the joint factors into the product of the marginals: P(X=x, Y=y) = P(X=x) · P(Y=y) for all x, y. When that factorization fails, the variables are dependent and the marginals fail to capture the relationship. This asymmetry — joint implies marginals, but marginals don't imply joint — is one of the foundational lessons of multivariate probability.
