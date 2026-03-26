---
id: bessel-parseval
title: Bessel's Inequality and Parseval's Identity
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: riesz-representation-theorem-hilbert
  type: hard
- id: orthonormal-bases
  type: hard
builds-toward:
- fourier-series-lp-theory
tags:
- hilbert-spaces
stage: expert
status: validated
---

# Bessel's Inequality and Parseval's Identity

## Core Idea
For an orthonormal sequence (eₙ), Bessel's inequality states Σ|⟨x, eₙ⟩|² ≤ ‖x‖². If the sequence is a complete orthonormal basis, Parseval's identity holds: Σ|⟨x, eₙ⟩|² = ‖x‖².

## Questions

```yaml
- question: "You have a Hilbert space H and an orthonormal sequence (eₙ). For a specific vector x, you compute Σ|⟨x, eₙ⟩|² and find the sum is strictly less than ‖x‖². What does this tell you?"
  type: multiple-choice
  options:
    - "The computation must contain an error — Parseval's identity requires the sum to equal ‖x‖² for any orthonormal sequence"
    - "The vector x has a component that is not captured by the sequence (eₙ) — the sequence is not a complete orthonormal basis"
    - "The vector x does not belong to the Hilbert space H"
    - "The sequence (eₙ) is not orthonormal — only normalized sequences satisfy the inequality"
  answer: 1
  explanation: "Bessel's inequality guarantees Σ|⟨x, eₙ⟩|² ≤ ‖x‖² for any orthonormal sequence; a strict inequality is perfectly consistent and means the sequence is incomplete — it fails to span a dense subspace of H. The 'missing' energy, ‖x‖² − Σ|⟨x, eₙ⟩|², is the squared norm of the component of x that is orthogonal to every eₙ. Parseval's equality holds only when no such orthogonal component can exist, which is exactly the definition of a complete orthonormal basis."

- question: "In signal processing, a signal x is analyzed using a complete orthonormal frequency basis. Parseval's identity holds. Which statement correctly interprets this?"
  type: multiple-choice
  options:
    - "The signal has an equal number of time samples and frequency components"
    - "The total energy computed from the time-domain signal equals the total energy computed from the Fourier coefficients — no energy is lost in the frequency representation"
    - "The signal can be perfectly reconstructed from any finite subset of its Fourier coefficients"
    - "The Fourier coefficients all have the same magnitude, since energy is conserved"
  answer: 1
  explanation: "Parseval's identity says ‖x‖² = Σ|⟨x, eₙ⟩|² — the norm (energy) computed in the original domain equals the sum of squared coefficients in the frequency domain. This is an energy conservation statement: the change of basis from time domain to frequency domain preserves total energy. It does NOT mean all coefficients are equal (option D) or that finite truncations suffice (option C). Option C is false because a finite partial sum always loses the energy in the omitted components."

- question: "Bessel's inequality Σ|⟨x, eₙ⟩|² ≤ ‖x‖² holds for any orthonormal sequence (eₙ) in a Hilbert space, regardless of whether that sequence forms a complete basis."
  type: true-false
  answer: true
  explanation: "Bessel's inequality is unconditional — it follows from the non-negativity of ‖x − Sₙ‖² ≥ 0 for the partial projection Sₙ, and this holds for any orthonormal sequence regardless of completeness. Completeness is the additional condition that makes the inequality into an equality (Parseval). Without completeness, the sum converges to some value ≤ ‖x‖², and the gap represents the squared norm of the projection of x onto the orthogonal complement of the sequence's closed span."

- question: "If Parseval's identity Σ|⟨x, eₙ⟩|² = ‖x‖² holds for one specific vector x, the orthonormal sequence should be a complete orthonormal basis."
  type: true-false
  answer: false
  explanation: "Parseval holding for a single vector does not imply completeness. A sequence could capture all the energy of one particular vector while failing to span the full space. For example, if x happens to lie in the closed span of the sequence, Parseval holds for x even if the sequence misses an orthogonal subspace entirely. Completeness requires Parseval's identity to hold for ALL vectors in H — it is a global condition on the sequence, not a local condition on any single vector."

- question: "What is the precise condition that distinguishes Parseval's identity (equality) from Bessel's inequality, and what does this condition mean geometrically in the Hilbert space?"
  type: short-answer
  answer: "The condition is completeness: the orthonormal sequence (eₙ) must form a complete orthonormal basis, meaning its closed linear span is all of H (or equivalently, the only vector orthogonal to every eₙ is the zero vector). Geometrically, this means no vector in H has a nonzero 'shadow' outside the span of the basis. When the basis is complete, the partial projections Sₙ = Σᵢ⁼¹ⁿ⟨x,eᵢ⟩eᵢ converge in norm to x itself (‖x − Sₙ‖ → 0), so all of ‖x‖² is accounted for by the coefficients and none is lost to an orthogonal complement."
  explanation: "Bessel's inequality always holds because the projection onto any finite-dimensional subspace never exceeds the original norm. The inequality becomes equality exactly when the 'leftover' ‖x − Sₙ‖ → 0, which happens if and only if the basis spans a dense subspace. The concept of completeness in infinite-dimensional Hilbert spaces is subtler than in finite dimensions (where any basis automatically spans the space), making Parseval the canonical criterion for testing whether an orthonormal sequence is truly a basis."
```

## Explainer

From orthonormal bases in finite-dimensional linear algebra, you know that if {u₁, ..., uₙ} is an ONB for ℝⁿ, then any vector v can be written as v = Σ⟨v, uᵢ⟩uᵢ and the Pythagorean theorem gives ‖v‖² = Σ|⟨v, uᵢ⟩|². Now suppose you're in a Hilbert space — an infinite-dimensional inner product space that is complete — and you have a countably infinite **orthonormal sequence** (eₙ). The **Fourier coefficients** ⟨x, eₙ⟩ measure how much of the vector x lies along each basis direction, just as in the finite case.

**Bessel's inequality** says that the sum of squared Fourier coefficients never exceeds ‖x‖²: Σ|⟨x, eₙ⟩|² ≤ ‖x‖². The proof is elegant: form the partial sum Sₙ = Σᵢ₌₁ⁿ ⟨x, eᵢ⟩eᵢ (the projection of x onto the span of the first n basis vectors) and use the Pythagorean theorem on the orthogonal decomposition x = Sₙ + (x − Sₙ). Since ‖x − Sₙ‖² ≥ 0, we get ‖x‖² = ‖Sₙ‖² + ‖x − Sₙ‖² ≥ ‖Sₙ‖² = Σᵢ₌₁ⁿ|⟨x, eᵢ⟩|². The inequality survives as n → ∞. Bessel says the orthonormal sequence captures *at most* all of the "energy" of x.

**Parseval's identity** is the equality case: Σ|⟨x, eₙ⟩|² = ‖x‖². This holds precisely when the orthonormal sequence is a **complete orthonormal basis** — one that spans a dense subspace, meaning every vector in the Hilbert space can be approximated arbitrarily well by finite linear combinations of the basis vectors. Completeness ensures the remainder ‖x − Sₙ‖ → 0 as n → ∞, so no energy is "left over." The Riesz representation theorem (your prerequisite) guarantees that the bounded linear functionals on a Hilbert space are exactly the inner products with fixed vectors, which is the machinery that makes this convergence rigorous.

The physical and applied interpretation is that of energy conservation. In signal processing, x is a signal, the eₙ are frequency components, and ⟨x, eₙ⟩ are the amplitudes. Parseval says the total energy computed in the time domain (‖x‖²) equals the total energy computed in the frequency domain (Σ|⟨x, eₙ⟩|²). This equality is the foundation of Fourier analysis: it is what lets you work with coefficients instead of functions, confident that no information is lost in the representation.
