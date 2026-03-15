---
id: hartree-fock-method
title: The Hartree-Fock Self-Consistent Field Method
domain: chemistry
course: physical-chemistry
prerequisites:
- id: quantum-chemistry-foundations
  type: hard
- id: variational-principle-chemistry
  type: hard
- id: linear-algebra
  type: soft
- id: quantum-mechanics-postulates-core
  type: hard
builds-toward:
- density-functional-theory-intro
tags:
- Hartree-Fock
- self-consistent-field
- Slater-determinant
- basis-sets
- electron-correlation
- mean-field
stage: advanced
status: draft
---

# The Hartree-Fock Self-Consistent Field Method

## Core Idea
The Hartree-Fock (HF) method approximates the many-electron wavefunction as a single Slater determinant -- an antisymmetrized product of one-electron orbitals that automatically satisfies the Pauli exclusion principle. Each electron moves in the mean field of all other electrons, and the orbitals are optimized iteratively: guess orbitals, compute the mean field (Fock operator), solve for new orbitals, repeat until self-consistency. The variational principle guarantees the HF energy is an upper bound to the true energy. Basis sets (STO-3G, 6-31G*, cc-pVDZ, etc.) expand each molecular orbital in a finite set of known functions, and basis set size controls accuracy versus cost. The fundamental limitation is that HF neglects electron correlation -- the instantaneous electron-electron interactions beyond the mean-field approximation -- which typically accounts for ~1% of total energy but can be chemically decisive for bond energies and reaction barriers.

## How It's Best Learned
Run HF calculations on small molecules (H2, H2O, HF) using computational chemistry software with progressively larger basis sets. Compare the computed bond lengths and energies to experimental values and to correlated methods, seeing how the correlation energy gap persists regardless of basis set completeness.

## Common Misconceptions
- Believing Hartree-Fock includes all quantum effects; it captures exchange exactly (via the Slater determinant) but misses dynamic and static electron correlation entirely.
- Confusing basis set incompleteness error with the correlation problem; these are independent sources of error that must be addressed separately.
