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
status: validated
---

# Lorentz Gauge and Coulomb Gauge

## Core Idea
Gauge conditions select specific potentials to simplify calculations. The Lorentz gauge (∇·A + (1/c²)∂φ/∂t = 0) decouples the potential equations and manifests Lorentz covariance. The Coulomb gauge (∇·A = 0) simplifies static problems. Each gauge has advantages for different applications.

## Questions

```yaml
- question: "Under a gauge transformation, which of the following quantities changes?"
  type: multiple-choice
  options:
    - "The electric field E"
    - "The magnetic field B"
    - "The vector potential A"
    - "The current density J"
  answer: 2
  explanation: "Gauge transformations are defined precisely to leave E and B unchanged — they are the observable fields. The transformation A → A + ∇λ and φ → φ − ∂λ/∂t changes the potentials, but these changes cancel when computing E = −∇φ − ∂A/∂t and B = ∇×A. Source quantities (ρ, J) are physical and do not transform. Only the potentials (A and φ) change under a gauge transformation."

- question: "In the Coulomb gauge, the scalar potential φ satisfies the instantaneous Poisson equation, appearing to change everywhere at once when charge moves. Why doesn't this violate special relativity?"
  type: multiple-choice
  options:
    - "It does violate relativity; the Coulomb gauge is only valid for non-relativistic problems"
    - "The instantaneous propagation is real but the effect is too small to detect at ordinary energies"
    - "φ alone is not observable; only the combination that produces E and B is physical, and that propagates causally"
    - "In the Coulomb gauge, the vector potential A cancels the instantaneous term before any observable effect reaches a test charge"
  answer: 2
  explanation: "The observable quantity is E = −∇φ − ∂A/∂t, not φ alone. The unphysical instantaneous part of φ in the Coulomb gauge is exactly canceled by a corresponding term in ∂A/∂t, so the total electric field propagates causally. This is a crucial conceptual point: gauge potentials are mathematical tools with no direct physical meaning individually — only the combinations that give E and B are observable. The apparent 'action at a distance' in φ is a gauge artifact, not a physical signal."

- question: "The Lorentz gauge is preferred over the Coulomb gauge in relativistic treatments because the Lorentz condition preserves its form under Lorentz transformations."
  type: true-false
  answer: true
  explanation: "The Lorentz gauge condition ∇·A + (1/c²)∂φ/∂t = 0 is Lorentz covariant — it holds in all inertial frames related by Lorentz boosts. This makes it natural for relativistic field theory and quantum electrodynamics, where maintaining spacetime symmetry is essential. The Coulomb gauge condition ∇·A = 0 is not Lorentz covariant; boosting to a new frame breaks the condition and requires a re-gauging. The Lorentz gauge manifests the relativistic unity of space and time directly in the potential equations."

- question: "The Lorentz gauge condition completely fixes the gauge — once you impose ∇·A + (1/c²)∂φ/∂t = 0, there is a unique pair (φ, A) describing the physical situation."
  type: true-false
  answer: false
  explanation: "The Lorentz condition constrains gauge freedom but does not eliminate it. There remains residual gauge freedom: you can still perform additional gauge transformations with any scalar function λ that satisfies the wave equation □²λ = 0, since such λ preserves the Lorentz condition while changing the potentials. The Lorentz condition defines a family of gauges, not a single unique one. Complete gauge fixing — selecting a unique representative — requires additional constraints beyond the Lorentz condition."

- question: "Explain why choosing between the Lorentz gauge and the Coulomb gauge does not change the physical predictions of a problem, even though the equations look very different in each gauge."
  type: short-answer
  answer: "Both gauges describe the same physical fields E and B — the observable quantities that govern all measurable forces and radiation. The potentials φ and A are not directly observable; only ∇×A = B and −∇φ − ∂A/∂t = E are physical. Different gauge choices change the potentials but cannot change these combinations. Like choosing a coordinate system, a gauge choice affects only the algebra, not the physics."
  explanation: "This is the deep meaning of gauge freedom: an entire family of mathematically different (φ, A) pairs all describe exactly the same physics. The Lorentz gauge makes radiation problems algebraically cleaner by decoupling the potential equations symmetrically. The Coulomb gauge makes static charge problems simpler by reducing φ to a Poisson equation. In both cases, computing E and B gives identical results. Gauge choice is a calculational strategy, and the freedom to choose is a consequence of the fact that potentials carry redundant mathematical information."
```

## Explainer

From gauge transformations, you know that the physically observable fields **E** and **B** do not uniquely determine the potentials φ and **A** — you can add gradients and time derivatives to the potentials without changing any observable. Specifically, the transformation φ → φ − ∂λ/∂t and **A** → **A** + ∇λ (for any scalar function λ) leaves **E** and **B** unchanged. This is gauge freedom: an infinite family of (φ, **A**) pairs all describe exactly the same physical situation. A **gauge condition** is a mathematical constraint that picks one representative from this family, chosen to make the equations easiest to solve.

The **Lorentz gauge** imposes ∇·**A** + (1/c²)∂φ/∂t = 0. Substituting this into Maxwell's equations produces a beautiful result: the equations for φ and **A** decouple completely and each satisfies an identical wave equation — □²φ = −ρ/ε₀ and □²**A** = −μ₀**J**, where □² = ∇² − (1/c²)∂²/∂t² is the **d'Alembertian** operator. The scalar and vector potentials are driven independently by their respective sources (charge density ρ and current density **J**). This decoupling makes the Lorentz gauge the natural choice for radiation problems, where both potentials are dynamically active. The condition is also **Lorentz covariant** — it preserves its form under Lorentz boosts — which makes it the gauge of choice in relativistic and quantum field theory treatments.

The **Coulomb gauge** (also called the **transverse gauge**) imposes ∇·**A** = 0 instead. This does not decouple the equations as cleanly: the scalar potential still satisfies the instantaneous Poisson equation ∇²φ = −ρ/ε₀, which seems to imply φ propagates instantaneously — faster than light. This apparent violation of relativity is illusory: φ alone is not observable; only the combination that produces **E** and **B** is physical, and that combination propagates causally. The Coulomb gauge trades relativistic transparency for computational convenience in problems with a clear static charge distribution: φ is found quickly from Poisson's equation, then the more complicated equation for **A** handles the radiation. It is popular in quantum optics and condensed matter, where non-relativistic approximations are appropriate.

Choosing a gauge is like choosing a coordinate system: the physics is the same regardless, but the algebra can be very different. The Lorentz gauge is the relativist's and radiator's tool — it keeps the equations symmetric and covariant. The Coulomb gauge is the electrostatics and quantum optics practitioner's tool — it separates the "near-field" Coulomb interaction from the radiation field with minimal computation. As you advance to retarded potentials and quantum electrodynamics, you will encounter both again and again, choosing between them based on which makes the physics most transparent for the problem at hand.
