---
id: hydrogen-energy-levels
title: Energy Levels of the Hydrogen Atom
domain: physics
course: quantum-mechanics
prerequisites:
- id: hydrogen-atom-solution
  type: hard
tags:
- hydrogen-atom
- energy-levels
stage: advanced
status: draft
---

# Energy Levels of the Hydrogen Atom

## Core Idea
Energy depends only on principal quantum number: E_n = −13.6 eV / n². Each level has degeneracy (2n)² from varying l and m_l. This formula predicts spectral lines.

## Explainer

From solving the hydrogen atom, you know the wavefunction is labeled by three quantum numbers: principal n (n = 1, 2, 3, …), orbital angular momentum l (0 ≤ l ≤ n−1), and magnetic m_l (−l ≤ m_l ≤ l). The remarkable result is that the energy depends on n alone: **E_n = −13.6 eV / n²**. This is not obvious — a priori you might expect the energy to depend on the shape of the orbit (l) as well. The fact that it does not is a special property of the Coulomb potential, related to a hidden symmetry (SO(4)) that classical Kepler orbits also possess. In any other central potential, l-degeneracy is broken.

The degeneracy count follows directly from the quantum number ranges. For a given n, l can take values 0, 1, …, n−1 — that is n values. For each l, m_l takes 2l+1 values. Summing: Σ_{l=0}^{n-1} (2l+1) = n². Accounting for the two spin states of the electron (m_s = ±1/2, which we include here even though it doesn't appear in the energy), the total degeneracy is **2n²**. So the n = 2 level is 8-fold degenerate, accommodating states 2s and three 2p orbitals, each with two spin states.

The energy formula predicts the spectrum. When an electron transitions from level n_i to n_f (with n_f < n_i), it emits a photon with energy ΔE = 13.6 eV (1/n_f² − 1/n_i²). Transitions down to n_f = 1 are the **Lyman series** (ultraviolet), to n_f = 2 are the **Balmer series** (visible), and to n_f = 3 are the **Paschen series** (infrared). The Balmer series is why hydrogen glows red in discharge tubes: the dominant transition is n = 3 → 2 at 656 nm. This direct connection between the energy formula and observable light frequencies was one of the great triumphs of early quantum theory.

The ground state energy −13.6 eV is also the **ionization energy** of hydrogen — the energy required to remove the electron entirely (n → ∞, E → 0). Notice the sign: negative energy means the electron is bound; n → ∞ corresponds to a free electron at rest. The n = 1 level sits deepest in the potential well, and the spacing between levels decreases as n increases (the levels crowd together toward the ionization limit). This accumulation is visible in hydrogen's spectrum as a series limit — the lines converge to a continuum above the ionization energy.


