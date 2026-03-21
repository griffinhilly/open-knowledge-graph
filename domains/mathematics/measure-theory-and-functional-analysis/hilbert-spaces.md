---
id: hilbert-spaces
title: Hilbert Spaces
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: inner-products
  type: hard
- id: banach-spaces
  type: hard
builds-toward:
- orthogonality-hilbert-spaces
tags:
- hilbert-spaces
stage: advanced
status: draft
---

# Hilbert Spaces

## Core Idea
A Hilbert space is a complete inner product space. The inner product induces a norm, and completeness ensures limits exist. L² spaces exemplify Hilbert spaces, which are fundamental in quantum mechanics and harmonic analysis.

## Questions

```yaml
- question: "A space of functions has a well-defined inner product, but a Cauchy sequence of functions in the space converges to a function that is not in the space. What does this tell you about the space?"
  type: multiple-choice
  options:
    - "The inner product is not well-defined, because a valid inner product would prevent sequences from leaving the space"
    - "The space is not complete, and therefore it is not a Hilbert space even though it has an inner product"
    - "The space is a Hilbert space because it possesses an inner product — completeness is automatically guaranteed by the inner product axioms"
    - "Cauchy sequences are not a relevant criterion in function spaces, only in finite-dimensional vector spaces"
  answer: 1
  explanation: "A Hilbert space requires two properties: an inner product AND completeness. Completeness means every Cauchy sequence converges to a limit that lies within the space. If a Cauchy sequence escapes the space, completeness fails, and the space is not Hilbert — it is merely an inner product space. The common misconception is that having an inner product is enough; it is not. The space of continuous functions C([0,1]) with the L² inner product is an inner product space that is not complete — Cauchy sequences can converge to discontinuous functions outside C([0,1])."

- question: "Why is L²(Ω) — the space of square-integrable functions — the natural setting for Fourier analysis, rather than C(Ω), the space of continuous functions?"
  type: multiple-choice
  options:
    - "C(Ω) has no natural inner product, so Fourier coefficients cannot be defined for continuous functions"
    - "L²(Ω) is complete: Fourier series may converge to functions with discontinuities that belong to L² but not to C(Ω), and completeness guarantees these limits stay in the space"
    - "L² functions are computationally easier to work with than continuous functions"
    - "C(Ω) does not contain trigonometric functions, so Fourier bases cannot be defined there"
  answer: 1
  explanation: "C(Ω) does have an inner product (the L² inner product), but it is not complete under it — sequences of continuous functions can converge to discontinuous functions (like a square wave). These limit functions are outside C(Ω), so infinite Fourier sums would 'fall off the edge' of the space. L²(Ω) is complete: it includes all square-integrable functions, continuous or not, and every Fourier series that converges in the L² sense converges to something inside L². Completeness is what makes infinite superpositions a safe operation."

- question: "Every Hilbert space is a Banach space, but not every Banach space is a Hilbert space."
  type: true-false
  answer: true
  explanation: "A Hilbert space's inner product induces a norm via ‖v‖ = √⟨v,v⟩, and completeness with respect to this norm makes it a Banach space. So every Hilbert space satisfies the definition of a Banach space. But the converse fails: a Banach space has a norm but may not come from any inner product. The parallelogram law (‖u+v‖² + ‖u−v‖² = 2‖u‖² + 2‖v‖²) is necessary and sufficient for a norm to come from an inner product — not all Banach space norms satisfy it. For example, L¹ is Banach but not Hilbert."

- question: "An inner product space is automatically a Hilbert space, because the inner product structure provides all the geometric information needed for analysis."
  type: true-false
  answer: false
  explanation: "An inner product space has angle, length, and orthogonality, but it may fail to be complete. Completeness — that every Cauchy sequence converges to a limit inside the space — is a separate, independent requirement. Without it, infinite-dimensional operations become unreliable: a Fourier series might converge to something outside the space, making the expansion meaningless. Hilbert spaces are inner product spaces that have been 'filled in' (completed), so no limits can escape. The completeness requirement is not redundant — it is what makes functional analysis work."

- question: "Explain in your own words why completeness is essential for Hilbert spaces. Use Fourier series as your example: what could go wrong in an incomplete space?"
  type: short-answer
  answer: "In a Fourier series, you build up an approximation of a function by adding infinitely many sinusoidal terms. Each partial sum is a valid element of the space, and as you add more terms, the sequence of partial sums becomes a Cauchy sequence — the terms get closer and closer together. Completeness guarantees that this Cauchy sequence converges to something inside the space. Without completeness, the limit might not exist within the space, making the Fourier series a sequence that goes 'nowhere' inside the space. Infinite superpositions — the fundamental tool of Fourier and quantum analysis — would be undefined."
  explanation: "Completeness is what separates a mathematically safe arena for analysis from one full of holes. In physics, quantum states are superpositions of basis states (analogous to Fourier coefficients), and completeness ensures that any such superposition is itself a valid quantum state. In signal processing, every square-integrable signal has a Fourier expansion that converges back to it in the L² sense. Both of these guarantees require completeness. The practical consequence is: Hilbert spaces are the right spaces for any theory that involves infinite sums or infinite-dimensional expansions."
```

## Explainer

You've already studied two structural properties of infinite-dimensional spaces separately: **inner products**, which give you a notion of angle, length, and orthogonality via ⟨u, v⟩; and **Banach spaces**, which are normed spaces where Cauchy sequences converge. A **Hilbert space** unifies both requirements: it is an inner product space whose inner product induces a norm ‖v‖ = √⟨v,v⟩, and in which that norm makes the space complete. Every Cauchy sequence converges to a limit that stays inside the space.

The necessity of completeness becomes vivid with Fourier series. You can approximate a function by taking finite sums of sines and cosines. Each partial sum is a legitimate element of your function space. But as you add more and more terms, the partial sums form a Cauchy sequence — they stabilize — and the limit is the function itself. Without completeness, that limit might not belong to your space, leaving infinite sums as meaningless operations. Hilbert spaces guarantee that these limit operations are safe: infinite superpositions always converge to an element that remains in the space.

The canonical example is **L²(Ω)**, the space of square-integrable functions on a domain Ω. The inner product is ⟨f, g⟩ = ∫_Ω f(x)g(x) dx, which induces the norm ‖f‖² = ∫_Ω |f(x)|² dx — a measure of the total "energy" of a function. L²(Ω) is a Hilbert space, and it is the natural arena for Fourier analysis: sinusoids form an orthonormal basis, every square-integrable function has a convergent Fourier expansion, and Parseval's theorem says the energy of a signal equals the sum of squared Fourier coefficients.

In quantum mechanics, the state of a physical system is a unit vector in a Hilbert space (typically L²(ℝ³)), observable quantities correspond to self-adjoint operators on this space, and the inner product encodes probability amplitudes. The abstract geometry you're studying — orthogonality, projections, basis expansions — governs physical reality at the microscopic scale. This is not a coincidence: the axioms of quantum mechanics were chosen precisely because Hilbert space geometry captures the probabilistic structure of measurement.
