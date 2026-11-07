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
stage: expert
status: validated
---

# Scattering Theory

## Core Idea
Scattering theory describes collisions where particles interact via a potential V(r). Far from the interaction region, the wavefunction is a superposition of incident plane wave and outgoing scattered wave ψ ≈ e^{ikz} + f(θ,φ) e^{ikr}/r. The scattering amplitude f(θ,φ) encodes all information about the interaction; differential cross-section dσ/dΩ = |f|². Scattering theory bridges quantum mechanics and experiment.

## How It's Best Learned
Begin with a one-dimensional step or square barrier, where incident, reflected and transmitted waves play the roles of beam and scattered wave. Then move to three dimensions and derive dσ/dΩ = |f|² from the probability currents. Compare the classical hard-sphere cross section πR² with the quantum results to see what the wave picture changes.

## Common Misconceptions
- The total cross section is the target's geometric area. (It is an effective area. In quantum scattering it can differ from the geometric area by a large factor, especially near a resonance.)
- The scattering amplitude f is itself a probability. (f is a complex amplitude. The measured rate in a direction is |f|², and the phase of f matters for interference and the optical theorem.)
- A resonance is a peak at a particular scattering angle. (A resonance is a sharp rise in the cross section near a particular energy. It reflects a quasi-bound state of the potential.)

## Questions

```yaml
- question: "An experimenter measures the angular distribution of particles scattered by an atomic nucleus and finds a sharp intensity peak at θ = 30°. What does this most directly indicate?"
  type: multiple-choice
  options:
    - "The nucleus has a physical size corresponding to the scattering angle 30°"
    - "The scattering amplitude |f(30°)| is large at that angle, so the interaction sends many particles into that direction"
    - "The nucleus deflects all particles by exactly 30°, meaning the potential is directionally asymmetric"
    - "A detector artifact — quantum scattering amplitudes must be uniform across angles for a spherically symmetric potential"
  answer: 1
  explanation: "The differential cross-section dσ/dΩ = |f(θ,φ)|² measures how many particles are deflected into each direction. A sharp peak means |f| is large at that angle — the interaction strongly redirects particles there. An angular peak like this usually comes from interference between partial waves (diffraction by the target). A resonance (a quasi-bound state inside the potential) is different: it is a peak as a function of energy, not angle. The cross-section is about the interaction, not the physical dimensions of the target."

- question: "The total cross-section σ (the integral of dσ/dΩ over all solid angles) physically represents:"
  type: multiple-choice
  options:
    - "The actual geometric size of the target particle, measured in square meters"
    - "The probability that any given incident particle is deflected, independent of direction"
    - "An effective target area: a disk of area σ placed in the beam would scatter the same number of particles as the actual target"
    - "The total energy carried away from the beam by all scattered particles"
  answer: 2
  explanation: "The cross-section is an effective area, not the literal physical size of the target. If you imagine a disk of area σ placed perpendicular to the beam, it would intercept (and scatter) exactly as many particles as the actual target does. For a quantum target, σ can differ dramatically from the geometric cross-section — for hard spheres, quantum effects add diffraction corrections; near resonances, σ can far exceed the geometric area. The 'area' interpretation is an effective one encoding interaction strength."

- question: "In quantum scattering, the total cross-section of a target can exceed the classical geometric cross-section of the target's physical extent."
  type: true-false
  answer: true
  explanation: "In classical physics, scattering is geometric: only particles on a collision course with the target are deflected. In quantum mechanics, the wave nature of particles means they can be scattered even when passing well outside the classical target radius — and near resonances, the scattering amplitude is dramatically enhanced, making σ_total far exceed πR². This has no classical analog and is one of the signature features of quantum scattering that makes it fundamentally different from billiard-ball physics."

- question: "The scattering amplitude f(θ,φ) directly gives the probability of a particle being detected at angle (θ,φ) after scattering."
  type: true-false
  answer: false
  explanation: "The probability-related quantity is the differential cross-section dσ/dΩ = |f(θ,φ)|², not f itself. The scattering amplitude f is a complex number with both magnitude and phase. The phase of f is physically significant — it enters interference effects between different partial waves and is essential for the optical theorem — but probability requires the modulus squared. Confusing f with a probability amplitude in the single-particle sense misses the role of the phase, which carries independent physical information."

- question: "Explain the optical theorem: why does the total scattering cross-section equal (4π/k)Im[f(0)]? What physical principle forces this relationship?"
  type: short-answer
  answer: "The optical theorem follows from conservation of probability (unitarity). When particles scatter, some are deflected away from the forward direction, depleting the forward beam. This depletion must equal the total scattered flux in all other directions. The forward scattering amplitude f(0) encodes how the incident plane wave is modified by the scatterer — its imaginary part measures how much probability is removed from the forward beam. Setting beam depletion equal to total scattered flux (unitarity) yields σ_total = (4π/k)Im[f(0)]."
  explanation: "The result is remarkable because it connects a measurable global quantity (total cross-section, integrated over all angles) to a single quantity in one specific direction (the forward scattering amplitude). It has no classical analog — classically, forward scattering carries no information about the total scattering. The optical theorem is one of the deepest consequences of quantum mechanical unitarity and is used in nuclear, particle, and atomic physics to extract total cross-sections from forward-scattering measurements."
```

## Explainer

Most of what we know about the subatomic world comes from scattering experiments: fire particles at a target and analyze what bounces back. Rutherford discovered the atomic nucleus by scattering alpha particles off gold foil; high-energy colliders are fundamentally scattering experiments at enormous energies. Quantum scattering theory provides the framework for connecting measured deflection patterns to the underlying potential.

The setup begins far from the interaction region, where the quantum state must approach a well-defined **asymptotic form**. From your knowledge of quantum postulates, you know the Schrödinger equation governs the wavefunction everywhere. For a particle incoming along the z-axis with momentum ℏk, the incident wavefunction is a plane wave e^{ikz}. Far from the scattering center, the full solution looks like: ψ ≈ e^{ikz} + f(θ, φ) e^{ikr}/r. The first term is the undisturbed incident wave; the second is the **scattered wave** — an outgoing spherical wave whose amplitude in direction (θ, φ) is the **scattering amplitude** f(θ, φ). The factor e^{ikr}/r ensures the scattered wave intensity falls as 1/r² at large distances (conservation of particles), while f encodes all information about the interaction.

The observable quantity in experiment is the **differential cross-section** dσ/dΩ = |f(θ, φ)|². Conceptually, dσ/dΩ measures the number of particles deflected into a small solid angle dΩ per unit incident flux. Integrating over all angles gives the **total cross-section** σ — a quantity with units of area, representing the effective "target size" of the scatterer. For a hard sphere of radius R, σ = πR² classically; quantum mechanically σ → 4πR² at long wavelengths (kR ≪ 1) and σ → 2πR² at short wavelengths (kR ≫ 1), where diffraction adds a forward "shadow" peak. For quantum targets like atoms or nuclei, the cross-section displays sharp peaks (**resonances**) at particular energies where the scattering amplitude is greatly enhanced, signaling quasi-bound states inside the potential.

Different theoretical methods compute f(θ, φ) from V(r). The **Born approximation** treats V as a small perturbation and gives f as a Fourier transform of the potential — valid for weak or high-energy scattering, and powerfully simple. **Partial wave analysis** expands f in angular momentum eigenstates: at low energy, only a few partial waves contribute (particles with high angular momentum miss the target), making this method practical for slow-scattering problems. Both methods connect to a deep result: the **optical theorem**, which follows from probability conservation and states that σ_total = (4π/k) Im[f(0)]. The total scattering cross-section is determined by the imaginary part of the forward scattering amplitude — a remarkable consequence of unitarity that has no classical analog.
