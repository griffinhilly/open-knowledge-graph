---
id: conservation-laws-em
title: Conservation Laws in Electromagnetism
domain: physics
course: electrodynamics
prerequisites:
- id: maxwells-equations-differential-form
  type: hard
- id: multivariable-calculus
  type: hard
builds-toward:
- poynting-vector-and-energy-flux
tags:
- conservation
- charge
- energy-momentum
stage: formal-systems
status: validated
---

# Conservation Laws in Electromagnetism

## Core Idea
The continuity equation ∂ρ/∂t + ∇·J = 0 expresses charge conservation. Energy conservation emerges from the Poynting theorem. Momentum conservation relates to the Maxwell stress tensor. These conservation laws are implicit in Maxwell's equations and reflect fundamental symmetries.

## Questions

```yaml
- question: "The continuity equation ∂ρ/∂t + ∇·J = 0 is derived from Maxwell's equations. Which operation produces it?"
  type: multiple-choice
  options:
    - "Taking the curl of Faraday's law and applying vector identities"
    - "Taking the divergence of the Ampère-Maxwell equation and substituting Gauss's law"
    - "Integrating the Lorentz force law over a volume and applying the divergence theorem"
    - "Taking the gradient of the electric scalar potential and using superposition"
  answer: 1
  explanation: "The divergence of any curl is zero: ∇·(∇×B) = 0. Applying this to the Ampère-Maxwell equation ∇×B = μ₀J + μ₀ε₀∂E/∂t gives 0 = μ₀∇·J + μ₀ε₀∂(∇·E)/∂t. Substituting Gauss's law ∇·E = ρ/ε₀ yields ∂ρ/∂t + ∇·J = 0. The derivation is algebraic — no additional physics is assumed beyond what's already in Maxwell's equations."

- question: "A student adds 'charge conservation' to her list of fundamental postulates of classical electrodynamics alongside Maxwell's four equations. What is wrong with this?"
  type: multiple-choice
  options:
    - "Nothing — charge conservation is an independent experimental fact that must be stated separately"
    - "Charge conservation is a theorem that follows from Maxwell's equations; listing it as an independent postulate is redundant — it is already encoded in the equations"
    - "The student should include energy conservation but not charge conservation as an independent postulate"
    - "Charge conservation is only approximately valid at large scales and should not be listed as exact"
  answer: 1
  explanation: "The continuity equation — and therefore charge conservation — is derived directly from Maxwell's equations by taking the divergence of Ampère-Maxwell. It is not an extra assumption; it is a mathematical consequence of the equations already listed. Adding it as an independent postulate would be like listing 'the area of a square is s²' as an independent axiom of Euclidean geometry — it is already implied."

- question: "The Poynting vector S = (1/μ₀)(E × B) represents the direction and rate at which electromagnetic energy is flowing through space at each point."
  type: true-false
  answer: true
  explanation: "The Poynting theorem identifies S as the electromagnetic energy flux density: energy per unit time per unit area crossing a surface in the direction of S. Its appearance in the energy continuity equation ∂u/∂t + ∇·S = −J·E means that the rate of energy decrease in a volume equals the net energy flowing out through the surface (∇·S term) plus the power delivered to charges (J·E term)."

- question: "The Maxwell stress tensor is redundant once the Poynting vector is known, because the Poynting vector already fully accounts for electromagnetic momentum."
  type: true-false
  answer: false
  explanation: "The Poynting vector gives electromagnetic momentum density (g = S/c²), but momentum density is not the same as momentum flux. The Maxwell stress tensor describes how electromagnetic momentum flows across surfaces — the rate at which momentum is transferred through each area element. Both are needed for the complete momentum conservation law: T gives the flux that appears in ∂g/∂t = ∇·T − f. They are complementary, not redundant."

- question: "What does it mean physically that charge conservation is 'not a separate postulate' of electrodynamics but a theorem embedded in Maxwell's equations?"
  type: short-answer
  answer: "It means any field configuration satisfying Maxwell's equations automatically satisfies charge conservation — you cannot have Maxwell's equations hold in a region while charge is simultaneously created or destroyed there. The continuity equation is not an extra constraint imposed from outside; it falls out algebraically from the structure of the equations. This reflects the mathematical consistency of Maxwell's system: the equations were not assembled arbitrarily, and their structure encodes the fundamental symmetries (via Noether's theorem) that give rise to conservation laws. Charge conservation follows from global phase symmetry, which is built into the form of the equations."
  explanation: "This is the deep point about the relationship between symmetry, mathematical structure, and conservation laws. Maxwell's equations are not just four separate experimental summaries — they form a mathematically coherent system in which conservation laws are consequences, not inputs. The same pattern holds for energy (time-translation symmetry) and momentum (spatial-translation symmetry): these conservation laws are implicit in the structure of the equations, not layered on top of them."
```

## Explainer

From your work with Maxwell's equations in differential form, you know that ∇·E = ρ/ε₀ and ∇×B = μ₀J + μ₀ε₀∂E/∂t. Taking the divergence of the Ampère-Maxwell equation and using ∇·(∇×B) = 0, you get 0 = μ₀∇·J + μ₀ε₀∂(∇·E)/∂t = μ₀(∇·J + ∂ρ/∂t). This gives the **continuity equation** ∂ρ/∂t + ∇·J = 0 — not a separate postulate, but a theorem derived directly from Maxwell's equations. Physically, it says charge cannot be created or destroyed locally: any decrease in charge density at a point must be accompanied by a current flowing outward. Integrating over a volume and applying the divergence theorem yields dQ_enclosed/dt = −∮J·dA: the rate of change of enclosed charge equals the net current flowing out through the boundary.

The energy account starts by asking how fast the fields do work on charges. The power delivered to currents is P = ∫J·E dV. Using Maxwell's equations to rewrite J·E, you can show P = −∂u/∂t − ∇·S, where u = ½(ε₀E² + B²/μ₀) is the **electromagnetic energy density** and S = (1/μ₀)(E × B) is the **Poynting vector**. This is the Poynting theorem: the power delivered to matter comes from decreasing field energy and convergence of the energy flux S. The Poynting vector points in the direction electromagnetic energy is flowing, with units of W/m². From your multivariable calculus, you recognize this as a continuity equation for energy: the divergence theorem converts ∇·S into surface integrals, giving a total energy accounting statement for any volume.

Electromagnetic momentum is less intuitive but equally real. The fields themselves carry momentum density g = μ₀ε₀S = S/c². The **Maxwell stress tensor** T_ij encodes the flux of this momentum and the electromagnetic forces transmitted across surfaces. The momentum conservation law ∂g/∂t = ∇·T − f (where f is the force density on charges) parallels the charge and energy conservation statements exactly. Together, these three conservation laws — charge, energy, and momentum — are not additional assumptions layered onto Maxwell's equations. They are consequences embedded in the structure of the equations themselves, reflecting the deep symmetries of electromagnetism first identified by Noether's theorem: charge conservation follows from global phase symmetry, energy from time-translation symmetry, and momentum from spatial-translation symmetry.
