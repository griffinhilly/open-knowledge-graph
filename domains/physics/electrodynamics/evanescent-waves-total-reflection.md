---
id: evanescent-waves-total-reflection
title: Evanescent Waves and Total Internal Reflection
domain: physics
course: electrodynamics
prerequisites:
- id: group-velocity-and-dispersion
  type: hard
- id: electromagnetic-waves-in-media
  type: hard
tags:
- evanescent-waves
- total-reflection
- surface-waves
- tunneling
stage: expert
status: validated
---

# Evanescent Waves and Total Internal Reflection

## Core Idea
When the wave vector becomes imaginary (above the cutoff frequency for the medium), waves decay exponentially rather than propagate. At interfaces beyond the critical angle, evanescent waves extend into the second medium and can tunnel through thin barriers.

## Questions

```yaml
- question: "Two glass prisms are arranged hypotenuse-to-hypotenuse with an air gap. Total internal reflection occurs at the first hypotenuse. When the gap is reduced to a fraction of a wavelength, light is observed in the second prism. A student says: 'This is impossible — TIR means total reflection, so no field exists in the air gap.' What is the correct explanation?"
  type: multiple-choice
  options:
    - "The student is correct: reducing the gap mechanically disrupts the TIR condition, causing partial transmission through a different mechanism"
    - "At very small gaps, quantum tunneling allows photons to jump across the gap, bypassing the classical wave equations"
    - "TIR reflects the traveling wave but an evanescent field — non-propagating, exponentially decaying — still exists in the air gap; when the second prism is close enough, this field couples into propagating modes there, transferring power (frustrated TIR)"
    - "The student is correct that no field exists, but diffraction at the edge of the prism redirects light into the second prism"
  answer: 2
  explanation: "TIR means the time-averaged energy flux (Poynting vector) into the second medium is zero — no net power is transmitted. But fields are not zero: Maxwell's boundary conditions require a field in the second medium, which takes the form of an exponentially decaying evanescent wave. When a second medium is brought within this decay length, the evanescent field can couple into propagating modes there. This is frustrated TIR. The student's error is conflating 'total reflection of propagating energy' with 'no fields at all.'"

- question: "A wave vector k = iκ (with κ real and positive) in the wave factor e^{ikx} describes which physical situation?"
  type: multiple-choice
  options:
    - "A traveling wave with a 90° phase shift relative to a standard plane wave"
    - "A standing wave formed by two counterpropagating waves with equal amplitude"
    - "An exponentially decaying field (e^{−κx}) — an evanescent wave that carries no net power in the decay direction"
    - "A wave with reduced phase velocity due to dispersion in a dense medium"
  answer: 2
  explanation: "Substituting k = iκ into e^{ikx} gives e^{i(iκ)x} = e^{−κx}: pure exponential decay with no oscillation in x. This is an evanescent wave. It occurs whenever k² < 0, which happens in total internal reflection (angle exceeds critical angle), below plasma cutoff frequency, or in a waveguide below its cutoff. The field amplitude decays on a length scale ~1/κ, typically of order one wavelength."

- question: "In total internal reflection, the electromagnetic field in the second (rarer) medium is exactly zero — TIR produces complete exclusion of the field from that medium."
  type: true-false
  answer: false
  explanation: "TIR requires that Maxwell's boundary conditions be satisfied at the interface, which forces the existence of a field in the second medium. That field is evanescent: it decays exponentially with distance from the interface and carries zero net power. The fields are real and measurable — frustrated TIR, near-field microscopy, and attenuated total reflectance spectroscopy all exploit this non-zero evanescent field. 'Total reflection' refers to the power balance, not the field amplitude."

- question: "Because evanescent waves carry no net power, they have no physical consequences and can seldom be detected or exploited in technology."
  type: true-false
  answer: false
  explanation: "Evanescent fields are physically significant despite carrying no net power in the decay direction. Near-field optical microscopy uses evanescent waves to achieve resolution beyond the classical diffraction limit. Attenuated total reflectance spectroscopy places a sample in contact with the evanescent field to measure its absorption spectrum. Optical fiber couplers operate by overlapping evanescent tails of two fibers. Frustrated TIR itself is the basis for some optical switches and sensors. Zero net power flux is not the same as zero physical effect."

- question: "Why is frustrated total internal reflection considered the optical analogue of quantum-mechanical tunneling?"
  type: short-answer
  answer: "In quantum tunneling, a particle's wavefunction decays exponentially through a classically forbidden potential barrier but re-emerges as a propagating wave on the other side, allowing transmission with finite probability. In frustrated TIR, the evanescent electromagnetic field decays exponentially through the air gap (the 'barrier') and re-emerges as a propagating wave in the second prism. Both phenomena are described by the same mathematical equation — exponential decay of the wave amplitude through a region where the wave vector is imaginary — and in both cases, the 'barrier' does not need to be traversed by a classical traveling wave for transmission to occur."
  explanation: "The mathematical identity is not coincidental: the Schrödinger equation and Maxwell's wave equations are both second-order linear equations, and imaginary wave vector solutions play the same structural role in both. This connection is part of why wave mechanics and electromagnetic theory share so much formal structure, and why insights from optics (TIR, evanescent waves) historically contributed to early quantum theory."
```

## Explainer

You know from studying electromagnetic waves in media that the wave vector k = n·ω/c, where n is the refractive index of the medium. The refractive index can depend on frequency (dispersion), and in some situations — below a plasma cutoff frequency, inside a waveguide below its cutoff, or beyond the critical angle at an interface — the requirement that k² = (n·ω/c)² forces k² to be negative. A negative k² means k itself is imaginary: k = iκ where κ is real and positive. Substituting this into the plane-wave factor e^(ikx) gives e^(−κx): not oscillation, but **exponential decay**. This is an **evanescent wave**.

The most vivid physical setting is **total internal reflection** (TIR). When a wave travels from a denser medium (refractive index n₁) to a rarer one (n₂ < n₁) and strikes the interface at an angle θᵢ greater than the critical angle θ_c = arcsin(n₂/n₁), Snell's law would require sin θₜ = (n₁/n₂)sin θᵢ > 1 — which has no real solution for the transmitted angle. The wave in medium 2 must still satisfy Maxwell's boundary conditions, but it does so with an evanescent field that decays exponentially away from the interface in the transverse direction while appearing to travel parallel to it. The time-averaged Poynting vector into medium 2 is zero — no net power is transmitted — yet the fields are not zero. They exist in a thin skin extending a wavelength or so beyond the interface.

This non-zero but non-propagating field makes TIR more subtle than it first appears, and it has a measurable consequence: **frustrated total internal reflection**. If you bring a second piece of glass close to the first (within a fraction of a wavelength), the evanescent field from the first glass can couple into the propagating modes of the second. Power flows across the gap even though there is no traveling wave in the air between them. This is the optical analogue of quantum-mechanical tunneling — a particle wave decays exponentially through a classically forbidden barrier but re-emerges as a propagating wave on the other side. The two phenomena obey mathematically identical equations.

Evanescent waves are not just a curiosity: they underpin **near-field optics**, allowing imaging beyond the diffraction limit by collecting the high-spatial-frequency evanescent components that a conventional lens discards. They also explain the operation of optical fiber couplers (where bending creates a geometry where the evanescent tail of one fiber overlaps the second) and attenuated total reflectance spectroscopy, where a sample placed near the reflecting surface absorbs from the evanescent field to reveal its absorption spectrum. Any time you see decaying rather than propagating fields — near an antenna below resonance, in a cutoff waveguide section, at a TIR interface — you are dealing with the same mathematics: imaginary wave vector, exponential envelope, zero net power transport.
