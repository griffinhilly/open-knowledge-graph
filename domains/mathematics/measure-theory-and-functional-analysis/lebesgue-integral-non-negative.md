---
id: lebesgue-integral-non-negative
title: Lebesgue Integral for Non-Negative Functions
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lebesgue-integral-simple-functions
  type: hard
builds-toward:
- lebesgue-integral-general-definition
- monotone-convergence-theorem-analysis
- fatou-lemma-measure-theory
tags:
- integration
- lebesgue-integral
stage: expert
status: draft
---

# Lebesgue Integral for Non-Negative Functions

## Core Idea
For non-negative measurable f, define ∫f dμ = sup{∫φ dμ : φ simple, φ ≤ f}. This definition is monotone: f ≤ g implies ∫f ≤ ∫g. The integral may be infinite but is always defined.

## Questions

```yaml
- question: "For a non-negative measurable function f that is not simple, how is ∫f dμ defined?"
  type: multiple-choice
  options:
    - "As the limit of Riemann sums using equally-spaced partitions of the domain"
    - "As the supremum of ∫φ dμ over all simple functions φ satisfying 0 ≤ φ ≤ f"
    - "As the infimum of ∫ψ dμ over all simple functions ψ satisfying ψ ≥ f"
    - "As the limit of ∫fₙ dμ where fₙ are the truncations fₙ = min(f, n)"
  answer: 1
  explanation: "The Lebesgue integral for non-negative f is defined by approximating from *below*: take all simple functions dominated by f, integrate each one (which is well-defined from the prior definition), and take the supremum of those values. This is philosophically distinct from Riemann sums (which partition the domain) — Lebesgue integration partitions the *range*. The infimum from above (option C) gives a different object; the truncation approach (option D) would work but is not the primary definition — it's a consequence via the Monotone Convergence Theorem."

- question: "Let f(x) = 1/√x on (0,1] and f(0) = 0, with Lebesgue measure μ. What is ∫f dμ?"
  type: multiple-choice
  options:
    - "Undefined — f is not bounded and therefore not Lebesgue integrable"
    - "0 — the singularity at x = 0 has measure zero and contributes nothing"
    - "+∞ — the Lebesgue integral is defined but equals infinity"
    - "2 — the improper Riemann integral converges, and Lebesgue agrees"
  answer: 3
  explanation: "∫₀¹ x^{-1/2} dx = 2 as an improper Riemann integral, and the Lebesgue integral agrees with the improper Riemann integral whenever the latter exists and the function is non-negative. The Lebesgue integral is defined (by supremum of simple functions) and equals 2. Option A is wrong because the Lebesgue integral handles unbounded functions cleanly — it is defined for any non-negative measurable function, possibly equaling +∞. Option C would be correct for a function like 1/x (which has infinite integral on (0,1]) but not 1/√x."

- question: "The Lebesgue integral for non-negative functions is undefined when the function is unbounded, since no simple function can approximate an infinite value."
  type: true-false
  answer: false
  explanation: "The Lebesgue integral is *always* defined for non-negative measurable functions, whether bounded or not. The supremum of a set of non-negative numbers is either a finite non-negative number or +∞ — never undefined. If f is unbounded and the supremum is +∞, then ∫f dμ = +∞, which is a valid well-defined value in [0, +∞]. Indefiniteness (true 'undefined') only arises when you try to define the integral for a function with large positive and negative parts, where you might get ∞ − ∞. Non-negative functions avoid this problem entirely."

- question: "If f ≤ g everywhere (both non-negative measurable), then every simple function dominated by f is also dominated by g, which implies ∫f dμ ≤ ∫g dμ."
  type: true-false
  answer: true
  explanation: "This is the monotonicity property, and its proof follows directly from the supremum definition. If φ is simple and 0 ≤ φ ≤ f ≤ g, then φ is also a candidate in the supremum defining ∫g dμ. So every value in the set {∫φ : 0 ≤ φ ≤ f, φ simple} also appears in {∫φ : 0 ≤ φ ≤ g, φ simple}. The second set is at least as large, so its supremum is at least as large. Monotonicity is the key property that powers the Monotone Convergence Theorem: if fₙ ↑ f pointwise, the integrals ∫fₙ form a non-decreasing sequence bounded above by ∫f."

- question: "Why is the Lebesgue integral for non-negative functions defined using a supremum over simple functions below f, and what goes wrong if you try to apply the same approach to functions that can take negative values?"
  type: short-answer
  answer: "For non-negative functions, approximating from below is unambiguous: simple functions below f contribute less area than f, and the supremum captures the exact total area. The definition is always well-defined because the supremum of non-negative numbers is either finite or +∞, never undefined. For functions with negative values, the 'approximate from below' approach creates the problem ∞ − ∞: if f has a large positive part and a large negative part, the supremum of simple functions below f could be +∞ (capturing the positive part) and the 'correction' for the negative part would also be −∞, leaving the integral as ∞ − ∞, which is undefined. The solution is to decompose f into its positive part f⁺ = max(f, 0) and negative part f⁻ = max(−f, 0), integrate each using the non-negative definition, and compute ∫f = ∫f⁺ − ∫f⁻, which is well-defined as long as at least one of ∫f⁺, ∫f⁻ is finite."
  explanation: "This two-step structure — define for non-negative functions first, then extend by decomposition — is how measure theory builds integration rigorously. The non-negative case establishes the floor; the general case inherits its properties. The Monotone Convergence Theorem, Fatou's Lemma, and the Dominated Convergence Theorem are all proved first for non-negative functions and then extended."
```

## Explainer

You already know how to integrate **simple functions** — those that take only finitely many values on measurable sets. A simple function looks like a staircase: constant on each of finitely many pieces. Integrating it is easy: multiply each constant value by the measure of the set where it achieves that value, then sum. The Lebesgue integral for non-negative functions extends this to every non-negative measurable function by a single elegant move: approximate from below.

The key idea is the **supremum definition**: ∫f dμ = sup{∫φ dμ : φ simple, 0 ≤ φ ≤ f}. You take all the simple functions that underestimate f everywhere, integrate each one, and then take the least upper bound of all those numbers. If f is itself simple, this recovers the simple function integral. If f is a smooth curve, it approximates f from below with ever-finer staircases. The supremum captures the "total area" even when no single simple function achieves it.

This definition handles two important edge cases cleanly. First, it is always defined — the supremum of a set of non-negative numbers is either a finite non-negative number or +∞, never undefined. A function like 1/√x near 0 may have infinite integral; that's allowed and just equals +∞. Second, it is **monotone**: if f ≤ g everywhere, then every simple function below f is also below g, so the supremum for f is ≤ the supremum for g. This monotonicity is the engine behind the Monotone Convergence Theorem you'll see next.

Why restrict to non-negative functions first? Because non-negative functions have a clean order structure: if φ ≤ f, then more of φ means more of f. Negative values break this — you could have a function that is sometimes large-positive and sometimes large-negative, and the cancellations make "approximating from below" ambiguous. The general Lebesgue integral (for functions that can be negative) is built on top of this: split f into its positive part f⁺ = max(f, 0) and negative part f⁻ = max(−f, 0), integrate both as non-negative functions, and subtract — but only when at least one is finite to avoid ∞ − ∞.
