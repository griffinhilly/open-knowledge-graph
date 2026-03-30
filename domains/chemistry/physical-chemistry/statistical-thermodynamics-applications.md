---
id: statistical-thermodynamics-applications
title: 'Statistical Thermodynamics: Properties from Partition Functions'
domain: chemistry
course: physical-chemistry
prerequisites:
- id: molecular-partition-functions
  type: hard
- id: thermochemistry-enthalpy
  type: soft
- id: equipartition-theorem
  type: soft
- id: entropy-in-thermodynamic-processes
  type: soft
- id: heat-capacity-of-gases
  type: soft
builds-toward:
- transition-state-theory
tags:
- Helmholtz
- internal-energy
- heat-capacity
- entropy
- equilibrium-constant
- standard-state
stage: expert
status: validated
---

# Statistical Thermodynamics: Properties from Partition Functions

## Core Idea
All thermodynamic functions can be derived from the partition function through standard relations: U = kT²(∂ln Q/∂T)_V, A = −kT ln Q (Helmholtz free energy), S = (U−A)/T, and G = A + pV. The heat capacity at constant volume is C_V = (∂U/∂T)_V. Equilibrium constants can be computed from the standard Gibbs energies of reactants and products, which in turn come from partition functions — enabling ab initio predictions of chemical equilibria. This framework explains why vibrational modes are 'frozen out' at low temperatures (contributing R to C_V only above their characteristic temperature θ_vib = hν/k) and provides a molecular interpretation of the third law of thermodynamics.

## How It's Best Learned
Calculate C_V as a function of temperature for a diatomic gas, showing the stepwise activation of translation (3/2 R), rotation (+R), and vibration (+R). Reconcile with the classical equipartition theorem at high temperature.

## Common Misconceptions
- Assuming equipartition always holds; it is only valid when kT >> level spacing.
- Forgetting that electronic contributions to thermodynamic functions are usually negligible unless the ground state is degenerate or excited states are low-lying.

## Questions

```yaml
- question: "A diatomic ideal gas is at a temperature where kT is much larger than the rotational energy spacing but much smaller than the vibrational energy spacing. What is the molar heat capacity C_V?"
  type: multiple-choice
  options:
    - "3/2 R (translation only)"
    - "5/2 R (translation + rotation)"
    - "7/2 R (translation + rotation + vibration)"
    - "R (rotation only)"
  answer: 1
  explanation: "When kT >> rotational level spacing, rotational modes are fully thermally populated and each contributes R/2 per degree of freedom (2 rotational DOF for a linear molecule = R total). When kT << vibrational level spacing, the vibrational mode is frozen out — it cannot be thermally excited and contributes ~0 to C_V. The translational contribution is always 3/2 R. Total: 3/2 R + R = 5/2 R. At very high temperatures where kT >> hν_vib, vibration contributes an additional R (one for KE + one for PE), giving 7/2 R."

- question: "Even well below the characteristic vibrational temperature θ_vib, vibrational modes still contribute approximately R to the molar heat capacity."
  type: true-false
  answer: false
  explanation: "Vibrational modes are quantum mechanically 'frozen out' when kT << hν_vib (equivalently, when T << θ_vib = hν/k). In this regime, nearly all molecules remain in the vibrational ground state and thermal fluctuations lack enough energy to excite the first vibrational level. The contribution to C_V drops exponentially toward zero, not to R. This freezing out is a purely quantum effect — classical equipartition, which predicts R per vibrational mode at all temperatures, fails to describe this behavior."

- question: "How does statistical thermodynamics provide a molecular interpretation of the third law of thermodynamics (S → 0 as T → 0)?"
  type: short-answer
  answer: "At absolute zero, all molecules occupy the unique ground state, so the number of accessible microstates W = 1. Since S = k ln W, this gives S = 0."
  explanation: "The Boltzmann entropy formula S = k ln W connects macroscopic entropy to the number of ways W of arranging a system at a given energy. As temperature approaches zero, thermal energy becomes insufficient to populate any state above the non-degenerate ground state, so W → 1. The logarithm of 1 is 0, giving S = 0. This is a natural result of quantum mechanics (discrete energy levels) that cannot be derived from classical thermodynamics alone. If the ground state is degenerate (W > 1), a residual entropy k ln W persists at 0 K."
```

## Explainer

The molecular partition function Q encodes everything about the statistical behavior of a system: it is the sum of Boltzmann factors e^(−E_i/kT) over all accessible energy levels, weighting each level by how likely it is to be occupied at temperature T. Once you have Q, you can derive all thermodynamic quantities from it by taking derivatives. The Helmholtz free energy A = −kT ln Q is the central bridge, and from A you get internal energy U = kT²(∂ln Q/∂T)_V, entropy S = (U − A)/T, and heat capacity C_V = (∂U/∂T)_V. This is not an approximation — it is an exact statistical mechanical result.

For an ideal molecular gas, Q factorizes into independent contributions from translational, rotational, vibrational, and electronic modes: Q = q_trans × q_rot × q_vib × q_elec. This factorization works because the energy levels of each mode are approximately independent. It means the thermodynamic functions add up as separate contributions from each mode. Translational partition functions are extremely dense (the level spacing is tiny for macroscopic containers), so translational modes are always fully excited and contribute the classical equipartition value of 3/2 R to C_V. Rotational levels have slightly larger spacing — for light molecules like H₂ they can be frozen at very low temperatures, but for most gases they are fully excited at room temperature, adding R (for linear molecules).

Vibrational modes tell a more dramatic story. The characteristic vibrational temperature θ_vib = hν/k is typically hundreds to thousands of kelvins — much higher than room temperature. Below θ_vib, the thermal energy kT cannot bridge the gap to the first excited vibrational level, so the mode is frozen out and contributes nearly zero to C_V. Above θ_vib, the mode is fully excited and contributes the classical R (½ R from kinetic energy + ½ R from potential energy of the oscillator). The stepwise activation of modes — translation always on, rotation on above a few kelvins, vibration on only at high temperatures — explains why C_V of a diatomic gas rises from 5/2 R at room temperature toward 7/2 R at very high temperatures. This behavior was a deep puzzle in classical physics; statistical mechanics resolves it completely.

Beyond heat capacities, partition functions enable ab initio computation of equilibrium constants. The standard Gibbs energy of a species is calculated from its partition functions (including zero-point energy), and K = exp(−ΔG°/RT) follows directly. This means that for a reaction with well-characterized energy surfaces, you can predict the equilibrium constant from first principles, without measuring it — a capability of enormous practical value in atmospheric chemistry, astrochemistry, and industrial catalysis.

The third law also emerges naturally here. As T → 0, the Boltzmann factor e^(−E_i/kT) → 0 for all excited states, so the partition function collapses to just the ground-state degeneracy. If the ground state is unique (W = 1), then S = k ln W = 0. This molecular picture is far more satisfying than the classical statement of the third law — it shows why entropy vanishes at absolute zero, not just that it does, and it predicts exactly when residual entropy will persist (whenever the ground state is degenerate or disordered, as in certain crystals with molecular orientational disorder).
