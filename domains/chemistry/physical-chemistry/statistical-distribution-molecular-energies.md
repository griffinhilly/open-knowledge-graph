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

## Explainer

From your work on the Maxwell-Boltzmann distribution, you already know that molecules in a gas do not all move at the same speed — there is a spread of velocities described by a characteristic bell-shaped curve that shifts and broadens with temperature. The **Boltzmann distribution** generalizes this idea from molecular speeds to any form of energy: translational, rotational, vibrational, or electronic. The central claim is deceptively simple: at thermal equilibrium, the probability of a molecule occupying a quantum state with energy Eᵢ is proportional to exp(−Eᵢ/kT), where k is Boltzmann's constant and T is absolute temperature.

The exponential factor exp(−Eᵢ/kT) is the heart of the distribution and deserves careful intuition. It says that higher-energy states are always less probable than lower-energy states, but the ratio depends on how the energy compares to kT. If Eᵢ is much smaller than kT, the exponential is close to 1 and the state is nearly as populated as the ground state. If Eᵢ is much larger than kT, the exponential is vanishingly small and essentially no molecules reach that state. The quantity kT acts as a **thermal energy scale** — at room temperature (298 K), kT ≈ 2.5 kJ/mol, which is enough to populate many rotational levels but far too small to excite most vibrational modes. This is why molecules rotate freely at room temperature but vibrate only when heated significantly.

To get the actual fraction of molecules in a particular state, you divide by the **partition function** Z = Σ exp(−Eᵢ/kT), which sums the Boltzmann factors over all accessible states. The partition function is a normalization constant, but it is far more than bookkeeping — it encodes all the thermodynamic information about the system. Once you know Z, you can derive the average energy, entropy, heat capacity, and free energy through straightforward calculus. For example, the average energy is simply ⟨E⟩ = kT² × (∂ ln Z/∂T), and the entropy is S = k ln Z + ⟨E⟩/T. The partition function is the single most important quantity in statistical mechanics.

The practical power of the Boltzmann distribution appears everywhere in chemistry. In spectroscopy, it tells you the relative populations of rotational and vibrational levels, which determines the intensity pattern of spectral lines — this is why rotational spectra show an intensity maximum at an intermediate J value rather than at J = 0. In chemical kinetics, the Boltzmann distribution explains the Arrhenius equation: the fraction of molecules with energy exceeding the activation barrier Ea is proportional to exp(−Ea/kT), which is exactly the temperature-dependent factor in the rate constant. In thermodynamics, the distribution explains why reactions become feasible at high temperatures even when they are endothermic — more molecules can access the higher-energy product states. The Boltzmann distribution is not just a formula; it is the fundamental reason that temperature controls chemistry.
