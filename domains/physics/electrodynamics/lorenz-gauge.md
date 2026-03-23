---
id: lorenz-gauge
title: Lorenz Gauge
domain: physics
course: electrodynamics
prerequisites:
- id: gauge-transformations
  type: hard
- id: scalar-vector-potentials
  type: hard
builds-toward:
- retarded-potentials
- electromagnetic-field-tensor
tags:
- lorenz-gauge
- covariant
- relativistic
stage: expert
status: draft
---

# Lorenz Gauge

## Core Idea
The Lorenz gauge (∂φ/∂t + c²∇·A = 0) is manifestly covariant under Lorentz transformations, treating the scalar and vector potentials symmetrically. Both φ and A satisfy decoupled wave equations in this gauge, making it ideal for relativistic problems and for quantizing the electromagnetic field. The gauge condition elegantly encodes causality and charge conservation.

## Questions

```yaml
- question: "In the Lorenz gauge, the scalar potential φ at a field point depends on the charge distribution at what time?"
  type: multiple-choice
  options:
    - "The current time t — the potential responds instantaneously"
    - "The retarded time t − r/c, where r is the source-to-field distance"
    - "The advanced time t + r/c — the potential anticipates future sources"
    - "An averaged time, since the gauge condition mixes past and present"
  answer: 1
  explanation: "In the Lorenz gauge, both φ and A satisfy wave equations whose solutions are the retarded potentials: the field at point r and time t depends on sources at the retarded time t − r/c, meaning the information takes exactly r/c (light travel time) to propagate from source to field point. This makes causal structure manifest — cause precedes effect by the light-travel delay. Option A describes the Coulomb gauge, where φ satisfies an instantaneous Poisson equation (∇²φ = −ρ/ε₀) — an apparent instantaneous action that is nonetheless physically harmless because it cancels in the final E and B fields."

- question: "What is the key mathematical simplification that imposing the Lorenz gauge condition achieves in Maxwell's equations?"
  type: multiple-choice
  options:
    - "It eliminates the vector potential A, leaving only a scalar equation for φ"
    - "It reduces Maxwell's four equations to two"
    - "It decouples the equations for φ and A, each satisfying its own wave equation driven by its source"
    - "It transforms the equations to static form, valid only for slowly varying fields"
  answer: 2
  explanation: "Without a gauge condition, the equations for φ and A are coupled — changes in one affect the other. Substituting the Lorenz condition ∇·A + (1/c²)∂φ/∂t = 0 into Maxwell's equations yields two independent wave equations: □²φ = −ρ/ε₀ and □²A = −μ₀J. Each potential is driven only by its own source (charge density or current density), with no cross-coupling. This is a dramatic simplification that makes the equations amenable to the retarded Green's function technique and to quantization. By contrast, in the Coulomb gauge φ satisfies an instantaneous equation, and the equation for A contains a coupling term involving φ."

- question: "The Lorenz gauge condition ∂_μ A^μ = 0 takes the same form in all inertial reference frames — it is a Lorentz-covariant equation."
  type: true-false
  answer: true
  explanation: "This is the defining virtue of the Lorenz gauge. Written in four-vector notation as ∂_μ A^μ = 0, the condition is the four-divergence of the four-potential, which is a Lorentz scalar equation — it transforms properly under Lorentz boosts and has the same form in all inertial frames. This is in sharp contrast to the Coulomb gauge ∇·A = 0, which is a condition on only the spatial components of A and does not maintain the same form after a Lorentz boost (a boosted observer generally sees a non-zero ∇·A). The covariance of the Lorenz gauge makes it the natural choice for relativistic electrodynamics and quantum field theory."

- question: "In the Coulomb gauge, the scalar potential φ propagates causally at the speed of light, which makes the Coulomb gauge more suitable for problems involving radiation than the Lorenz gauge."
  type: true-false
  answer: false
  explanation: "This is backwards. In the Coulomb gauge, φ satisfies the instantaneous Poisson equation ∇²φ = −ρ/ε₀, meaning φ responds to charge density changes instantaneously across all space — an apparent violation of causality. In reality, causality is preserved because the instantaneous φ is exactly canceled by compensating terms in A when computing the physical fields E and B, but this cancellation is non-obvious and requires careful treatment. The Lorenz gauge is far superior for radiation and relativistic problems precisely because both φ and A satisfy wave equations that propagate at c, making the causal structure manifest rather than hidden."

- question: "Why does the Lorenz gauge make the causal structure of electrodynamics transparent, while the Coulomb gauge obscures it, even though both gauges describe identical physical fields?"
  type: short-answer
  answer: "In the Lorenz gauge, both φ and A satisfy wave equations and their solutions are retarded potentials — each depends on sources at the retarded time t − r/c, so the light-travel delay is explicit. In the Coulomb gauge, φ satisfies an instantaneous Poisson equation (φ responds everywhere at once to charge changes), but A contains compensating terms that, together with φ, always produce retarded E and B. The causality is real in both cases, but in the Coulomb gauge it is hidden in a cancellation between φ and A, whereas in the Lorenz gauge it is directly encoded in each potential individually."
  explanation: "Gauge freedom means many (φ, A) pairs describe the same E and B. Physical observables (E, B) are always causal — they propagate at c. But the potentials themselves are not directly observable, so they can behave non-causally (like Coulomb-gauge φ) without violating physics, as long as the final fields come out causal. The Lorenz gauge is the 'honest' representation: each potential individually reflects the causal structure. The Coulomb gauge is valid but involves a sort of accounting trick — instantaneous φ plus compensating A conspire to give causal fields. For this reason, the Lorenz gauge is preferred in relativistic and quantum-field-theory contexts where manifest covariance simplifies the analysis greatly."
```

## Explainer

From gauge transformations, you know that the physically observable fields E and B are unchanged when you shift the scalar potential φ → φ − ∂χ/∂t and the vector potential A → A + ∇χ for any smooth function χ. This freedom means there are infinitely many (φ, A) pairs that describe the same physical fields — the gauge is unspecified until you impose a constraint. Different choices of gauge constraint are mathematically equivalent in terms of physics, but certain choices drastically simplify the equations for certain problems. The **Lorenz gauge** is the choice that makes the potentials satisfy the most elegant wave equations.

The Lorenz condition is ∇·A + (1/c²)∂φ/∂t = 0. (Note: this gauge is named after Ludvig Lorenz, the Danish physicist, not Hendrik Lorentz of the Lorentz transformation — a historically persistent confusion.) What makes this condition special is its **Lorentz covariance**: in four-vector notation, the Lorenz condition is simply ∂_μ A^μ = 0, the four-divergence of the four-potential vanishes. This is a single covariant equation, symmetric in space and time, that transforms properly under Lorentz boosts. Both φ/c and A together form a four-vector A^μ = (φ/c, **A**), and the Lorenz condition treats all four components on equal footing.

When you substitute the Lorenz gauge condition into Maxwell's equations, the scalar and vector potentials **decouple**. Each satisfies its own wave equation driven by the appropriate source: □²φ = −ρ/ε₀ and □²**A** = −μ₀**J**, where □² = ∂²/∂t² /c² − ∇² is the d'Alembertian wave operator. This is a massive simplification — in other gauges (such as the Coulomb gauge ∇·**A** = 0), the equations for φ and **A** are coupled together and φ satisfies an instantaneous Poisson equation that appears to violate relativity (the instantaneous action is an artifact, not a real signal). In the Lorenz gauge, both equations are manifestly wave equations that propagate at c, encoding causality directly into the structure of the equations.

The solutions to these wave equations are the **retarded potentials** — φ and **A** at a field point at time t depend on sources at the retarded time t − r/c, where r is the distance from source to field point. The signal travels at the speed of light; cause precedes effect by exactly the light-travel time. This retardation is where the Lorenz gauge's encoding of causality becomes visible. In the Coulomb gauge, the same physical causality is present but hidden — the instantaneous φ is canceled by compensating terms in **A** to give retarded E and B. The Lorenz gauge makes the causal structure transparent, which is why it is the natural starting point for quantizing the electromagnetic field in quantum electrodynamics.
