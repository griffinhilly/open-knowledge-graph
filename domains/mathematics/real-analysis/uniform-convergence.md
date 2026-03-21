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

## Questions

```yaml
- question: "The sequence fₙ(x) = xⁿ on [0, 1) converges pointwise to 0 but fails to converge uniformly. What is the essential reason for this failure?"
  type: multiple-choice
  options:
    - "The limit function is zero, and uniform convergence requires convergence to a nonzero function"
    - "Near x = 1, fₙ(x) stays close to 1 for arbitrarily large n, so no single N works for all x simultaneously"
    - "The functions fₙ are continuous, but the pointwise limit is not, which rules out uniform convergence on any interval"
    - "Uniform convergence cannot occur on open intervals — it requires a closed, bounded domain"
  answer: 1
  explanation: "Uniform convergence requires one N (depending only on ε) such that |fₙ(x) − f(x)| < ε for *all* x simultaneously. For fₙ(x) = xⁿ with limit f = 0, we need xⁿ < ε for all x ∈ [0, 1). But for any n, choosing x close enough to 1 makes xⁿ as large as we like below 1. The 'tube' around 0 can never contain the entire graph of fₙ near x = 1. Option C describes a consequence (discontinuous limits), not the reason for this specific failure."

- question: "Which of the following is guaranteed by uniform convergence but cannot be guaranteed from pointwise convergence alone?"
  type: multiple-choice
  options:
    - "The limit function f exists at every point in the domain"
    - "The limit of a sequence of continuous functions is continuous"
    - "The sequence eventually reaches f exactly at each point"
    - "All functions in the sequence share the same maximum value"
  answer: 1
  explanation: "The Uniform Limit Theorem states that if fₙ are continuous and fₙ → f uniformly, then f is continuous. This fails spectacularly under mere pointwise convergence: fₙ(x) = xⁿ on [0, 1] consists entirely of continuous functions yet converges pointwise to a discontinuous limit (0 on [0,1) and 1 at x=1). Uniform convergence is precisely the condition that prevents this kind of 'convergence to a worse function,' and it also enables the interchange of limit and integral."

- question: "Uniform convergence requires that for every ε > 0 there exists N depending only on ε — not on x — such that |fₙ(x) − f(x)| < ε holds for all x in the domain whenever n > N."
  type: true-false
  answer: true
  explanation: "This is the defining difference between uniform and pointwise convergence. In pointwise convergence, the required N can depend on both ε and the specific point x — different points may need different N values. Uniform convergence demands a single N that works everywhere simultaneously. Geometrically: the entire graph of fₙ must fit inside the ε-tube around the graph of f for all sufficiently large n."

- question: "If fₙ → f pointwise and each fₙ is continuous, then f must also be continuous."
  type: true-false
  answer: false
  explanation: "Pointwise convergence does not preserve continuity. The standard counterexample is fₙ(x) = xⁿ on [0, 1]: each fₙ is continuous, but the pointwise limit is 0 on [0, 1) and 1 at x = 1, which is discontinuous. Continuity is preserved by uniform convergence (the Uniform Limit Theorem), but not by pointwise convergence. This is precisely why the stronger condition of uniform convergence matters in analysis."

- question: "What is the key difference between pointwise and uniform convergence, and why does it matter for preserving the continuity of limit functions?"
  type: short-answer
  answer: "In pointwise convergence, each point x gets its own N(ε, x): the speed of convergence can vary arbitrarily across the domain. In uniform convergence, a single N(ε) works for all x simultaneously — convergence is equally fast across the entire domain. Continuity is preserved under uniform convergence because you can use the uniform N to control |f(x) − fₙ(x)| and |fₙ(y) − f(y)| uniformly near any point, then invoke continuity of fₙ for the middle term in an ε/3 argument. Pointwise convergence allows convergence to stall near some points, which can create jumps in the limit function."
  explanation: "The ε/3 proof of the Uniform Limit Theorem splits |f(x) − f(y)| ≤ |f(x) − fₙ(x)| + |fₙ(x) − fₙ(y)| + |fₙ(y) − f(y)|. The first and third terms are controlled by uniform convergence (they are both less than ε/3 for large enough n, independently of x and y). The middle term is controlled by continuity of fₙ. Without uniform convergence, the first and third terms depend on x and y, so you cannot choose n before choosing the nearby point y."
```

## Explainer

You already know **pointwise convergence**: fₙ → f pointwise if for each fixed x, fₙ(x) → f(x). In other words, if you plant a flag at a single point x and watch the sequence of values f₁(x), f₂(x), f₃(x), ... converge to f(x), that's pointwise. The catch is that the convergence speed can vary wildly across different points. At some x, fₙ might reach ε-closeness by n = 5; at another x, you might need n = 500; at a third, n = 5,000,000. Pointwise convergence makes no promise about which N works globally — each point gets its own N depending on both ε *and* x.

**Uniform convergence** changes one word in the definition but changes everything in the theory. The key phrase is that N depends only on ε, not on x. Formally: for every ε > 0, there exists N such that for *all* n > N and *all* x ∈ S, |fₙ(x) − f(x)| < ε. The geometric picture is clean: uniform convergence means the entire graph of fₙ eventually fits inside an ε-tube around the graph of f. The sequence fₙ(x) = xⁿ on [0, 1) is a canonical counterexample: it converges pointwise to the function that is 0 on [0, 1) and 1 at 1, but not uniformly — near x = 1, you always need a larger N to get within ε of 0. The "tube" can never be closed because fₙ bulges up toward 1 near the right endpoint no matter how large n is.

Why does this distinction matter so much? Because pointwise convergence is too weak to transfer analytic properties from fₙ to f. A pointwise limit of continuous functions can be discontinuous (the xⁿ example shows this: each fₙ is continuous, but the limit function has a jump). A pointwise limit of integrable functions can fail to satisfy ∫ fₙ → ∫ f. Uniform convergence repairs all of this. The **Uniform Limit Theorem** states: if each fₙ is continuous and fₙ → f uniformly, then f is continuous. The proof is a classic ε/3 argument — you split the error |f(x) − f(y)| ≤ |f(x) − fₙ(x)| + |fₙ(x) − fₙ(y)| + |fₙ(y) − f(y)|, control the outer two terms using uniform convergence, and control the middle term using continuity of fₙ. Uniform convergence also justifies swapping limits and integrals: ∫ limₙ fₙ = limₙ ∫ fₙ. This interchange is exactly what breaks down for pointwise convergence and is exactly what the Dominated Convergence Theorem later restores in a more general form.
