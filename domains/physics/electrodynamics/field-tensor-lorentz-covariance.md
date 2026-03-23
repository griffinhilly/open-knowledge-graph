---
id: field-tensor-lorentz-covariance
title: Electromagnetic Field Tensor and Covariance
domain: physics
course: electrodynamics
prerequisites:
- id: electromagnetic-field-tensor
  type: hard
- id: lorentz-transformations-em-fields
  type: hard
builds-toward:
- relativistic-particle-em-coupling
tags:
- field-tensor
- lorentz-covariance
- 4-vector-formalism
stage: expert
status: validated
---

# Electromagnetic Field Tensor and Covariance

## Core Idea
The electromagnetic field tensor Fμν is a 4×4 antisymmetric tensor with entries proportional to E and B fields. Lorentz transformations act linearly on Fμν, ensuring that Maxwell's equations take identical form in all inertial frames. Invariants like E·B and E² - c²B² are frame-independent.

## Questions

```yaml
- question: "In frame S, there is a purely magnetic field B pointing in the z-direction and no electric field (E = 0). An observer in frame S' moves relative to S along the x-axis. What does the observer in S' measure?"
  type: multiple-choice
  options:
    - "The same purely magnetic field B, since magnetic fields are Lorentz invariant"
    - "Both an electric field and a magnetic field, because E and B mix under Lorentz boosts"
    - "No fields at all, since moving observers see fields Doppler-shifted to zero"
    - "Only an electric field, since the magnetic field is fully converted to electric in the moving frame"
  answer: 1
  explanation: "E and B are not separately Lorentz invariant — they are components of a single antisymmetric tensor Fμν and mix under boosts. Under a boost along x, the transverse components transform as E'_y = γ(E_y − vB_z) and B'_y = γ(B_y + vE_z/c²), with similar expressions for z-components. Starting with E = 0 and B in the z-direction, a boost along x produces nonzero transverse E fields in S'. This mixing is the physical motivation for packaging E and B into a single tensor rather than treating them as independently meaningful fields."

- question: "In one inertial frame, a plane electromagnetic wave has E and B fields that are perpendicular to each other (E·B = 0). A physicist claims this orthogonality might not hold in other frames. Is this correct?"
  type: multiple-choice
  options:
    - "Yes — orthogonality of E and B is frame-dependent and can change under boosts"
    - "No — E·B is a Lorentz invariant; if it equals zero in one frame, it equals zero in all frames"
    - "Only if the wave is circularly polarized; linear polarization does not preserve orthogonality"
    - "Yes — the invariant is |B|² − |E|²/c², not E·B, so orthogonality can vary"
  answer: 1
  explanation: "The pseudoscalar F_μν F̃^μν ∝ E·B is a Lorentz invariant: every inertial observer computes the same value. If E·B = 0 in one frame, it is zero in all frames. The orthogonality of E and B for plane electromagnetic waves is a frame-independent fact, not an artifact of the particular frame used to describe them. Similarly, B² − E²/c² is the other independent invariant — if this is positive in one frame, it is positive in all frames."

- question: "The four Maxwell equations (two inhomogeneous, two homogeneous) can be expressed as exactly two tensor equations using the electromagnetic field tensor Fμν."
  type: true-false
  answer: true
  explanation: "In tensor form: the two inhomogeneous equations (Gauss's law and Ampère's law) become ∂_ν F^μν = μ₀ J^μ, and the two homogeneous equations (Faraday's law and ∇·B = 0) become ∂_[λ F_μν] = 0, equivalently ∂_ν F̃^μν = 0 with the dual tensor. Both are tensor equations that transform covariantly under Lorentz transformations — they hold in the same form in every inertial frame. This compactness is not merely aesthetic; it makes Lorentz covariance manifest and demonstrates that Maxwell's equations are already fully consistent with special relativity."

- question: "The electric field E and magnetic field B are independently Lorentz invariant: their individual magnitudes may change between frames, but the physical distinction between electric and magnetic is frame-independent."
  type: true-false
  answer: false
  explanation: "E and B are not independently invariant — they are observer-dependent projections of the single antisymmetric tensor Fμν and mix freely under Lorentz boosts. A purely electric field in one frame has both electric and magnetic components in a moving frame, and vice versa. There is no frame-independent division of Fμν into 'the electric part' and 'the magnetic part.' What are frame-independent are the two Lorentz scalar invariants: F_μν F^μν ∝ B² − E²/c² and F_μν F̃^μν ∝ E·B."

- question: "Why does the fact that E and B mix under Lorentz transformations motivate packaging them into a single tensor Fμν? What does the tensor formalism make possible that component-by-component transformation rules do not?"
  type: short-answer
  answer: "The mixing under boosts reveals that E and B are not independently meaningful objects — they are observer-dependent projections of a single underlying structure. Using separate transformation rules for E and B components is correct but opaque: it requires memorizing six transformation equations and gives no immediate insight into what is frame-independent. The tensor Fμν contains all six independent components and transforms via the single law F'^μν = Λ^μ_ρ Λ^ν_σ F^ρσ, which is manifestly Lorentz covariant. This makes several things possible: Maxwell's equations reduce to two compact tensor equations obviously covariant by form; Lorentz invariants like E·B and B² − E²/c² arise naturally as tensor contractions; and the field's intrinsic character can be classified frame-independently."
  explanation: "The tensor formalism is not just notation — it reveals the deep structure of electromagnetism as a relativistic field theory and is the direct foundation for the Lagrangian formulation and extension to quantum field theory."
```

## Explainer

From Lorentz transformations of E and B fields, you already know something striking: a purely electric field in one frame has both electric and magnetic components in a moving frame. This mixing is not approximate — it is exact — and it signals that E and B are not independently Lorentz-invariant objects. They are two aspects of a single underlying entity. The **electromagnetic field tensor** F^μν is the mathematical package that makes this explicit: it combines all six field components (three for E, three for B) into a single 4×4 antisymmetric tensor, so that Lorentz transformations act on the whole package via the same matrix law that applies to 4-vectors.

The entries of F^μν follow a standard convention: F^{0i} = E_i/c and F^{ij} = −ε^{ijk}B_k (with antisymmetry enforcing F^μν = −F^νμ, which kills all diagonal entries and leaves only 6 independent components). Under a Lorentz boost along the x-direction, the transformed tensor F'^μν = Λ^μ_ρ Λ^ν_σ F^ρσ reproduces exactly the field transformation rules you already know from the four-vector approach: E'_∥ = E_∥, B'_∥ = B_∥ (longitudinal components unchanged), and the transverse components mix through γ. The tensor formalism does not give new answers — it provides a systematic framework that makes **Lorentz covariance manifest**.

The payoff is in writing Maxwell's equations. In component form, the two inhomogeneous Maxwell equations (Gauss's law and Ampere's law) become ∂_ν F^μν = μ₀ J^μ, where J^μ = (cρ, **J**) is the 4-current. The two homogeneous equations (Faraday's law and ∇·B = 0) become ∂_[λ F_μν] = 0, or equivalently ∂_ν F̃^μν = 0 where F̃^μν = ½ε^μνρσ F_ρσ is the dual tensor. Both equations are manifestly covariant — they transform as tensor equations and hold identically in all inertial frames. Maxwell's equations, once a collection of four separate vector equations, are now two tensor equations of breathtaking compactness.

**Lorentz invariants** are the frame-independent quantities that every observer agrees on. For the electromagnetic field, there are exactly two independent scalar invariants: F_μν F^μν = 2(B² − E²/c²), proportional to B² − E²/c², and the pseudoscalar F_μν F̃^μν ∝ E·B. If E·B = 0 in one frame, it is zero in all frames; the orthogonality of E and B for plane waves is not a frame-dependent accident. If B² > E²/c² in one frame, a boost exists in which E vanishes entirely; if E² > c²B², a boost exists in which B vanishes. These invariants let you classify electromagnetic fields by their intrinsic character rather than their representation in any particular frame — the tensor formalism makes this classification both natural and rigorous.

