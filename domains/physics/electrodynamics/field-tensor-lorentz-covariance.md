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
stage: advanced
status: draft
---

# Electromagnetic Field Tensor and Covariance

## Core Idea
The electromagnetic field tensor Fμν is a 4×4 antisymmetric tensor with entries proportional to E and B fields. Lorentz transformations act linearly on Fμν, ensuring that Maxwell's equations take identical form in all inertial frames. Invariants like E·B and E² - c²B² are frame-independent.

## Explainer

From Lorentz transformations of E and B fields, you already know something striking: a purely electric field in one frame has both electric and magnetic components in a moving frame. This mixing is not approximate — it is exact — and it signals that E and B are not independently Lorentz-invariant objects. They are two aspects of a single underlying entity. The **electromagnetic field tensor** F^μν is the mathematical package that makes this explicit: it combines all six field components (three for E, three for B) into a single 4×4 antisymmetric tensor, so that Lorentz transformations act on the whole package via the same matrix law that applies to 4-vectors.

The entries of F^μν follow a standard convention: F^{0i} = E_i/c and F^{ij} = −ε^{ijk}B_k (with antisymmetry enforcing F^μν = −F^νμ, which kills all diagonal entries and leaves only 6 independent components). Under a Lorentz boost along the x-direction, the transformed tensor F'^μν = Λ^μ_ρ Λ^ν_σ F^ρσ reproduces exactly the field transformation rules you already know from the four-vector approach: E'_∥ = E_∥, B'_∥ = B_∥ (longitudinal components unchanged), and the transverse components mix through γ. The tensor formalism does not give new answers — it provides a systematic framework that makes **Lorentz covariance manifest**.

The payoff is in writing Maxwell's equations. In component form, the two inhomogeneous Maxwell equations (Gauss's law and Ampere's law) become ∂_ν F^μν = μ₀ J^μ, where J^μ = (cρ, **J**) is the 4-current. The two homogeneous equations (Faraday's law and ∇·B = 0) become ∂_[λ F_μν] = 0, or equivalently ∂_ν F̃^μν = 0 where F̃^μν = ½ε^μνρσ F_ρσ is the dual tensor. Both equations are manifestly covariant — they transform as tensor equations and hold identically in all inertial frames. Maxwell's equations, once a collection of four separate vector equations, are now two tensor equations of breathtaking compactness.

**Lorentz invariants** are the frame-independent quantities that every observer agrees on. For the electromagnetic field, there are exactly two independent scalar invariants: F_μν F^μν = 2(B² − E²/c²), proportional to B² − E²/c², and the pseudoscalar F_μν F̃^μν ∝ E·B. If E·B = 0 in one frame, it is zero in all frames; the orthogonality of E and B for plane waves is not a frame-dependent accident. If B² > E²/c² in one frame, a boost exists in which E vanishes entirely; if E² > c²B², a boost exists in which B vanishes. These invariants let you classify electromagnetic fields by their intrinsic character rather than their representation in any particular frame — the tensor formalism makes this classification both natural and rigorous.

