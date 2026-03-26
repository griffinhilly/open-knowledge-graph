---
id: analytic-continuation
title: Analytic Continuation
domain: mathematics
course: complex-analysis
prerequisites:
- id: taylor-series-complex
  type: hard
tags:
- analytic-continuation
- extension
- identity-theorem
stage: advanced
status: validated
---

# Analytic Continuation

## Core Idea
If two analytic functions agree on a set with a limit point in their common domain, then they are identical on the entire connected component of their domain. This identity theorem implies that an analytic function is completely determined by its values on any small open set, and can be uniquely extended (continued) along paths in the plane — the basis for understanding multi-valued functions and Riemann surfaces.

## Questions

```yaml
- question: "Two holomorphic functions f and g are defined on the same connected open domain D. A student discovers that f(1/n) = g(1/n) for every positive integer n. What can the Identity Theorem conclude?"
  type: multiple-choice
  options:
    - "f and g agree on all rational inputs in D, but may differ on irrational inputs"
    - "f and g are identical throughout all of D, because the sequence {1/n} has a limit point (0) inside D"
    - "f and g agree on an interval around 0, but may diverge further from the origin"
    - "No conclusion can be drawn without knowing the Taylor series of both functions at every point"
  answer: 1
  explanation: "The Identity Theorem requires only that two holomorphic functions agree on a set with a limit point inside the connected domain — and {1/n} converges to 0, a limit point. That single condition forces f ≡ g throughout all of D. This rigidity has no analogue in real analysis: a smooth real function could be modified arbitrarily on any interval while agreeing with another function on {1/n}. The remarkable power of complex analyticity is that values on any limit-point-containing set determine the function globally."

- question: "A mathematician continues log(z) starting from z = 1 (where log(1) = 0) along a path that winds once counterclockwise around the origin and returns to z = 1. What value does the continuation assign to z = 1 after this loop?"
  type: multiple-choice
  options:
    - "0 — the continuation returns to the starting value because z = 1 is the same point"
    - "2πi — the continuation tracks the accumulated argument, which increased by 2π around the origin"
    - "The continuation is undefined because log is not holomorphic along a circular path"
    - "−2πi — the continuation loses one branch worth of argument when returning to the start"
  answer: 1
  explanation: "This is monodromy in action. As z travels counterclockwise around the origin, its argument increases by 2π. Since log(z) = ln|z| + i·arg(z), the imaginary part accumulates 2π over one full loop, returning log(1) with value 0 + 2πi = 2πi, not 0. Analytic continuation is locally unique — no other extension exists in any overlapping disk — but globally path-dependent around branch points. This path-dependence is what a Riemann surface resolves by separating the branches into distinct sheets."

- question: "The Identity Theorem implies that a holomorphic function is more rigidly determined by local data than any smooth real-valued function, because matching values on a set with a limit point forces global equality on the entire connected domain."
  type: true-false
  answer: true
  explanation: "The Explainer explicitly contrasts this with real analysis: 'A smooth real function can be freely modified on any interval without affecting its values elsewhere. A holomorphic complex function has no such freedom.' The Identity Theorem's hypothesis requires only a set with a limit point (not even density), yet the conclusion is global identity throughout the connected domain. This rigidity is the source of analytic continuation's power — it means that any holomorphic extension to an overlapping domain is unique."

- question: "Analytic continuation usually produces the same value regardless of the path taken, because the Identity Theorem guarantees that holomorphic extensions are unique."
  type: true-false
  answer: false
  explanation: "The Identity Theorem guarantees local uniqueness — there is only one holomorphic extension in any overlapping disk. But global continuation along paths can be path-dependent when the path encircles branch points (like the origin for log z or z^(1/2)). Monodromy — returning a different value after a closed loop — is a consequence of the multi-valued nature of these functions in the plane. Path-independence holds only in simply connected domains containing no branch points; the Riemann surface resolves the ambiguity by providing a globally single-valued domain."

- question: "The Riemann zeta function is defined by Σ n⁻ˢ, which converges only for Re(s) > 1. Why does analytic continuation matter for understanding ζ(s) beyond this region?"
  type: short-answer
  answer: "Analytic continuation uniquely extends ζ(s) to all of ℂ minus the pole at s = 1, because the Identity Theorem guarantees that any two holomorphic functions agreeing on an open set must be identical throughout their connected domain. The extended function is the unique analytic function that matches the series where the series converges. This matters because the extended function reveals properties invisible in the convergent region — including the zeros in the critical strip 0 < Re(s) < 1, whose distribution is the subject of the Riemann Hypothesis."
  explanation: "This example shows why analytic continuation is not merely a technical extension trick but a conceptual expansion of what a function is. The series Σ n⁻ˢ is not 'the' Riemann zeta function — it is a representation valid in one region. The analytically continued function, which has no series representation in the critical strip, is the complete mathematical object, and understanding the distinction is essential for complex analysis and analytic number theory."
```

## Explainer

From your study of Taylor series in the complex plane, you know that a holomorphic function on a disk is completely encoded by its power series, and the power series converges on the largest disk that avoids singularities. This suggests something striking: knowing a function on a small disk might determine it everywhere. The **Identity Theorem** makes this precise and provides the theoretical foundation for analytic continuation.

The Identity Theorem states: if f and g are holomorphic on a connected open domain D, and they agree on any set that has a limit point inside D — even an infinite sequence of distinct points converging to an interior point — then f ≡ g throughout D. This rigidity has no real-analysis counterpart. A smooth real function can be freely modified on any interval without affecting its values elsewhere. A holomorphic complex function has no such freedom: its Taylor coefficients at any point are forced by the function values on any nearby limit-containing set, and matching Taylor coefficients on one disk forces equality on every overlapping disk, propagating throughout the connected domain.

**Analytic continuation** exploits this rigidity to extend functions beyond their original domains. Given f holomorphic on a disk D₁, suppose you find a holomorphic function g on an overlapping disk D₂ that agrees with f on D₁ ∩ D₂. The Identity Theorem guarantees that g is the *unique* analytic extension of f to D₂ — there is no other way to extend f holomorphically to D₂. Repeat the process disk by disk along a path to reach far beyond the original domain. The classic instance is the Riemann zeta function: the series Σ n⁻ˢ converges only for Re(s) > 1, but analytic continuation uniquely extends it to all of ℂ minus a simple pole at s = 1.

A subtlety arises when continuation can travel along loops. If you continue log(z) starting near z = 1, where log(1) = 0, and travel along a path that winds once around the origin, you return to z = 1 with value 2πi instead of 0. The continuation is path-dependent: the value you recover depends on how many times you've encircled the origin. This **monodromy** is the source of multi-valued functions — log z and z^(1/2) are not truly multi-valued but are single-valued functions on a **Riemann surface**, a multi-sheeted domain that unwinds the loop. Analytic continuation reveals this structure: when continuing around a loop fails to return to the starting value, the domain itself must be extended into multiple sheets to accommodate the function globally.
