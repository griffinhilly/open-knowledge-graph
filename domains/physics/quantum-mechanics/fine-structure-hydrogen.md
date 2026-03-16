---
id: fine-structure-hydrogen
title: Fine Structure and Relativistic Corrections
domain: physics
course: quantum-mechanics
prerequisites:
- id: hydrogen-atom-solution
  type: hard
- id: spin-angular-momentum
  type: hard
tags:
- fine-structure
- relativistic
stage: formal-systems
status: draft
---

# Fine Structure and Relativistic Corrections

## Core Idea
Fine structure arises from relativistic corrections and spin-orbit coupling. Total J⃗ = L⃗ + S⃗ becomes the good quantum number, splitting levels with same n, l but different j.

## Explainer

From your solution of the hydrogen atom, you know that energy levels depend only on the principal quantum number n: Eₙ = −13.6 eV / n². States with the same n but different orbital quantum number l are degenerate — they sit at exactly the same energy. This degeneracy is an artifact of the ideal Bohr model. Fine structure is what happens when you treat the electron more carefully, including corrections that the basic Schrödinger equation ignores.

Two physical effects contribute comparably to **fine structure**. First, the relativistic kinetic energy correction: the electron is moving fast enough (especially in inner orbits) that the classical p²/2m underestimates its kinetic energy. Using the full relativistic expression K = (γ − 1)mc² and expanding to order (v/c)², you get a correction term proportional to p⁴. This lowers the energy and depends on both n and l. Second, **spin-orbit coupling**: in the electron's rest frame, the proton appears to orbit it, creating a magnetic field. The electron's magnetic moment (arising from its spin s = ½) interacts with this field. The coupling energy is proportional to L⃗ · S⃗, and its size depends on n, l, and the relative orientation of L⃗ and S⃗.

Because the Hamiltonian now contains L⃗ · S⃗, the individual L_z and S_z quantum numbers m_l and m_s are no longer conserved — L⃗ and S⃗ precess around the total **J⃗ = L⃗ + S⃗**. The good quantum numbers become n, l, j, and m_j, where j = l ± ½ for an electron (since s = ½). For example, the 2p level (n = 2, l = 1) splits into two sublevels: j = 3/2 (four states) and j = 1/2 (two states). In spectroscopic notation these are written 2P₃/₂ and 2P₁/₂. The 2S₁/₂ level (l = 0, j = ½) remains close to 2P₁/₂ but is separated by the Lamb shift (a quantum electrodynamics correction, not fine structure).

The magnitude of fine structure is set by the **fine structure constant** α ≈ 1/137. The fine structure energy corrections are of order α² × 13.6 eV ≈ 10⁻³ eV — about 10,000 times smaller than the gross structure spacing. This is why spectral lines that appear single at low resolution reveal doublets and multiplets at higher resolution. The famous sodium D-line doublet (the two yellow lines at 589.0 and 589.6 nm) is a direct experimental signature of the 3P₃/₂ − 3P₁/₂ fine structure splitting.
