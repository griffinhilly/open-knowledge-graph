---
id: joint-distributions-and-marginals-rigorous
title: Joint Distributions and Marginals (Rigorous)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: distribution-and-density-functions
  type: hard
- id: iterated-integrals
  type: soft
builds-toward:
- conditional-expectation
- independence-of-sigma-algebras
tags:
- multivariate
- marginals
- joint-distributions
stage: advanced
status: draft
---

# Joint Distributions and Marginals (Rigorous)

## Core Idea
The joint distribution of (X, Y) is a probability measure on ℝ² induced by the random vector. Marginal distributions are obtained by integrating over the other variable. Dependence structure is encoded in the joint distribution; independence means the joint factors as a product of marginals.

## Explainer

From your study of distribution and density functions, you know that a single random variable X is characterized by a probability measure on ℝ — a distribution function F(x) = P(X ≤ x), and for continuous random variables, a density f(x) satisfying P(X ∈ A) = ∫_A f(x) dx. When you have two random variables X and Y defined on the same probability space, you need a way to describe their joint behavior — not just what X does alone or what Y does alone, but how they interact. The **joint distribution** of (X, Y) is a probability measure on ℝ², capturing all this information at once.

Concretely, the **joint CDF** is F(x, y) = P(X ≤ x, Y ≤ y), and for jointly continuous random variables, a **joint density** f(x, y) satisfies P((X, Y) ∈ A) = ∫∫_A f(x, y) dx dy for any Borel set A. The joint density is a surface over the xy-plane, and probabilities are volumes under that surface. Your prerequisite knowledge of iterated integrals is exactly what's needed here: computing P(X ∈ [a,b], Y ∈ [c,d]) means integrating f(x, y) over a rectangle using Fubini's theorem.

**Marginal distributions** recover the individual behavior of X or Y from the joint. The marginal density of X is fₓ(x) = ∫_{-∞}^{∞} f(x, y) dy — you integrate out (marginalize over) y. The marginal density of Y is f_Y(y) = ∫_{-∞}^{∞} f(x, y) dx. Notice that the marginals are uniquely determined by the joint distribution, but the reverse is not true: the same marginals are consistent with many different joint distributions. Two random variables can have the same individual distributions but dramatically different joint behavior depending on how they covary.

**Independence** in the rigorous sense means the joint distribution factorizes: f(x, y) = fₓ(x) · f_Y(y) for all (x, y). This is the analogue of your probability prerequisite — events A and B are independent iff P(A ∩ B) = P(A)·P(B), and independence of random variables is just this condition holding for all events expressible in terms of X and Y. When the joint density factors as a product, X and Y are statistically uninformative about each other — knowing X gives no information about Y. Checking factorizability is the rigorous test for independence; it directly generalizes to independence of σ-algebras, which you will study next.
