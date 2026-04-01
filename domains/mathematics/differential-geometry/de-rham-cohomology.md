---
id: de-rham-cohomology
title: de Rham Cohomology
domain: mathematics
course: differential-geometry
prerequisites:
  - id: exterior-derivative
    type: hard
  - id: differential-forms-introduction
    type: hard
  - id: stokes-theorem-on-manifolds
    type: hard
  - id: connectedness-definition-examples
    type: soft
tags:
  - de-rham-cohomology
  - closed-forms
  - exact-forms
  - topological-invariants
stage: expert
status: validated
---

# de Rham Cohomology

## Core Idea
The de Rham cohomology Hᵏ(M) = {closed k-forms}/{exact k-forms} measures the topological complexity of a manifold using differential forms. It detects "holes" of various dimensions: H⁰ counts connected components, H¹ detects loops that are not boundaries, and Hⁿ detects orientation. The de Rham theorem proves this analytic construction equals the purely topological singular cohomology, establishing one of the deepest bridges between analysis and topology. De Rham cohomology is computable, functorial, and fundamental to modern geometry and physics.

## Questions

```yaml
- question: "H⁰(M) is the space of smooth functions f on M satisfying df = 0. For a connected manifold, what is H⁰(M)?"
  type: multiple-choice
  options:
    - "The zero vector space"
    - "ℝ (the constant functions)"
    - "C∞(M) (all smooth functions)"
    - "ℝⁿ where n = dim(M)"
  answer: 1
  explanation: "A function f with df = 0 has zero derivative everywhere, hence is locally constant. On a connected manifold, locally constant functions are globally constant. So H⁰(M) = {constant functions} ≅ ℝ. For a manifold with k connected components, H⁰(M) ≅ ℝᵏ — one constant for each component. This is the simplest example of how de Rham cohomology encodes topology."

- question: "The Poincaré lemma states that on a contractible open set U, every closed form is exact: Hᵏ(U) = 0 for k ≥ 1. This means de Rham cohomology is a global invariant, not a local one."
  type: true-false
  answer: true
  explanation: "Locally (on any sufficiently small open ball), there are no nontrivial cohomology classes — every closed form can be written as dα. Nontrivial cohomology arises only from the global topology of M. For instance, the 1-form dθ on S¹ is closed but not exact (its integral around S¹ is 2π ≠ 0), and this reflects the nontrivial topology of the circle (it has a hole). The Poincaré lemma means de Rham cohomology is entirely a global phenomenon."

- question: "The de Rham theorem establishes that the de Rham cohomology H*_dR(M) is isomorphic to which other cohomology theory?"
  type: short-answer
  answer: "The singular cohomology H*_sing(M; ℝ) with real coefficients. The isomorphism is given by the integration pairing: a closed k-form ω and a singular k-cycle σ pair to give the number ∫_σ ω. Stokes' theorem ensures this pairing is well-defined on cohomology and homology classes. The de Rham theorem says this pairing is a perfect pairing, establishing an isomorphism H^k_dR(M) ≅ H^k_sing(M; ℝ). This means topological invariants (Betti numbers, cup products) can be computed using differential forms."
  explanation: "The de Rham theorem is remarkable because it equates a construction from analysis (differential forms, exterior derivative) with a construction from algebraic topology (singular chains, boundary operator). It implies that the Betti numbers bₖ = dim Hᵏ(M) are finite for compact manifolds and satisfy Poincaré duality. The theorem justifies using differential forms as a computational tool for topology."

- question: "For the n-torus Tⁿ = (S¹)ⁿ, the de Rham cohomology is Hᵏ(Tⁿ) ≅ ℝ^{C(n,k)}, where C(n,k) is the binomial coefficient."
  type: true-false
  answer: true
  explanation: "The n-torus has coordinates (θ₁,...,θₙ), and the closed forms dθ_{i₁} ∧ ... ∧ dθ_{iₖ} for i₁ < ... < iₖ represent a basis for Hᵏ(Tⁿ). There are C(n,k) such forms, so dim Hᵏ(Tⁿ) = C(n,k). The total dimension Σ_k dim Hᵏ = Σ_k C(n,k) = 2ⁿ, and the Euler characteristic χ = Σ(-1)ᵏ C(n,k) = 0 for n ≥ 1. The Künneth formula (cohomology of a product is the tensor product of cohomologies) makes this computation systematic."
```

## Explainer

The exterior derivative d creates a **chain complex** of differential forms: 0 → Ω⁰(M) →d Ω¹(M) →d Ω²(M) →d ... →d Ωⁿ(M) → 0. The identity d² = 0 means every exact form (image of d) is closed (kernel of d), so im(d) ⊂ ker(d) at each stage. The **de Rham cohomology** Hᵏ(M) = ker(d : Ωᵏ → Ωᵏ⁺¹) / im(d : Ωᵏ⁻¹ → Ωᵏ) measures the "gap" between closed and exact forms. A nonzero element of Hᵏ(M) is a closed form that cannot be written as dα — it represents a topological obstruction.

The simplest examples are illuminating. For **H⁰**: closed 0-forms are locally constant functions, so H⁰(M) ≅ ℝᵇ⁰ where b₀ is the number of connected components. For **H¹**: on the circle S¹, the form dθ is closed but not exact (∫_{S¹} dθ = 2π ≠ 0, but θ is not a globally defined function). So H¹(S¹) ≅ ℝ, reflecting the hole in S¹. On the 2-torus T², H¹(T²) ≅ ℝ² (two independent loops) and H²(T²) ≅ ℝ (the area form). On **ℝⁿ**, the Poincaré lemma gives Hᵏ(ℝⁿ) = 0 for k ≥ 1 — no topology means no cohomology.

The **de Rham theorem** states that H*_dR(M) is naturally isomorphic to the singular cohomology H*_sing(M; ℝ). The isomorphism is given by integration: a closed k-form ω acts on a k-cycle σ by ω(σ) = ∫_σ ω. Stokes' theorem ensures this is well-defined on equivalence classes (adding an exact form to ω does not change the integral over a cycle, and integrating over a boundary gives zero by Stokes). The **Betti numbers** bₖ = dim Hᵏ(M) are topological invariants: b₀ = number of components, b₁ = number of independent loops, bₙ = 1 if M is compact and oriented, 0 otherwise. The alternating sum χ(M) = Σ(-1)ᵏ bₖ is the Euler characteristic.

De Rham cohomology has a **ring structure**: the wedge product of closed forms is closed, and wedging with an exact form gives an exact form, so ∧ descends to cohomology. The resulting ring (H*(M), ∧) is isomorphic to the cup product ring of singular cohomology. Cohomology rings distinguish manifolds that Betti numbers alone cannot — for instance, CP² and S² ∨ S⁴ have the same Betti numbers but different cohomology rings. The Mayer-Vietoris sequence, Künneth formula, and Poincaré duality are powerful computational tools. In physics, de Rham cohomology classifies gauge field configurations (the first Chern class), magnetic monopole charges, and topological sectors of quantum field theories.
