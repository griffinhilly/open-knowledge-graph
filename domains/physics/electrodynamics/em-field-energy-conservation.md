---
id: em-field-energy-conservation
title: Electromagnetic Field Energy and Conservation
domain: physics
course: electrodynamics
prerequisites:
- id: energy-stored-in-fields
  type: hard
- id: maxwell-equations-integral-form
  type: hard
builds-toward:
- poynting-theorem-conservation-law
- em-field-momentum-density
tags:
- energy-density
- field-energy
- energy-flow
stage: advanced
status: draft
---

# Electromagnetic Field Energy and Conservation

## Core Idea
The energy density u = (ε₀E² + B²/μ₀)/2 stored in electromagnetic fields represents energy localized in space. Conservation of total energy requires the Poynting theorem relating energy flow to the rate of work on charges.

## Questions

```yaml
- question: "In a simple DC circuit with a wire and a resistor, how does the electrical energy actually reach the resistor?"
  type: multiple-choice
  options:
    - "Energy flows through the wire as drifting electrons carry kinetic energy to the resistor"
    - "Energy flows through the electromagnetic field in the space surrounding the wire, not through the wire itself"
    - "Energy is carried by the magnetic field alone, since no electric field exists outside a conductor"
    - "Energy diffuses through the wire lattice via thermal vibrations"
  answer: 1
  explanation: "The Poynting vector S = (1/μ₀)(E × B) points radially inward toward a resistor carrying current, meaning electromagnetic energy flows through the surrounding space into the resistor — exactly accounting for the Joule heating rate. The wires enforce the boundary conditions for the fields, but the energy itself travels through the field outside the wire. Option A describes the common misconception; electron drift velocity is far too slow to account for the near-instantaneous energy delivery in circuits."

- question: "What does the divergence ∇·S of the Poynting vector represent in a small volume?"
  type: multiple-choice
  options:
    - "The rate of work done by the electromagnetic field on free charges inside the volume"
    - "The magnetic energy density stored at that point"
    - "The net rate at which electromagnetic energy is flowing out of that volume"
    - "The total electromagnetic energy density at that point"
  answer: 2
  explanation: "The Poynting theorem in differential form is ∂u/∂t + ∇·S = −J·E. The divergence ∇·S is the net outward energy flux per unit volume — if ∇·S > 0, more energy is flowing out of the region than in, so the local field energy decreases. Option A describes −J·E (the work term), not the divergence. Option D describes u = ε₀E²/2 + B²/(2μ₀), the energy density itself."

- question: "The total electromagnetic energy density at a point in free space is simply the electric energy density ε₀E²/2, since magnetic fields do not store energy."
  type: true-false
  answer: false
  explanation: "Both electric and magnetic fields store energy. The total electromagnetic energy density is u = ε₀E²/2 + B²/(2μ₀) — the sum of the electric and magnetic contributions. This is directly analogous to how both capacitors and inductors store energy in circuits. Ignoring the magnetic term would give incorrect results for any situation involving time-varying fields or propagating waves."

- question: "The Poynting vector for a current-carrying resistor points radially inward from the surrounding space, and its surface integral over the resistor's surface exactly equals the Joule heating rate I²R."
  type: true-false
  answer: true
  explanation: "This is the striking consequence of Poynting's theorem applied to a resistor. A current-carrying wire has an axial E field inside (driving the current) and a circumferential B field outside (from the current). Their cross product S = (1/μ₀)E × B points radially inward toward the wire. Integrating S over the surface gives exactly the Joule heating rate — confirming that energy enters the resistor from the surrounding field, not from charge kinetic energy."

- question: "Why does Poynting's theorem have the same mathematical structure as the charge continuity equation ∂ρ/∂t + ∇·J = 0, and what physical principle does this structural similarity express?"
  type: short-answer
  answer: "Both are local conservation laws expressed as continuity equations. In Poynting's theorem (∂u/∂t + ∇·S = −J·E), u is the energy density, S is the energy flux, and −J·E is the source/sink term (work done by fields on charges). In charge continuity, ρ is the charge density, J is the charge flux, and the right side is zero (charge is strictly conserved). The structural parallel means both express the same idea: a conserved quantity can only change locally if it flows in or out (or is created/destroyed by a local source). For charge, there are no sources; for electromagnetic energy, the source term J·E accounts for the conversion between field energy and mechanical/thermal energy of charges."
  explanation: "This structural similarity reveals that Poynting's theorem is not just a useful formula — it is a local conservation law, meaning energy cannot teleport; it must flow continuously through space. The continuity equation form applies to any conserved quantity (charge, energy, momentum, probability in quantum mechanics). Recognizing this structure lets you interpret ∂u/∂t as the rate of change of energy stored locally, ∇·S as the divergence of the energy current, and J·E as the coupling between electromagnetic energy and matter."
```

## Explainer

From your prerequisite on energy stored in fields, you know that assembling a charge distribution or building up a current in an inductor requires work, and that work is stored as potential energy in the electric or magnetic field itself. This topic extends that idea to its full dynamical form: when fields change in time — as they do whenever charges move or currents vary — energy flows through space from one region to another. The question is: where does the energy go, and how do we track it?

The **Poynting theorem** answers this precisely. Starting from Maxwell's equations, one can derive a local conservation law for energy. It states that the rate at which electromagnetic energy decreases in a volume equals the rate at which work is done on charges inside *plus* the rate at which energy flows out through the bounding surface. The energy flux is carried by the **Poynting vector** S = (1/μ₀)(E × B), which has units of watts per square meter — it is literally the energy streaming through a unit area per unit time. The **energy density** of the combined electromagnetic field is u = ε₀E²/2 + B²/(2μ₀), the sum of the electric and magnetic contributions you already know.

Written as a continuity equation, Poynting's theorem says ∂u/∂t + ∇·S = −J·E. The right side is the rate of work done by the field on free currents (positive J·E means the field is accelerating charges and doing positive work, which depletes field energy). The divergence term ∇·S describes how energy spreads out: positive divergence means more energy is flowing out of a small volume than in, so the local field energy decreases. This is exactly the same mathematical structure as charge conservation (∂ρ/∂t + ∇·J = 0), but for energy rather than charge.

A striking consequence is that energy in a circuit does not travel through the wires — it travels through the electromagnetic field in the surrounding space. In a resistor carrying current, the Poynting vector points radially inward from the surrounding field into the resistor, exactly accounting for the Joule heating rate. This counterintuitive picture is correct: the wires guide the boundary conditions for the field, but the energy itself flows through the space outside. This field-centric view of energy becomes indispensable when analyzing radiation, where energy escapes to infinity as electromagnetic waves carry it away permanently.
