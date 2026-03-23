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
status: validated
---

# Convergence in L^p

## Core Idea
Xₙ converges to X in L^p if lim_{n→∞} E[|Xₙ - X|^p] = 0, equivalently ||Xₙ - X||_p → 0 in the L^p norm. L^p spaces form a Banach space of random variables with finite p-th moment. Convergence in L² (mean square convergence) is particularly important because it preserves inner products.

## Explainer

From your study of measure-theoretic expectation, you know that E[|X|^p] computes the p-th moment of the absolute value of a random variable — an integral with respect to the probability measure P. **L^p convergence** uses this integral to define a notion of distance between random variables: Xₙ converges to X in L^p if the p-th moment of their difference vanishes, that is, E[|Xₙ − X|^p] → 0 as n → ∞. Equivalently, ||Xₙ − X||_p → 0, where ||Y||_p = (E[|Y|^p])^{1/p} is the L^p norm. This is a genuine norm on the space of random variables with finite p-th moment (identifying variables that agree almost surely), making L^p a **Banach space** — a complete normed vector space.

The case p = 2 is special because L² is not just a Banach space but a **Hilbert space**, equipped with the inner product ⟨X, Y⟩ = E[XY]. This inner product gives L² a geometric structure — orthogonality, projections, the Cauchy-Schwarz inequality — that other L^p spaces lack. Convergence in L² (mean-square convergence) preserves inner products: if Xₙ → X and Yₙ → Y in L², then E[XₙYₙ] → E[XY]. This is why L² is the natural setting for defining conditional expectation as an orthogonal projection, for least-squares estimation, and for the spectral analysis of stationary processes. The geometry of L² turns probabilistic questions into problems of projecting onto subspaces.

L^p convergence is **stronger** than convergence in probability but **weaker** than almost sure convergence — though the exact relationships are subtle. The standard counterexample is the **typewriter sequence** on [0, 1]: indicator functions on subintervals that cycle through the interval with shrinking width. This sequence converges to 0 in every L^p (since E[|Xₙ|^p] = length of the subinterval → 0) but does not converge almost surely (at any point ω, the sequence returns to 1 infinitely often). In the other direction, convergence in probability does not imply L^p convergence without an additional condition: the sequence must be **uniformly integrable** in L^p. Without this, the tails of the distribution can carry enough mass to prevent L^p convergence even when the random variables are converging in probability.

The hierarchy of L^p spaces is governed by **Lyapunov's inequality**: on a probability space (where total measure is 1), ||X||_q ≤ ||X||_p whenever 1 ≤ q ≤ p. This means convergence in a higher L^p automatically implies convergence in every lower L^q. If Xₙ → X in L², then Xₙ → X in L¹ as well. The converse fails: L¹ convergence does not imply L² convergence. Understanding these relationships — which modes of convergence imply which, and what additional conditions bridge the gaps — is essential for the rigorous study of limit theorems, estimator properties, and stochastic processes.

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
