---
id: diffusion-controlled-reaction-kinetics
title: Diffusion-Controlled Reaction Kinetics
domain: chemistry
course: physical-chemistry
prerequisites:
- id: collision-theory-advanced-kinetics
  type: hard
- id: diffusion-and-ficks-laws
  type: hard
- id: partial-derivatives
  type: soft
- id: autocatalytic-reactions-mechanisms
  type: soft
builds-toward:
- bimolecular-collision-dynamics-trajectory
tags:
- kinetics
- diffusion
- reaction-rate
stage: advanced
status: validated
---
# Diffusion-Controlled Reaction Kinetics

## Core Idea
Diffusion-controlled reactions reach a rate limit when reactants meet by diffusion before reacting; the measured rate is controlled by how fast reactants can approach, not their intrinsic reactivity. This limit depends on diffusion coefficients and viscosity via the Stokes-Einstein relation. Very fast reactions approach or achieve diffusion-controlled rates.

## Questions

```yaml
- question: "A radical recombination reaction is measured in two solvents: water (low viscosity) and glycerol (high viscosity). The reaction shows essentially no activation energy. What do you predict?"
  type: multiple-choice
  options:
    - "The rate is identical in both solvents — without an activation barrier, solvent doesn't matter"
    - "The rate is faster in glycerol — higher viscosity increases collision frequency"
    - "The rate is faster in water — lower viscosity means reactants diffuse together more rapidly"
    - "The rate depends only on temperature, not on solvent viscosity"
  answer: 2
  explanation: "A reaction with essentially no activation energy operates in the diffusion-controlled regime — it reacts essentially every time two molecules meet. The rate is therefore set by how quickly diffusion delivers encounter pairs. Lower viscosity means higher diffusion coefficients (via the Stokes-Einstein relation D = kT/6πηr), so reactants find each other faster in water than in glycerol. In activation-controlled reactions solvent viscosity matters little; in diffusion-controlled reactions it is the primary determinant of rate."

- question: "A chemist increases the temperature of a diffusion-controlled reaction and observes that the rate increases. What is the primary reason for this increase?"
  type: multiple-choice
  options:
    - "More molecules now have enough energy to overcome the activation barrier"
    - "Higher temperature reduces solvent viscosity, which increases diffusion coefficients and encounter frequency"
    - "The Arrhenius pre-exponential factor increases with temperature"
    - "Higher temperature increases the steric factor, making collisions more productive"
  answer: 1
  explanation: "In a diffusion-controlled reaction, there is no significant activation barrier — essentially every encounter leads to reaction. The rate increase with temperature is therefore not due to overcoming a barrier, but because higher temperature reduces solvent viscosity (via the Stokes-Einstein relation), which increases diffusion coefficients and allows reactants to encounter each other more frequently. The apparent activation energy (typically 10–20 kJ/mol) reflects the temperature dependence of viscosity, not a chemical barrier."

- question: "A diffusion-controlled reaction has a large activation energy that can only be overcome at high temperatures, which is why such reactions are faster at elevated temperatures."
  type: true-false
  answer: false
  explanation: "This describes activation-controlled kinetics, not diffusion-controlled kinetics. In diffusion-controlled reactions, the activation barrier is negligible — the chemical step occurs essentially instantaneously upon every encounter. The rate is limited by how fast reactants diffuse together, not by overcoming an energy barrier. The small apparent activation energy (10–20 kJ/mol) reflects the temperature dependence of viscosity via the Stokes-Einstein relation, not a chemical transition state."

- question: "Any measured bimolecular rate constant approaching 10⁹–10¹⁰ M⁻¹s⁻¹ in aqueous solution is a signal that the reaction may be operating near the diffusion-controlled limit."
  type: true-false
  answer: true
  explanation: "The Smoluchowski equation sets the diffusion-controlled upper bound in water at room temperature at roughly 10⁹–10¹⁰ M⁻¹s⁻¹. A measured rate constant in this range indicates that the intrinsic chemical step must be extremely fast — fast enough that diffusion has become the bottleneck. This is a practical diagnostic: if your measured k approaches this limit, you should consider whether conventional Arrhenius analysis is appropriate, since the reaction is not primarily controlled by an activation barrier."

- question: "Why do diffusion-controlled reactions show a different temperature dependence than activation-controlled reactions, and what does the apparent 'activation energy' in a diffusion-controlled reaction actually reflect?"
  type: short-answer
  answer: "In activation-controlled reactions, the Arrhenius activation energy measures the energy barrier that molecules must overcome to react; increasing temperature exponentially increases the fraction of molecules with sufficient energy. In diffusion-controlled reactions, there is essentially no barrier — every encounter leads to reaction — so the rate depends on how fast molecules encounter each other. Temperature increases the rate primarily by reducing solvent viscosity (via the Stokes-Einstein relation), which increases diffusion coefficients. The apparent activation energy (typically 10–20 kJ/mol) therefore reflects the temperature dependence of viscosity, not a chemical barrier."
  explanation: "This distinction has practical consequences: for activation-controlled reactions, you can dramatically accelerate the reaction by raising temperature, since the rate scales exponentially with 1/T. For diffusion-controlled reactions, the rate increase with temperature is much more modest (viscosity changes slowly with temperature), and the best handle on rate is solvent choice rather than temperature."
```

## Explainer

From collision theory, you know that a bimolecular reaction requires two reactant molecules to meet with sufficient energy and proper orientation. From Fick's laws, you understand that molecules in solution move by diffusion — random thermal motion governed by diffusion coefficients. **Diffusion-controlled kinetics** addresses what happens when the intrinsic chemical step (bond breaking and forming) is so fast that it occurs essentially every time two reactants encounter each other. In this limit, the overall reaction rate is no longer determined by activation energy or molecular orientation — it is determined entirely by how quickly diffusion brings the reactants together.

Think of it this way: every bimolecular reaction in solution involves two sequential processes — diffusion to form an **encounter pair** (the two molecules within reaction distance) followed by the chemical reaction itself. If the chemical step has a high activation barrier, diffusion is fast compared to reaction, and the rate is controlled by the activation energy — this is the typical "activation-controlled" regime covered by Arrhenius kinetics. But if the activation barrier is very low (or zero, as in many radical recombinations, proton transfers, and enzyme-substrate encounters), then molecules react the instant they meet. Now diffusion becomes the bottleneck — the rate cannot exceed the rate at which diffusion delivers reactant pairs.

The **Smoluchowski equation** quantifies this upper limit. It models one reactant as a stationary sphere of radius R and calculates the steady-state flux of the other reactant (with diffusion coefficient D) arriving at its surface. The resulting diffusion-controlled rate constant is k_diff = 4πR·D·Nₐ, where the relevant R and D are sums over both reactants (R = rA + rB, D = DA + DB). Using the **Stokes-Einstein relation** D = kT/(6πηr) to estimate diffusion coefficients, you can see that k_diff depends on temperature and solvent **viscosity** η. In water at room temperature, the diffusion-controlled limit works out to roughly 10⁹–10¹⁰ M⁻¹s⁻¹. Any measured rate constant approaching this magnitude signals that you are in or near the diffusion-controlled regime.

The practical consequences are significant. Diffusion-controlled reactions show an unusual temperature dependence: their rate increases with temperature primarily because viscosity decreases (faster diffusion), not because more molecules overcome an activation barrier. The apparent activation energy is small — typically 10–20 kJ/mol, reflecting the temperature dependence of viscosity rather than a chemical barrier. Solvent viscosity becomes a direct handle on the rate: the same reaction runs faster in water than in glycerol simply because molecules diffuse faster in less viscous media. Acid-base neutralizations, many fluorescence quenching processes, and radical recombinations are classic examples of reactions that operate at or near the diffusion-controlled limit.
