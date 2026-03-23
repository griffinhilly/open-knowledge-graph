---
id: far-field-radiation-limit
title: Far-Field Limit and Radiation Zone
domain: physics
course: electrodynamics
prerequisites:
- id: retarded-potentials
  type: hard
- id: radiation-from-accelerated-charges
  type: hard
builds-toward:
- radiation-directivity-and-pattern
- radiation-angular-distribution-em
tags:
- far-field
- radiation-zone
- multipole-expansion
stage: expert
status: draft
---

# Far-Field Limit and Radiation Zone

## Core Idea
In the radiation zone (kr >> 1), retarded potentials simplify to pure radiation fields with E ∝ ∇ × a_ret and B = (k̂ × E)/c. The electric field near a small source becomes (1/4πε₀c²r)[k̂ × (k̂ × p̈)], proportional to acceleration, decaying as 1/r.

## Questions

```yaml
- question: "An accelerating charge produces two field terms: one decaying as 1/r and one decaying as 1/r². As r → ∞, which carries energy to infinity and why?"
  type: multiple-choice
  options:
    - "The 1/r² term carries energy to infinity because it is stronger near the source and dominates the total energy"
    - "The 1/r term carries energy to infinity: the Poynting vector scales as E² ∝ 1/r², so power through a sphere (∝ r²) is constant in r"
    - "The 1/r term dominates at large r, but the total power through a sphere still falls to zero as r → ∞"
    - "Both terms contribute equally to the total radiated power at all distances"
  answer: 1
  explanation: "Energy flux (the Poynting vector) scales as S ∝ E². For the 1/r radiation field, S ∝ 1/r². Integrated over the surface of a sphere of radius r (area ∝ r²), total power P = ∮ S · dA ∝ (1/r²)(r²) = constant — independent of r. This constant power flow is what it means to 'radiate': energy genuinely escapes to infinity. For the 1/r² near-field term, S ∝ 1/r⁴, so P ∝ (1/r⁴)(r²) = 1/r² → 0. The near-field term stores and returns energy locally; only the radiation field carries energy irreversibly away."

- question: "In the radiation zone (kr >> 1), the electric field E of an oscillating dipole and the direction of propagation k̂ satisfy:"
  type: multiple-choice
  options:
    - "E is parallel to k̂ — the wave is longitudinal, like a sound wave"
    - "E has no fixed relationship to k̂ — the polarization depends on the observation angle in an arbitrary way"
    - "E is perpendicular to k̂ (transverse), with B also perpendicular to both E and k̂, and |B| = |E|/c"
    - "E and B are both parallel to k̂, since they must point in the direction of energy propagation"
  answer: 2
  explanation: "Far-field radiation is always a transverse electromagnetic wave: E and B are both perpendicular to k̂ (the propagation direction) and to each other, with |B| = |E|/c. This follows from the double cross product in the radiation field formula E ∝ k̂ × (k̂ × p̈), which projects p̈ onto the plane perpendicular to k̂. Option A (longitudinal) would violate Maxwell's equations in free space. The transverse nature is a defining feature of the radiation zone and underlies antenna theory."

- question: "The total power radiated by an oscillating dipole, calculated as the integral of the Poynting vector over a sphere, decreases as the sphere's radius increases."
  type: true-false
  answer: false
  explanation: "This is the defining property of radiation: the Poynting vector S ∝ 1/r², and the surface area of the sphere grows as 4πr², so total power P = ∮ S · dA is constant in r. This r-independence is what it means for radiation to carry energy to infinity — every spherical shell, no matter how large, captures the same amount of power per unit time. If power fell with r, the source would not be truly radiating in the sense of irreversible energy loss."

- question: "In the radiation zone, the electric field of a dipole source is proportional to the second time derivative (acceleration) of the dipole moment, not the moment itself or its first derivative."
  type: true-false
  answer: true
  explanation: "The radiation field formula E ∝ (1/r)[k̂ × (k̂ × p̈)] shows that E depends on p̈ — the acceleration of the charge distribution, not its position or velocity. This is why a charge moving at constant velocity does not radiate (p̈ = 0 for uniform motion), while an accelerating charge does. The p̈ dependence is also the origin of the Larmor formula for radiated power (P ∝ p̈²), which underpins all classical radiation theory."

- question: "Why does the 1/r² near-field term of an accelerating charge NOT contribute to radiation, while the 1/r term does? Use the concept of total power through a sphere in your answer."
  type: short-answer
  answer: "The Poynting vector (energy flux) is proportional to E². For the 1/r² near-field term, E² ∝ 1/r⁴, so the total power through a sphere of radius r scales as (1/r⁴)(4πr²) = 4π/r² → 0 as r → ∞. The near-field carries no net energy to infinity; it stores energy in the fields near the source and returns it on each cycle. For the 1/r radiation term, E² ∝ 1/r², so power through a sphere scales as (1/r²)(4πr²) = 4π = constant. This r-independent power flow means energy irreversibly leaves the source — the hallmark of radiation."
  explanation: "The distinction between near-field and radiation field is fundamentally about whether energy escapes permanently. Near-field terms are associated with the static and inductive fields of the source — they create a reactive energy 'halo' that oscillates in and out but doesn't propagate. Only the 1/r term, produced by acceleration, creates the self-sustaining electromagnetic wave that propagates to infinity. This is why antennas must have accelerating charges (oscillating currents) to radiate — uniform current flow produces only near-field."
```

## Explainer

From your work with **retarded potentials**, you know that the fields of a moving charge are not instantaneous: they reflect the charge's position and velocity at the retarded time t_ret = t − r/c, the moment when the "news" of the charge's motion was emitted. The full fields of an accelerating charge (the Liénard-Wiechert fields) contain two terms: one that decays as 1/r² and one that decays as 1/r. At close range, the 1/r² term dominates and looks like a modified Coulomb field that is dragged along with the charge. At large distances, the 1/r² term becomes negligible and only the 1/r term survives.

This 1/r term is the **radiation field**, and its survival at large distances is what makes radiation important. Energy flux (the Poynting vector S = E × B / μ₀) scales as E² ∝ 1/r². Multiply by the surface area of a sphere (4πr²), and the total power flowing outward through any sphere is independent of r — radiation carries energy to infinity. The 1/r² Coulomb-like term contributes a Poynting vector that falls as 1/r⁴, so the power through a sphere goes as 1/r² and vanishes at infinity. Only the 1/r radiation field represents genuine energy loss from the source.

In the **radiation zone** (r >> λ, equivalently kr >> 1), you can simplify the retarded potential calculation drastically. For a small source (size a << λ), the radiation field from an oscillating dipole moment p(t) takes the clean form E = (1/4πε₀c²r)[k̂ × (k̂ × p̈)], where k̂ is the unit vector pointing from source to field point and p̈ is the second time derivative of the dipole moment (the acceleration of the charge distribution). The double cross product k̂ × (k̂ × p̈) extracts the component of p̈ transverse to the direction of observation — fields in the radiation zone are always **transverse waves**, with E and B perpendicular to k̂ and to each other, with |B| = |E|/c.

The 1/r dependence and transverse polarization together define what it means for radiation to be "far field." In addition to distance, far field also means that you are far compared to the source size, so all parts of the source contribute nearly the same retardation delay. This approximation — retaining only the dominant 1/r term — is what makes antenna theory and radiation pattern analysis tractable. The angular distribution of power (dP/dΩ ∝ sin²θ for a linear dipole oscillating along ẑ) reveals the **radiation pattern**: maximum emission perpendicular to the oscillation axis, zero emission along it. These patterns, derived from the far-field limit, are exactly what antenna engineers optimize when designing directional transmitters.
