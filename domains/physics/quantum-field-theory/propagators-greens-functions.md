---
id: propagators-greens-functions
title: Propagators and Green's Functions
domain: physics
course: quantum-field-theory
prerequisites:
- id: klein-gordon-field-quantization
  type: hard
- id: feynman-path-integral
  type: soft
tags:
- propagator
- greens-function
- feynman-propagator
stage: expert
status: validated
---

# Propagators and Green's Functions

## Core Idea
The propagator (Feynman propagator) is the amplitude for a particle to travel from one spacetime point to another. Mathematically, it is the time-ordered vacuum expectation value of two field operators, and it equals the Green's function of the classical field equation. Propagators are the internal lines in Feynman diagrams.

## Questions

```yaml
- question: "The Feynman propagator for the Klein-Gordon field is D_F(x-y) = <0|T{phi(x)phi(y)}|0>, where T denotes time ordering. Why is time ordering essential rather than just using <0|phi(x)phi(y)|0>?"
  type: multiple-choice
  options:
    - "Time ordering ensures the propagator is real-valued"
    - "Without time ordering, the propagator would not be Lorentz invariant"
    - "Time ordering ensures that positive-frequency modes propagate forward in time and negative-frequency modes propagate backward — the correct causal structure for a relativistic theory where antiparticles propagate backward in time"
    - "Time ordering is merely a convention with no physical significance"
  answer: 2
  explanation: "The time-ordered product T{phi(x)phi(y)} places the later-time operator to the left. This ensures the correct boundary conditions: particles propagate forward in time (positive-energy poles contribute for t_x > t_y) and antiparticles propagate backward in time (negative-energy poles contribute for t_y > t_x). In momentum space, this corresponds to the Feynman i-epsilon prescription: D_F(p) = i/(p^2 - m^2 + i epsilon), where the small imaginary part shifts the poles off the real axis in the way that produces causal propagation. Different time orderings give different Green's functions (retarded, advanced) with different physical interpretations."

- question: "In momentum space, the Feynman propagator for a scalar field is D_F(p) = i/(p^2 - m^2 + i epsilon). The pole at p^2 = m^2 corresponds to what physical situation?"
  type: multiple-choice
  options:
    - "A virtual particle that violates energy-momentum conservation"
    - "An on-shell particle satisfying the relativistic energy-momentum relation — the propagator diverges when the intermediate particle is real"
    - "A bound state of the field"
    - "An ultraviolet divergence that must be regularized"
  answer: 1
  explanation: "The condition p^2 = m^2 is exactly the on-shell condition for a real particle of mass m. When an intermediate particle in a Feynman diagram is on-shell, the propagator diverges (the denominator vanishes). Off-shell (virtual) particles have p^2 != m^2 and the propagator is finite. The i epsilon prescription tells you how to handle the pole — it determines the causal boundary conditions. In scattering calculations, the on-shell poles correspond to physical intermediate states and are handled by the optical theorem and cutting rules."

- question: "The propagator for a massive field falls off exponentially at spacelike separations with a characteristic length scale of 1/m (the Compton wavelength). This means that virtual particles cannot propagate farther than their Compton wavelength."
  type: true-false
  answer: false
  explanation: "The propagator does fall off as e^{-m|x-y|} for spacelike separations, and this sets the natural range scale. However, saying virtual particles 'cannot propagate farther' is misleading. The propagator is nonzero at all separations — it is exponentially suppressed but never exactly zero. In Feynman diagrams, virtual particles with any momentum (including very small momenta, corresponding to long distances) contribute. The exponential suppression means that long-range effects from massive fields are strongly suppressed, which is why the nuclear forces (mediated by massive mesons or W/Z bosons) are short-ranged while electromagnetism (massless photon propagator, falling off as 1/|x-y|^2) is long-ranged."

- question: "Explain the physical meaning of the Feynman propagator and why it serves as the building block for all perturbative calculations in QFT."
  type: short-answer
  answer: "The Feynman propagator D_F(x-y) = <0|T{phi(x)phi(y)}|0> gives the amplitude for a field disturbance to propagate from y to x (or equivalently, for a particle created at y to be detected at x, with antiparticle contributions when x^0 < y^0). In perturbation theory, interactions are treated as small corrections to free propagation. Every internal line in a Feynman diagram represents a free propagator — the amplitude for a virtual particle to travel between two interaction vertices. The full scattering amplitude is built by multiplying propagators (internal lines) with vertex factors (interaction couplings) and integrating over all intermediate momenta. The propagator is the Green's function of the free field equation, so it encodes the response of the field to a point-like disturbance."
  explanation: "The connection between propagators and Green's functions is exact: (partial^2 + m^2)D_F(x-y) = -i delta^4(x-y). This means the propagator tells you how the field responds to a localized source at point y. The entire Feynman diagram expansion is an iterative solution of the full interacting field equation, using the free propagator as the kernel."
```

## Explainer

The **propagator** is the most fundamental object in perturbative quantum field theory. For a free scalar field, the Feynman propagator is defined as D_F(x - y) = <0|T{phi(x) phi(y)}|0>, where T denotes time ordering (placing the later-time operator to the left). Physically, it represents the amplitude for a particle to propagate from spacetime point y to point x when x^0 > y^0, and the amplitude for an antiparticle to propagate from x to y when x^0 < y^0. The time ordering ensures the correct causal structure.

In momentum space, the Feynman propagator takes the elegant form D_F(p) = i / (p^2 - m^2 + i epsilon), where epsilon is a positive infinitesimal. The pole at p^2 = m^2 corresponds to on-shell particles (real particles satisfying the energy-momentum relation). The i epsilon prescription determines the contour of integration in the complex energy plane and encodes the causal boundary conditions: positive-energy modes propagate forward in time, negative-energy modes backward. This single expression contains all the information about free-particle propagation.

The propagator is also the **Green's function** of the free field equation: applying the Klein-Gordon operator to D_F gives a delta function, (partial^2 + m^2)D_F(x - y) = -i delta^4(x - y). This means the propagator describes the field's response to a point-like disturbance -- exactly what a Green's function does in classical physics. Each type of field has its own propagator: the Klein-Gordon propagator i/(p^2 - m^2) for scalars, the Dirac propagator i(gamma^mu p_mu + m)/(p^2 - m^2) for spin-1/2 fermions, and the photon propagator -i g_{mu nu}/(k^2) (in Feynman gauge) for the electromagnetic field.

In Feynman diagrams, **every internal line is a propagator**. When two particles scatter, the interaction is mediated by the exchange of virtual particles, and each virtual particle line contributes a factor of the propagator. The full scattering amplitude is built by connecting propagators at interaction vertices (where the coupling constant enters), summing over all possible intermediate states, and integrating over all possible intermediate momenta. The propagator is therefore the building block from which all perturbative predictions in quantum field theory are constructed.
