---
id: scattering-theory-quantum
title: Scattering Theory
domain: physics
course: quantum-mechanics
prerequisites:
- id: quantum-postulates
  type: hard
builds-toward:
- born-approximation
- partial-wave-analysis
tags:
- scattering
- cross-section
- asymptotic-states
stage: advanced
status: draft
---

# Scattering Theory

## Core Idea
Scattering theory describes collisions where particles interact via a potential V(r). Far from the interaction region, the wavefunction is a superposition of incident plane wave and outgoing scattered wave ψ ≈ e^{ikz} + f(θ,φ) e^{ikr}/r. The scattering amplitude f(θ,φ) encodes all information about the interaction; differential cross-section dσ/dΩ = |f|². Scattering theory bridges quantum mechanics and experiment.

## Explainer

Most of what we know about the subatomic world comes from scattering experiments: fire particles at a target and analyze what bounces back. Rutherford discovered the atomic nucleus by scattering alpha particles off gold foil; high-energy colliders are fundamentally scattering experiments at enormous energies. Quantum scattering theory provides the framework for connecting measured deflection patterns to the underlying potential.

The setup begins far from the interaction region, where the quantum state must approach a well-defined **asymptotic form**. From your knowledge of quantum postulates, you know the Schrödinger equation governs the wavefunction everywhere. For a particle incoming along the z-axis with momentum ℏk, the incident wavefunction is a plane wave e^{ikz}. Far from the scattering center, the full solution looks like: ψ ≈ e^{ikz} + f(θ, φ) e^{ikr}/r. The first term is the undisturbed incident wave; the second is the **scattered wave** — an outgoing spherical wave whose amplitude in direction (θ, φ) is the **scattering amplitude** f(θ, φ). The factor e^{ikr}/r ensures the scattered wave intensity falls as 1/r² at large distances (conservation of particles), while f encodes all information about the interaction.

The observable quantity in experiment is the **differential cross-section** dσ/dΩ = |f(θ, φ)|². Conceptually, dσ/dΩ measures the number of particles deflected into a small solid angle dΩ per unit incident flux. Integrating over all angles gives the **total cross-section** σ — a quantity with units of area, representing the effective "target size" of the scatterer. For a hard sphere of radius R, σ = πR² classically; quantum interference modifies this at short wavelengths. For quantum targets like atoms or nuclei, the cross-section displays sharp peaks (**resonances**) at particular energies where the scattering amplitude is greatly enhanced, signaling quasi-bound states inside the potential.

Different theoretical methods compute f(θ, φ) from V(r). The **Born approximation** treats V as a small perturbation and gives f as a Fourier transform of the potential — valid for weak or high-energy scattering, and powerfully simple. **Partial wave analysis** expands f in angular momentum eigenstates: at low energy, only a few partial waves contribute (particles with high angular momentum miss the target), making this method practical for slow-scattering problems. Both methods connect to a deep result: the **optical theorem**, which follows from probability conservation and states that σ_total = (4π/k) Im[f(0)]. The total scattering cross-section is determined by the imaginary part of the forward scattering amplitude — a remarkable consequence of unitarity that has no classical analog.
