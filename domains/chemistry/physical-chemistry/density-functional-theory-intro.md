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
