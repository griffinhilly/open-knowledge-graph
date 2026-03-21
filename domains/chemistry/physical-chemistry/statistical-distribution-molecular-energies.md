---
id: statistical-distribution-molecular-energies
title: Statistical Distribution of Molecular Energies
domain: chemistry
course: physical-chemistry
prerequisites:
- id: statistical-mechanics-foundations
  type: hard
- id: maxwell-boltzmann-distribution
  type: hard
builds-toward:
- canonical-ensemble-physical-chemistry
- pre-exponential-factor-collision-theory
tags:
- statistical-mechanics
- boltzmann
- distribution
- energy
stage: advanced
status: draft
---

# Statistical Distribution of Molecular Energies

## Core Idea
At thermal equilibrium, molecular energies follow the Boltzmann distribution: the fraction of molecules in state i is proportional to exp(-Eᵢ/kT). This distribution predicts what fraction of molecules have sufficient energy for reaction (explains temperature dependence of rates), which rotational/vibrational levels are populated (explains spectra), and macroscopic thermodynamic properties. The Boltzmann distribution is the bridge between microscopic quantum states and macroscopic thermodynamics.

## Questions

```yaml
- question: "At room temperature (298 K), kT ≈ 2.5 kJ/mol. A vibrational energy level lies 40 kJ/mol above the ground state. What does the Boltzmann distribution predict for the population of this level?"
  type: multiple-choice
  options:
    - "Roughly half the molecules occupy this level, since it is accessible at room temperature"
    - "The level is essentially unpopulated — exp(−40/2.5) ≈ 10⁻⁷, so fewer than one in ten million molecules reach it"
    - "All molecules occupy the ground state; no thermal population of excited states occurs at 298 K"
    - "The fraction depends only on the degeneracy of the level, not the energy gap"
  answer: 1
  explanation: "The Boltzmann factor exp(−E/kT) = exp(−40/2.5) ≈ 10⁻⁷ means this vibrational level is almost completely unpopulated at room temperature. This is why most molecules vibrate in the ground state at 298 K — vibrational spacings are typically much larger than kT. Rotational levels (spacings ~ 0.1–1 kJ/mol) are well-populated because their energies are comparable to kT."

- question: "Which change most significantly increases the fraction of molecules with energy exceeding a fixed threshold E_a?"
  type: multiple-choice
  options:
    - "Doubling the number of molecules in the container"
    - "Doubling the absolute temperature T, because kT doubles and the Boltzmann factor exp(−E_a/kT) increases substantially"
    - "Cutting the activation energy E_a in half has no more effect than doubling T"
    - "Increasing pressure at constant temperature, because higher pressure compresses the distribution"
  answer: 1
  explanation: "The fraction of molecules exceeding E_a scales as exp(−E_a/kT). Doubling T halves E_a/kT in the exponent, dramatically increasing this fraction. For E_a = 50 kJ/mol at 300 K: exp(−50/2.49) ≈ 1.3 × 10⁻⁹. At 600 K: exp(−50/4.99) ≈ 3.6 × 10⁻⁵ — a 27,000-fold increase. This exponential sensitivity to T is why small temperature increases cause large rate accelerations."

- question: "The partition function Z = Σ exp(−Eᵢ/kT) is merely a normalization constant that ensures probabilities sum to 1."
  type: true-false
  answer: false
  explanation: "The partition function encodes all the thermodynamic information about the system. From Z you can derive the average energy (⟨E⟩ = kT² ∂ ln Z/∂T), entropy (S = k ln Z + ⟨E⟩/T), heat capacity, and free energy. Calling it 'just a normalization constant' misses that it is the single most important quantity in statistical mechanics — it bridges microscopic quantum states and macroscopic thermodynamic properties."

- question: "Increasing temperature shifts the Boltzmann distribution so that higher-energy states become more populated relative to lower-energy states."
  type: true-false
  answer: true
  explanation: "As T increases, kT increases, reducing the value of E/kT for all states. The Boltzmann factor exp(−E/kT) for higher-energy states becomes less suppressed — their fractional population increases. The distribution broadens and its peak shifts toward higher energies. This is the microscopic reason why reaction rates, spectral intensity patterns, and heat capacities all depend on temperature."

- question: "Explain why the Arrhenius equation k = A·exp(−Ea/RT) has its particular temperature dependence, connecting it to the Boltzmann distribution."
  type: short-answer
  answer: "The Arrhenius equation follows directly from the Boltzmann distribution. For a reaction to occur, colliding molecules must have kinetic energy exceeding the activation barrier Ea. The fraction of molecules with energy ≥ Ea is proportional to exp(−Ea/kT) = exp(−Ea/RT) (converting per-molecule to per-mole units). Because only these molecules can react, the rate constant is proportional to this fraction. Temperature enters only through kT — it sets the scale against which Ea is measured. When kT is much smaller than Ea (low temperature), very few molecules can react; as T rises, the fraction grows exponentially."
  explanation: "The pre-exponential factor A accounts for collision frequency and geometric orientation factors, but the temperature dependence of the rate is entirely determined by the Boltzmann distribution. This is why activation energy can be measured from the slope of ln(k) vs. 1/T — the slope equals −Ea/R."
```

## Explainer

From your work on the Maxwell-Boltzmann distribution, you already know that molecules in a gas do not all move at the same speed — there is a spread of velocities described by a characteristic bell-shaped curve that shifts and broadens with temperature. The **Boltzmann distribution** generalizes this idea from molecular speeds to any form of energy: translational, rotational, vibrational, or electronic. The central claim is deceptively simple: at thermal equilibrium, the probability of a molecule occupying a quantum state with energy Eᵢ is proportional to exp(−Eᵢ/kT), where k is Boltzmann's constant and T is absolute temperature.

The exponential factor exp(−Eᵢ/kT) is the heart of the distribution and deserves careful intuition. It says that higher-energy states are always less probable than lower-energy states, but the ratio depends on how the energy compares to kT. If Eᵢ is much smaller than kT, the exponential is close to 1 and the state is nearly as populated as the ground state. If Eᵢ is much larger than kT, the exponential is vanishingly small and essentially no molecules reach that state. The quantity kT acts as a **thermal energy scale** — at room temperature (298 K), kT ≈ 2.5 kJ/mol, which is enough to populate many rotational levels but far too small to excite most vibrational modes. This is why molecules rotate freely at room temperature but vibrate only when heated significantly.

To get the actual fraction of molecules in a particular state, you divide by the **partition function** Z = Σ exp(−Eᵢ/kT), which sums the Boltzmann factors over all accessible states. The partition function is a normalization constant, but it is far more than bookkeeping — it encodes all the thermodynamic information about the system. Once you know Z, you can derive the average energy, entropy, heat capacity, and free energy through straightforward calculus. For example, the average energy is simply ⟨E⟩ = kT² × (∂ ln Z/∂T), and the entropy is S = k ln Z + ⟨E⟩/T. The partition function is the single most important quantity in statistical mechanics.

The practical power of the Boltzmann distribution appears everywhere in chemistry. In spectroscopy, it tells you the relative populations of rotational and vibrational levels, which determines the intensity pattern of spectral lines — this is why rotational spectra show an intensity maximum at an intermediate J value rather than at J = 0. In chemical kinetics, the Boltzmann distribution explains the Arrhenius equation: the fraction of molecules with energy exceeding the activation barrier Ea is proportional to exp(−Ea/kT), which is exactly the temperature-dependent factor in the rate constant. In thermodynamics, the distribution explains why reactions become feasible at high temperatures even when they are endothermic — more molecules can access the higher-energy product states. The Boltzmann distribution is not just a formula; it is the fundamental reason that temperature controls chemistry.
