---
id: ferromagnetism-heisenberg-model
title: Ferromagnetism and Heisenberg Model
domain: physics
course: condensed-matter-physics
prerequisites:
- id: magnetism-paramagnetism-diamagnetism
  type: hard
- id: ising-model-statmech
  type: hard
- id: mean-field-theory
  type: soft
tags:
- ferromagnetism
- heisenberg-model
- exchange-interaction
- curie-temperature
- spontaneous-magnetization
stage: expert
status: validated
---

# Ferromagnetism and Heisenberg Model

## Core Idea
Ferromagnetism — the spontaneous alignment of magnetic moments below a Curie temperature T_C — arises from the quantum mechanical exchange interaction, not from magnetic dipole forces (which are far too weak). The Heisenberg model H = -J sum_{<ij>} S_i · S_j with J > 0 captures this: the exchange coupling J favoring parallel spins originates from the Pauli exclusion principle and Coulomb repulsion. Mean-field theory predicts T_C = zJS(S+1)/(3k_B), spontaneous magnetization below T_C, and Curie-Weiss susceptibility chi = C/(T - T_C) above T_C. Real ferromagnets (Fe, Co, Ni) have T_C values of 600-1400 K, confirming that exchange is an electronic energy scale, not a magnetic one.

## Questions

```yaml
- question: "The exchange interaction J responsible for ferromagnetism has an electrostatic origin (Coulomb repulsion + Pauli exclusion), not a magnetic one. Why is this distinction important?"
  type: multiple-choice
  options:
    - "It means ferromagnetism is not really a magnetic phenomenon"
    - "Magnetic dipole-dipole interactions between atomic moments give energies of order μ_B²/a³ ~ 0.1 K, far too small to explain Curie temperatures of ~1000 K. Exchange interactions are electrostatic (eV scale) and arise because the Pauli principle correlates spatial and spin wavefunctions — electrons with parallel spins must be spatially antisymmetric, reducing Coulomb repulsion"
    - "It means that ferromagnetism only occurs in metals"
    - "The exchange interaction is weaker than the dipole interaction but acts over longer range"
  answer: 1
  explanation: "If ferromagnetism were due to magnetic dipole forces, the ordering temperature would be ~0.1 K, not ~1000 K. The actual mechanism is exchange: the interplay between the Pauli exclusion principle (which correlates spin and spatial wavefunctions) and the Coulomb interaction (which depends on the spatial configuration). For two electrons, the triplet (parallel spin) state has an antisymmetric spatial wavefunction that keeps electrons apart, reducing Coulomb repulsion by an energy J. This exchange energy J is of order 0.01-0.1 eV, corresponding to temperatures of 100-1000 K — matching observed Curie temperatures."

- question: "Mean-field theory predicts the critical exponent β = 1/2 for the spontaneous magnetization near T_C (M ∝ (T_C - T)^{1/2}). Experiment gives β ≈ 0.33 for real ferromagnets. What causes this discrepancy?"
  type: multiple-choice
  options:
    - "Mean-field theory neglects spin-orbit coupling"
    - "Mean-field theory replaces the actual fluctuating local environment with a single effective field, ignoring correlations and critical fluctuations near T_C. Near the critical point, fluctuations on all length scales become important, and the true critical behavior is determined by universality class (dimension and symmetry), not by mean-field theory"
    - "The Heisenberg model is fundamentally incorrect for real materials"
    - "Mean-field theory uses the wrong value of S for iron"
  answer: 1
  explanation: "Mean-field theory is exact in infinite dimensions but becomes increasingly inaccurate near T_C in real (3D) systems because it ignores the correlated fluctuations that dominate near critical points. The renormalization group shows that critical exponents depend only on the spatial dimension and symmetry of the order parameter (universality class), not on microscopic details. 3D Heisenberg models have β ≈ 0.365, 3D Ising β ≈ 0.326, both far from the mean-field β = 0.5. Mean-field theory remains useful far from T_C and for estimating T_C itself."

- question: "The Heisenberg model H = -J Σ S_i · S_j treats all spin components (S^x, S^y, S^z) symmetrically. The Ising model keeps only H = -J Σ S_i^z S_j^z. How does this symmetry difference affect the physics?"
  type: true-false
  answer: true
  explanation: "This is not a true-false question as stated, but the key point is: the Heisenberg model has full SU(2) (continuous rotational) symmetry, meaning the magnetization can point in any direction. This allows Goldstone modes (spin waves/magnons) — low-energy excitations where the magnetization direction rotates smoothly. The Ising model has only Z₂ (discrete up/down) symmetry and has no such gapless excitations. In 2D, the Mermin-Wagner theorem forbids spontaneous breaking of continuous symmetry at finite T (no 2D Heisenberg ferromagnet), but the 2D Ising model can order. The symmetry of the order parameter determines the universality class and qualitative physics."

- question: "Why are iron, cobalt, and nickel ferromagnetic while most other transition metals are not?"
  type: short-answer
  answer: "Ferromagnetism requires that the exchange interaction J > 0 (favoring parallel spins) AND that the gain from exchange alignment exceeds the kinetic energy cost of spin polarization (Stoner criterion). In Fe, Co, Ni, the 3d band is narrow (high density of states at E_F) and less than half-filled or positioned such that the Stoner criterion I·g(E_F) > 1 is satisfied, where I is the exchange integral. Other transition metals like Cr, Mn, V have different band fillings where antiferromagnetic coupling or the Stoner criterion not being met prevents ferromagnetism. The specific band structure — not just the existence of d electrons — determines the magnetic ground state."
  explanation: "The Stoner criterion I·g(E_F) > 1 captures the competition: I measures the exchange energy gained by polarizing spins, g(E_F) measures how many states can be polarized at low energy cost. High g(E_F) (narrow bands, large density of states) favors ferromagnetism. This is why ferromagnetism is rare — most metals fail the criterion."
```

## Explainer

Ferromagnetism — the phenomenon behind permanent magnets — is one of the oldest known physical effects and one of the most striking demonstrations of quantum mechanics at macroscopic scales. Below the **Curie temperature** T_C, a ferromagnetic material develops a spontaneous magnetization even in zero applied field. The moments of billions of atoms align cooperatively, producing a macroscopic magnetic field. The driving force is the **exchange interaction**: a purely quantum mechanical effect arising from the interplay of the Pauli exclusion principle and Coulomb repulsion.

The **Heisenberg model** H = -J sum_{<ij>} S_i · S_j captures the essential physics. Each lattice site i carries a spin operator S_i, and the coupling J between nearest neighbors <ij> determines whether parallel alignment (J > 0, ferromagnetic) or antiparallel alignment (J < 0, antiferromagnetic) is favored. The exchange constant J is not a magnetic interaction — it is electrostatic in origin and typically 10^4 times larger than magnetic dipole energies. For two electrons, the triplet state (parallel spins, antisymmetric spatial wavefunction) and singlet state (antiparallel spins, symmetric spatial wavefunction) have different Coulomb energies because of their different spatial correlations. The energy difference is J.

**Mean-field theory** provides the simplest analysis: replace the fluctuating exchange field from neighboring spins with its thermal average, giving an effective field B_eff = zJ<S>/g mu_B, where z is the coordination number. Self-consistently solving the resulting Brillouin function equation yields the Curie temperature T_C = zJS(S+1)/(3k_B) and the Curie-Weiss susceptibility chi = C/(T - T_C) above T_C. Below T_C, the spontaneous magnetization grows continuously from zero — a second-order phase transition with the magnetization as the order parameter.

The limitations of mean-field theory become apparent near T_C, where critical fluctuations dominate and the actual critical exponents differ from mean-field predictions. The renormalization group treatment shows that the critical behavior depends only on dimension and symmetry (universality class), not on microscopic details. Away from T_C, the elementary excitations of the ordered state are **spin waves** (magnons): collective precession modes where the magnetization direction varies smoothly in space, with a characteristic omega proportional to k^2 dispersion for ferromagnets. Magnons reduce the magnetization at finite temperature, contributing to the Bloch T^{3/2} law for the spontaneous magnetization: M(T) = M(0)[1 - (T/T_C)^{3/2}] at low T.
