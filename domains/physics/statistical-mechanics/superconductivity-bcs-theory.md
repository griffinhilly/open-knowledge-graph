---
id: superconductivity-bcs-theory
title: Superconductivity and BCS Theory
domain: physics
course: statistical-mechanics
prerequisites:
- id: fermi-dirac-statistics
  type: hard
- id: ideal-fermi-gas-t-equals-zero
  type: hard
tags:
- superconductivity
- pairing
- condensed-matter
stage: advanced
status: draft
---

# Superconductivity and BCS Theory

## Core Idea
BCS theory explains superconductivity as a phase transition where electrons form Cooper pairs via a phonon-mediated attractive interaction. The ground state is a superfluid of paired electrons with energy gap Δ; excitations cost finite energy, yielding zero resistance. Theory predicts isotope effects and specific heat discontinuities observed experimentally.

## Explainer

From your study of the ideal Fermi gas and Fermi-Dirac statistics, you know that at low temperatures electrons fill states up to the Fermi energy and the system behaves as a degenerate quantum gas. The puzzle of superconductivity — discovered experimentally in 1911 but unexplained until 1957 — is that below a critical temperature T_c, metals suddenly acquire zero electrical resistance and expel magnetic fields. The key insight of Bardeen, Cooper, and Schrieffer is that the Fermi sea is unstable to even a tiny attractive interaction between electrons, causing them to pair up and condense into a qualitatively different ground state.

The **phonon-mediated attraction** works like this: electron 1 passes through the lattice and attracts the positive ions toward its path. The ions respond slowly (their mass is ~10⁴ times the electron mass), so by the time electron 2 arrives at the same spot a short time later, the lattice has relaxed and the local positive charge density is still elevated. Electron 2 is attracted to this residual positive polarization left by electron 1. The net effect is a weak, retarded, attractive interaction between the two electrons, mediated by the lattice vibrations (phonons). This attraction competes with the direct Coulomb repulsion; when the phonon-mediated term wins, pairing occurs.

**Cooper's theorem** (1956) showed that this pairing has a dramatic consequence: two electrons near the Fermi surface with opposite momenta (**k**, −**k**) and opposite spins (↑, ↓) form a bound state — a **Cooper pair** — no matter how weak the attractive interaction, because the filled Fermi sea below them blocks all scattering except those preserving total momentum **k** + (−**k**) = 0. BCS theory extends this to all electrons simultaneously: the ground state is a coherent superposition of paired states, and the many-body wavefunction has a definite quantum mechanical phase. This **phase coherence** is the essence of superconductivity — the paired electrons move as a collective quantum object that cannot scatter incoherently off impurities.

The **energy gap Δ** is the binding energy per electron in a Cooper pair, and it is the key observable prediction of BCS theory. To break a pair and create an excitation costs a minimum energy 2Δ; no excitations are available below this threshold. Because all scattering processes require creating excitations, and no excitations exist below 2Δ at low temperatures, the electrical resistance is exactly zero — current flows without dissipation. The gap also predicts a **specific heat discontinuity** at T_c (a jump, not a divergence) and an **isotope effect**: T_c ∝ M^{−1/2} where M is the atomic mass, because heavier atoms vibrate more slowly, weakening the phonon coupling. Both predictions were confirmed experimentally and provided strong evidence for the phonon-pairing mechanism before the full BCS theory was published.
