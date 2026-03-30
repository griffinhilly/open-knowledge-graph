---
id: gravitational-waves
title: Gravitational Waves
domain: physics
course: general-relativity
prerequisites:
- id: linearized-gravity
  type: hard
- id: einstein-field-equations
  type: hard
tags:
- gravitational-waves
- LIGO
- quadrupole-formula
- wave-polarization
- radiation
stage: expert
status: validated
---

# Gravitational Waves

## Core Idea
Gravitational waves are propagating ripples in the fabric of spacetime, predicted by Einstein's field equations and first directly detected by LIGO in 2015. They arise from accelerating masses with time-varying quadrupole (or higher) moments — merging black holes, neutron star binaries, supernovae. In linearized GR, they satisfy a wave equation and travel at the speed of light. They have two independent polarizations (plus and cross, h₊ and h×) that produce transverse, traceless tidal distortions: a ring of test particles is alternately stretched and squeezed in perpendicular directions as a wave passes. The leading-order energy loss rate is given by the quadrupole formula: dE/dt = -(G/5c⁵)⟨d³I_ij/dt³ d³I^ij/dt³⟩, where I_ij is the mass quadrupole moment. Gravitational waves carry energy, momentum, and angular momentum away from their source, causing orbital inspiral in binary systems.

## Questions

```yaml
- question: "Gravitational waves have two polarization states. What distinguishes the plus (h₊) polarization from the cross (h×) polarization?"
  type: multiple-choice
  options:
    - "h₊ stretches space in one direction and compresses it in the perpendicular direction, while h× does the same but rotated by 45 degrees"
    - "h₊ produces longitudinal compression while h× produces transverse compression"
    - "h₊ is left-circularly polarized and h× is right-circularly polarized"
    - "h₊ and h× differ by a factor of 2 in amplitude but have the same pattern"
  answer: 0
  explanation: "Both h₊ and h× produce transverse, traceless tidal distortions. The plus polarization stretches along the x-axis and compresses along the y-axis (and vice versa half a cycle later). The cross polarization does the same but along axes rotated by 45 degrees. This 45-degree offset (rather than 90 degrees as in electromagnetic waves) reflects the spin-2 nature of gravitational waves — the graviton has spin 2, compared to the photon's spin 1. Circular polarizations are formed by combining h₊ and h× with a π/2 phase offset."

- question: "A spherically symmetric mass distribution (such as a radially pulsating star) cannot emit gravitational waves."
  type: true-false
  answer: true
  explanation: "Gravitational wave emission requires a time-varying mass quadrupole moment (or higher multipole). A spherically symmetric source has a monopole moment (total mass) that is constant and no quadrupole moment by symmetry — all mass shells expand and contract uniformly. This is the gravitational analog of the fact that a uniformly pulsating charge does not radiate electromagnetic waves (which require a time-varying dipole or higher moment). The absence of gravitational monopole and dipole radiation is deeper than electromagnetism: monopole radiation is forbidden by mass conservation, and dipole radiation is forbidden by momentum conservation."

- question: "The first direct detection of gravitational waves (GW150914) measured a strain h ~ 10⁻²¹. Explain what this strain means physically for LIGO's 4-km detector arms."
  type: short-answer
  answer: "The strain h = ΔL/L represents the fractional change in the proper distance between two points caused by the passing gravitational wave. For h ~ 10⁻²¹ and arm length L = 4 km, the change in arm length is ΔL = hL ≈ 10⁻²¹ × 4000 m ≈ 4 × 10⁻¹⁸ m — about one-thousandth the diameter of a proton. LIGO detects this minuscule displacement using laser interferometry: the two perpendicular arms experience opposite length changes (one stretches while the other compresses), producing a differential phase shift in the recombined laser beams."
  explanation: "The extraordinary sensitivity of LIGO — measuring displacements smaller than a proton — is achieved through power recycling (increasing effective laser power), Fabry-Perot cavities (increasing effective arm length), seismic isolation, and quantum noise reduction techniques. The transverse, traceless nature of gravitational waves (opposite effects in perpendicular directions) makes the Michelson interferometer configuration naturally suited to detection."

- question: "Explain why the Hulse-Taylor binary pulsar provided indirect evidence for gravitational waves before LIGO's direct detection."
  type: short-answer
  answer: "The Hulse-Taylor binary pulsar PSR B1913+16 consists of two neutron stars in a tight, eccentric orbit. GR predicts that the binary loses energy to gravitational wave emission, causing the orbit to shrink and the orbital period to decrease. Over decades of timing observations (1974-present), the cumulative shift in the orbital period matches the GR quadrupole formula prediction to better than 0.2%. This is indirect evidence because the gravitational waves themselves were not detected — only their effect on the orbit was measured. The agreement is so precise that it constitutes compelling proof of gravitational wave emission, earning Hulse and Taylor the 1993 Nobel Prize."
  explanation: "The orbital decay rate depends on the gravitational wave luminosity, which is set by the quadrupole formula. The binary pulsar measurement tests both the existence of gravitational waves and the correctness of the quadrupole formula simultaneously. The subsequent direct detection by LIGO in 2015 confirmed what the binary pulsar had already demonstrated indirectly."
```

## Explainer

Einstein predicted gravitational waves in 1916, shortly after completing general relativity, though he and others spent decades debating whether they were physically real or merely coordinate artifacts. The resolution came from recognizing that gravitational waves carry energy and produce measurable tidal effects — both coordinate-independent statements. In linearized GR, small perturbations h_μν of the flat Minkowski metric satisfy a wave equation □h_μν = 0 in vacuum (in the Lorenz gauge and transverse-traceless gauge), with solutions propagating at the speed of light. The two physical polarizations, h₊ and h×, produce transverse tidal distortions: a passing gravitational wave alternately stretches and compresses space in perpendicular directions transverse to the propagation direction.

The generation of gravitational waves is governed by the quadrupole formula, valid for sources whose internal velocities are much less than c and whose gravitational self-energy is weak. The leading-order power radiated is P = (G/5c⁵)⟨d³I_ij/dt³ d³I^ij/dt³⟩, where I_ij is the reduced mass quadrupole moment tensor. The factor G/c⁵ ≈ 2.6 × 10⁻⁵³ W⁻¹ is extraordinarily small, making gravitational radiation negligible for all but the most extreme astrophysical sources. There is no gravitational monopole radiation (mass is conserved) and no dipole radiation (momentum is conserved), so the quadrupole is the leading order — a fundamental difference from electromagnetism, where dipole radiation dominates. Efficient gravitational wave sources require large masses undergoing violent, asymmetric acceleration: merging compact binaries (black holes and neutron stars), asymmetric supernovae, and rotating neutron stars with non-axisymmetric deformations.

The first indirect evidence for gravitational waves came from the Hulse-Taylor binary pulsar PSR B1913+16, discovered in 1974. This system of two neutron stars in a tight orbit provided an extraordinary natural laboratory: the orbital period is measured with microsecond precision via pulsar timing, and its gradual decrease — about 76 microseconds per year — matches the GR prediction for energy loss to gravitational radiation with better than 0.2% accuracy. Over four decades of observation, the cumulative orbital phase shift has tracked the GR prediction with remarkable fidelity, earning Hulse and Taylor the 1993 Nobel Prize.

Direct detection came on September 14, 2015, when the two LIGO detectors simultaneously recorded the signal GW150914: the inspiral, merger, and ringdown of two black holes (36 and 29 solar masses) at a distance of about 1.3 billion light-years. The peak strain was about 10⁻²¹, corresponding to a length change of 4 × 10⁻¹⁸ m in LIGO's 4-km arms — about one-thousandth the diameter of a proton. The signal matched the predictions of numerical relativity with extraordinary precision, confirming the nonlinear strong-field regime of GR for the first time. Since then, LIGO and Virgo have detected dozens of events, including binary neutron star mergers (GW170817, also observed electromagnetically) and black hole-neutron star mergers, opening gravitational wave astronomy as a new observational window on the universe. The 2017 Nobel Prize in Physics was awarded to Weiss, Barish, and Thorne for the detection.
