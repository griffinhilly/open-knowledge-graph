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

## Explainer

In rectangular waveguides, the flat walls impose boundary conditions that the tangential electric field vanishes at each wall. With two pairs of flat walls, the solutions are products of sines and cosines — standing wave patterns in x and y. A circular guide has a cylindrical boundary instead. Applying the same wave equation in cylindrical coordinates (r, φ, z), the radial part of the solution is no longer a sine — it becomes a **Bessel function** J_n(k_c r), the natural oscillating solution to the radial wave equation in cylindrical geometry. Bessel functions look like damped sinusoids: they start positive, oscillate, and slowly decay in amplitude as their argument grows. Crucially, like sines, they pass through zero at specific values, and those zeros are what the boundary conditions latch onto.

For **TM modes** in a circular guide, the boundary condition requires the axial electric field E_z to vanish at the conducting wall (r = a): J_n(k_c a) = 0. For **TE modes**, the boundary condition requires the radial derivative of the axial magnetic field to vanish at r = a: J_n'(k_c a) = 0. In each case, the allowed values of k_c are determined by the zeros of J_n or J_n' — labeled j_{nm} and j'_{nm} respectively, where m counts which zero (m = 1, 2, 3, ...) and n is the **azimuthal order**. The cutoff frequency of mode TE_{nm} or TM_{nm} is f_c = c·j_{nm}/(2πa), so lower zeros mean lower cutoff frequencies.

The two integers in the mode label encode different physical structures. The **azimuthal index n** describes how the field varies as you travel around the circumference: n = 0 means azimuthal symmetry (field looks the same at all angles), n = 1 means one complete oscillation as you go around the full circle, n = 2 means two oscillations, and so on. The **radial index m** counts the number of radial half-periods — essentially how many zeros appear as you travel from the center to the wall. The TE₁₁ mode (first zero of J_1') has the lowest cutoff frequency in a circular guide and propagates like the TE₁₀ dominant mode in a rectangular guide.

A subtlety absent in rectangular guides is **mode degeneracy**: because a circle has full rotational symmetry, a TE₁₁ mode polarized vertically and a TE₁₁ mode polarized horizontally have exactly the same cutoff frequency. They are physically distinct modes that coexist at the same frequency. This degeneracy is useful in rotating joints — where microwave power must pass through a spinning connection — because the circular symmetry allows any polarization to propagate. However, it also creates coupling problems in real guides: surface imperfections can mix the two degenerate polarizations, converting a clean single-polarization input into a scrambled superposition. Managing this polarization mixing is a central engineering challenge in circular-waveguide applications.
