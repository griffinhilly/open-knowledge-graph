---
id: density-functional-theory-molecules
title: Density Functional Theory for Molecular Structure
domain: chemistry
course: physical-chemistry
prerequisites:
- id: variational-principle-chemistry
  type: hard
- id: electron-configuration
  type: soft
builds-toward:
- electron-correlation-approximations
tags:
- dft
- quantum
- electronic-structure
- functional
stage: expert
status: validated
---

# Density Functional Theory for Molecular Structure

## Core Idea
Density functional theory maps the complex many-electron problem onto an effective single-electron problem by expressing energy as a functional of electron density ρ(r) rather than the full wavefunction. The Kohn-Sham equations incorporate exchange-correlation effects through approximations like the local density approximation (LDA) and generalized gradient approximation (GGA). DFT is computationally efficient and remarkably accurate for many molecular properties including geometries, vibrational frequencies, and reaction barriers.

## Questions

```yaml
- question: "A molecule has 50 electrons. Compared to specifying the full many-electron wavefunction, how many spatial coordinates does the electron density ρ(r) depend on?"
  type: multiple-choice
  options:
    - "50 — one per electron"
    - "150 — three per electron"
    - "3 — regardless of the number of electrons"
    - "It depends on the basis set used in the calculation"
  answer: 2
  explanation: "The electron density ρ(r) is a function of three spatial coordinates (x, y, z) regardless of how many electrons are present. This is DFT's core advantage: the wavefunction of a 50-electron system depends on 150 spatial coordinates, making optimization exponentially harder, while the density always lives in 3D space. DFT replaces the 3N-dimensional wavefunction optimization with a 3D density optimization."

- question: "A researcher uses DFT with the PBE (GGA) functional and obtains excellent geometry predictions. A critic says 'DFT is inherently approximate because it only approximates the wavefunction.' What is the most accurate response to this critique?"
  type: multiple-choice
  options:
    - "The critic is right — DFT approximates the wavefunction and so errors are unavoidable regardless of functional choice"
    - "The Hohenberg-Kohn theorems guarantee the exact energy is a functional of density; the approximation lies in the exchange-correlation functional, not in DFT's conceptual foundation"
    - "DFT is not approximate — the Kohn-Sham equations solve the exact Schrödinger equation for the real interacting system"
    - "DFT accuracy is limited only by basis set completeness, not the choice of exchange-correlation functional"
  answer: 1
  explanation: "DFT does not approximate a wavefunction — it does not produce one at all. The Hohenberg-Kohn theorems establish that the exact ground-state energy is in principle determined by the electron density alone. The practical approximation is the exchange-correlation functional: the exact form is unknown, so LDA, GGA, and hybrid functionals are used as approximations. Option C is wrong because the Kohn-Sham equations describe a fictitious non-interacting system, not the real interacting electrons."

- question: "The Hohenberg-Kohn theorem guarantees that practical DFT calculations yield the exact ground-state energy for any molecular system."
  type: true-false
  answer: false
  explanation: "The Hohenberg-Kohn theorem establishes that the exact ground-state energy is uniquely determined by the electron density — in principle. In practice, the exact exchange-correlation functional is unknown. Every practical DFT calculation uses an approximation (LDA, GGA, hybrid, etc.), which introduces errors. The theorem guarantees the existence of an exact density-based route to the answer; it does not guarantee that our current functional approximations achieve it."

- question: "In the Kohn-Sham DFT scheme, a fictitious system of non-interacting electrons is constructed to reproduce the same electron density as the real interacting system."
  type: true-false
  answer: true
  explanation: "This is the central insight of the Kohn-Sham approach. The real many-electron problem is mapped onto an auxiliary set of non-interacting electrons whose density exactly matches the real system. These non-interacting electrons satisfy one-electron Schrödinger-like equations (the Kohn-Sham equations), which are far more tractable. All the complexity of electron-electron interaction is folded into the exchange-correlation functional."

- question: "Why does DFT scale more favorably with molecular size than exact wavefunction-based methods like full configuration interaction?"
  type: short-answer
  answer: "DFT works with the electron density — a function of only 3 spatial coordinates — rather than the N-electron wavefunction, which depends on 3N coordinates. The Kohn-Sham equations reduce the problem to N coupled one-electron equations, giving approximately O(N³) scaling. Full configuration interaction must account for all electron correlation explicitly, scaling exponentially with N. GGA and hybrid DFT functionals typically scale as O(N³), making calculations on hundreds of atoms feasible."
  explanation: "The 3D density formulation is the key: no matter how many electrons a molecule has, the density is always a function of (x, y, z). This dimensional reduction is what makes DFT practical for large systems like drug molecules or extended solids, where wavefunction methods become computationally prohibitive."
```

## Explainer

From the variational principle, you know that any trial wavefunction gives an energy at or above the true ground-state energy, and that improving the wavefunction lowers the energy toward the exact answer. The problem is that a wavefunction for N electrons depends on 3N spatial coordinates — for a molecule with 100 electrons, that is a function of 300 variables. Storing and optimizing such a function is computationally prohibitive. Density functional theory sidesteps this by recognizing that you do not need the full wavefunction: the **electron density** ρ(r), which depends on only three spatial coordinates regardless of how many electrons are present, contains all the information needed to determine the ground-state energy.

This remarkable claim rests on the **Hohenberg-Kohn theorems** (1964). The first theorem proves that the external potential (and hence all ground-state properties) is uniquely determined by the electron density. The second establishes a variational principle for the density: the true ground-state density minimizes the energy functional. In principle, you could find the exact ground-state energy by searching over all possible three-dimensional density functions — a dramatically simpler optimization than searching over 3N-dimensional wavefunctions.

The practical implementation comes from the **Kohn-Sham scheme**. Instead of tackling the interacting many-electron system directly, you set up a fictitious system of non-interacting electrons that produces the same density as the real system. Each Kohn-Sham electron occupies its own orbital and moves in an effective potential that includes the nuclear attraction, classical electron-electron repulsion (Coulomb/Hartree term), and an **exchange-correlation functional** that captures everything else — the quantum mechanical exchange interaction and electron correlation effects. The Kohn-Sham equations look like one-electron Schrödinger equations and are solved self-consistently, much like the Hartree-Fock method you may have encountered, but with the exchange-correlation functional replacing the exact exchange operator.

The catch is that the exact exchange-correlation functional is unknown. In practice, chemists use approximations arranged in a "Jacob's ladder" of increasing sophistication: the **local density approximation (LDA)** uses only the local value of ρ(r); **generalized gradient approximations (GGA)** like PBE and BLYP add dependence on the gradient ∇ρ; **hybrid functionals** like B3LYP mix in a fraction of exact Hartree-Fock exchange. Each rung generally improves accuracy but increases cost. For most molecular geometries and vibrational frequencies, GGA or hybrid functionals achieve errors comparable to much more expensive post-Hartree-Fock methods at a fraction of the computational cost — scaling as roughly N³ rather than N⁵ or worse. This favorable cost-accuracy tradeoff is why DFT dominates modern computational chemistry, from drug design to materials science.
