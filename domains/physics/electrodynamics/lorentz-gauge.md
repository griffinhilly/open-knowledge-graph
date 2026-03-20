---
id: lorentz-gauge
title: Lorentz Gauge and Coulomb Gauge
domain: physics
course: electrodynamics
prerequisites:
- id: gauge-transformations
  type: hard
- id: maxwells-equations-differential-form
  type: soft
builds-toward:
- retarded-potentials
- electromagnetic-waves-in-media
tags:
- gauge-choices
- lorentz
- coulomb
stage: formal-systems
status: draft
---

# Lorentz Gauge and Coulomb Gauge

## Core Idea
Gauge conditions select specific potentials to simplify calculations. The Lorentz gauge (∇·A + (1/c²)∂φ/∂t = 0) decouples the potential equations and manifests Lorentz covariance. The Coulomb gauge (∇·A = 0) simplifies static problems. Each gauge has advantages for different applications.

## Explainer

From gauge transformations, you know that the physically observable fields **E** and **B** do not uniquely determine the potentials φ and **A** — you can add gradients and time derivatives to the potentials without changing any observable. Specifically, the transformation φ → φ − ∂λ/∂t and **A** → **A** + ∇λ (for any scalar function λ) leaves **E** and **B** unchanged. This is gauge freedom: an infinite family of (φ, **A**) pairs all describe exactly the same physical situation. A **gauge condition** is a mathematical constraint that picks one representative from this family, chosen to make the equations easiest to solve.

The **Lorentz gauge** imposes ∇·**A** + (1/c²)∂φ/∂t = 0. Substituting this into Maxwell's equations produces a beautiful result: the equations for φ and **A** decouple completely and each satisfies an identical wave equation — □²φ = −ρ/ε₀ and □²**A** = −μ₀**J**, where □² = ∇² − (1/c²)∂²/∂t² is the **d'Alembertian** operator. The scalar and vector potentials are driven independently by their respective sources (charge density ρ and current density **J**). This decoupling makes the Lorentz gauge the natural choice for radiation problems, where both potentials are dynamically active. The condition is also **Lorentz covariant** — it preserves its form under Lorentz boosts — which makes it the gauge of choice in relativistic and quantum field theory treatments.

The **Coulomb gauge** (also called the **transverse gauge**) imposes ∇·**A** = 0 instead. This does not decouple the equations as cleanly: the scalar potential still satisfies the instantaneous Poisson equation ∇²φ = −ρ/ε₀, which seems to imply φ propagates instantaneously — faster than light. This apparent violation of relativity is illusory: φ alone is not observable; only the combination that produces **E** and **B** is physical, and that combination propagates causally. The Coulomb gauge trades relativistic transparency for computational convenience in problems with a clear static charge distribution: φ is found quickly from Poisson's equation, then the more complicated equation for **A** handles the radiation. It is popular in quantum optics and condensed matter, where non-relativistic approximations are appropriate.

Choosing a gauge is like choosing a coordinate system: the physics is the same regardless, but the algebra can be very different. The Lorentz gauge is the relativist's and radiator's tool — it keeps the equations symmetric and covariant. The Coulomb gauge is the electrostatics and quantum optics practitioner's tool — it separates the "near-field" Coulomb interaction from the radiation field with minimal computation. As you advance to retarded potentials and quantum electrodynamics, you will encounter both again and again, choosing between them based on which makes the physics most transparent for the problem at hand.
