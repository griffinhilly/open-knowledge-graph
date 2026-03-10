---
id: transition-state-theory
title: Transition State Theory and the Eyring Equation
domain: chemistry
course: physical-chemistry
prerequisites:
- id: potential-energy-surfaces
  type: hard
- id: statistical-thermodynamics-applications
  type: hard
- id: arrhenius-equation
  type: soft
- id: potential-energy
  type: soft
- id: exponential-functions-and-graphs
  type: soft
- id: maxwell-boltzmann-distribution
  type: soft
builds-toward:
- unimolecular-reaction-mechanisms
tags:
- transition-state-theory
- activated-complex
- Eyring-equation
- activation-enthalpy
- activation-entropy
- transmission-coefficient
stage: advanced
status: draft
---

# Transition State Theory and the Eyring Equation

## Core Idea
Transition state theory (TST) assumes that reactants are in quasi-equilibrium with the activated complex (transition state), and that the rate is proportional to the concentration of transition states multiplied by their rate of crossing the barrier. The Eyring equation k = (k_B T/h)·κ·exp(−ΔG‡/RT) provides the rate constant from the free energy of activation ΔG‡ = ΔH‡ − TΔS‡. Unlike collision theory, TST uses thermodynamic quantities for the transition state, making it straightforward to separate enthalpic (barrier height) and entropic (geometric constraint) contributions. The transmission coefficient κ accounts for recrossing trajectories and quantum tunneling (important for proton transfer reactions).

## How It's Best Learned
Analyze Eyring plots (ln(k/T) vs 1/T) for several reactions to extract ΔH‡ and ΔS‡. Interpret negative ΔS‡ as an ordered transition state (bimolecular associations) and positive ΔS‡ as a looser one (unimolecular dissociations).

## Common Misconceptions
- Treating TST as exact; it assumes no recrossing of the dividing surface, which is often violated.
- Confusing ΔG‡ (activation free energy from reactants to TS) with E_a (empirical Arrhenius activation energy); they differ by RT for simple cases.
