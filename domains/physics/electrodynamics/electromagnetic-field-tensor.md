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
stage: expert
status: draft
---

# The Electromagnetic Field Tensor

## Core Idea
The electromagnetic field tensor F^μν unifies the electric and magnetic fields into a single relativistic object transforming like a 4×4 antisymmetric tensor. This tensor encodes that E and B are not fundamental separate entities but different manifestations of the same field viewed from different reference frames. The tensor formalism reveals the deep connection between electricity and magnetism and provides a covariant framework for electrodynamics.

## Questions

```yaml
- question: "An observer in frame S sees a pure electric field pointing in the y-direction and no magnetic field. A second observer in frame S' moves along the x-axis relative to S. What does the second observer measure?"
  type: multiple-choice
  options:
    - "The same electric field and no magnetic field, since the electric field is perpendicular to the boost direction"
    - "A stronger electric field and no magnetic field, since boosts only affect components parallel to the motion"
    - "Both an electric field and a magnetic field, because the Lorentz boost mixes E and B components"
    - "No electric or magnetic field, since the field is transformed away in the new frame"
  answer: 2
  explanation: "When you boost between frames, the components of E and B that are perpendicular to the boost direction mix with each other. A pure electric field Ey in frame S transforms under a boost along x to give both E'y and B'z in S'. This is precisely what the field tensor formalism encodes: E and B are not separately invariant — they are components of F^μν, and a Lorentz boost mixes them just as it mixes space and time components. The 'mystery' of why motion creates magnetic fields from electric ones becomes automatic bookkeeping in the tensor language."

- question: "Maxwell's equations consist of four equations in classical notation. Why do they collapse to just two equations in the tensor formalism?"
  type: multiple-choice
  options:
    - "The tensor formalism drops two of Maxwell's equations as redundant"
    - "Two of Maxwell's equations (Gauss's law for magnetism and Faraday's law) are encoded in the Bianchi identity, and the other two in the source equation — each bundling two 3D equations into one 4D equation"
    - "The tensor formalism approximates Maxwell's equations to simplify calculation"
    - "Two equations become trivial (equal to zero) in the relativistic formulation"
  answer: 1
  explanation: "All four of Maxwell's equations are preserved — none are dropped. The Bianchi identity ∂_[μ F_{νρ}] = 0 encodes both ∇·B = 0 (no magnetic monopoles) and Faraday's law ∇×E = −∂B/∂t. The source equation ∂_μ F^μν = μ₀ J^ν encodes both Gauss's law (∇·E = ρ/ε₀) and the Ampere-Maxwell law. The collapse from four to two equations reflects the power of covariant notation: four 3D equations become two 4D equations, and their Lorentz covariance is built in rather than requiring separate verification."

- question: "The electric and magnetic fields are fundamentally distinct physical entities that happen to be related by Maxwell's equations."
  type: true-false
  answer: false
  explanation: "This is the key misconception the field tensor corrects. E and B are not separate fundamental entities — they are different manifestations of a single object, the electromagnetic field tensor F^μν, viewed from different reference frames. A pure electric field in one frame appears as a mix of electric and magnetic fields in another. What we call 'electric' and 'magnetic' are frame-dependent decompositions of F^μν, not independently existing fields. This is why electricity and magnetism are 'unified' in special relativity: they are two projections of one tensor."

- question: "The antisymmetric 4×4 tensor F^μν has exactly six independent components, matching the three components of E and the three of B."
  type: true-false
  answer: true
  explanation: "An antisymmetric n×n tensor has n(n−1)/2 independent components. For a 4×4 antisymmetric tensor: 4×3/2 = 6 independent components. Diagonal entries are all zero (since F^μμ = −F^μμ implies 0). The six off-diagonal independent entries encode exactly E_x, E_y, E_z, B_x, B_y, B_z. This is not a coincidence — the electromagnetic field in 4D spacetime has exactly six degrees of freedom, and antisymmetric 4×4 tensors have exactly six independent components. The tensor is the natural home for electromagnetic fields."

- question: "Two Lorentz-invariant scalars can be built from F^μν: F^μν F_{μν} ∝ (B²c² − E²) and ε^μνρσ F_{μν} F_{ρσ} ∝ E⃗·B⃗. Why does the existence of these scalars prove that the relative magnitudes and angles of E and B are frame-independent facts?"
  type: short-answer
  answer: "A Lorentz scalar has the same numerical value in every inertial frame — that is the definition of a scalar under Lorentz transformations. If F^μν F_{μν} = 2(B²c² − E²) is a scalar, then the quantity B²c² − E² is numerically identical in every frame. Therefore, if E² > B²c² in one frame, it is true in every frame. Similarly, if E⃗·B⃗ = 0 in one frame, the second scalar guarantees this holds in all frames. You cannot boost your way into a frame where two fields that were parallel become perpendicular, or vice versa. This is a direct consequence of the field tensor formalism: because E and B are components of a single tensor, Lorentz-invariant combinations of that tensor's components encode physical facts that no change of reference frame can alter."
  explanation: "This has practical consequences: a configuration where E⃗ and B⃗ are parallel (E⃗·B⃗ ≠ 0) is physically different from one where they are perpendicular (E⃗·B⃗ = 0), and no Lorentz boost can convert one to the other. The invariant scalars are the fingerprints of the electromagnetic field that survive all changes of observer."
```

## Explainer

From your prerequisite work on Lorentz covariance, you know that special relativity demands that physical laws take the same form in all inertial frames. You also know that while a four-vector like the four-momentum transforms simply under Lorentz transformations, the six components of the electromagnetic field — three for E⃗ and three for B⃗ — intermix when you boost between frames. A pure electric field in one frame has a magnetic component in another. This intermixing is a signal: E and B are not separately invariant objects. They are components of a single, more fundamental structure.

That structure is the **electromagnetic field tensor** F^μν, a 4×4 antisymmetric matrix (so F^μν = −F^νμ, and all diagonal entries are zero). Because it is antisymmetric, it has at most 4×3/2 = 6 independent components — exactly the number needed to encode the three components of E⃗ and the three of B⃗. The standard convention places the electric field components in the first row and column (F^{0i} = E^i/c) and the magnetic field components in the spatial block (F^{12} = B^z, etc.). Under a Lorentz boost along the x-axis, the tensor transforms via F'^μν = Λ^μ_α Λ^ν_β F^αβ, and the result is exactly the known mixing rules: E⃗ and B⃗ components parallel to the boost are unchanged, while perpendicular components combine with the boost factor γ. What looked like a puzzle — why does boosting create magnetic fields from electric ones? — becomes automatic bookkeeping.

The power of the tensor formalism is that Maxwell's equations collapse into just two compact covariant equations. The **Bianchi identity** ∂_[μ F_{νρ]} = 0 encodes two of Maxwell's four equations: ∇·B⃗ = 0 (no monopoles) and Faraday's law ∇×E⃗ = −∂B⃗/∂t. The **source equation** ∂_μ F^μν = μ₀ J^ν encodes the other two: Gauss's law and the Ampere-Maxwell law. Here J^ν = (cρ, J⃗) is the four-current you have seen from the Lorentz covariance treatment. Four equations in three dimensions become two equations in four-dimensional spacetime — and their Lorentz covariance is manifest, not something that has to be separately verified.

Two Lorentz-invariant scalars can be built from F^μν. The first, F^μν F_{μν} = 2(B²c² − E²), tells you that if E² > B²c² in one frame, it remains so in every frame. The second, ε^μνρσ F_{μν} F_{ρσ} ∝ E⃗·B⃗, tells you that the angle between E and B is a relativistic invariant. These scalars are useful in advanced work: a configuration with E⃗·B⃗ = 0 in one frame remains so in all frames. The tensor formalism is the entry point to gauge field theory, the language of all modern fundamental physics — in quantum electrodynamics, the photon field is literally the quantization of the four-potential A^μ from which F^μν derives.
