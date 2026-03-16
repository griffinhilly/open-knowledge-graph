---
id: electron-correlation-approximations
title: Electron Correlation and Computational Approximations
domain: chemistry
course: physical-chemistry
prerequisites:
- id: density-functional-theory-molecules
  type: soft
- id: molecular-orbital-theory-advanced
  type: hard
tags:
- correlation
- approximations
- quantum-chemistry
- methods
stage: advanced
status: draft
---

# Electron Correlation and Computational Approximations

## Core Idea
Electron correlation refers to the instantaneous repulsion between electrons that causes their positions to be interdependent. Mean-field methods (Hartree-Fock, DFT) neglect dynamic correlation, leading to systematic errors. Configuration interaction, coupled cluster, and perturbation theory methods recover correlation at increasing computational cost. Understanding when approximations are valid is crucial for accurate chemical predictions.

## Explainer

From molecular orbital theory, you know that the Hartree-Fock (HF) method finds the best single-determinant wavefunction — it assigns each electron to a molecular orbital and accounts for electron-electron repulsion only in an averaged way. Each electron moves in the **mean field** created by all the other electrons, as if they were smeared-out charge clouds. This is a powerful approximation, but it misses something fundamental: electrons are not smeared out. They are point charges that avoid each other instantaneously. The energy error introduced by ignoring this instantaneous avoidance is the **correlation energy**, defined as the difference between the exact non-relativistic energy and the Hartree-Fock energy. For most molecules, this error is on the order of 1 eV per electron pair — seemingly small on an absolute scale, but often comparable to the energy differences that determine reaction barriers, bond strengths, and molecular geometries.

The simplest post-Hartree-Fock approach is **Møller-Plesset perturbation theory** (MP2), which treats correlation as a perturbation to the HF solution. It recovers a large fraction of the correlation energy at modest computational cost (scaling as N⁵ with system size) by mixing in doubly-excited determinants — configurations where two electrons have been promoted from occupied to virtual orbitals. MP2 works well for many ground-state properties but can fail badly for systems with near-degenerate orbitals or significant multireference character. **Configuration interaction** (CI) takes a more systematic approach: it constructs the wavefunction as a linear combination of the HF determinant and all possible excited determinants (singles, doubles, triples, etc.). Full CI — including all excitations — gives the exact answer within a given basis set, but scales factorially and is feasible only for tiny molecules. Truncated CI (e.g., CISD, including only singles and doubles) is practical but suffers from a subtle flaw: it is not **size-consistent**, meaning the energy of two non-interacting molecules computed together does not equal the sum of their separate energies.

**Coupled cluster theory** (CC) solves the size-consistency problem by using an exponential ansatz: Ψ = exp(T)|Φ_HF⟩, where T is a cluster operator that generates excitations. The exponential structure automatically includes disconnected higher excitations (e.g., products of double excitations) even when T is truncated. CCSD(T) — coupled cluster with singles, doubles, and perturbative triples — is often called the "gold standard" of quantum chemistry because it recovers ~99% of the correlation energy for well-behaved single-reference systems. Its computational cost scales as N⁷, limiting it to molecules with roughly a few dozen heavy atoms, but it serves as the benchmark against which cheaper methods are calibrated.

The practical challenge is choosing the right method for the right problem. DFT with modern functionals captures much of the correlation energy at low cost (N³–N⁴ scaling) and is the workhorse for large systems, but its accuracy depends on the functional chosen and it can fail unpredictably for dispersion interactions, transition states, or strongly correlated systems. MP2 is reliable for weak interactions but overkills simple geometries. CCSD(T) is the arbiter of accuracy but is too expensive for routine use on large molecules. The art of computational chemistry lies in matching the level of theory to the question being asked — using cheap methods for screening and expensive methods for definitive answers on the quantities that matter most.
