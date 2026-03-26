---
id: uniform-convergence-functions
title: Uniform Convergence
domain: mathematics
course: real-analysis
prerequisites:
- id: pointwise-convergence-functions
  type: hard
builds-toward:
- uniform-convergence-preserves-continuity
- weierstrass-m-test
- interchange-limit-integral
- interchange-limit-derivative
tags:
- uniform-convergence
- function-sequences
- strengthened
stage: advanced
status: validated
---

# Uniform Convergence

## Core Idea
A sequence of functions (fₙ) converges uniformly to f on a set S if for every ε > 0, there exists N (independent of x) such that for all x ∈ S, n > N implies |fₙ(x) - f(x)| < ε. Uniform convergence is stronger than pointwise and guarantees that limits can be exchanged with derivatives and integrals. It is fundamental to analysis on function spaces.

## Questions

```yaml
- question: "Consider fₙ(x) = xⁿ on [0,1], which converges pointwise to f(x)=0 for x∈[0,1) and f(1)=1. A student says this sequence also converges uniformly because 'every fₙ is continuous and they converge at every point.' What is wrong?"
  type: multiple-choice
  options:
    - "Nothing is wrong — pointwise convergence at every point implies uniform convergence"
    - "The argument ignores that the pointwise limit is discontinuous — uniform convergence of continuous functions always produces a continuous limit, so this sequence cannot converge uniformly"
    - "The argument is wrong because uniform convergence only applies to differentiable functions"
    - "The student is correct for closed intervals like [0,1] but wrong for open intervals"
  answer: 1
  explanation: "Uniform convergence preserves continuity: if each fₙ is continuous and fₙ → f uniformly, then f is continuous. Since the pointwise limit here is discontinuous (jumps at x=1), the convergence cannot be uniform. The failure of uniform convergence can also be confirmed via the supremum criterion: sup_{x∈[0,1]} |xⁿ − f(x)| does not go to zero."

- question: "Which condition correctly captures uniform convergence of fₙ to f on S?"
  type: multiple-choice
  options:
    - "For each x∈S, there exists N(x,ε) such that n>N implies |fₙ(x)−f(x)| < ε"
    - "For every ε>0, there exists N(ε) independent of x such that for all x∈S, n>N implies |fₙ(x)−f(x)| < ε"
    - "sup_{x∈S}|fₙ(x)−f(x)| is bounded for all n"
    - "There exists a fixed N such that |fₙ(x)−f(x)| < ε for all n and all x"
  answer: 1
  explanation: "Option A is pointwise convergence — each x has its own N that can grow without bound. Option B is uniform convergence — one N serves all x simultaneously. The critical distinction is whether N depends on x. Option C only says the differences are bounded, not that they converge to zero."

- question: "Uniform convergence of a sequence of continuous functions guarantees that the limit function is also continuous."
  type: true-false
  answer: true
  explanation: "This is the key theorem separating uniform from pointwise convergence. If fₙ are all continuous on S and fₙ → f uniformly, then f is continuous on S. The proof uses the uniform N to control all three parts of the ε/3 argument simultaneously — something pointwise convergence cannot do because different points need different N values."

- question: "If fₙ → f pointwise on S, then the limit function f inherits most of the properties of the individual fₙ (continuity, integrability, differentiability)."
  type: true-false
  answer: false
  explanation: "Pointwise convergence does not preserve these properties. The canonical counterexample: fₙ(x) = xⁿ on [0,1] is a sequence of continuous, differentiable functions, but the pointwise limit is discontinuous. Uniform convergence is required to guarantee that such properties pass to the limit."

- question: "Explain the key difference between pointwise and uniform convergence using the idea of a 'deadline N.' Why does this difference matter for preserving continuity?"
  type: short-answer
  answer: "In pointwise convergence, each point x gets its own deadline N(x,ε) — different points can take arbitrarily long to converge. In uniform convergence, a single deadline N(ε) applies to all points simultaneously: once n exceeds N, every point in the domain is within ε of the limit at the same time. This shared deadline is what allows continuity to be preserved: near a point x₀, we can choose n large enough that all nearby points are simultaneously close to their respective limit values, making the limit function continuous at x₀."
  explanation: "The key insight is that continuity requires controlling behavior at an entire neighborhood of points simultaneously — exactly what uniform convergence provides and pointwise convergence does not."
```

## Explainer

You already understand **pointwise convergence**: fₙ converges pointwise to f if, for each fixed x, the number sequence fₙ(x) converges to f(x). Every x gets its own race to the finish line — every x eventually arrives, but different points may need wildly different amounts of time. This "each x on its own schedule" aspect is what makes pointwise convergence too weak for preserving analytical structure.

**Uniform convergence** tightens this: the entire domain must finish by the same lap N. Formally, for every ε > 0, there is a single N depending only on ε (not on x) such that once n > N, every point in the domain is within ε of f simultaneously. Picture it geometrically: the tube of width ±ε around the limit function f eventually swallows the entire graph of fₙ at once — not pointwise region by region.

The classic counterexample that separates the two notions is fₙ(x) = xⁿ on [0, 1]. Pointwise, this converges to f(x) = 0 for x ∈ [0, 1) and f(1) = 1 — a discontinuous limit function. Each fₙ is continuous, but the pointwise limit is not. This discontinuity cannot arise under uniform convergence: the uniform limit of continuous functions is always continuous. This theorem is the key example of why uniform convergence is the "right" notion for preserving analytical properties.

The practical test is the **supremum criterion**: fₙ → f uniformly if and only if sup_{x∈S} |fₙ(x) − f(x)| → 0 as n → ∞. This converts a universal quantifier over x into a single limit on a supremum — a much more tractable object. For series, the **Weierstrass M-test** provides a sufficient condition: if |gₙ(x)| ≤ Mₙ for all x and ΣMₙ converges (as a series of constants), then Σgₙ converges uniformly and absolutely. This is the standard tool for establishing uniform convergence of power series and Fourier series. Everything downstream — preserving continuity, exchanging limits with integrals, exchanging limits with derivatives — depends on whether this one uniform convergence condition holds.
