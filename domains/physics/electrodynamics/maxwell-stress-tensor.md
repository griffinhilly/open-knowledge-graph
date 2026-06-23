---
id: maxwell-stress-tensor
title: Maxwell Stress Tensor and Radiation Pressure
domain: physics
course: electrodynamics
prerequisites:
- id: poynting-vector-and-energy-flux
  type: hard
- id: maxwells-equations-integral-form
  type: soft
- id: poynting-vector-energy-flow
  type: soft
builds-toward:
- radiation-from-accelerated-charges
tags:
- stress
- momentum
- radiation-pressure
stage: expert
status: validated
---

# Maxwell Stress Tensor and Radiation Pressure

## Core Idea
The Maxwell stress tensor T_ij encodes electromagnetic momentum density g = ε₀(E × B) and represents stresses exerted by fields. Radiation carries momentum and exerts pressure on absorbing surfaces. This provides a unified view of electromagnetic forces through momentum conservation.

## Questions

```yaml
- question: "A beam of light with intensity I strikes a perfectly reflecting mirror. What is the radiation pressure on the mirror?"
  type: multiple-choice
  options:
    - "I/c — the same as for a perfectly absorbing surface, since reflection conserves energy"
    - "2I/c — the mirror reverses the light's momentum, so the total momentum transfer per unit area per unit time is doubled"
    - "I/2c — only half the momentum is transferred because the other half is carried away by the reflected beam"
    - "Zero — photons have no rest mass and therefore carry no momentum that can be transferred"
  answer: 1
  explanation: "An absorbing surface removes the light's momentum, giving a radiation pressure of I/c. A perfectly reflecting mirror reverses the momentum: the incoming photons carry momentum I/c toward the mirror, and the outgoing photons carry momentum I/c away. The total momentum transferred to the mirror is the difference: I/c − (−I/c) = 2I/c. This factor of 2 is why reflectors experience twice the radiation pressure of absorbers — both the removal of incoming momentum and the imparting of reversed outgoing momentum act in the same direction (pushing the mirror). Option D reflects the misconception that massless particles carry no momentum; photons carry momentum p = E/c regardless of rest mass."

- question: "The electromagnetic momentum density in a region of space where electric field E and magnetic field B are present is:"
  type: multiple-choice
  options:
    - "ε₀(E + B) — the vector sum of the field contributions"
    - "ε₀(E × B) — equal to S/c², where S is the Poynting vector"
    - "(1/2)ε₀E² — the electric energy density alone"
    - "(E × B)/μ₀ — which equals the Poynting vector S, the energy flux"
  answer: 1
  explanation: "The electromagnetic momentum density is g = ε₀(E × B). Since the Poynting vector is S = (1/μ₀)(E × B), we have g = μ₀ε₀ S = S/c² (using c² = 1/μ₀ε₀). This is the momentum stored per unit volume in the electromagnetic field — not energy flux, not electric energy density. Option D is the Poynting vector S itself, which gives energy flux (watts per square meter), not momentum density. The key relationship g = S/c² parallels the relativistic relation between energy and momentum for massless radiation (p = E/c), and confirms that wherever electromagnetic energy flows, momentum also flows in the same direction at rate 1/c² times the energy flux."

- question: "The Maxwell stress tensor allows the total electromagnetic force on all matter inside a volume to be computed as a surface integral over the boundary of that volume, without knowing the internal charge or current distribution."
  type: true-false
  answer: true
  explanation: "This is the central practical power of the Maxwell stress tensor. The force on any enclosed matter can be written as F_i = ∮ T_ij dA_j − d/dt ∫ g_i dV, where the first term is the surface integral of T over the boundary and the second is the rate of change of field momentum inside. To find the force, you only need to know the fields on the boundary surface — not the detailed distribution of charges, currents, or material properties inside. This is analogous to using Gauss's law to find electric fields without knowing where exactly the enclosed charges sit. Choosing a convenient enclosing surface (e.g., one far from the object where fields are simple) can greatly simplify force calculations."

- question: "Because electromagnetic waves have no rest mass, they carry energy but not momentum — radiation pressure is therefore an approximation valid mainly at very high field intensities."
  type: true-false
  answer: false
  explanation: "Radiation pressure is not an approximation — it is an exact consequence of electromagnetic momentum conservation. The electromagnetic field carries real momentum with density g = ε₀(E × B) = S/c², regardless of intensity. This is not contingent on quantum mechanics or photons; it follows from Maxwell's equations and the conservation of total (mechanical + electromagnetic) momentum. The effect is small — sunlight exerts about 5 micronewtons per square meter — but measurable. Solar sail spacecraft use it for propulsion. At the quantum level, each photon carries momentum p = ħk = E/c, and the macroscopic radiation pressure is the average over many photon impacts. Rest mass is irrelevant to electromagnetic momentum."

- question: "How does the Maxwell stress tensor unify the concept of electromagnetic force with the conservation of momentum?"
  type: short-answer
  answer: "The Maxwell stress tensor T_ij expresses the local conservation of total (mechanical + electromagnetic) momentum, in exact parallel to how Poynting's theorem expresses local conservation of energy. T_ij gives the flux of the i-th component of electromagnetic momentum in the j-th direction across a surface. The total force on any matter inside a volume equals the rate of electromagnetic momentum flowing into that volume through its boundary surface (given by the surface integral of T) minus the rate of change of momentum stored in the fields themselves. This means all electromagnetic forces — radiation pressure, Coulomb forces, magnetic forces — are aspects of a single unified momentum conservation law: mechanical momentum changes when electromagnetic momentum flows into matter, and the stress tensor accounts for every cross-surface momentum flux. The fields are not just abstract mathematical tools; they are physical momentum carriers."
```

## Explainer

You already know from the Poynting vector that electromagnetic fields carry energy flowing at rate S = (1/μ₀)E × B per unit area. A natural question follows: if electromagnetic waves carry energy, do they also carry momentum? The answer is yes — and the **Maxwell stress tensor** is the mathematical tool that makes momentum conservation in electromagnetic systems precise in exactly the same way that Poynting's theorem made energy conservation precise.

The **electromagnetic momentum density** is g = ε₀(E × B) = S/c², meaning the momentum stored per unit volume in the field is proportional to the energy flux divided by c². This is not merely an analogy to mechanical momentum — it is real momentum that can be transferred to matter. When a light wave hits an absorbing surface, it deposits momentum, producing a measurable **radiation pressure**: P = I/c for a perfectly absorbing surface (intensity divided by the speed of light) and P = 2I/c for a perfect reflector. The force from sunlight on a square meter of surface is tiny (about 5 micronewtons), but it is real — solar sail spacecraft use it for propulsion.

The **Maxwell stress tensor** T_ij is the object that systematizes this. Just as a mechanical stress tensor tells you the force per unit area exerted across a surface in a material, T_ij tells you the flux of the i-th component of electromagnetic momentum in the j-th direction. The total electromagnetic force on all matter inside a volume V can be written as a surface integral of T over the boundary: F_i = ∮ T_ij dAⱼ − d/dt ∫ gᵢ dV. The first term is the momentum flowing in through the surface; the second term is the rate of change of momentum stored in the fields inside. In steady state, the surface integral alone gives the force — you can calculate the force on any object (conductor, dielectric, current loop) by integrating the stress tensor over a surface enclosing it, without needing to know the microscopic charge distribution.

The conceptual payoff is unification: mechanical force, radiation pressure, and electromagnetic momentum are all aspects of a single conservation law for total (mechanical + field) momentum. Just as energy is conserved locally by Poynting's theorem, momentum is conserved locally by the stress tensor formulation. This framework extends naturally to radiation from accelerating charges and to the momentum carried by photons in quantum electrodynamics, where each photon carries momentum p = ħk = E/c — the macroscopic radiation pressure is just the classical average of countless photon impacts.
