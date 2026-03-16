---
id: classical-electron-radius
title: Classical Electron Radius and Radiation Effects
domain: physics
course: electrodynamics
prerequisites:
- id: radiation-reaction-self-force
  type: hard
- id: larmor-formula
  type: hard
builds-toward:
- radiation-damping-radiation-reaction
tags:
- electron-radius
- self-energy
- classical-limit
stage: advanced
status: draft
---

# Classical Electron Radius and Radiation Effects

## Core Idea
The classical electron radius re = q²/(4πε₀mc²) ≈ 2.8 × 10⁻¹⁵ m sets the scale where radiation reaction effects become important. The ratio of radiation damping to inertial force scales as (re/r)·(a/c²), indicating when classical electrodynamics requires quantum corrections.

## Explainer

From the Larmor formula, you know that an accelerating charge radiates power P = q²a²/(6πε₀c³). From your study of radiation reaction, you know this radiated energy must come from somewhere — the charge experiences a self-force (the Abraham-Lorentz force) that acts as a back-reaction, extracting kinetic energy and converting it to radiation. The **classical electron radius** is the length scale at which this self-interaction becomes comparable to the particle's inertia, marking the boundary of classical electrodynamics' validity.

The definition r_e = q²/(4πε₀m_e c²) ≈ 2.8 × 10⁻¹⁵ m has a clean physical interpretation. The numerator, q²/(4πε₀), is proportional to the electrostatic self-energy of a sphere of charge q with radius r — the energy stored in the electric field surrounding such a ball. Setting this self-energy equal to the electron's rest-mass energy m_e c² and solving for the radius gives r_e. In other words, r_e is the classical size the electron *would need to be* if all of its rest mass originated from the energy stored in its own electric field. The actual electron has no measurable size down to ~10⁻¹⁸ m, so this "radius" is not a physical surface — it is a characteristic scale encoding the relationship between electrostatic self-energy and rest mass.

The ratio r_e/λ (where λ ~ c/ω is the wavelength of radiation being emitted) appears naturally when comparing radiation damping to inertia. For macroscopic oscillators or even atomic transitions, r_e/λ is extremely small and radiation reaction is negligible. As frequencies approach γ-ray scales or as fields probe nuclear dimensions, r_e/λ approaches unity and classical electrodynamics develops internal inconsistencies (runaway solutions to the Abraham-Lorentz equation, pre-acceleration). These pathologies signal that quantum mechanics — specifically quantum electrodynamics — must replace the classical picture at these scales.

Despite marking the failure of classical electrodynamics, r_e survives usefully in quantum physics. The **Thomson scattering cross-section** σ_T = (8π/3)r_e² ≈ 6.65 × 10⁻²⁹ m² governs how free electrons scatter electromagnetic radiation, and it is the dominant opacity source in stellar interiors and X-ray plasmas. The appearance of r_e in quantum field theory cross-sections signals that the quantum theory remembers this classical scale: r_e is not an artifact of the classical approximation but a fundamental combination of the electron charge, mass, and the speed of light that reappears wherever charge and radiation interact.
