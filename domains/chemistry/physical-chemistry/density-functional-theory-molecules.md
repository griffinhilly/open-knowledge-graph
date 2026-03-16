---
id: density-functional-theory-molecules
title: Density Functional Theory for Molecular Structure
domain: chemistry
course: physical-chemistry
prerequisites:
- id: variational-principle-quantum-chemistry
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
stage: advanced
status: draft
---

# Density Functional Theory for Molecular Structure

## Core Idea
Density functional theory maps the complex many-electron problem onto an effective single-electron problem by expressing energy as a functional of electron density ρ(r) rather than the full wavefunction. The Kohn-Sham equations incorporate exchange-correlation effects through approximations like the local density approximation (LDA) and generalized gradient approximation (GGA). DFT is computationally efficient and remarkably accurate for many molecular properties including geometries, vibrational frequencies, and reaction barriers.

## Explainer

From the variational principle, you know that any trial wavefunction gives an energy at or above the true ground-state energy, and that improving the wavefunction lowers the energy toward the exact answer. The problem is that a wavefunction for N electrons depends on 3N spatial coordinates — for a molecule with 100 electrons, that is a function of 300 variables. Storing and optimizing such a function is computationally prohibitive. Density functional theory sidesteps this by recognizing that you do not need the full wavefunction: the **electron density** ρ(r), which depends on only three spatial coordinates regardless of how many electrons are present, contains all the information needed to determine the ground-state energy.

This remarkable claim rests on the **Hohenberg-Kohn theorems** (1964). The first theorem proves that the external potential (and hence all ground-state properties) is uniquely determined by the electron density. The second establishes a variational principle for the density: the true ground-state density minimizes the energy functional. In principle, you could find the exact ground-state energy by searching over all possible three-dimensional density functions — a dramatically simpler optimization than searching over 3N-dimensional wavefunctions.

The practical implementation comes from the **Kohn-Sham scheme**. Instead of tackling the interacting many-electron system directly, you set up a fictitious system of non-interacting electrons that produces the same density as the real system. Each Kohn-Sham electron occupies its own orbital and moves in an effective potential that includes the nuclear attraction, classical electron-electron repulsion (Coulomb/Hartree term), and an **exchange-correlation functional** that captures everything else — the quantum mechanical exchange interaction and electron correlation effects. The Kohn-Sham equations look like one-electron Schrödinger equations and are solved self-consistently, much like the Hartree-Fock method you may have encountered, but with the exchange-correlation functional replacing the exact exchange operator.

The catch is that the exact exchange-correlation functional is unknown. In practice, chemists use approximations arranged in a "Jacob's ladder" of increasing sophistication: the **local density approximation (LDA)** uses only the local value of ρ(r); **generalized gradient approximations (GGA)** like PBE and BLYP add dependence on the gradient ∇ρ; **hybrid functionals** like B3LYP mix in a fraction of exact Hartree-Fock exchange. Each rung generally improves accuracy but increases cost. For most molecular geometries and vibrational frequencies, GGA or hybrid functionals achieve errors comparable to much more expensive post-Hartree-Fock methods at a fraction of the computational cost — scaling as roughly N³ rather than N⁵ or worse. This favorable cost-accuracy tradeoff is why DFT dominates modern computational chemistry, from drug design to materials science.
