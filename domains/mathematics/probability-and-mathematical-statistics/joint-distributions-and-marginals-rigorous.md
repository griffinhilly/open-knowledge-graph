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
status: validated
---

# Joint Distributions and Marginals (Rigorous)

## Core Idea
The joint distribution of (X, Y) is a probability measure on ℝ² induced by the random vector. Marginal distributions are obtained by integrating over the other variable. Dependence structure is encoded in the joint distribution; independence means the joint factors as a product of marginals.

## Questions

```yaml
- question: "Two random variables X and Y each have an exponential marginal distribution with rate 1. Which statement is correct?"
  type: multiple-choice
  options:
    - "X and Y must be independent since they have the same marginal distribution"
    - "The joint density must be f(x,y) = e^{-x} · e^{-y}, since that is the only density with these marginals"
    - "The marginals alone tell us nothing about whether X and Y are independent — the joint distribution is needed"
    - "X and Y must be identically equal almost surely if they have the same marginal distribution"
  answer: 2
  explanation: "The same marginals are consistent with infinitely many joint distributions. f(x,y) = e^{-x}·e^{-y} (the independent case) is one possibility, but so is the joint distribution of (X, X) — where Y = X almost surely and the variables are perfectly dependent. Independence means the joint FACTORS as a product of marginals; having the same marginals, or even any particular marginals, says nothing about independence."

- question: "A joint density is given by f(x,y) = 2 for 0 < x < y < 1. What is the marginal density of X?"
  type: multiple-choice
  options:
    - "fₓ(x) = 2x"
    - "fₓ(x) = 2(1 − x)"
    - "fₓ(x) = 2"
    - "fₓ(x) = 1"
  answer: 1
  explanation: "To find the marginal of X, integrate out y over all y values consistent with the constraint 0 < x < y < 1. For fixed x, y ranges from x to 1: fₓ(x) = ∫_x^1 2 dy = 2(1 − x). This integrates to 1 over [0,1] as required. The constraint 0 < x < y < 1 means the support is the upper triangle of the unit square, so the y-range for each x is not the full [0,1] — getting this wrong (integrating over all of [0,1]) is the typical error."

- question: "Two random variables can each have a standard normal marginal distribution and yet be strongly positively correlated."
  type: true-false
  answer: true
  explanation: "The bivariate normal with correlation ρ ∈ (0,1) has standard normal marginals for any value of ρ. The marginals tell you only about the individual variables; the correlation — encoded in the joint distribution — is invisible from the marginals alone. This is precisely why the joint distribution contains strictly more information than the pair of marginals."

- question: "If the joint density factors as f(x,y) = fₓ(x) · f_Y(y) for most (x,y), then X and Y is expected to have the same marginal distribution."
  type: true-false
  answer: false
  explanation: "Independence (joint = product of marginals) places no restriction on the relationship between fₓ and f_Y. X could be exponential and Y could be uniform, and they could still be independent — as long as f(x,y) = fₓ(x)·f_Y(y). The factorization condition says the joint contains no additional information beyond the marginals separately; it says nothing about whether those marginals are similar to each other."

- question: "Why can you always recover marginal distributions from the joint distribution, but you generally cannot recover the joint distribution from the marginals alone?"
  type: short-answer
  answer: "The marginal of X is obtained by integrating out y: fₓ(x) = ∫ f(x,y) dy. This integration destroys all information about how X and Y covary. The same marginals are consistent with infinitely many joint distributions encoding different dependence structures — from full independence (joint = product of marginals) to perfect correlation (Y = g(X) almost surely). The joint distribution is strictly richer than its marginals: it encodes the full dependence structure, while each marginal captures only the behavior of one variable in isolation."
  explanation: "Independence is the special case where the joint is exactly determined by the marginals (it's their product). In general, knowing only the marginals is like knowing the row totals and column totals of a table but not the individual cell values — there are many tables consistent with any given set of margins."
```

## Explainer

From your study of distribution and density functions, you know that a single random variable X is characterized by a probability measure on ℝ — a distribution function F(x) = P(X ≤ x), and for continuous random variables, a density f(x) satisfying P(X ∈ A) = ∫_A f(x) dx. When you have two random variables X and Y defined on the same probability space, you need a way to describe their joint behavior — not just what X does alone or what Y does alone, but how they interact. The **joint distribution** of (X, Y) is a probability measure on ℝ², capturing all this information at once.

Concretely, the **joint CDF** is F(x, y) = P(X ≤ x, Y ≤ y), and for jointly continuous random variables, a **joint density** f(x, y) satisfies P((X, Y) ∈ A) = ∫∫_A f(x, y) dx dy for any Borel set A. The joint density is a surface over the xy-plane, and probabilities are volumes under that surface. Your prerequisite knowledge of iterated integrals is exactly what's needed here: computing P(X ∈ [a,b], Y ∈ [c,d]) means integrating f(x, y) over a rectangle using Fubini's theorem.

**Marginal distributions** recover the individual behavior of X or Y from the joint. The marginal density of X is fₓ(x) = ∫_{-∞}^{∞} f(x, y) dy — you integrate out (marginalize over) y. The marginal density of Y is f_Y(y) = ∫_{-∞}^{∞} f(x, y) dx. Notice that the marginals are uniquely determined by the joint distribution, but the reverse is not true: the same marginals are consistent with many different joint distributions. Two random variables can have the same individual distributions but dramatically different joint behavior depending on how they covary.

**Independence** in the rigorous sense means the joint distribution factorizes: f(x, y) = fₓ(x) · f_Y(y) for all (x, y). This is the analogue of your probability prerequisite — events A and B are independent iff P(A ∩ B) = P(A)·P(B), and independence of random variables is just this condition holding for all events expressible in terms of X and Y. When the joint density factors as a product, X and Y are statistically uninformative about each other — knowing X gives no information about Y. Checking factorizability is the rigorous test for independence; it directly generalizes to independence of σ-algebras, which you will study next.
