---
id: weierstrass-approximation-theorem
title: Weierstrass Approximation Theorem
domain: mathematics
course: real-analysis
prerequisites:
- id: uniform-convergence-functions
  type: hard
- id: polynomial-functions-degree-and-leading-coefficient
  type: soft
tags:
- weierstrass-approximation
- polynomials
- approximation
stage: advanced
status: draft
---

# Weierstrass Approximation Theorem

## Core Idea
Every continuous function on a closed interval [a,b] can be uniformly approximated by polynomials: for every ε > 0, there exists a polynomial P such that |f(x) - P(x)| < ε for all x ∈ [a,b]. This theorem shows that polynomials are dense in the space of continuous functions and is fundamental to approximation theory and functional analysis.

## Explainer

You have already studied **uniform convergence**, where a sequence of functions fₙ → f uniformly means the *worst-case* discrepancy supₓ |fₙ(x) − f(x)| → 0. The Weierstrass Approximation Theorem makes a striking claim in that language: for any continuous f on a closed interval [a,b], you can find polynomials that converge to f *uniformly*. Not just pointwise — uniformly, meaning the approximation is equally good across the entire interval simultaneously.

Why is this surprising? Polynomials are algebraically rigid objects — they have no wiggles beyond their degree, grow without bound outside compact sets, and are determined entirely by finitely many coefficients. An arbitrary continuous function can oscillate in complicated ways, have kinks, or behave strangely. The theorem says none of that complexity prevents polynomial approximation from working. The proof is constructive: the **Bernstein polynomials** Bₙ(f, x) = Σₖ f(k/n) C(n,k) xᵏ(1−x)ⁿ⁻ᵏ are an explicit sequence of polynomials converging uniformly to f on [0,1]. Each Bₙ is essentially a probability-weighted average of f's values, and the convergence follows from the law of large numbers applied to binomial random variables.

The theorem's deeper message is about **density**: polynomials form a dense subset of C([a,b]), the space of continuous functions on [a,b] with the uniform (sup-norm) topology. In other words, every continuous function can be approximated as closely as desired by a polynomial. This is an analogue of the fact that every real number can be approximated by rationals — rationals are dense in ℝ. Similarly, polynomials are the "rationals" of function space. Density results like this underlie the theory of function spaces and operator theory.

For applications, the theorem justifies using polynomial approximations (Taylor polynomials, Chebyshev polynomials, splines) to represent or compute with arbitrary continuous functions. It also motivates the more general Stone–Weierstrass theorem, which identifies abstract conditions under which a subalgebra of functions is dense — replacing "polynomials" with any family satisfying a few structural axioms. If you understand the Weierstrass theorem deeply, the Stone–Weierstrass generalization is a natural next step: the polynomials aren't special because they're polynomials, but because they *separate points* and *contain constants*, and those two properties alone drive the density.


