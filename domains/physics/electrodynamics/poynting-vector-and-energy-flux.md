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
stage: expert
status: draft
---

# Poynting Vector and Electromagnetic Energy Flow

## Core Idea
The Poynting vector S = (1/μ₀)(E × B) represents electromagnetic energy flux (power per unit area). Its integral ∮ S · dA gives power flow through a surface. Time-averaged Poynting vector magnitude equals wave intensity. This connects abstract Maxwell equations to observable electromagnetic energy transport.

## Questions

```yaml
- question: "A straight resistor carries steady DC current. In which direction does the Poynting vector point in the space just outside the resistor's surface?"
  type: multiple-choice
  options:
    - "Parallel to the wire, in the direction of conventional current flow"
    - "Radially inward, toward the wire's axis"
    - "Radially outward, away from the wire"
    - "Circumferentially around the wire, following the magnetic field lines"
  answer: 1
  explanation: "E⃗ points along the wire (driving the current) and B⃗ wraps around it (from Ampère's law). E⃗ × B⃗ therefore points radially inward. This means the energy that heats the resistor enters through its surface from the surrounding field — not by traveling down the wire from the battery. The battery maintains the fields; the fields carry the energy to the wire. Option A is the common misconception that energy 'flows along the wire.'"

- question: "For a sinusoidal electromagnetic plane wave with electric field amplitude E₀, what is the time-averaged intensity (time-averaged Poynting vector magnitude)?"
  type: multiple-choice
  options:
    - "E₀²/(μ₀c), the peak value of |S|"
    - "Zero, because S oscillates symmetrically around zero"
    - "E₀²/(2μ₀c), the average of the oscillating instantaneous power"
    - "2E₀²/(μ₀c), because power averages include both positive and negative half-cycles"
  answer: 2
  explanation: "The instantaneous Poynting vector oscillates at twice the wave frequency (since S ∝ E²). The time average of sin² or cos² is 1/2, so ⟨|S|⟩ = E₀²/(2μ₀c) = ε₀cE₀²/2. This time-averaged value is what photodetectors, radiometers, and skin actually respond to. Option A (the peak) fails because intensity is a time-averaged quantity; option B is wrong because S² is always nonnegative, so its average is not zero."

- question: "The Poynting vector S⃗ = (1/μ₀)(E⃗ × B⃗) can point in a direction different from the direction of wave propagation in some field configurations."
  type: true-false
  answer: true
  explanation: "S⃗ is determined purely by the local E⃗ and B⃗ fields, not by any predefined propagation direction. In complex situations — near antennas, inside waveguides, or around current-carrying conductors — E⃗ and B⃗ can be oriented so that S⃗ points sideways, inward, or in other directions relative to what an observer might call 'the wave direction.' The resistor example is the clearest case: energy flows radially inward even though there is no 'wave' propagating in that direction."

- question: "For a resistor carrying steady current, the energy that heats the resistor arrives by flowing longitudinally along the conducting wire from the battery terminals."
  type: true-false
  answer: false
  explanation: "The Poynting vector analysis shows that S⃗ points radially inward everywhere on the resistor's surface. The energy arrives from the surrounding electromagnetic field flowing through the surface of the wire, not by traveling along the conductor. The battery's role is to maintain the electric and magnetic fields; it is those fields that transport energy, not the conduction electrons moving slowly along the wire. This is one of the most counterintuitive results of Poynting's theorem, and it contradicts the everyday intuition that 'energy travels through wires.'"

- question: "Why does the Poynting vector for a current-carrying resistor point radially inward, and what does this reveal about how energy is delivered in electromagnetic systems?"
  type: short-answer
  answer: "E⃗ points along the wire (the field driving the current), and B⃗ circles around the wire (from Ampère's law). Their cross product E⃗ × B⃗ therefore points radially inward. This means the electromagnetic energy that heats the resistor enters from the surrounding field through the wire's surface — it does not flow along the wire from the battery. The battery's job is to sustain the fields, and the fields carry energy through space to wherever it is needed."
  explanation: "This result generalizes to all electromagnetic energy transport: it is the fields, not the charges, that are the primary carriers. Charges are the sources and sinks of fields, but energy propagates through the field itself. Poynting's theorem (∂u_em/∂t + ∇·S⃗ + J⃗·E⃗ = 0) is a local energy conservation law — energy neither appears nor disappears but flows continuously, with S⃗ tracking where it goes at every point in space."
```

## Explainer

From plane waves in vacuum you know that E⃗ and B⃗ are perpendicular to each other and to the direction of propagation, and that they oscillate in phase with the ratio |E|/|B| = c. An electromagnetic wave carries energy — that is obvious from sunlight warming your skin. But where exactly is that energy, and in which direction does it flow? The **Poynting vector** S⃗ = (1/μ₀)(E⃗ × B⃗) provides the precise, local, instantaneous answer: S⃗ at any point in space tells you the power per unit area (watts per square meter) flowing through that point, and its direction is the direction of energy transport.

The cross product E⃗ × B⃗ has a physical meaning that is consistent with everything you already know about plane waves. For a wave propagating in the +z direction, E⃗ points in x̂ and B⃗ points in ŷ (or some rotation thereof), so E⃗ × B⃗ points in ẑ — energy flows in the same direction as the wave's propagation. The magnitude |S⃗| = |E||B|/μ₀ = E²/( μ₀ c) = ε₀ c E². For a sinusoidal wave, E oscillates and S⃗ oscillates at twice the frequency, so the physically measurable quantity is the **time-averaged intensity** ⟨|S⃗|⟩ = E₀²/(2μ₀c) = ε₀ c E₀²/2, where E₀ is the amplitude. This is the quantity that meters, photodetectors, and your skin respond to.

The Poynting vector is not merely a bookkeeping tool — it is the statement that electromagnetic energy is a local quantity that flows through space, carried by the fields themselves. The full energy theorem (Poynting's theorem) follows directly from Maxwell's equations: −∂u_em/∂t = ∇·S⃗ + J⃗·E⃗, where u_em = (ε₀E² + B²/μ₀)/2 is the electromagnetic energy density. This is a continuity equation for energy: the rate of decrease of field energy in a volume equals the energy flowing out through its surface (∮ S⃗·dA⃗) plus the work done on charges (J⃗·E⃗). Energy is locally conserved — it neither appears nor disappears but flows continuously through the field.

A useful and slightly counterintuitive application: consider a resistor carrying steady current. E⃗ points along the wire (driving the current), and B⃗ wraps around it in circles (from the current). E⃗ × B⃗ therefore points radially *inward*, toward the axis of the wire. The Poynting vector says that the energy powering the resistor enters from the surrounding electromagnetic field flowing inward through the wire's surface — not traveling along the wire from the battery. The battery maintains the fields; the fields deliver energy to the wire everywhere simultaneously. This picture, though unfamiliar, is fully consistent with circuit theory and reveals that the fields, not the charges, are the primary carriers of energy in electromagnetism.
