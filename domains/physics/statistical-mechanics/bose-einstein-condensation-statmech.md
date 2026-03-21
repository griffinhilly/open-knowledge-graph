---
id: bose-einstein-condensation-statmech
title: Bose-Einstein Condensation and Order Parameter
domain: physics
course: statistical-mechanics
prerequisites:
- id: bose-gas-ideal-quantum
  type: hard
- id: order-parameter-phase-transition
  type: soft
builds-toward:
- phase-transition-equilibrium
- spontaneous-symmetry-breaking
tags:
- condensation
- order-parameter
- spontaneous-order
stage: advanced
status: draft
---

# Bose-Einstein Condensation and Order Parameter

## Core Idea
Below the critical temperature, a macroscopic number of bosons occupy the ground state, and the system acquires a non-zero order parameter: the condensate wavefunction ψ. This spontaneous breaking of gauge symmetry is the hallmark of a quantum phase transition and manifests in phenomena like superfluidity.

## Questions

```yaml
- question: "A system of N = 10²³ bosons is cooled below Tc, and approximately 50% of all particles pile into the single ground state. A student says: 'This is just ordinary cooling — particles always settle into the lowest energy state when temperature drops.' What does this miss about Bose-Einstein condensation?"
  type: multiple-choice
  options:
    - "The student is correct — BEC is simply the quantum version of classical particles cooling to the ground state"
    - "BEC is distinct because a macroscopic number of particles share not just the same energy but the same quantum state, including the same phase, producing long-range phase coherence that has no classical analog and enables phenomena like superfluidity"
    - "BEC differs from ordinary cooling only in requiring temperatures near absolute zero, whereas classical cooling can occur at room temperature"
    - "BEC is distinct because the particles stop obeying the Bose-Einstein distribution below Tc and instead follow Maxwell-Boltzmann statistics"
  answer: 1
  explanation: "Classical cooling means particles occupy lower-energy states, but different particles have different phases — they are incoherent. In BEC, a macroscopic fraction (O(N)) of particles share the same single quantum state, including a definite quantum phase. This coherence is qualitatively new: it cannot be captured by any classical distribution. The ground state occupation goes from O(1) to O(N) — a qualitative transition, not a smooth continuation. This macroscopic phase coherence is what enables superfluidity, where the condensate flows without viscosity because scattering it requires disrupting the coherent quantum state of O(N) particles simultaneously."

- question: "What role does spontaneous symmetry breaking play in Bose-Einstein condensation, and what symmetry is broken?"
  type: multiple-choice
  options:
    - "Below Tc, the system spontaneously picks a definite phase φ for the condensate wavefunction ψ = √(n₀)e^(iφ), even though all choices of phase are equivalent — this selection of a specific phase from the continuous U(1) symmetry is the spontaneous breaking"
    - "BEC breaks the translational symmetry of the gas, causing the particles to crystallize into a regular lattice"
    - "The broken symmetry is time-reversal symmetry, because the condensate has a preferred direction of particle flow"
    - "U(1) symmetry breaking below Tc means the total particle number N is no longer conserved in the condensate"
  answer: 0
  explanation: "The condensate wavefunction ψ = √(n₀)e^(iφ) is the order parameter. Above Tc, ψ = 0 (no definite phase). Below Tc, ψ ≠ 0 — the system selects a specific phase φ from a continuous circle of equivalent choices. This is spontaneous U(1) symmetry breaking: the Hamiltonian is symmetric under ψ → e^(iα)ψ (any global phase shift), but the ground state below Tc is not — it has a definite φ. This is the same abstract structure as ferromagnetism breaking rotational symmetry by choosing a preferred spin direction, but here applied to a quantum many-body system with a complex order parameter."

- question: "The condensate order parameter ψ is zero above Tc and nonzero below Tc, with |ψ|² equal to the fraction of particles in the ground state."
  type: true-false
  answer: true
  explanation: "The condensate wavefunction ψ = √(n₀)e^(iφ) is defined so that |ψ|² = n₀, the density of particles in the ground state. Above Tc, n₀ = O(1)/V → 0 in the thermodynamic limit, so ψ = 0 — the order parameter vanishes. Below Tc, a finite fraction N₀/N of all particles occupies the ground state, making n₀ = N₀/V a macroscopic density, so |ψ|² ≠ 0. The sharpness of this transition — from ψ = 0 to ψ ≠ 0 at Tc — identifies BEC as a genuine phase transition, not a smooth crossover."

- question: "Bose-Einstein condensation occurs in any collection of bosons whenever they are cooled sufficiently, regardless of their density."
  type: true-false
  answer: false
  explanation: "BEC requires that the thermal de Broglie wavelength λ_dB = h/√(2πmkT) become comparable to the interparticle spacing: nλ_dB³ ≈ 2.612. This means that both high enough density n and low enough temperature T are required for the condition to be met. At extremely low density, T would need to be so close to absolute zero that the condition may be experimentally unachievable. The famous 1995 experiments with ultracold atomic gases achieved BEC by combining laser cooling and evaporative cooling at densities around 10¹⁴ atoms/cm³ — a much lower density than ordinary gases, but achievable precisely because the temperature could be pushed to nanokelvin range."

- question: "Explain why phase coherence — rather than mere macroscopic ground-state occupation — is the key to superfluidity in a Bose-Einstein condensate."
  type: short-answer
  answer: "When a macroscopic number of particles share the same quantum state, they share the same phase. A superfluid flows without viscosity because viscous flow requires momentum transfer to the walls — which means scattering the condensate into a different state. But scattering O(N) phase-coherent particles simultaneously requires a large energy barrier; small perturbations cannot disturb the condensate. Ground-state occupation alone (without phase coherence) would not produce this protection — what makes the condensate rigid to perturbation is the long-range order of the phase, which turns the condensate into a single macroscopic quantum object rather than a collection of individual ground-state particles."
  explanation: "This is the conceptual core connecting BEC to superfluidity. In normal matter, viscosity arises from particles scattering off each other and the container walls — momentum gets randomized. In a superfluid, the condensate flows as a coherent quantum entity: to scatter it requires changing the quantum state of all N₀ condensate particles simultaneously, costing O(N₀) energy. Below a critical velocity, no excitation is energetically available to do this, and the flow is dissipationless. The same phase-coherence argument underlies Cooper pair condensation in superconductors and the coherent state of photons in a laser."
```

## Explainer

From your study of the ideal Bose gas, you know that bosons do not obey the Pauli exclusion principle — any number of them can occupy the same single-particle quantum state. The Bose-Einstein distribution nₖ = 1/(exp((εₖ − μ)/kT) − 1) describes the average occupation. For the chemical potential to remain negative (so that occupation numbers stay positive), μ must satisfy μ < ε₀ = 0 (the ground state energy). As temperature decreases, μ increases toward zero. At the **critical temperature** Tc, μ hits zero — and the ground state occupation n₀ = 1/(exp(−μ/kT) − 1) becomes macroscopic. Below Tc, a finite fraction of all N particles pile into the ground state. This macroscopic ground state occupation is **Bose-Einstein condensation**.

The phrase "macroscopic occupation" is key. In a normal gas at temperature T, each single-particle state has of order 1 particle on average (or much less). In the condensate, the ground state has of order N particles — a number proportional to the system size. This is a qualitative distinction. You can estimate Tc from the condition that the thermal de Broglie wavelength λ_dB becomes comparable to the interparticle spacing: nλ_dB³ ≈ 2.612. When particles are close enough together that their wavefunctions overlap significantly, they "feel" the bosonic statistics and begin to collectively pile up.

The connection to your prerequisite on **order parameters** is subtle but important. In a standard phase transition, the order parameter is a classical object (average magnetization, average density difference). For BEC, the **condensate wavefunction** ψ = √(n₀) e^(iφ) plays this role — it is a complex number, with both a magnitude (the square root of condensate density) and a phase φ. Above Tc, ψ = 0. Below Tc, ψ ≠ 0 and a definite phase is chosen, spontaneously breaking the U(1) gauge symmetry (the symmetry ψ → e^(iα)ψ). This is a quantum phase transition: the order parameter is literally a quantum mechanical wavefunction that has become macroscopic.

The physical consequences are dramatic. When a macroscopic number of particles share the same quantum state, they also share the same phase — they are **phase coherent**. This coherence is what enables **superfluidity**: the condensate flows without viscosity because there is no mechanism to scatter it into a different phase-coherent state without paying a large energy cost. The same physics appears in superconductivity (where Cooper pairs of electrons condense) and in laser light (photons in a coherent state). Bose-Einstein condensation was first achieved experimentally in ultracold atomic gases in 1995, confirming predictions made by Einstein in 1924, and has since become a leading platform for studying quantum many-body physics in controlled laboratory settings.
