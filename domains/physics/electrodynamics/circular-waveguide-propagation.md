---
id: circular-waveguide-propagation
title: Propagation in Circular Waveguides
domain: physics
course: electrodynamics
prerequisites:
- id: transverse-electric-modes
  type: hard
- id: transverse-magnetic-modes
  type: hard
- id: cylindrical-harmonics-em
  type: soft
tags:
- circular-waveguide
- bessel-modes
- azimuthal-modes
stage: advanced
status: draft
---

# Propagation in Circular Waveguides

## Core Idea
In circular guides with radius a, azimuthal symmetry is broken by propagation or mode numbers. TE and TM modes are characterized by Bessel function zeros, with cutoff frequencies given by jₙₘ = (λc/2πa)·(ωc/ω). Degenerate modes have the same cutoff frequency.

## Questions

```yaml
- question: "In a rectangular waveguide, TE modes with different indices generally have different cutoff frequencies. In a circular waveguide, two TE₁₁ modes — one polarized horizontally, one vertically — have exactly the same cutoff frequency. Why?"
  type: multiple-choice
  options:
    - "The circular guide has full rotational symmetry, so any rotation relates one polarization to the other; physically equivalent modes must have the same cutoff"
    - "Bessel functions happen to have paired zeros that force equal cutoff frequencies for orthogonal polarizations"
    - "Circular guides are designed to filter out one polarization, making both appear at the same threshold"
    - "The two modes actually have different cutoff frequencies in a geometrically perfect circular guide"
  answer: 0
  explanation: "Mode degeneracy is a direct consequence of the circular guide's continuous rotational symmetry. A 90° rotation maps the horizontally polarized TE₁₁ to the vertically polarized TE₁₁ exactly, so both must satisfy the same boundary conditions and have the same cutoff frequency. In a rectangular guide, the two pairs of flat walls break this symmetry, lifting the degeneracy. Option D is wrong: a perfect circular guide has exactly degenerate polarizations; only physical imperfections lift the degeneracy."

- question: "The TE₁₁ mode is labeled with n = 1 (azimuthal index) and m = 1 (radial index). A student claims that n = 1 means 'the field makes one radial half-oscillation from the center to the wall.' What is wrong with this claim?"
  type: multiple-choice
  options:
    - "Nothing — n correctly describes the number of radial half-oscillations"
    - "The radial index m counts radial zeros; n = 1 means the field completes one full oscillation as you travel around the circumference (azimuthal), not radially"
    - "Both n and m describe azimuthal behavior; neither describes the radial field variation"
    - "The labeling convention is arbitrary and has no consistent physical interpretation"
  answer: 1
  explanation: "The two indices encode physically distinct structures. The azimuthal index n describes angular variation: n = 0 is azimuthally symmetric, n = 1 means one full oscillation as you go around the full circle (360°), n = 2 means two oscillations, and so on. The radial index m counts the number of zeros in the Bessel function between the center and the wall — essentially how many radial bands the field has. Confusing the two indices leads to misidentifying which mode is propagating."

- question: "Mode degeneracy in circular waveguides is useful in rotating joints but also creates an engineering challenge because surface imperfections can couple the two degenerate polarizations."
  type: true-false
  answer: true
  explanation: "The same rotational symmetry that makes the two TE₁₁ polarizations degenerate also makes them susceptible to coupling. Any asymmetric perturbation — a slight ellipticity, conductor roughness, or non-uniformity — breaks the exact degeneracy and allows power to transfer between the two polarization modes. A clean single-polarization input can emerge as a scrambled superposition. Managing this polarization mixing is a central engineering challenge in circular-waveguide design."

- question: "In a circular waveguide, TM modes require the axial magnetic field H_z to vanish at the conducting wall, while TE modes require the axial electric field E_z to vanish at the wall."
  type: true-false
  answer: false
  explanation: "The boundary conditions are reversed. TM modes are defined by E_z ≠ 0 and H_z = 0 throughout; the boundary condition at the wall requires E_z = 0 there, giving J_n(k_c a) = 0. TE modes are defined by H_z ≠ 0 and E_z = 0 throughout; the boundary condition requires the normal derivative of H_z to vanish at the wall, giving J_n'(k_c a) = 0. Swapping which field is nonzero in each mode type is one of the most common errors in waveguide analysis."

- question: "Why do circular waveguides use Bessel functions rather than sinusoids to describe the radial field variation, and what role do the Bessel function zeros play in determining allowed modes?"
  type: short-answer
  answer: "Bessel functions are the natural solutions to the wave equation written in cylindrical coordinates — the radial part of the cylindrical Laplacian produces Bessel's equation rather than the harmonic oscillator equation. At the conducting wall (r = a), the boundary conditions require either the Bessel function (for TM modes, E_z = 0) or its derivative (for TE modes, ∂H_z/∂r = 0) to vanish. The allowed values of the transverse wavenumber k_c — and thus the cutoff frequencies — are fixed by the discrete zeros j_{nm} or j'_{nm} of J_n or J_n'."
  explanation: "Just as sinusoidal standing waves in a rectangular guide have discrete allowed wavelengths set by the wall spacing, Bessel functions in a circular guide have discrete zeros set by the radius. The Bessel zeros play exactly the same role as the integers that appear in rectangular waveguide mode conditions — they are the allowed quantized values of k_c, each corresponding to a distinct mode with its own field pattern and cutoff frequency."
```

## Explainer

In rectangular waveguides, the flat walls impose boundary conditions that the tangential electric field vanishes at each wall. With two pairs of flat walls, the solutions are products of sines and cosines — standing wave patterns in x and y. A circular guide has a cylindrical boundary instead. Applying the same wave equation in cylindrical coordinates (r, φ, z), the radial part of the solution is no longer a sine — it becomes a **Bessel function** J_n(k_c r), the natural oscillating solution to the radial wave equation in cylindrical geometry. Bessel functions look like damped sinusoids: they start positive, oscillate, and slowly decay in amplitude as their argument grows. Crucially, like sines, they pass through zero at specific values, and those zeros are what the boundary conditions latch onto.

For **TM modes** in a circular guide, the boundary condition requires the axial electric field E_z to vanish at the conducting wall (r = a): J_n(k_c a) = 0. For **TE modes**, the boundary condition requires the radial derivative of the axial magnetic field to vanish at r = a: J_n'(k_c a) = 0. In each case, the allowed values of k_c are determined by the zeros of J_n or J_n' — labeled j_{nm} and j'_{nm} respectively, where m counts which zero (m = 1, 2, 3, ...) and n is the **azimuthal order**. The cutoff frequency of mode TE_{nm} or TM_{nm} is f_c = c·j_{nm}/(2πa), so lower zeros mean lower cutoff frequencies.

The two integers in the mode label encode different physical structures. The **azimuthal index n** describes how the field varies as you travel around the circumference: n = 0 means azimuthal symmetry (field looks the same at all angles), n = 1 means one complete oscillation as you go around the full circle, n = 2 means two oscillations, and so on. The **radial index m** counts the number of radial half-periods — essentially how many zeros appear as you travel from the center to the wall. The TE₁₁ mode (first zero of J_1') has the lowest cutoff frequency in a circular guide and propagates like the TE₁₀ dominant mode in a rectangular guide.

A subtlety absent in rectangular guides is **mode degeneracy**: because a circle has full rotational symmetry, a TE₁₁ mode polarized vertically and a TE₁₁ mode polarized horizontally have exactly the same cutoff frequency. They are physically distinct modes that coexist at the same frequency. This degeneracy is useful in rotating joints — where microwave power must pass through a spinning connection — because the circular symmetry allows any polarization to propagate. However, it also creates coupling problems in real guides: surface imperfections can mix the two degenerate polarizations, converting a clean single-polarization input into a scrambled superposition. Managing this polarization mixing is a central engineering challenge in circular-waveguide applications.
