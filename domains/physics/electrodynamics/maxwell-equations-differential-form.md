---
id: maxwell-equations-differential-form
title: Maxwell's Equations in Differential Form
domain: physics
course: electrodynamics
prerequisites:
- id: maxwell-equations-integral-form
  type: hard
- id: partial-derivatives
  type: hard
- id: curl-and-divergence
  type: hard
- id: curl-divergence
  type: hard
- id: curl-and-divergence-operators
  type: hard
builds-toward:
- electromagnetic-wave-equation
- boundary-value-problems-electrostatics
tags:
- maxwell-equations
- pdes
- differential-forms
stage: expert
status: validated
---

# Maxwell's Equations in Differential Form

## Core Idea
The differential (local) forms of Maxwell's equations describe how electric and magnetic fields change at each point in space and time. Using divergence and curl operators, these four equations express the same physics as the integral forms but as partial differential equations. The differential forms are essential for deriving wave equations and solving problems computationally.

## How It's Best Learned
Derive the differential forms from the integral versions using the divergence and Stokes theorems. Practice interpreting each equation physically: ∇·E relates to local charge density, ∇·B = 0 reflects no monopoles, ∇×E = -∂B/∂t couples electric and magnetic fields, and ∇×B involves current and displacement current.

## Common Misconceptions
- Thinking divergence and curl are abstract; remember they describe how fields spread out and circulate.
- Applying these equations outside their domain of validity (classical limit, non-relativistic speeds).
- Neglecting boundary conditions, which are essential for solving the resulting differential equations.

## Questions

```yaml
- question: "Maxwell added the displacement current term (μ₀ε₀∂E/∂t) to Ampere's law. What would go wrong without this term?"
  type: multiple-choice
  options:
    - "Gauss's law would fail — ∇·E would no longer equal ρ/ε₀ in static situations"
    - "Faraday's law would predict that changing B fields create no electric field in vacuum"
    - "The equations would be internally inconsistent — charge conservation would be violated, and self-sustaining electromagnetic waves in vacuum could not exist"
    - "The magnetic Gauss's law would require ∇·B ≠ 0, implying magnetic monopoles"
  answer: 2
  explanation: "Without the displacement current, Ampere's law (∇×B = μ₀J) is inconsistent with charge conservation: taking the divergence of both sides gives 0 = μ₀∇·J, which requires ∇·J = 0 always — but this contradicts the continuity equation ∂ρ/∂t + ∇·J = 0 whenever charge density changes. Maxwell's fix (adding μ₀ε₀∂E/∂t) restores consistency. Additionally, without this term, taking ∇×(∇×E) and substituting does not yield a wave equation — electromagnetic waves in vacuum are impossible without the displacement current."

- question: "The electromagnetic wave equation (∇²E = μ₀ε₀∂²E/∂t²) is derived by manipulating Maxwell's equations. Why is this derivation impossible using only the integral forms?"
  type: multiple-choice
  options:
    - "The integral forms apply only to static fields and break down in the wave regime"
    - "The derivation requires taking the curl of a field equation, which is a point-wise operation that cannot be applied to integrals over finite surfaces or loops"
    - "The integral forms do not include the displacement current term that Maxwell added"
    - "Stokes's theorem only converts curl integrals in one direction — from differential to integral, not the reverse"
  answer: 1
  explanation: "The wave equation derivation requires applying ∇× to Faraday's law (itself already a curl equation), yielding a second-order differential equation. The curl operator acts point-wise on vector fields — you cannot take the curl of a circulation integral over a finite loop, because the loop integral is a single number, not a vector field. The differential forms express each law as a local equation valid at every point in space, which is exactly what is needed to apply vector differential operators and derive PDEs."

- question: "∇·B = 0 everywhere in space, reflecting the fact that magnetic field lines always form closed loops and no magnetic monopoles exist."
  type: true-false
  answer: true
  explanation: "This is the magnetic analogue of Gauss's law. Unlike ∇·E = ρ/ε₀ (which can be nonzero where charges exist), ∇·B = 0 holds everywhere without exception. Physically, this means B field lines have no sources or sinks — they never begin or end, only form closed loops. The existence of a magnetic monopole would require ∇·B ≠ 0 at its location, which has never been observed. This equation is one of the four pillars of classical electromagnetism."

- question: "The differential form ∇·E = ρ/ε₀ means that the electric field E has nonzero divergence everywhere in space, not just near charges."
  type: true-false
  answer: false
  explanation: "∇·E = ρ/ε₀ means divergence equals charge density divided by ε₀. In regions of space where no charge is present (ρ = 0), ∇·E = 0 — the field has no local sources or sinks and passes through uniformly. Only where charge exists does E diverge: positive charges are sources (field lines radiate outward) and negative charges are sinks (field lines converge inward). This is a point-wise, local equation — it describes the field behavior at each individual point, not over any region."

- question: "What is the physical significance of Maxwell's displacement current term (μ₀ε₀∂E/∂t) in Ampere's law, and why did Maxwell add it?"
  type: short-answer
  answer: "The displacement current term accounts for the fact that a changing electric field generates a magnetic field, even in the absence of actual current flow. Maxwell added it because without it, Ampere's law (∇×B = μ₀J) is inconsistent with charge conservation: taking the divergence gives ∇·J = 0 always, contradicting the continuity equation when charges accumulate or disperse. By adding μ₀ε₀∂E/∂t, Maxwell restored mathematical consistency. The deeper consequence was that this term — together with Faraday's law — allows E and B to sustain each other in vacuum: a changing B produces E (Faraday), and a changing E produces B (Maxwell's addition), enabling self-propagating electromagnetic waves at speed c = 1/√(μ₀ε₀). This unified optics and electromagnetism."
  explanation: "The displacement current is arguably the most consequential single addition in the history of classical physics. It was added on theoretical grounds (consistency) and immediately predicted electromagnetic waves, which were later confirmed experimentally by Hertz. Without it, Maxwell's equations would describe only quasi-static fields and could not account for light."
```

## Explainer

You know the integral forms of Maxwell's equations: Gauss's law relates total electric flux through a closed surface to enclosed charge; Ampere-Maxwell relates B's circulation around a loop to enclosed current plus displacement current; Faraday's law relates E's circulation to the rate of change of magnetic flux; and the magnetic Gauss's law says no net magnetic flux ever exits a closed surface. The differential forms say the same things, but at every individual point in space rather than averaged over finite regions — a far more powerful perspective for deriving new results and solving problems computationally.

The translation uses two theorems from vector calculus you've studied: the divergence theorem (converts a surface flux integral into a volume integral of ∇·F) and Stokes's theorem (converts a circulation integral into a surface integral of ∇×F). Applying these to the integral forms yields the four differential equations. **∇·E = ρ/ε₀** (Gauss): the divergence of E at a point equals the charge density there. Where there is positive charge, E field lines diverge outward; where negative charge, they converge inward. No charge means no net divergence — E lines pass straight through. **∇·B = 0** (magnetic Gauss): B always has zero divergence everywhere — B field lines form closed loops, never beginning or ending.

**∇×E = −∂B/∂t** (Faraday): the curl of E at a point equals the negative rate of change of B at that point. Where B is increasing in time, E circulates around it — this is what drives current in a transformer secondary coil. **∇×B = μ₀J + μ₀ε₀∂E/∂t** (Ampere-Maxwell): B circulates around regions of current density J, and also around regions where E is changing in time. That last term — the **displacement current** μ₀ε₀∂E/∂t that Maxwell added — is what makes the four equations consistent and predicts electromagnetic waves even in vacuum.

The differential forms become essential when deriving the electromagnetic wave equation. Take the curl of Faraday's law: ∇×(∇×E) = −∂(∇×B)/∂t. Substitute Ampere-Maxwell (with J = 0 in vacuum): ∇×(∇×E) = −μ₀ε₀∂²E/∂t². Apply the vector identity ∇×(∇×E) = ∇(∇·E) − ∇²E, and use ∇·E = 0 in free space: the result is ∇²E = μ₀ε₀∂²E/∂t², the wave equation, with propagation speed c = 1/√(μ₀ε₀). This derivation — entirely impossible without the differential forms — is one of the great results in physics. It showed that light is an electromagnetic wave, unifying optics and electromagnetism.
