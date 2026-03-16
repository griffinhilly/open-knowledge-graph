---
id: fine-structure-splitting
title: Fine Structure and Relativistic Corrections
domain: physics
course: quantum-mechanics
prerequisites:
- id: hydrogen-atom-spectrum
  type: hard
- id: spin-orbit-coupling
  type: hard
tags:
- hydrogen-atom
- spin-orbit
- fine-structure
stage: advanced
status: draft
---

# Fine Structure and Relativistic Corrections

## Core Idea
Fine structure arises from relativistic corrections to kinetic energy and spin-orbit coupling, splitting degenerate levels into states labeled by total angular momentum j. Hyperfine structure results from interaction between electron and nuclear spins. Both effects are small corrections crucial for precision spectroscopy and atomic clocks.

## Explainer

The Bohr model and the Schrödinger hydrogen atom give energy levels En = −13.6 eV / n². At a given n, states with different orbital quantum number ℓ are predicted to be exactly degenerate. Experimentally, they are not — spectral lines that appear single under low resolution split into closely spaced components when examined carefully. This **fine structure** is the imprint of two relativistic effects that the non-relativistic Schrödinger equation ignores.

The first correction is **relativistic kinetic energy**. The non-relativistic kinetic energy p²/2m is just the leading term in the relativistic expansion T = mc²(γ−1) ≈ p²/2m − p⁴/8m³c² + .... The next term −p⁴/8m³c² acts as a perturbation on the Schrödinger states. It is negative and largest for states where the electron has high momentum (small ℓ, which brings the electron close to the nucleus), so it lowers those levels preferentially, breaking the ℓ degeneracy. The second correction is **spin-orbit coupling**, which you already know from your prerequisite: the interaction between the electron's intrinsic spin and the magnetic field it sees due to its orbital motion around the nucleus. This interaction is proportional to L·S and also breaks the ℓ degeneracy — but in a way that depends on the relative orientation of L and S.

Because both effects mix orbital and spin degrees of freedom, neither L nor S is individually conserved; instead, the **total angular momentum** j = ℓ + s is the good quantum number. The fine-structure energy depends on n and j but not on ℓ and mⱼ separately — a result called the **j-degeneracy** that survives even after both corrections are applied (it is lifted further only by the Lamb shift, a quantum electrodynamics effect). States are labeled by spectroscopic notation nˡⱼ (e.g., 2p₁/₂ and 2p₃/₂), where the subscript j distinguishes the split levels. The energy splitting scales as α² × (13.6 eV / n³), where α ≈ 1/137 is the **fine structure constant** — which is precisely why this whole phenomenon is called fine structure.

**Hyperfine structure** is a further, much smaller splitting caused by the interaction between the electron's magnetic moment and the nuclear magnetic moment. The proton's magnetic moment is about 1/1836 times the electron's (mass ratio), so hyperfine splittings are roughly 1000× smaller than fine-structure splittings. The most famous example is the 21-cm hydrogen line (hyperfine transition of the ground state 1s), used in radio astronomy. The cesium hyperfine transition at 9,192,631,770 Hz is the definition of the SI second, illustrating how these "tiny" corrections underpin modern precision metrology.
