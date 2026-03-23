---
id: dispersion-relations-em-waves
title: Dispersion Relations for Electromagnetic Waves
domain: physics
course: electrodynamics
prerequisites:
- id: electromagnetic-waves-in-dielectrics
  type: hard
- id: plane-electromagnetic-waves
  type: hard
builds-toward:
- refractive-index-and-dispersion
tags:
- dispersion
- wave-velocity
- frequency-dependence
stage: expert
status: validated
---

# Dispersion Relations for Electromagnetic Waves

## Core Idea
The dispersion relation ω(k) connects frequency and wavenumber for waves in a medium, determining the wave velocity v_phase = ω/k and group velocity v_group = dω/dk. Different frequency components travel at different speeds due to material dispersion, causing pulse broadening and chromatic effects. Understanding dispersion is crucial for signal propagation, optical design, and analyzing material properties.

## Questions

```yaml
- question: "A light pulse containing a range of frequencies is launched into a long optical fiber. After traveling thousands of kilometers, the pulse has spread out in time and can no longer be distinguished from adjacent pulses. What is the fundamental cause of this broadening?"
  type: multiple-choice
  options:
    - "The pulse loses energy to absorption, which stretches its duration"
    - "Different frequency components travel at different phase velocities, arriving at the receiver at different times"
    - "The group velocity increases along the fiber, causing later components to catch up and overlap with earlier ones"
    - "Reflection at the fiber walls mixes frequency components together"
  answer: 1
  explanation: "In a dispersive medium, the dispersion relation ω(k) is nonlinear, so phase velocity v_phase = ω/k varies with frequency. A pulse is a superposition of many frequency components; in a dispersive fiber these components 'walk apart' as they travel because each propagates at a slightly different speed. What was a sharp pulse at the transmitter arrives as a smeared-out pulse at the receiver. Absorption (option A) reduces amplitude but doesn't cause spreading. This pulse broadening directly limits fiber data rates because adjacent pulses must be spaced far enough that they don't overlap after spreading."

- question: "In a dispersive medium, which velocity determines how quickly a signal or information is transmitted?"
  type: multiple-choice
  options:
    - "Phase velocity (ω/k), because it describes how fast the wave crests propagate"
    - "Group velocity (dω/dk), because it describes how fast the envelope of a wave packet propagates"
    - "The arithmetic average of phase and group velocity"
    - "The speed of light in vacuum, which all signals must obey"
  answer: 1
  explanation: "Phase velocity is the speed of a particular crest in an infinite sinusoidal wave — a mathematical abstraction that doesn't carry information. Group velocity (dω/dk) is the speed at which a localized wave packet (the superposition of nearby frequencies) moves, and crucially, it is the speed at which energy and information propagate. In vacuum, phase and group velocity both equal c. In dispersive media they differ, and it is the group velocity that matters for signal engineering. Option D is incorrect: phase velocity can exceed c in anomalous dispersion regions without violating relativity, because it does not carry information."

- question: "In vacuum, a light pulse containing many different frequencies will spread out over time because each frequency travels at a slightly different speed."
  type: true-false
  answer: false
  explanation: "In vacuum, the dispersion relation is simply ω = ck — a linear relationship between angular frequency and wavenumber. This means phase velocity v_phase = ω/k = c and group velocity v_group = dω/dk = c for all frequencies. Every component of the pulse travels at the same speed c, so the pulse maintains its shape indefinitely. Dispersion and pulse spreading only occur in media where ω(k) is nonlinear — i.e., where the index of refraction varies with frequency."

- question: "Phase velocity and group velocity can differ significantly in a dispersive medium, and the group velocity is the physically meaningful quantity for the transmission of energy and information."
  type: true-false
  answer: true
  explanation: "This is the central distinction in dispersion theory. In a dispersive medium, the nonlinear ω(k) causes v_phase = ω/k to differ from v_group = dω/dk. Phase velocity can even exceed c in regions of anomalous dispersion without violating special relativity, because no information travels at the phase velocity. All signal transmission, energy flow, and information encoding occur at the group velocity, which is constrained to be ≤ c in physical systems."

- question: "Explain why pulse broadening in optical fibers limits data transmission rates, and what property of the dispersion relation determines how severe the broadening is."
  type: short-answer
  answer: "A data pulse is not monochromatic — it spans a range of frequencies. In a dispersive fiber, different frequency components travel at slightly different group velocities (because v_group = dω/dk varies with frequency). Components that were synchronized at launch arrive at the receiver at different times, spreading the pulse. If adjacent pulses spread enough to overlap, the receiver cannot distinguish separate bits. The severity of broadening is determined by group velocity dispersion (GVD), proportional to d²ω/dk² — the rate at which group velocity varies with frequency. At a wavelength where GVD ≈ 0 (the zero-dispersion point), broadening is minimized, and dispersion-managed fiber design exploits this."
  explanation: "This is why fiber-optic systems operate near specific wavelengths and use dispersion-compensating fiber: engineering the dispersion profile is as important as minimizing loss. Higher data rates require shorter pulses, which span broader frequency ranges, which suffer more from dispersion — creating a fundamental engineering trade-off directly governed by the dispersion relation."
```

## Explainer

From your study of plane electromagnetic waves and waves in dielectrics, you know that a monochromatic wave traveling in a medium can be written as e^{i(kx − ωt)}, where k is the wavenumber (spatial frequency) and ω is the angular frequency (temporal frequency). In vacuum, these are locked together by the simple relation ω = ck — frequency and wavenumber are always proportional, and every frequency travels at the same speed c. A **dispersion relation** ω(k) is the medium's specific version of this constraint. When ω(k) is not simply proportional to k — when the function is nonlinear — the medium is called dispersive, and different frequency components of a wave travel at different speeds.

The two distinct velocities that emerge from a dispersion relation deserve careful attention. The **phase velocity** v_phase = ω/k is the speed at which a single-frequency sinusoidal wave pattern moves — the rate at which a particular crest propagates. The **group velocity** v_group = dω/dk is the speed at which a localized packet of waves (a superposition of nearby frequencies) moves, and crucially, it is the speed at which energy and information travel. In vacuum they are equal (both equal c), but in a dispersive medium they can differ significantly. You can build the intuition with a simple picture: if you superpose two sine waves of slightly different frequency, you get a slowly beating envelope. The phase velocity is how fast the individual fringes move; the group velocity is how fast the envelope moves. For normal dispersion, v_group < v_phase; in anomalous dispersion regions, counterintuitive orderings can occur.

Why do real materials disperse? The answer lies in the response of bound electrons and ions. When an electromagnetic wave drives the charges in a material, they respond resonantly — near an atomic or molecular resonance frequency, the polarization is large and strongly frequency-dependent. The index of refraction n(ω) = ck/ω captures this frequency dependence, and its variation with ω is what causes dispersion. A glass prism spreads white light into a spectrum precisely because n is slightly different for red and violet light; violet photons travel more slowly and refract more. This is normal dispersion: dn/dω > 0, so higher-frequency (violet) light has a larger n and slower phase velocity.

The practical consequence of dispersion is **pulse broadening**. A light pulse in an optical fiber contains a range of frequencies — it is not a single monochromatic wave. In a dispersive medium, these frequency components walk apart: higher-frequency components slow down relative to lower-frequency ones. After propagating a long distance, what started as a sharp pulse has spread into a longer, blurrier pulse. In fiber-optic communications, this limits data rates: pulses must be spaced far enough apart that they don't overlap after broadening. Dispersion-managed fiber design and the careful choice of operating wavelength near dispersion-zero points (where dv_group/dω ≈ 0) are central engineering challenges, making the dispersion relation not just a theoretical curiosity but a daily design constraint.
