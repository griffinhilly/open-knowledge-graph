---
id: uniform-convergence
title: Uniform Convergence
domain: mathematics
course: real-analysis
prerequisites:
- id: pointwise-convergence-function-sequences
  type: hard
builds-toward:
- uniform-convergence-preserves-continuity
- interchange-limit-integral
- weierstrass-m-test
tags:
- uniform-convergence
- function-sequences
- limits
stage: advanced
status: draft
---

# Uniform Convergence

## Core Idea
A sequence (fₙ) converges uniformly to f on S if for every ε > 0, there exists N (depending only on ε, not on x) such that for all n > N and all x in S, |fₙ(x) − f(x)| < ε. Uniform convergence is stronger than pointwise and preserves many properties: limits of continuous functions are continuous, we can interchange limit and integral, etc.

## Explainer

You already know **pointwise convergence**: fₙ → f pointwise if for each fixed x, fₙ(x) → f(x). In other words, if you plant a flag at a single point x and watch the sequence of values f₁(x), f₂(x), f₃(x), ... converge to f(x), that's pointwise. The catch is that the convergence speed can vary wildly across different points. At some x, fₙ might reach ε-closeness by n = 5; at another x, you might need n = 500; at a third, n = 5,000,000. Pointwise convergence makes no promise about which N works globally — each point gets its own N depending on both ε *and* x.

**Uniform convergence** changes one word in the definition but changes everything in the theory. The key phrase is that N depends only on ε, not on x. Formally: for every ε > 0, there exists N such that for *all* n > N and *all* x ∈ S, |fₙ(x) − f(x)| < ε. The geometric picture is clean: uniform convergence means the entire graph of fₙ eventually fits inside an ε-tube around the graph of f. The sequence fₙ(x) = xⁿ on [0, 1) is a canonical counterexample: it converges pointwise to the function that is 0 on [0, 1) and 1 at 1, but not uniformly — near x = 1, you always need a larger N to get within ε of 0. The "tube" can never be closed because fₙ bulges up toward 1 near the right endpoint no matter how large n is.

Why does this distinction matter so much? Because pointwise convergence is too weak to transfer analytic properties from fₙ to f. A pointwise limit of continuous functions can be discontinuous (the xⁿ example shows this: each fₙ is continuous, but the limit function has a jump). A pointwise limit of integrable functions can fail to satisfy ∫ fₙ → ∫ f. Uniform convergence repairs all of this. The **Uniform Limit Theorem** states: if each fₙ is continuous and fₙ → f uniformly, then f is continuous. The proof is a classic ε/3 argument — you split the error |f(x) − f(y)| ≤ |f(x) − fₙ(x)| + |fₙ(x) − fₙ(y)| + |fₙ(y) − f(y)|, control the outer two terms using uniform convergence, and control the middle term using continuity of fₙ. Uniform convergence also justifies swapping limits and integrals: ∫ limₙ fₙ = limₙ ∫ fₙ. This interchange is exactly what breaks down for pointwise convergence and is exactly what the Dominated Convergence Theorem later restores in a more general form.
