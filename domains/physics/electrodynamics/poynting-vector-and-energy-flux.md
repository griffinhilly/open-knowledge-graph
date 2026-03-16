---
id: poynting-vector-and-energy-flux
title: Poynting Vector and Electromagnetic Energy Flow
domain: physics
course: electrodynamics
prerequisites:
- id: plane-waves-in-vacuum
  type: hard
- id: maxwells-equations-differential-form
  type: soft
- id: divergence-theorem
  type: soft
builds-toward:
- maxwell-stress-tensor
- electromagnetic-waves-in-media
tags:
- energy-flow
- poynting
- intensity
stage: abstract-reasoning
status: draft
---

# Poynting Vector and Electromagnetic Energy Flow

## Core Idea
The Poynting vector S = (1/μ₀)(E × B) represents electromagnetic energy flux (power per unit area). Its integral ∮ S · dA gives power flow through a surface. Time-averaged Poynting vector magnitude equals wave intensity. This connects abstract Maxwell equations to observable electromagnetic energy transport.

## Explainer

From plane waves in vacuum you know that E⃗ and B⃗ are perpendicular to each other and to the direction of propagation, and that they oscillate in phase with the ratio |E|/|B| = c. An electromagnetic wave carries energy — that is obvious from sunlight warming your skin. But where exactly is that energy, and in which direction does it flow? The **Poynting vector** S⃗ = (1/μ₀)(E⃗ × B⃗) provides the precise, local, instantaneous answer: S⃗ at any point in space tells you the power per unit area (watts per square meter) flowing through that point, and its direction is the direction of energy transport.

The cross product E⃗ × B⃗ has a physical meaning that is consistent with everything you already know about plane waves. For a wave propagating in the +z direction, E⃗ points in x̂ and B⃗ points in ŷ (or some rotation thereof), so E⃗ × B⃗ points in ẑ — energy flows in the same direction as the wave's propagation. The magnitude |S⃗| = |E||B|/μ₀ = E²/( μ₀ c) = ε₀ c E². For a sinusoidal wave, E oscillates and S⃗ oscillates at twice the frequency, so the physically measurable quantity is the **time-averaged intensity** ⟨|S⃗|⟩ = E₀²/(2μ₀c) = ε₀ c E₀²/2, where E₀ is the amplitude. This is the quantity that meters, photodetectors, and your skin respond to.

The Poynting vector is not merely a bookkeeping tool — it is the statement that electromagnetic energy is a local quantity that flows through space, carried by the fields themselves. The full energy theorem (Poynting's theorem) follows directly from Maxwell's equations: −∂u_em/∂t = ∇·S⃗ + J⃗·E⃗, where u_em = (ε₀E² + B²/μ₀)/2 is the electromagnetic energy density. This is a continuity equation for energy: the rate of decrease of field energy in a volume equals the energy flowing out through its surface (∮ S⃗·dA⃗) plus the work done on charges (J⃗·E⃗). Energy is locally conserved — it neither appears nor disappears but flows continuously through the field.

A useful and slightly counterintuitive application: consider a resistor carrying steady current. E⃗ points along the wire (driving the current), and B⃗ wraps around it in circles (from the current). E⃗ × B⃗ therefore points radially *inward*, toward the axis of the wire. The Poynting vector says that the energy powering the resistor enters from the surrounding electromagnetic field flowing inward through the wire's surface — not traveling along the wire from the battery. The battery maintains the fields; the fields deliver energy to the wire everywhere simultaneously. This picture, though unfamiliar, is fully consistent with circuit theory and reveals that the fields, not the charges, are the primary carriers of energy in electromagnetism.
