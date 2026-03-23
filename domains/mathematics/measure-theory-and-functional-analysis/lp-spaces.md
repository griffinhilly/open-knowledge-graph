---
id: lp-spaces
title: Lᵖ Spaces
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lebesgue-integral
  type: hard
- id: vector-spaces
  type: hard
builds-toward:
- holder-inequality
tags:
- lp-spaces
- banach-spaces
stage: expert
status: validated
---

# Lᵖ Spaces

## Core Idea
Lᵖ(μ) is the space of measurable functions with ∫|f|ᵖ dμ < ∞, identified modulo null sets, equipped with norm ‖f‖ₚ = (∫|f|ᵖ dμ)^(1/p). These are the fundamental function spaces in functional analysis and harmonic analysis.

## Questions

```yaml
- question: "Which Lᵖ space is the only one that is also a Hilbert space, and why?"
  type: multiple-choice
  options:
    - "L¹, because it contains the most integrable functions and therefore has the richest structure"
    - "L², because the exponent p = 2 enables a genuine inner product ⟨f, g⟩ = ∫fg dμ satisfying all inner product axioms"
    - "L∞, because bounded functions have the most regularity and smoothness"
    - "All Lᵖ spaces are Hilbert spaces for p ≥ 1"
  answer: 1
  explanation: "A Hilbert space requires an inner product, not just a norm. An inner product must satisfy the parallelogram law: ‖f + g‖² + ‖f − g‖² = 2‖f‖² + 2‖g‖². This identity holds in L² — where ‖f‖₂² = ∫|f|² dμ corresponds to a genuine dot-product structure — but fails for all Lᵖ with p ≠ 2. L² has the inner product ⟨f,g⟩ = ∫fḡ dμ, making it the natural home for Fourier analysis, quantum mechanics, and spectral theory, all of which rely on orthogonality and projections."

- question: "A function f: [0,1] → ℝ is defined as f(x) = 0 for all x except f(1/2) = 10⁶. In L²([0,1]) with Lebesgue measure, this function is:"
  type: multiple-choice
  options:
    - "A non-trivial L² element with ‖f‖₂ = 10⁶, since it takes a large value at x = 1/2"
    - "Identified with the zero function, because {1/2} has Lebesgue measure zero so ‖f‖₂ = 0"
    - "Not in L² because its pointwise value exceeds 1"
    - "In L² with norm equal to 1, because Lebesgue measure normalizes point masses"
  answer: 1
  explanation: "‖f‖₂² = ∫₀¹ |f|² dμ = 0, because the single point {1/2} has Lebesgue measure zero — it contributes nothing to a Lebesgue integral. Since ‖f‖₂ = 0 while f is not identically zero, the norm would be degenerate if we treated such functions as distinct elements. The solution is that Lᵖ elements are equivalence classes: f ~ g if they agree almost everywhere. This function is identified with the zero function because they differ only on a null set."

- question: "Lᵖ spaces are Banach spaces — complete normed vector spaces — meaning every Cauchy sequence in Lᵖ converges to an element that is also in Lᵖ."
  type: true-false
  answer: true
  explanation: "Completeness is the key structural property that makes Lᵖ spaces analytically useful. Without it, limits of sequences of Lᵖ functions might escape the space, making analysis intractable. The Riesz-Fischer theorem establishes that Lᵖ is complete for all 1 ≤ p ≤ ∞. This property underpins all convergence theorems in functional analysis and makes Lᵖ spaces suitable for solving differential equations, optimization problems, and approximation questions."

- question: "On a probability space (total measure 1), every function in L¹ is also in L², since a finite integral automatically implies a finite squared integral."
  type: true-false
  answer: false
  explanation: "The inclusion goes the other direction: on a probability space, L∞ ⊆ L² ⊆ L¹. A function can have finite integral (L¹) without having finite squared integral (L²). For example, f(x) = x^(−3/4) on (0,1]: ∫₀¹ x^(−3/4) dx = 4 (finite, so f ∈ L¹), but ∫₀¹ x^(−3/2) dx diverges (f ∉ L²). Higher Lᵖ membership is the more restrictive condition — being in L² is a stronger requirement than being in L¹ on probability spaces."

- question: "Explain why elements of Lᵖ spaces are defined as equivalence classes of functions rather than individual functions, and what property of the norm makes this identification necessary."
  type: short-answer
  answer: "A norm must satisfy positive-definiteness: ‖f‖ₚ = 0 should imply f is 'zero.' But ‖f‖ₚ = (∫|f|ᵖ dμ)^(1/p) = 0 whenever f = 0 almost everywhere — including functions that are nonzero only on a set of measure zero. If these were treated as distinct elements, the norm would not be positive-definite. The fix is to identify any two functions that agree almost everywhere as the same Lᵖ element. On equivalence classes, ‖[f]‖ₚ = 0 if and only if f = 0 a.e., which is the same as [f] = [0], restoring positive-definiteness."
  explanation: "This identification reflects the fundamental measure-theoretic principle that integration cannot detect what a function does on a null set. Modifying a function on a null set produces an indistinguishable function from the measure's perspective. The equivalence class construction is not a technicality to be ignored — it is essential to the mathematical integrity of Lᵖ as a normed space, and understanding it clarifies why 'a.e.' appears throughout functional analysis."
```

## Explainer

From your study of vector spaces, you know that a norm is a way of measuring the "size" of an element. From the Lebesgue integral, you can integrate measurable functions. **Lᵖ spaces** combine both ideas: they are vector spaces of measurable functions, equipped with a norm built from integration. The defining idea is that f belongs to Lᵖ(μ) if the integral of |f|ᵖ is finite — meaning f is "p-th power integrable." The norm ‖f‖ₚ = (∫|f|ᵖ dμ)^(1/p) generalizes the familiar Euclidean length formula ‖v‖ = (Σvᵢ²)^(1/2) from finite dimensions by replacing the sum with an integral and the exponent 2 with p.

Different values of p emphasize different aspects of a function's behavior. **L¹** functions are simply integrable — they have finite total area. **L²** functions are square-integrable; L² is the only Lᵖ space that is also a Hilbert space (inner product space), with ⟨f, g⟩ = ∫fg dμ. This makes L² the natural home for Fourier series and quantum mechanics. **L∞** is a limiting case defined by the essential supremum: ‖f‖_∞ = inf{M : |f| ≤ M almost everywhere}, capturing the "maximum size" of a function while ignoring sets of measure zero. As p increases from 1 to ∞, the Lᵖ norm becomes increasingly sensitive to large peaks and less sensitive to the overall bulk of the function.

A key subtlety: Lᵖ functions are not individual functions but **equivalence classes** — two functions that differ only on a set of measure zero are identified as the same Lᵖ element. This is necessary to make the norm nondegenerate (‖f‖ₚ = 0 should imply f is "zero," but a function that is nonzero only on a null set has zero norm). This identification is philosophically natural in measure theory, where "almost everywhere" is the operative notion of truth.

The most important structural fact is that Lᵖ spaces are **Banach spaces** — complete normed vector spaces, meaning every Cauchy sequence converges to an element of the same space. Completeness is what makes Lᵖ spaces analytically tractable: limits of sequences stay in the space. The containment relationships between Lᵖ spaces depend on whether the measure space has finite or infinite total measure, but on a probability space (μ(X) = 1), we have the inclusion L∞ ⊆ Lq ⊆ Lp ⊆ L¹ whenever p ≤ q. These spaces, together with Hölder's inequality (your next topic), form the backbone of modern analysis.
