---
id: waveguides-transmission-lines
title: Waveguides and Transmission Lines
domain: physics
course: electrodynamics
prerequisites:
- id: em-waves-in-conductors
  type: hard
- id: dispersion-relations
  type: soft
builds-toward:
- cavity-resonators
tags:
- waveguides
- transmission-lines
- modes
stage: abstract-reasoning
status: draft
---

# Waveguides and Transmission Lines

## Core Idea
Waveguides and transmission lines confine waves to propagate along a path. Metallic waveguide boundary conditions permit only discrete modes above cutoff frequency. Transmission lines support TEM modes. Essential for RF engineering, telecommunications, and accelerators.

## Explainer

From your study of EM waves in conductors, you know that a good conductor forces the tangential electric field to zero at its surface. When you enclose a wave inside a metallic tube or between two parallel conductors, these boundary conditions do not merely attenuate the wave — they fundamentally reshape what wave patterns are allowed. The result is a rich spectrum of **modes**, each a self-consistent solution to Maxwell's equations inside the guide that satisfies the conductor boundary conditions on the walls.

For a **rectangular metallic waveguide** (a hollow tube of rectangular cross-section), the boundary conditions require the transverse electric field to vanish at the walls. This quantizes the transverse wavenumber: only specific transverse spatial patterns fit cleanly inside the guide, labeled by integers (m, n) — the **TE_mn** and **TM_mn** modes (transverse electric and transverse magnetic). Each mode has a **cutoff frequency** f_c = (c/2)√((m/a)² + (n/b)²) below which it cannot propagate — it decays exponentially instead. Above cutoff, the mode propagates, but its **phase velocity** v_ph = ω/k_z = c/√(1 − (f_c/f)²) exceeds c. This is not a violation of relativity: the *group velocity* (the speed of energy and information) is v_g = c√(1 − (f_c/f)²) < c. The product v_ph × v_g = c², a characteristic of dispersive waveguide propagation that follows directly from the dispersion relation you studied earlier.

**Transmission lines** — two-conductor systems like coaxial cables or parallel wires — support a fundamentally different type of mode: the **TEM mode** (transverse electromagnetic), where both E and B are entirely transverse to the propagation direction. TEM modes have no cutoff frequency and propagate at a fixed velocity v = 1/√(με) ≈ c/√εᵣ regardless of frequency. This is why coaxial cables work all the way down to DC, while a hollow waveguide cannot propagate below its cutoff. The trade-off is that TEM requires two conductors, while a single hollow metallic tube supports only TE and TM modes.

The engineering significance is direct: designing a waveguide means choosing cross-sectional dimensions so that the desired operating frequency lies above the cutoff of the dominant (lowest) mode but below the cutoff of the next mode. This single-mode operation ensures the signal propagates cleanly without mode mixing. **Particle accelerators** use metallic cavities (closed waveguide sections) operating at specific resonant modes to accelerate charged beams; microwave ovens use waveguide feeds to deliver power to a cavity; optical fibers are the dielectric analog, guiding light through total internal reflection rather than metallic walls. In all these cases, the physics is the same: boundary conditions imposed by the confining structure quantize the allowed wave patterns and determine the propagation characteristics.
