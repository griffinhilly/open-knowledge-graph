---
id: em-field-momentum-density
title: Momentum Density in Electromagnetic Fields
domain: physics
course: electrodynamics
prerequisites:
- id: em-field-energy-conservation
  type: hard
- id: poynting-vector-and-energy-flux
  type: hard
builds-toward:
- em-angular-momentum-density
- maxwell-stress-tensor-forces
tags:
- momentum-density
- radiation-pressure
- field-momentum
stage: expert
status: validated
---

# Momentum Density in Electromagnetic Fields

## Core Idea
Electromagnetic fields carry momentum density g = S/c² = (ε₀/c²)(E × B), where S is the Poynting vector. This momentum transfers to matter in the form of radiation pressure, with magnitude equal to energy density divided by c².

## Questions

```yaml
- question: "A laser beam strikes an absorbing surface and exerts a measurable force on it. According to the concept of EM field momentum, what is the physical origin of this force?"
  type: multiple-choice
  options:
    - "The electric field directly repels free electrons in the surface outward"
    - "The magnetic Lorentz force on charges set in motion by the wave's electric field pushes the surface forward along the propagation direction"
    - "Radiation pressure is purely a quantum effect with no classical explanation"
    - "The oscillating electric field creates eddy currents whose heating expands the surface"
  answer: 1
  explanation: "The mechanism is classical and purely Lorentz-force based. The wave's electric field accelerates charges in the surface. Those moving charges then experience a magnetic Lorentz force from the wave's B field, directed along the propagation direction. This forward push is the transfer of field momentum to matter. Option C is wrong: radiation pressure is a classical result, fully derivable from Maxwell's equations and confirmed quantum mechanically later."

- question: "Compared to a perfect absorber, the radiation pressure on a perfect reflector for the same incident wave is:"
  type: multiple-choice
  options:
    - "The same — the wave's energy is unchanged upon reflection, so the pressure is unchanged"
    - "Half as much — only the incoming wave contributes, not the reflected one"
    - "Twice as much — the field momentum reverses direction, doubling the impulse delivered to the surface"
    - "Four times as much — both the electric and magnetic field momenta must be counted separately"
  answer: 2
  explanation: "Force equals rate of momentum transfer. For an absorber, the incoming field momentum is fully transferred to the surface. For a reflector, the incoming momentum is transferred AND the reflected wave carries momentum in the opposite direction — so the surface provides that momentum too. The total change in field momentum is 2|g| per unit time, giving twice the force. The same principle applies in mechanics: catching a ball and throwing it back imparts twice the impulse of just catching it."

- question: "Momentum in electromagnetic fields is a quantum mechanical effect that has no place in classical electrodynamics."
  type: true-false
  answer: false
  explanation: "EM field momentum is a purely classical result, derivable from Maxwell's equations and Newton's laws of momentum conservation. The momentum density g = ε₀(E × B) = S/c² follows from requiring that momentum be conserved when light interacts with charged matter. Quantum mechanics later confirmed this result at the photon level (p = E/c for massless photons), but the classical field theory already anticipates it. The two are consistent precisely because the photon picture is the quantization of the classical field."

- question: "The ratio of momentum density to energy density in an electromagnetic wave equals 1/c."
  type: true-false
  answer: true
  explanation: "For a plane wave, energy density u = ε₀E² (SI units) and Poynting vector S = cu (since the wave travels at c). Momentum density g = S/c² = u/c. So g/u = 1/c. This is exactly the massless-particle relation p = E/c, which for photons gives p = hf/c = h/λ. The classical field result and the quantum photon result are consistent — field momentum per unit volume equals the quantum-mechanical count of photon momenta."

- question: "Why does a perfect reflector experience twice the radiation pressure of a perfect absorber, even though it absorbs no energy from the incident wave?"
  type: short-answer
  answer: "Radiation pressure results from the transfer of field momentum to the surface. For a perfect absorber, all the incoming field momentum (directed forward) is transferred to the surface. For a perfect reflector, the surface must supply the incoming forward momentum to the wave upon reflection AND reverse its direction — effectively transferring 2|g| of momentum to itself. The force on the surface is the rate of momentum transfer, which is doubled for a reflector."
  explanation: "The key is that force depends on the change in momentum of the field, not the change in energy. A perfect reflector does zero net work on the wave (the wave's energy is conserved), but it completely reverses the wave's momentum. By Newton's third law, the surface receives a force equal to twice the incoming momentum flux. An analogy: catching a rubber ball and throwing it back imparts twice the impulse of catching it and holding it still."
```

## Explainer

You've already established from the Poynting vector that electromagnetic fields carry energy, with energy flux S = (1/μ₀)(E × B) measured in watts per square meter. The deeper and perhaps more surprising result is that fields also carry **momentum**. This isn't obvious classically — momentum seems like a property of matter — but it follows inescapably from the requirement that momentum be conserved when light interacts with matter.

Here's the argument: when an electromagnetic wave hits an absorbing surface and the charges in the surface begin to move, the Lorentz force F = q(E + v×B) has two parts. The electric field accelerates the charges, and then the magnetic field exerts a force on those moving charges. This secondary magnetic force is directed along the propagation direction of the wave — it pushes the surface forward. Something must be carrying that momentum before the wave is absorbed, and that something is the field itself. The **momentum density** is g = S/c² = ε₀(E × B), pointing in the same direction as the energy flow, with magnitude equal to the energy density divided by c.

The transfer of field momentum to matter is called **radiation pressure**. For a plane wave with energy density u, the radiation pressure on a perfect absorber is P = u (in SI units of N/m²), and on a perfect reflector it's P = 2u (because the momentum reverses). These are tiny forces in everyday life — the radiation pressure of sunlight on Earth is about 5 μPa — but they become significant in astrophysics (stellar winds blow material away from stars), in optical trapping (laser tweezers grip microscopic beads), and in proposed solar sail spacecraft.

The relationship g = S/c² has a profound implication: energy and momentum in electromagnetic fields are not independent, but tied by g = u/c = energy/(c·volume). This is exactly the relationship for massless particles, and it foreshadows the photon picture in quantum mechanics — photons carry energy E = hf and momentum p = h/λ = E/c. The classical result for field momentum per unit volume matches the quantum mechanical count of photon momenta, confirming that even the classical field theory anticipates the quantum nature of light.
