---
id: transverse-magnetic-modes
title: Transverse Magnetic (TM) Modes
domain: physics
course: electrodynamics
prerequisites:
- id: waveguide-equations-general
  type: hard
builds-toward:
- rectangular-waveguide-propagation
- circular-waveguide-propagation
tags:
- tm-modes
- guided-waves
- cutoff-frequency
stage: advanced
status: draft
---

# Transverse Magnetic (TM) Modes

## Core Idea
TM modes have zero longitudinal magnetic field (Hz = 0) but nonzero Ez. Like TE modes, they have cutoff frequencies. The boundary condition Ez = 0 at perfect conductors determines allowed transverse wavenumbers and mode patterns.

## Explainer

From your study of general waveguide theory, you know that electromagnetic fields inside a metallic waveguide can be decomposed into two independent families: **transverse electric (TE)** modes, which have Ez = 0, and **transverse magnetic (TM)** modes, which have Hz = 0. In TM modes, the magnetic field is entirely transverse to the propagation direction, while the electric field has both transverse components and a longitudinal component Ez along the guide axis.

The governing equation for TM modes comes from substituting Hz = 0 into the waveguide equations. The longitudinal electric field satisfies the 2D Helmholtz equation in the transverse plane: (∇²ₜ + γ²c)Ez = 0, where γc = √(k² − β²) is the transverse wavenumber, k = ω/c is the free-space wavenumber, and β is the propagation constant along the guide. Once Ez is found by solving this equation with boundary conditions, all transverse field components (Eₓ, Eᵧ, Hₓ, Hᵧ) follow algebraically.

The crucial difference between TM and TE modes lies in their boundary condition. For a perfect conductor, the tangential electric field must vanish at the walls. Since Ez is tangential to the transverse walls of a rectangular guide, the condition is **Ez = 0 on all conducting surfaces**. This is a Dirichlet boundary condition for Ez, the same structure as the "particle in a box" in quantum mechanics. For a rectangular guide with width a and height b, the allowed transverse modes are Ez ∝ sin(mπx/a)sin(nπy/b) with integers m,n ≥ 1. Neither m nor n can be zero in TM modes — setting either to zero makes Ez identically zero everywhere, which would make the entire TM mode trivial. This is why the lowest TM mode in a rectangular guide is TM₁₁, unlike TE modes where TE₁₀ (with one index zero) is the fundamental mode.

Each (m,n) combination defines a **cutoff frequency** fc = (c/2π)√((mπ/a)² + (nπ/b)²) below which that mode cannot propagate — it becomes evanescent. Above cutoff, the mode propagates with phase velocity v_p = ω/β > c and group velocity v_g = dω/dβ < c, so energy travels slower than light even though phase fronts travel faster. This dispersion is a direct consequence of the transverse boundary conditions selecting only discrete wavenumbers. Understanding TM modes alongside TE modes gives you the complete modal structure of waveguides, which is the foundation for designing microwave components, cavity resonators, and antenna feed systems.
