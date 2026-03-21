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

## Questions

```yaml
- question: "The hydrogen atom has states labeled n = 2, l = 0 (the 2s orbital) and n = 2, l = 1 (the 2p orbital). How do their energies compare?"
  type: multiple-choice
  options:
    - "E(2p) > E(2s), because higher angular momentum corresponds to higher energy"
    - "E(2s) > E(2p), because s orbitals have electrons more concentrated near the nucleus"
    - "E(2s) = E(2p), because energy in hydrogen depends only on the principal quantum number n"
    - "E(2s) = E(2p) only in the ground state; for n > 1 they differ"
  answer: 2
  explanation: "In hydrogen, E_n = −13.6 eV/n² depends only on n, not on l or m_l. The 2s and 2p states are both at n = 2 and have exactly the same energy. This l-degeneracy is a special property of the Coulomb potential (related to a hidden SO(4) symmetry) and does not hold for other central potentials. In multi-electron atoms, where the effective potential deviates from pure Coulomb, this degeneracy is broken and 2s lies lower than 2p. Option A applies the classical intuition that angular momentum raises energy, which fails for the quantum hydrogen atom."

- question: "How many distinct quantum states (including spin) are at the n = 3 energy level of hydrogen?"
  type: multiple-choice
  options:
    - "3, because there are 3 allowed values of l (0, 1, 2)"
    - "9, because there are 9 combinations of l and m_l"
    - "18, because there are 9 spatial states and 2 spin states each"
    - "6, because only l = 0 and l = 1 are physically relevant for n = 3"
  answer: 2
  explanation: "The degeneracy is 2n². For n = 3: l can be 0, 1, or 2. The m_l count for each l is 2l+1: 1 + 3 + 5 = 9 spatial states. With 2 spin states each, total = 18 = 2(3²). Option B counts only spatial states (n² = 9) and forgets spin. Option A counts only the number of l values, not the m_l sublevels within each. Option D incorrectly excludes l = 2 (the 3d orbitals), which are fully accessible at n = 3."

- question: "The fact that hydrogen's energy depends only on n, and not on l, holds for all central potentials — it is a universal quantum mechanical result."
  type: true-false
  answer: false
  explanation: "The l-degeneracy is specific to the Coulomb potential V(r) ∝ 1/r, which has a hidden symmetry (SO(4)) beyond the rotational symmetry (SO(3)) that all central potentials share. For any other central potential — a harmonic oscillator, a finite square well, the screened potential of multi-electron atoms — states with different l at the same n generally have different energies. This is precisely why s, p, d orbitals split in energy in atoms beyond hydrogen."

- question: "The negative sign in E_n = −13.6 eV / n² indicates that higher n states have lower energy than the ground state."
  type: true-false
  answer: false
  explanation: "The negative sign indicates the electron is bound (bound below the ionization energy of 0 eV). Higher n states have energies closer to zero — less negative, so higher in energy. E₁ = −13.6 eV, E₂ = −3.4 eV, E₃ ≈ −1.5 eV: as n increases, energy increases toward 0. The ground state (n = 1) is the most tightly bound, with the most negative energy. The misconception reverses the ordering by confusing 'more negative' with 'lower.'"

- question: "Why does energy in hydrogen depend only on n and not on l, and what physical symmetry explains this?"
  type: short-answer
  answer: "The Coulomb potential V(r) = −e²/r has a hidden dynamical symmetry beyond ordinary rotational symmetry (SO(3)): the SO(4) symmetry corresponding to conservation of the Laplace-Runge-Lenz vector (which constrains classical Kepler orbits to be closed ellipses). Quantum mechanically, this symmetry means states with different l but the same n are related by symmetry operations and must have the same energy. For any other central potential, the LRL vector is not conserved, the SO(4) symmetry is broken, and different-l states at the same n have different energies. The hydrogen atom's l-degeneracy is a fingerprint of the 1/r potential, not a general quantum mechanical fact."
  explanation: "The classical analogue is illuminating: Kepler orbits are the only bound orbits (besides the harmonic oscillator) that are closed ellipses rather than precessing rosettes. Both the classical orbit closure and the quantum l-degeneracy stem from the same underlying SO(4) symmetry of the Coulomb potential."
```

## Explainer

From solving the hydrogen atom, you know the wavefunction is labeled by three quantum numbers: principal n (n = 1, 2, 3, …), orbital angular momentum l (0 ≤ l ≤ n−1), and magnetic m_l (−l ≤ m_l ≤ l). The remarkable result is that the energy depends on n alone: **E_n = −13.6 eV / n²**. This is not obvious — a priori you might expect the energy to depend on the shape of the orbit (l) as well. The fact that it does not is a special property of the Coulomb potential, related to a hidden symmetry (SO(4)) that classical Kepler orbits also possess. In any other central potential, l-degeneracy is broken.

The degeneracy count follows directly from the quantum number ranges. For a given n, l can take values 0, 1, …, n−1 — that is n values. For each l, m_l takes 2l+1 values. Summing: Σ_{l=0}^{n-1} (2l+1) = n². Accounting for the two spin states of the electron (m_s = ±1/2, which we include here even though it doesn't appear in the energy), the total degeneracy is **2n²**. So the n = 2 level is 8-fold degenerate, accommodating states 2s and three 2p orbitals, each with two spin states.

The energy formula predicts the spectrum. When an electron transitions from level n_i to n_f (with n_f < n_i), it emits a photon with energy ΔE = 13.6 eV (1/n_f² − 1/n_i²). Transitions down to n_f = 1 are the **Lyman series** (ultraviolet), to n_f = 2 are the **Balmer series** (visible), and to n_f = 3 are the **Paschen series** (infrared). The Balmer series is why hydrogen glows red in discharge tubes: the dominant transition is n = 3 → 2 at 656 nm. This direct connection between the energy formula and observable light frequencies was one of the great triumphs of early quantum theory.

The ground state energy −13.6 eV is also the **ionization energy** of hydrogen — the energy required to remove the electron entirely (n → ∞, E → 0). Notice the sign: negative energy means the electron is bound; n → ∞ corresponds to a free electron at rest. The n = 1 level sits deepest in the potential well, and the spacing between levels decreases as n increases (the levels crowd together toward the ionization limit). This accumulation is visible in hydrogen's spectrum as a series limit — the lines converge to a continuum above the ionization energy.


