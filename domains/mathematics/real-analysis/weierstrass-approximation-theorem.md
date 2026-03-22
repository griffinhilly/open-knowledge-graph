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

## Questions

```yaml
- question: "A function f on [0,1] is continuous everywhere but has a sharp corner — it is not differentiable at one point. According to the Weierstrass Approximation Theorem, which of the following is true?"
  type: multiple-choice
  options:
    - "f cannot be uniformly approximated by polynomials because polynomials are smooth and f has a corner"
    - "f can be uniformly approximated by polynomials because only continuity is required"
    - "f can only be approximated pointwise, not uniformly, because of the non-differentiable point"
    - "The theorem does not apply since f fails to be smooth"
  answer: 1
  explanation: "The Weierstrass Approximation Theorem requires only continuity on a closed interval — not differentiability, smoothness, or any other regularity condition. The most tempting wrong answer (option A) reflects the misconception that since polynomials are infinitely differentiable, they can only approximate functions of similar smoothness. But uniform approximation does not require matching derivatives — it only requires making |f(x) − P(x)| small for all x simultaneously. A corner poses no barrier."

- question: "What does it mean to say polynomials are 'dense' in C([a,b]) — the space of continuous functions on [a,b] with the uniform norm?"
  type: multiple-choice
  options:
    - "Every continuous function is itself a polynomial"
    - "Every continuous function is the limit of polynomials in the pointwise sense at every x"
    - "Every continuous function can be approximated arbitrarily closely by some polynomial in the sup-norm"
    - "Polynomials make up more than half the functions in C([a,b])"
  answer: 2
  explanation: "Density in the uniform (sup-norm) topology means that for any f ∈ C([a,b]) and any ε > 0, there exists a polynomial P with sup_{x∈[a,b]} |f(x) − P(x)| < ε. This is precisely what 'uniformly approximated' means. Option B describes pointwise convergence, which is weaker — it allows the approximation error to depend on x. The theorem guarantees the stronger, uniform version: the worst-case error over the entire interval can be made as small as desired."

- question: "The Weierstrass Approximation Theorem guarantees that for any ε > 0, there exists a polynomial P such that |f(x) − P(x)| < ε holds simultaneously for all x in [a,b], not just at individual points."
  type: true-false
  answer: true
  explanation: "This is exactly the content of the theorem — the approximation is uniform, meaning the same error bound holds across the entire interval at once. This is stronger than pointwise approximation, where ε could depend on x. The Bernstein polynomial construction achieves this: for each n, Bₙ(f, x) approximates f at every x, and as n → ∞ the sup-norm distance to f goes to zero."

- question: "Because polynomials are infinitely differentiable, the Weierstrass Approximation Theorem applies only to continuous functions that are also differentiable on (a,b)."
  type: true-false
  answer: false
  explanation: "The theorem's hypothesis is continuity on the closed interval [a,b] — differentiability is not required. The appeal of this misconception is that polynomials are smooth, so it seems they should only approximate smooth things. But uniform approximation is about how close function values are, not about matching derivatives. A continuous but nowhere-differentiable function (like the Weierstrass function itself!) can still be uniformly approximated by polynomials."

- question: "Why is it surprising that polynomials can uniformly approximate every continuous function on [a,b], and why does the theorem require a closed (bounded) interval rather than all of ℝ?"
  type: short-answer
  answer: "Polynomials are algebraically rigid — they grow without bound outside any bounded region and are determined by finitely many coefficients. An arbitrary continuous function can have complex local behavior. The surprise is that despite this rigidity, polynomials can track any continuous function to arbitrary precision on a compact interval. The closed interval is essential because polynomials diverge as x → ±∞, so uniform approximation over all of ℝ fails for any bounded function. Compactness allows the law-of-large-numbers argument in the Bernstein proof to control errors uniformly."
  explanation: "The compactness of [a,b] is doing real work: it ensures that the supremum of the error is actually attained (rather than approached), and that the Bernstein polynomials — which average f's values according to a binomial distribution — concentrate near any given x as n grows. On an unbounded domain, polynomial approximation can fail even for simple bounded continuous functions like sin(x)."
```

## Explainer

You have already studied **uniform convergence**, where a sequence of functions fₙ → f uniformly means the *worst-case* discrepancy supₓ |fₙ(x) − f(x)| → 0. The Weierstrass Approximation Theorem makes a striking claim in that language: for any continuous f on a closed interval [a,b], you can find polynomials that converge to f *uniformly*. Not just pointwise — uniformly, meaning the approximation is equally good across the entire interval simultaneously.

Why is this surprising? Polynomials are algebraically rigid objects — they have no wiggles beyond their degree, grow without bound outside compact sets, and are determined entirely by finitely many coefficients. An arbitrary continuous function can oscillate in complicated ways, have kinks, or behave strangely. The theorem says none of that complexity prevents polynomial approximation from working. The proof is constructive: the **Bernstein polynomials** Bₙ(f, x) = Σₖ f(k/n) C(n,k) xᵏ(1−x)ⁿ⁻ᵏ are an explicit sequence of polynomials converging uniformly to f on [0,1]. Each Bₙ is essentially a probability-weighted average of f's values, and the convergence follows from the law of large numbers applied to binomial random variables.

The theorem's deeper message is about **density**: polynomials form a dense subset of C([a,b]), the space of continuous functions on [a,b] with the uniform (sup-norm) topology. In other words, every continuous function can be approximated as closely as desired by a polynomial. This is an analogue of the fact that every real number can be approximated by rationals — rationals are dense in ℝ. Similarly, polynomials are the "rationals" of function space. Density results like this underlie the theory of function spaces and operator theory.

For applications, the theorem justifies using polynomial approximations (Taylor polynomials, Chebyshev polynomials, splines) to represent or compute with arbitrary continuous functions. It also motivates the more general Stone–Weierstrass theorem, which identifies abstract conditions under which a subalgebra of functions is dense — replacing "polynomials" with any family satisfying a few structural axioms. If you understand the Weierstrass theorem deeply, the Stone–Weierstrass generalization is a natural next step: the polynomials aren't special because they're polynomials, but because they *separate points* and *contain constants*, and those two properties alone drive the density.


