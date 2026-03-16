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
- id: quantum-tunneling
  type: soft
- id: activation-energy-catalysis-reaction-pathways
  type: soft
- id: collision-theory-advanced-kinetics
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
status: validated
---

# Transition State Theory and the Eyring Equation

## Core Idea
Transition state theory (TST) assumes that reactants are in quasi-equilibrium with the activated complex (transition state), and that the rate is proportional to the concentration of transition states multiplied by their rate of crossing the barrier. The Eyring equation k = (k_B T/h)·κ·exp(−ΔG‡/RT) provides the rate constant from the free energy of activation ΔG‡ = ΔH‡ − TΔS‡. Unlike collision theory, TST uses thermodynamic quantities for the transition state, making it straightforward to separate enthalpic (barrier height) and entropic (geometric constraint) contributions. The transmission coefficient κ accounts for recrossing trajectories and quantum tunneling (important for proton transfer reactions).

## How It's Best Learned
Analyze Eyring plots (ln(k/T) vs 1/T) for several reactions to extract ΔH‡ and ΔS‡. Interpret negative ΔS‡ as an ordered transition state (bimolecular associations) and positive ΔS‡ as a looser one (unimolecular dissociations).

## Common Misconceptions
- Treating TST as exact; it assumes no recrossing of the dividing surface, which is often violated.
- Confusing ΔG‡ (activation free energy from reactants to TS) with E_a (empirical Arrhenius activation energy); they differ by RT for simple cases.

## Questions

```yaml
- question: "A bimolecular reaction is observed to have a large negative ΔS‡. Which interpretation is most consistent with transition state theory?"
  type: multiple-choice
  options:
    - "The transition state is more disordered than the reactants, releasing entropy."
    - "The two reactants must adopt a precise, constrained geometry to reach the transition state."
    - "The activation enthalpy ΔH‡ is the dominant contribution to the reaction rate."
    - "Quantum tunneling through the barrier is significant, so κ ≪ 1."
  answer: 1
  explanation: "Entropy measures the number of accessible microstates. A large negative ΔS‡ means the transition state has far fewer accessible configurations than the reactants — both molecules must approach with the correct orientation and geometry. This entropic penalty slows the rate beyond what barrier height alone would predict. It is a hallmark of bimolecular reactions that demand tight steric and electronic alignment."

- question: "The Arrhenius activation energy E_a and the TST activation free energy ΔG‡ are equivalent quantities that can be used interchangeably."
  type: true-false
  answer: false
  explanation: "They are related but distinct. E_a is an empirical parameter extracted from the temperature dependence of ln k; it approximates the enthalpic barrier. ΔG‡ is the free energy difference between the transition state and reactants: ΔG‡ = ΔH‡ − TΔS‡. Even for a reaction with negligible entropy of activation, E_a ≈ ΔH‡ + RT, not ΔH‡ exactly. When ΔS‡ ≠ 0, the two quantities diverge further. Using E_a where ΔG‡ is required would ignore the entropic contribution to the rate."

- question: "What physical phenomenon does the transmission coefficient κ account for in the Eyring equation, and why does it become especially important for reactions involving proton transfer?"
  type: short-answer
  answer: "κ accounts for the probability that a trajectory reaching the transition state actually proceeds to products rather than recrossing back to reactants, and for quantum tunneling through the barrier. Proton transfer involves the lightest nucleus (mass ≈ 1 amu), so its de Broglie wavelength is large enough that it has significant probability of tunneling through rather than over the activation barrier, making κ substantially greater than it would be for heavier atom transfers."
  explanation: "Classical TST assumes every trajectory that reaches the top of the barrier proceeds forward — κ = 1. Real dynamics can involve recrossing (κ < 1) or tunneling (effectively κ > 1 relative to the classical rate). Protons tunnel because their small mass gives them a large quantum wavelength at thermal energies; deuterium, being twice as heavy, tunnels less, explaining the kinetic isotope effect often observed in proton-transfer reactions."
```

## Explainer

Transition state theory builds directly on potential energy surfaces, which describe how a system's energy changes as bonds break and form during a reaction. The reaction coordinate traces the path of lowest energy from reactants to products, and the highest point along that path — the saddle point — is the transition state (or activated complex). TST asks a precise question: given that the transition state exists, how fast does the reaction proceed?

The key assumption is quasi-equilibrium: the population of transition states is assumed to be in rapid equilibrium with the reactant population, governed by the Boltzmann factor exp(−ΔG‡/RT). The rate constant then equals the frequency at which transition states cross over the barrier multiplied by their equilibrium concentration. This gives the Eyring equation: k = (k_BT/h) · κ · exp(−ΔG‡/RT), where k_BT/h is a universal frequency (≈ 6 × 10¹² s⁻¹ at 298 K) and κ is the transmission coefficient. Because ΔG‡ = ΔH‡ − TΔS‡, the rate depends on both the height of the energy barrier (ΔH‡) and how constrained the geometry of the transition state is (ΔS‡). This is TST's major advantage over the Arrhenius equation, which lumps both effects into a single empirical E_a.

The entropy of activation is particularly informative. A large negative ΔS‡ means the transition state is highly ordered relative to the reactants — two molecules must find each other with precisely the right orientation, severely restricting the number of accessible configurations. This is common in bimolecular association reactions. A positive ΔS‡ indicates the transition state is looser than the reactants — a bond is substantially broken while little new constraint has been imposed — typical of unimolecular dissociations.

The transmission coefficient κ corrects for two effects that classical TST ignores. First, some trajectories that reach the barrier top recross back to reactants without proceeding forward, making κ < 1. Second, quantum tunneling allows light particles (most importantly protons) to pass *through* the barrier rather than over it. For proton transfer reactions, tunneling can make rates far higher than the classical Eyring equation predicts, explaining large kinetic isotope effects when hydrogen is replaced by deuterium.

Eyring plots — graphs of ln(k/T) versus 1/T — let you extract ΔH‡ from the slope (−ΔH‡/R) and ΔS‡ from the intercept. This separates the two thermodynamic contributions to reactivity, giving insight into whether a slow reaction suffers from a high barrier, an unfavorable geometric requirement, or both. The limitation to keep in mind is that TST is an approximation: real reaction dynamics on multidimensional potential energy surfaces do not always obey the no-recrossing assumption, and modern trajectory calculations often find κ significantly less than 1 for complex systems.


