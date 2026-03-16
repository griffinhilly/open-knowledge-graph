---
id: covariant-em
title: Electromagnetic Field Tensor and Special Relativity
domain: physics
course: electrodynamics
prerequisites:
- id: maxwells-equations-differential-form
  type: hard
- id: lorentz-gauge
  type: soft
tags:
- relativity
- four-vectors
- covariance
stage: abstract-reasoning
status: draft
---

# Electromagnetic Field Tensor and Special Relativity

## Core Idea
In special relativity, E and B unify into the electromagnetic field tensor F^μν (rank-2 4-tensor). Lorentz transformations show E and B fields mix: what is purely electric to one observer appears electric plus magnetic to a moving observer. Maxwell's equations take covariant form ∂_μF^μν = J^ν, manifesting relativistic consistency and deep spacetime structure.

## Explainer

You have mastered Maxwell's equations in differential form and worked with gauge potentials. Now comes the payoff of unification: when you embed electromagnetism in special relativity, the six field components (three for E, three for B) are not independent objects — they are components of a single geometrical object in spacetime. The **electromagnetic field tensor** F^μν is a rank-2 antisymmetric 4-tensor: a 4×4 matrix whose off-diagonal entries encode all six field components. The upper triangle holds the magnetic field components (B_x, B_y, B_z) and the mixed time-space entries hold the electric field components (E_x/c, E_y/c, E_z/c). The antisymmetry F^μν = −F^νμ ensures the diagonal vanishes and reduces the 16 entries to 6 independent ones.

The physical consequence is striking: **E and B are not separately observer-independent quantities**. When you apply a Lorentz boost to F^μν, the transformed tensor mixes E and B components in a precise way. A stationary charge creates a purely electric Coulomb field in its rest frame. To a moving observer, that same charge is moving — it constitutes a current — and a current produces a magnetic field. The "magnetic force" you feel on a test charge moving past a wire is, in the wire's rest frame, a purely electrostatic Coulomb force arising from charge density imbalances due to length contraction. There is no physical distinction between electric and magnetic; there is only the electromagnetic field tensor viewed from different reference frames. This is one of the deepest unifications in physics.

Maxwell's equations also simplify dramatically in this language. The four vector equations collapse into just two tensor equations: ∂_μF^μν = μ₀J^ν encodes Gauss's law and Ampère's law (the equations sourced by charge and current), while ∂_μ(½ε^μναβF_αβ) = 0, or equivalently ∂_[μF_νλ] = 0, encodes Faraday's law and Gauss's law for magnetism (the source-free equations). The Lorentz gauge condition you learned previously takes the manifestly covariant form ∂_μA^μ = 0, and the wave equation for the four-potential becomes simply ∂_μ∂^μ A^ν = μ₀J^ν — a single 4-vector equation replacing four scalar equations.

The deeper lesson is about **covariance**: an equation is Lorentz-covariant if it maintains the same form in all inertial frames. Maxwell's equations in tensor form are manifestly covariant by construction — each side transforms as the same type of tensor object. This is not just aesthetics; it is a proof that electromagnetism is fundamentally relativistic. Maxwell actually published his equations in 1865, forty years before Einstein, yet they were already consistent with special relativity. The formulation you are learning now makes that consistency transparent and provides the geometric language needed for general relativity, quantum field theory, and advanced gravitational physics.
