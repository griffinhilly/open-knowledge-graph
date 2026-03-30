---
id: density-functional-theory-cm
title: Density Functional Theory in Condensed Matter
domain: physics
course: condensed-matter-physics
prerequisites:
- id: band-structure-density-of-states
  type: hard
- id: schrodinger-equation-intro
  type: hard
tags:
- density-functional-theory
- kohn-sham
- exchange-correlation
- ab-initio
stage: expert
status: validated
---

# Density Functional Theory in Condensed Matter

## Core Idea
Density functional theory (DFT) replaces the intractable many-electron Schrodinger equation with an equivalent problem involving only the electron density n(r). The Hohenberg-Kohn theorems (1964) prove that the ground state energy is a unique functional of n(r) and that minimizing this functional yields the exact ground state density. The Kohn-Sham scheme (1965) maps the interacting problem onto non-interacting electrons moving in an effective potential that includes exchange and correlation effects. DFT with approximate exchange-correlation functionals (LDA, GGA, hybrid) has become the standard method for calculating band structures, crystal structures, lattice constants, elastic properties, and phase stability of real materials from first principles.

## Questions

```yaml
- question: "The Hohenberg-Kohn theorem states that the ground state energy is a unique functional of the electron density E = E[n(r)]. Why is this a profound simplification compared to solving the Schrodinger equation directly?"
  type: multiple-choice
  options:
    - "The density is easier to visualize than the wavefunction"
    - "The full many-body wavefunction Ψ(r₁,...,r_N) is a function of 3N coordinates (3 × 10²³ for a mole of atoms). The density n(r) is a function of just 3 coordinates, regardless of the number of electrons. The Hohenberg-Kohn theorem proves that this single function n(r) contains ALL the information needed to determine the ground state energy and all ground state properties — no information is lost in going from Ψ to n(r)"
    - "The density can be measured experimentally, unlike the wavefunction"
    - "The theorem eliminates the need for quantum mechanics"
  answer: 1
  explanation: "This dimensional reduction is the genius of DFT. A 10²³-particle wavefunction is fundamentally unknowable — you cannot store, compute, or reason about it. But the density n(r) is a simple 3D function that can be represented on a grid, computed self-consistently, and compared to experiment (via X-ray diffraction, for example). The Hohenberg-Kohn theorem guarantees that this reduction is exact in principle. The practical challenge is that the exact energy functional E[n] is unknown, and all DFT calculations use approximate functionals for the exchange-correlation contribution."

- question: "The Kohn-Sham equations look like single-particle Schrodinger equations with an effective potential V_eff(r) = V_ext(r) + V_H(r) + V_xc(r). The electrons in these equations are non-interacting. How can a non-interacting theory describe an interacting system?"
  type: multiple-choice
  options:
    - "It cannot — DFT is only an approximation"
    - "The Kohn-Sham trick: the fictitious non-interacting electrons are constructed to have the same ground state density n(r) as the real interacting system. All the many-body effects (exchange, correlation) are folded into the exchange-correlation potential V_xc = δE_xc[n]/δn(r), which is a functional of the density. The single-particle 'orbitals' are mathematical tools for computing the correct density, not physical electron states"
    - "The non-interacting electrons interact through the Hartree potential"
    - "The Kohn-Sham scheme only works for weakly interacting systems"
  answer: 1
  explanation: "This is the conceptual core of Kohn-Sham DFT. The real interacting ground state has density n(r). Kohn-Sham constructs a fictitious system of non-interacting electrons in a potential V_eff such that they produce the same n(r). The genius is that the kinetic energy of non-interacting electrons is easy to compute (sum of single-orbital kinetic energies), and the remaining 'hard' part (exchange-correlation energy) is typically small and can be approximated. The Kohn-Sham orbitals are not true electron wavefunctions, but the density they produce is (in principle) exact."

- question: "DFT with the local density approximation (LDA) systematically underestimates band gaps of semiconductors and insulators. This 'band gap problem' is not a failure of DFT itself."
  type: true-false
  answer: true
  explanation: "The Hohenberg-Kohn theorem guarantees the exact ground state density, not the exact excitation spectrum. Band gaps are excitation properties (the energy to add or remove an electron), and the Kohn-Sham eigenvalues are eigenvalues of the auxiliary non-interacting system — they have no rigorous physical meaning as quasiparticle energies. The 'band gap problem' arises because Kohn-Sham eigenvalue differences systematically underestimate the true quasiparticle gap (which requires the GW approximation or similar many-body correction). LDA typically gives gaps 30-50% too small. Hybrid functionals (mixing exact exchange) and the GW method partially correct this."

- question: "Despite its limitations, DFT has been called 'the most impactful computational method in condensed matter physics.' Justify this claim with specific examples of what DFT can predict."
  type: short-answer
  answer: "DFT routinely predicts with quantitative accuracy: (1) Crystal structures and lattice constants (to ~1% in LDA/GGA). (2) Elastic constants and phonon spectra. (3) Relative stability of different crystal phases and pressure-induced phase transitions. (4) Surface energies and adsorption geometries. (5) Magnetic ground states and magnetic moments. (6) Band structures (topology and shape, if not exact gap values). (7) Formation energies for defects, alloys, and interfaces. These predictions are 'from first principles' — requiring only atomic numbers and crystal symmetry as input, no experimental parameters. Materials databases (Materials Project, AFLOW) now contain DFT calculations for >100,000 compounds, enabling computational discovery of new materials (batteries, catalysts, thermoelectrics) before experimental synthesis."
  explanation: "The 1998 Nobel Prize in Chemistry was awarded to Walter Kohn for DFT's development. Its impact is quantifiable: DFT is the most cited method in condensed matter and materials science, used in thousands of papers per year. The combination of reasonable accuracy, computational feasibility, and parameter-free predictions makes it uniquely powerful."
```

## Explainer

The fundamental challenge of condensed matter theory is the many-body problem: N interacting electrons in N^{ion} ions, governed by the Schrodinger equation for a wavefunction Psi(r_1, ..., r_N) that depends on 3N coordinates. For a macroscopic solid, N ~ 10^{23}, and direct solution is utterly impossible. **Density functional theory** circumvents this by proving that the ground state energy is determined entirely by the electron density n(r) — a function of just three coordinates, regardless of N.

The **Hohenberg-Kohn theorems** (1964) established two results. First, the external potential V_ext(r) (and hence all properties) is a unique functional of the ground state density n(r) — there is a one-to-one mapping. Second, the true ground state density minimizes the energy functional E[n]. These theorems are exact but not directly useful because the kinetic energy functional T[n] and the exchange-correlation functional E_xc[n] are unknown. The breakthrough came with the **Kohn-Sham scheme** (1965), which maps the interacting problem onto a system of non-interacting electrons moving in an effective potential V_eff = V_ext + V_Hartree + V_xc. The non-interacting system is chosen to reproduce the exact ground state density, and its kinetic energy is computed exactly from single-particle orbitals. All the many-body complexity is isolated in E_xc[n], which is typically small and can be approximated.

The most common approximations for E_xc are the **local density approximation** (LDA), which uses the exchange-correlation energy of a uniform electron gas at the local density, and the **generalized gradient approximation** (GGA, e.g., PBE), which also includes density gradients. These approximations work remarkably well for ground state properties: lattice constants are predicted to ~1%, bulk moduli to ~5-10%, and crystal structure predictions are usually correct. The Kohn-Sham equations are solved self-consistently by iterating until the input and output densities agree, using plane-wave basis sets with pseudopotentials or augmented wave methods.

DFT's limitations are well understood. The Kohn-Sham eigenvalues are **not** quasiparticle energies, so band gaps are systematically underestimated (~30-50% in LDA/GGA). Strongly correlated systems (Mott insulators, heavy fermions) are poorly described because the exchange-correlation functional cannot capture the physics of strong on-site correlations. Van der Waals interactions are absent in standard LDA/GGA. These limitations have driven the development of extensions: hybrid functionals (B3LYP, HSE) for better gaps, DFT+U for correlated systems, RPA and GW for accurate excitation spectra, and DFT-D for dispersion corrections. Despite these caveats, DFT is the default first-principles method in condensed matter, chemistry, and materials science — it is arguably the most impactful computational method in all of physical science.
