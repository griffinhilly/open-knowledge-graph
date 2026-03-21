---
id: transition-state-theory-and-kinetics
title: Transition State Theory and Reaction Rate Constants
domain: chemistry
course: physical-chemistry
prerequisites:
- id: transition-state-theory
  type: hard
- id: elementary-reaction-mechanisms-catalysis
  type: soft
builds-toward:
- quantum-tunneling-and-reaction-rates
tags:
- kinetics
- transition-state
- activation-barrier
- rate-constants
stage: advanced
status: draft
---

# Transition State Theory and Reaction Rate Constants

## Core Idea
Transition state theory (TST) models reactions as passage over a free-energy barrier; k = (κ kB T / h) exp(−ΔG‡ / RT) relates rate to activation free energy and transmission coefficient κ. TST elegantly connects reaction rates to structure (via quantum-calculated transition-state geometry) and is foundational for catalysis design and enzyme kinetics. Its main limitation is assumption of transition-state equilibrium.

## How It's Best Learned
Calculate transition-state geometries for simple reactions (H + H₂ abstraction, SN2 nucleophilic attack) using quantum chemistry; predict rate constants and compare to experiment; examine how catalysts lower ΔG‡ without changing substrate or product energy.

## Common Misconceptions
- Assuming TST predicts rates exactly; transmission coefficient κ (≤ 1) accounts for dynamical recrossing, especially important when multiple TSs compete. - Treating transition-state geometry as unique; multiple local maxima on PES can contribute to TST rate expression.

## Questions

```yaml
- question: "Two reactions have identical activation enthalpies ΔH‡ = 50 kJ/mol, but reaction A involves two freely diffusing molecules combining into a tight cyclic transition state, while reaction B is a unimolecular rearrangement. At the same temperature, which reaction is faster?"
  type: multiple-choice
  options:
    - "Reaction A — bimolecular reactions always have more collision opportunities"
    - "Reaction B — the unimolecular rearrangement has a less negative activation entropy ΔS‡"
    - "They are identical — only ΔH‡ determines the rate constant in TST"
    - "Reaction A — higher molecularity means higher pre-exponential factor"
  answer: 1
  explanation: "TST gives k = (κ k_BT/h) · exp(−ΔG‡/RT) where ΔG‡ = ΔH‡ − TΔS‡. Even with equal ΔH‡, reaction A has a large negative ΔS‡ because two freely translating, rotating molecules must come together in a highly ordered, constrained transition state — losing translational and rotational degrees of freedom. This raises ΔG‡ and slows the reaction. The unimolecular rearrangement has a much smaller entropic penalty (ΔS‡ ≈ 0 or mildly negative). Ignoring entropy in TST is a common error that leads to wrong rate predictions."

- question: "An enzyme reduces ΔG‡ from 80 kJ/mol to 60 kJ/mol at 310 K (body temperature). By what factor does the rate increase? (Use RT ≈ 2.57 kJ/mol)"
  type: multiple-choice
  options:
    - "About 2-fold — a 20 kJ/mol reduction is modest"
    - "About 40-fold — reflecting the exponential sensitivity"
    - "About 2,800-fold — the exponential of 20/2.57 ≈ e^7.8"
    - "About 10^7-fold — catalysis always gives astronomical rate enhancements"
  answer: 2
  explanation: "The rate ratio is exp(ΔΔG‡/RT) = exp(20/2.57) = exp(7.78) ≈ 2,400. Option C is closest (e^7.8 ≈ 2,440; using 2.57 gives ~2,400). This illustrates exponential sensitivity to ΔG‡: a seemingly modest 20 kJ/mol reduction translates to roughly a 2,000-fold rate enhancement. The statement in the explainer — 5.7 kJ/mol reduction gives 10-fold increase — follows from the same logic: exp(5.7/2.57·ln10) ≈ 10. Enzymes achieving reductions of 20–50 kJ/mol can accelerate reactions by factors of 10^3 to 10^8."

- question: "According to transition state theory, a catalyst increases the reaction rate by raising the energy of the reactants relative to the transition state."
  type: true-false
  answer: false
  explanation: "A catalyst lowers the activation free energy ΔG‡ by providing an alternative reaction pathway with a lower-energy transition state — it does not change the energy of the reactants or products. The free energy difference between reactants and products (reaction thermodynamics, ΔG) is unaffected by catalysis. Raising the reactant energy would also increase the reverse reaction rate identically, and it is not how catalysts function. Enzymes work by stabilizing the transition state through electrostatic interactions, precise substrate positioning, and covalent intermediates."

- question: "A reaction can be slow even when the activation enthalpy ΔH‡ is small, if the activation entropy ΔS‡ is large and negative."
  type: true-false
  answer: true
  explanation: "ΔG‡ = ΔH‡ − TΔS‡. A large negative ΔS‡ (highly organized transition state) adds a positive contribution to ΔG‡, raising the barrier and slowing the reaction regardless of how small ΔH‡ is. This is particularly important for reactions that bring together two large molecules in a precisely ordered geometry. The entropic cost of organizing a bimolecular transition state can easily be 50–100 J/mol·K, which at 300 K contributes 15–30 kJ/mol to ΔG‡ — enough to slow a reaction by 3–5 orders of magnitude relative to what ΔH‡ alone would predict."

- question: "Why can a bimolecular reaction be slow even when its activation enthalpy ΔH‡ is relatively small?"
  type: short-answer
  answer: "The activation free energy ΔG‡ = ΔH‡ − TΔS‡ depends on both enthalpic and entropic terms. A bimolecular reaction that brings two freely moving molecules into a single, tightly ordered transition state pays a large entropic penalty (ΔS‡ << 0), because translational and rotational degrees of freedom are lost. Even if ΔH‡ is small, the TΔS‡ term adds a substantial positive contribution to ΔG‡, slowing the reaction by orders of magnitude. A slow reaction with small ΔH‡ is often entropically controlled."
  explanation: "This insight is why many enzyme mechanisms are designed to reduce the entropic cost of forming the transition state — by binding both substrates in the correct orientation, the enzyme effectively pre-organizes the transition state geometry, reducing the ΔS‡ penalty. Without the enzyme, both the enthalpic and entropic contributions to ΔG‡ must be overcome; with the enzyme, the entropic portion is largely paid by tight binding rather than by thermal fluctuation."
```

## Explainer

You already understand the basic transition state concept — a reaction passes through a high-energy configuration (the transition state or activated complex) on its way from reactants to products. Transition state theory (TST) turns this geometric picture into a quantitative rate equation by making one key assumption: the transition state is in quasi-equilibrium with the reactants. This means you can use equilibrium statistical mechanics to calculate the concentration of activated complexes, then simply count how fast they cross the barrier.

The central equation is **k = (κ k_BT / h) · exp(−ΔG‡ / RT)**, where k_B is Boltzmann's constant, T is temperature, h is Planck's constant, and ΔG‡ is the **activation free energy** — the Gibbs energy difference between the transition state and the reactants. The factor k_BT/h has units of frequency (about 6 × 10¹² s⁻¹ at room temperature) and represents the universal rate at which activated complexes decompose by crossing the barrier. The exponential term gives the fraction of molecules that reach the transition state energy. The transmission coefficient κ (between 0 and 1) corrects for the fact that some molecules reaching the top of the barrier may recross back to reactants rather than proceeding to products.

What makes TST so powerful is the connection between ΔG‡ and molecular structure. The activation free energy ΔG‡ = ΔH‡ − TΔS‡ splits into enthalpic and entropic contributions. The **activation enthalpy** ΔH‡ reflects how much bond breaking and partial bond forming occurs at the transition state — stronger bonds being broken mean a higher barrier. The **activation entropy** ΔS‡ reflects the structural tightness of the transition state. A bimolecular reaction that requires two freely translating molecules to form a single, ordered complex has a large negative ΔS‡, which raises ΔG‡ and slows the reaction beyond what the enthalpy alone would suggest. This is why reactions can be slow even when ΔH‡ is moderate — the entropic penalty of organizing the transition state can be substantial.

Consider how catalysis fits into this framework. A catalyst provides an alternative reaction pathway with a lower ΔG‡. It does not change the thermodynamics — the free energy difference between reactants and products is fixed — but it reshapes the potential energy surface to create a lower saddle point. Enzymes accomplish this through precise positioning of substrates (reducing the entropic penalty), electrostatic stabilization of charged transition states, and covalent intermediates that break a single high barrier into several lower ones. TST gives you the quantitative language to compare these effects: a catalyst that reduces ΔG‡ by just 5.7 kJ/mol speeds the reaction tenfold at room temperature.

The main limitation of TST is the quasi-equilibrium assumption itself. In reality, molecules do not always equilibrate before crossing the barrier — fast reactions, reactions with very flat barriers, or reactions involving quantum tunneling can violate this assumption. The transmission coefficient κ partially corrects for dynamical recrossing, but a full treatment requires molecular dynamics simulations that follow actual trajectories across the potential energy surface. Despite these limitations, TST remains the workhorse framework for interpreting and predicting reaction rates because it connects observables (rate constants, temperature dependence) to computable molecular properties (transition state geometry, vibrational frequencies, moments of inertia) through rigorous statistical mechanics.
