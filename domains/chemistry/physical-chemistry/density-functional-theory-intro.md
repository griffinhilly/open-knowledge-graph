---
id: density-functional-theory-intro
title: 'Introduction to Density Functional Theory: From Wavefunctions to Electron
  Density'
domain: chemistry
course: physical-chemistry
prerequisites:
- id: hartree-fock-method
  type: hard
- id: variational-principle-quantum-chemistry
  type: soft
- id: schrodinger-equation-intro
  type: hard
- id: variational-method-quantum
  type: soft
- id: quantum-mechanics-postulates-core
  type: soft
builds-toward: []
tags:
- DFT
- Hohenberg-Kohn
- Kohn-Sham
- exchange-correlation
- electron-density
- computational-chemistry
stage: advanced
status: draft
---

# Introduction to Density Functional Theory: From Wavefunctions to Electron Density

## Core Idea
Density functional theory (DFT) reformulates quantum mechanics so that the electron density rho(r) -- a function of just three spatial variables -- replaces the 3N-variable many-electron wavefunction as the fundamental quantity. The Hohenberg-Kohn theorems prove that (1) the ground-state energy is a unique functional of the density, and (2) the true density minimizes this energy functional. In practice, the Kohn-Sham approach maps the interacting electron problem onto a fictitious system of non-interacting electrons moving in an effective potential, reducing the problem to solving one-electron equations self-consistently -- similar in structure to Hartree-Fock but with an exchange-correlation functional that, in principle, captures all many-body effects. The accuracy and computational efficiency of DFT depend critically on the choice of exchange-correlation functional (LDA, GGA, hybrid functionals like B3LYP), which must be approximated since the exact form is unknown.

## How It's Best Learned
Compare DFT and HF results for the same molecules and properties (geometries, atomization energies, dipole moments), using different functionals. This builds intuition for when DFT outperforms HF (correlated systems) and where common functionals fail (dispersion interactions, strongly correlated systems, band gaps).

## Common Misconceptions
- Treating DFT as inherently approximate; the Hohenberg-Kohn theorems are exact -- it is only the exchange-correlation functional that is approximated.
- Assuming more expensive functionals are always more accurate; the "Jacob's ladder" of functionals (LDA < GGA < hybrid < double-hybrid) generally improves accuracy but not uniformly for all properties.

## Explainer

From Hartree-Fock theory, you know the fundamental challenge of quantum chemistry: the Schrödinger equation for a many-electron system is impossible to solve exactly because every electron interacts with every other electron. Hartree-Fock handles this by approximating each electron as moving in the average field of all the others, which captures exchange (the antisymmetry requirement from the Pauli principle) but completely misses **electron correlation** — the fact that electrons dynamically avoid each other beyond what the average field predicts. Post-HF methods (MP2, CCSD, etc.) recover correlation but become extremely expensive as system size grows. DFT offers a fundamentally different strategy.

The intellectual breakthrough of DFT is the **Hohenberg-Kohn theorem** (1964): the ground-state energy of any system of electrons in an external potential is uniquely determined by the electron density ρ(r) alone. Think about what this means — instead of needing a wavefunction that depends on 3N variables (three coordinates per electron, with N potentially being hundreds of atoms), you only need the electron density, which is always a function of just three spatial variables regardless of system size. The second Hohenberg-Kohn theorem adds that the true ground-state density is the one that minimizes the energy functional. In principle, if you knew the exact energy functional E[ρ], you could find the exact ground-state energy by minimizing it with respect to the density. The problem is that nobody knows the exact functional.

The practical implementation comes from **Kohn and Sham** (1965), who introduced a clever workaround. They imagined a fictitious system of non-interacting electrons that has the same density as the real interacting system. For non-interacting electrons, the kinetic energy and Coulomb energy are straightforward to compute. Everything that is left over — the difference between the true kinetic energy and the non-interacting kinetic energy, plus all the non-classical electron-electron interaction effects — gets swept into a single term called the **exchange-correlation functional** E_xc[ρ]. The Kohn-Sham equations look remarkably like Hartree-Fock equations (one-electron equations solved self-consistently), but they include an exchange-correlation potential that, in principle, captures all many-body effects exactly. The computational cost scales similarly to HF — roughly as N³ to N⁴ — making DFT applicable to systems with hundreds of atoms.

The entire accuracy question in DFT reduces to: how good is your approximation to E_xc[ρ]? The **Local Density Approximation (LDA)** treats the density as locally uniform, borrowing results from the homogeneous electron gas. It works surprisingly well for solids but overbinds molecules. **Generalized Gradient Approximations (GGA)**, like PBE and BLYP, add dependence on the gradient of the density and significantly improve molecular geometries and energies. **Hybrid functionals** like B3LYP mix in a fraction of exact Hartree-Fock exchange, which corrects many of GGA's systematic errors. This hierarchy — Perdew's "Jacob's ladder" — climbs toward the exact functional but never quite reaches it. Choosing a functional for a given problem is part science, part experience: B3LYP is a reliable default for organic molecules, PBE works well for solids, and dispersion-corrected functionals (DFT-D3, ωB97X-D) are essential when non-covalent interactions matter.
