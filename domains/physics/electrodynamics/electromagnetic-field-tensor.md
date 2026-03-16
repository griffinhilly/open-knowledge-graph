---
id: electromagnetic-field-tensor
title: The Electromagnetic Field Tensor
domain: physics
course: electrodynamics
prerequisites:
- id: lorentz-covariance-em
  type: hard
- id: special-relativity-postulates
  type: soft
builds-toward:
- lorentz-transformations-em-fields
tags:
- field-tensor
- four-vector
- relativity
stage: advanced
status: draft
---

# The Electromagnetic Field Tensor

## Core Idea
The electromagnetic field tensor F^μν unifies the electric and magnetic fields into a single relativistic object transforming like a 4×4 antisymmetric tensor. This tensor encodes that E and B are not fundamental separate entities but different manifestations of the same field viewed from different reference frames. The tensor formalism reveals the deep connection between electricity and magnetism and provides a covariant framework for electrodynamics.

## Explainer

From your prerequisite work on Lorentz covariance, you know that special relativity demands that physical laws take the same form in all inertial frames. You also know that while a four-vector like the four-momentum transforms simply under Lorentz transformations, the six components of the electromagnetic field — three for E⃗ and three for B⃗ — intermix when you boost between frames. A pure electric field in one frame has a magnetic component in another. This intermixing is a signal: E and B are not separately invariant objects. They are components of a single, more fundamental structure.

That structure is the **electromagnetic field tensor** F^μν, a 4×4 antisymmetric matrix (so F^μν = −F^νμ, and all diagonal entries are zero). Because it is antisymmetric, it has at most 4×3/2 = 6 independent components — exactly the number needed to encode the three components of E⃗ and the three of B⃗. The standard convention places the electric field components in the first row and column (F^{0i} = E^i/c) and the magnetic field components in the spatial block (F^{12} = B^z, etc.). Under a Lorentz boost along the x-axis, the tensor transforms via F'^μν = Λ^μ_α Λ^ν_β F^αβ, and the result is exactly the known mixing rules: E⃗ and B⃗ components parallel to the boost are unchanged, while perpendicular components combine with the boost factor γ. What looked like a puzzle — why does boosting create magnetic fields from electric ones? — becomes automatic bookkeeping.

The power of the tensor formalism is that Maxwell's equations collapse into just two compact covariant equations. The **Bianchi identity** ∂_[μ F_{νρ]} = 0 encodes two of Maxwell's four equations: ∇·B⃗ = 0 (no monopoles) and Faraday's law ∇×E⃗ = −∂B⃗/∂t. The **source equation** ∂_μ F^μν = μ₀ J^ν encodes the other two: Gauss's law and the Ampere-Maxwell law. Here J^ν = (cρ, J⃗) is the four-current you have seen from the Lorentz covariance treatment. Four equations in three dimensions become two equations in four-dimensional spacetime — and their Lorentz covariance is manifest, not something that has to be separately verified.

Two Lorentz-invariant scalars can be built from F^μν. The first, F^μν F_{μν} = 2(B²c² − E²), tells you that if E² > B²c² in one frame, it remains so in every frame. The second, ε^μνρσ F_{μν} F_{ρσ} ∝ E⃗·B⃗, tells you that the angle between E and B is a relativistic invariant. These scalars are useful in advanced work: a configuration with E⃗·B⃗ = 0 in one frame remains so in all frames. The tensor formalism is the entry point to gauge field theory, the language of all modern fundamental physics — in quantum electrodynamics, the photon field is literally the quantization of the four-potential A^μ from which F^μν derives.
