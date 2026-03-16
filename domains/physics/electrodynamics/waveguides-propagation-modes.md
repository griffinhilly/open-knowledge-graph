---
id: waveguides-propagation-modes
title: Electromagnetic Waveguides and Propagation Modes
domain: physics
course: electrodynamics
prerequisites:
- id: boundary-value-problems-electrostatics
  type: hard
- id: electromagnetic-waves-in-dielectrics
  type: soft
builds-toward:
- resonant-cavities-em
tags:
- waveguides
- modes
- confinement
stage: advanced
status: draft
---

# Electromagnetic Waveguides and Propagation Modes

## Core Idea
Waveguides confine and direct electromagnetic waves through structured channels (rectangular, cylindrical, optical fibers), supporting only discrete propagation modes at frequencies above a cutoff. Each mode has a unique field pattern and dispersion relation. Waveguides are fundamental to high-frequency communications, radar, microwaves, and photonics, with their mode structure determining transmission efficiency and bandwidth.

## Explainer

You already know that Maxwell's equations in a homogeneous medium admit plane-wave solutions: **E** and **B** oscillate sinusoidally and propagate in any direction. A waveguide imposes conducting walls, adding boundary conditions: the tangential E and normal B must vanish at the walls. These conditions are not satisfied by arbitrary plane waves — they sharply restrict which solutions are allowed, selecting a discrete family of **modes**.

The core method is separation of variables in the propagation direction z versus the transverse plane. Assume the fields vary as e^(i(kz−ωt)) in z, then the transverse part satisfies a 2D Helmholtz equation with the wall boundary conditions. This transverse eigenvalue problem produces discrete solutions indexed by integers (m, n) for rectangular guides, much like the quantum particle-in-a-box. Each eigenvalue gives a **transverse wave number** k⊥, and the propagation wave number follows from kz² = (ω/c)² − k⊥². The transverse modes are classified as **TE** (transverse electric, Ez = 0) or **TM** (transverse magnetic, Bz = 0) depending on which longitudinal field component is zero.

The **cutoff frequency** arises because kz² must be positive for propagation. If ω < ωc = c·k⊥, then kz² < 0, meaning kz is imaginary — the mode decays exponentially rather than propagating (an evanescent wave). Each mode has its own cutoff frequency, with the lowest-order mode (smallest k⊥) having the lowest cutoff. Operating the waveguide between the cutoff of the fundamental mode and the cutoff of the next mode guarantees **single-mode propagation**, which is essential for signal integrity. Above the second cutoff, multiple modes coexist with different phase velocities, leading to **modal dispersion** that smears out pulses.

The dispersion relation kz(ω) is not linear: the phase velocity vph = ω/kz > c (which is allowed, since phase velocity carries no energy), while the group velocity vg = dω/dkz < c is what carries information. Near cutoff, vg → 0, meaning energy barely propagates; well above cutoff, vg → c. This frequency-dependent propagation speed causes pulse broadening in waveguides, a key design constraint for broadband systems. Optical fibers are dielectric waveguides that use total internal reflection rather than conducting walls, but the modal structure — guided modes, cutoff conditions, single-mode operation — follows the same mathematical framework. The practical skill is choosing guide dimensions so that the desired operating frequency falls comfortably within the single-mode window.
