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

## Explainer

From your prerequisite on energy stored in fields, you know that assembling a charge distribution or building up a current in an inductor requires work, and that work is stored as potential energy in the electric or magnetic field itself. This topic extends that idea to its full dynamical form: when fields change in time — as they do whenever charges move or currents vary — energy flows through space from one region to another. The question is: where does the energy go, and how do we track it?

The **Poynting theorem** answers this precisely. Starting from Maxwell's equations, one can derive a local conservation law for energy. It states that the rate at which electromagnetic energy decreases in a volume equals the rate at which work is done on charges inside *plus* the rate at which energy flows out through the bounding surface. The energy flux is carried by the **Poynting vector** S = (1/μ₀)(E × B), which has units of watts per square meter — it is literally the energy streaming through a unit area per unit time. The **energy density** of the combined electromagnetic field is u = ε₀E²/2 + B²/(2μ₀), the sum of the electric and magnetic contributions you already know.

Written as a continuity equation, Poynting's theorem says ∂u/∂t + ∇·S = −J·E. The right side is the rate of work done by the field on free currents (positive J·E means the field is accelerating charges and doing positive work, which depletes field energy). The divergence term ∇·S describes how energy spreads out: positive divergence means more energy is flowing out of a small volume than in, so the local field energy decreases. This is exactly the same mathematical structure as charge conservation (∂ρ/∂t + ∇·J = 0), but for energy rather than charge.

A striking consequence is that energy in a circuit does not travel through the wires — it travels through the electromagnetic field in the surrounding space. In a resistor carrying current, the Poynting vector points radially inward from the surrounding field into the resistor, exactly accounting for the Joule heating rate. This counterintuitive picture is correct: the wires guide the boundary conditions for the field, but the energy itself flows through the space outside. This field-centric view of energy becomes indispensable when analyzing radiation, where energy escapes to infinity as electromagnetic waves carry it away permanently.
