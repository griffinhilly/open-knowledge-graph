---
id: convergence-in-lp
title: Convergence in L^p
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: expectation-measure-theoretic
  type: hard
- id: inner-product-spaces
  type: soft
builds-toward:
- relationships-modes-convergence
tags:
- convergence
- lp-spaces
- functional-analysis
stage: advanced
status: draft
---

# Convergence in L^p

## Core Idea
Xₙ converges to X in L^p if lim_{n→∞} E[|Xₙ - X|^p] = 0, equivalently ||Xₙ - X||_p → 0 in the L^p norm. L^p spaces form a Banach space of random variables with finite p-th moment. Convergence in L² (mean square convergence) is particularly important because it preserves inner products.

## Questions

```yaml
- question: "A sequence of random variables Xₙ converges to X in L². Which of the following is guaranteed?"
  type: multiple-choice
  options:
    - "Xₙ converges to X almost surely"
    - "E[|Xₙ - X|²] → 0 as n → ∞"
    - "Xₙ(ω) → X(ω) for every ω in the sample space"
    - "Var(Xₙ) = Var(X) for all sufficiently large n"
  answer: 1
  explanation: "Option B is the definition of L² convergence: the expected squared difference goes to zero. Option A (almost sure convergence) is not guaranteed by L² convergence — the classic 'typewriter sequence' converges in L² but not almost surely. Option C (pointwise convergence for every ω) is a much stronger condition. Option D confuses convergence of the sequence with eventual equality of distributions."

- question: "Suppose Xₙ → X in probability. Under which additional condition can we conclude Xₙ → X in L²?"
  type: multiple-choice
  options:
    - "No additional condition is needed — convergence in probability always implies L² convergence"
    - "The Xₙ must be identically distributed"
    - "The sequence must be uniformly integrable in L² (or dominated by a square-integrable variable)"
    - "X must be a constant random variable"
  answer: 2
  explanation: "Convergence in probability does NOT automatically imply L² convergence. A standard counterexample: let Xₙ = n · 1_{[0,1/n]}. Then Xₙ → 0 in probability, but E[Xₙ²] = n² · (1/n) = n → ∞, so L² convergence fails. Uniform integrability (or a domination condition) is the additional hypothesis that bridges the two modes. Option A is the common misconception."

- question: "If Xₙ → X in L^p for some p > 1, then Xₙ → X in L^q for every q with 1 ≤ q < p, provided the underlying probability space has total measure 1."
  type: true-false
  answer: true
  explanation: "By Lyapunov's inequality (a consequence of Jensen's inequality applied to the concave function t^{q/p}), we have E[|Y|^q]^{1/q} ≤ E[|Y|^p]^{1/p} on a probability space. Setting Y = Xₙ − X: if E[|Xₙ − X|^p] → 0 then E[|Xₙ − X|^q] → 0 for q ≤ p. The probability space having total measure 1 is what makes this direction work (it would fail on infinite measure spaces)."

- question: "L² convergence of Xₙ to X guarantees that Xₙ(ω) → X(ω) for almost every ω in the sample space."
  type: true-false
  answer: false
  explanation: "L² convergence and almost sure convergence are distinct modes that do not imply each other. The typewriter sequence is the canonical counterexample: define Xₙ on [0,1] by indicator functions on successively finer subintervals cycling through the interval. This sequence converges to 0 in every L^p but converges at no single point ω. Conversely, almost sure convergence does not imply L² convergence (a sequence can converge pointwise while its squared differences grow without bound in expectation)."

- question: "Why is convergence in L² particularly useful in probability theory compared to other L^p convergences, and what structural feature makes it special?"
  type: short-answer
  answer: "L² is special because it is a Hilbert space: the inner product ⟨X, Y⟩ = E[XY] provides geometric structure — orthogonality, projections, and the Cauchy-Schwarz inequality — that other L^p spaces lack. L² convergence preserves inner products (if Xₙ → X and Yₙ → Y in L², then E[XₙYₙ] → E[XY]), which makes it natural for defining conditional expectation as an orthogonal projection, for studying uncorrelated and orthogonal random variables, and for spectral analysis of stationary processes. These tools are not available in L¹ or L^p for p ≠ 2."
  explanation: "The L² inner product turns the space of square-integrable random variables into a Hilbert space, unlocking the full machinery of geometry in infinite dimensions. This is why mean-square convergence is the natural setting for least-squares estimation, the spectral theorem for covariance operators, and the theory of Hilbert-space-valued processes."
```
