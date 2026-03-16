---
id: transverse-electric-modes
title: Transverse Electric (TE) Modes
domain: physics
course: electrodynamics
prerequisites:
- id: waveguide-equations-general
  type: hard
builds-toward:
- rectangular-waveguide-propagation
- circular-waveguide-propagation
tags:
- te-modes
- guided-waves
- cutoff-frequency
stage: advanced
status: draft
---

# Transverse Electric (TE) Modes

## Core Idea
TE modes have zero longitudinal electric field (Ez = 0) but nonzero Hz. They exist for all frequencies above a cutoff frequency ωc, determined by boundary conditions. Below cutoff, the longitudinal wave vector becomes imaginary and modes are evanescent.

## Explainer

From your prerequisite on waveguide equations, you know that a hollow metallic waveguide supports guided waves by confining the electromagnetic field between conducting walls. The general solution strategy is to decompose the field into a longitudinal part (along the propagation axis z) and transverse parts (in the xy-plane), then classify modes by which longitudinal components are nonzero. **Transverse electric (TE) modes** are defined by the condition Ez = 0: the electric field has no component along the propagation direction, but the magnetic field does (Hz ≠ 0). This is in contrast to TM modes (Hz = 0, Ez ≠ 0) and TEM modes (both zero, which require two separate conductors).

The defining feature of TE modes is the **cutoff frequency**. Substituting Ez = 0 into Maxwell's equations and applying the conducting boundary conditions (tangential E = 0 at the walls) forces Hz to satisfy a two-dimensional Helmholtz equation in the cross-section with Neumann boundary conditions (∂Hz/∂n = 0 at the walls). The eigenvalues of this problem are discrete, labeled by integers (m, n) for a rectangular guide, and each eigenvalue determines a **cutoff frequency** ωc,mn. For a rectangular waveguide of dimensions a × b, the cutoff frequencies are ωc,mn = c·π√((m/a)² + (n/b)²). The mode with the lowest cutoff is called the **dominant mode** — for a rectangular guide it is TE₁₀.

Above the cutoff frequency, the longitudinal wavenumber kz = √(ω²/c² − kc²) is real and positive, meaning the mode propagates along the guide as a traveling wave with phase velocity vph = ω/kz > c. (The group velocity vg = c²/vph < c; information travels at group velocity.) Below cutoff, kz becomes imaginary: kz = iγ with γ real and positive. The mode decays exponentially as e^(−γz) — it is **evanescent** rather than propagating. This is analogous to total internal reflection in optics or quantum tunneling below a barrier: the mode tries to propagate but is forbidden by the boundary geometry, and instead decays within a few skin depths.

In practice, a waveguide is typically operated in a frequency range where only the dominant TE₁₀ mode propagates, while all higher modes are below their cutoffs and thus evanescent. This single-mode operation avoids interference between modes and preserves signal integrity. Understanding TE modes — how to identify them, compute their cutoff frequencies, and determine their field patterns — is foundational for designing microwave components including filters, horns, cavities, and antenna feeds.
