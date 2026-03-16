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

## Explainer

You already understand the basic transition state concept — a reaction passes through a high-energy configuration (the transition state or activated complex) on its way from reactants to products. Transition state theory (TST) turns this geometric picture into a quantitative rate equation by making one key assumption: the transition state is in quasi-equilibrium with the reactants. This means you can use equilibrium statistical mechanics to calculate the concentration of activated complexes, then simply count how fast they cross the barrier.

The central equation is **k = (κ k_BT / h) · exp(−ΔG‡ / RT)**, where k_B is Boltzmann's constant, T is temperature, h is Planck's constant, and ΔG‡ is the **activation free energy** — the Gibbs energy difference between the transition state and the reactants. The factor k_BT/h has units of frequency (about 6 × 10¹² s⁻¹ at room temperature) and represents the universal rate at which activated complexes decompose by crossing the barrier. The exponential term gives the fraction of molecules that reach the transition state energy. The transmission coefficient κ (between 0 and 1) corrects for the fact that some molecules reaching the top of the barrier may recross back to reactants rather than proceeding to products.

What makes TST so powerful is the connection between ΔG‡ and molecular structure. The activation free energy ΔG‡ = ΔH‡ − TΔS‡ splits into enthalpic and entropic contributions. The **activation enthalpy** ΔH‡ reflects how much bond breaking and partial bond forming occurs at the transition state — stronger bonds being broken mean a higher barrier. The **activation entropy** ΔS‡ reflects the structural tightness of the transition state. A bimolecular reaction that requires two freely translating molecules to form a single, ordered complex has a large negative ΔS‡, which raises ΔG‡ and slows the reaction beyond what the enthalpy alone would suggest. This is why reactions can be slow even when ΔH‡ is moderate — the entropic penalty of organizing the transition state can be substantial.

Consider how catalysis fits into this framework. A catalyst provides an alternative reaction pathway with a lower ΔG‡. It does not change the thermodynamics — the free energy difference between reactants and products is fixed — but it reshapes the potential energy surface to create a lower saddle point. Enzymes accomplish this through precise positioning of substrates (reducing the entropic penalty), electrostatic stabilization of charged transition states, and covalent intermediates that break a single high barrier into several lower ones. TST gives you the quantitative language to compare these effects: a catalyst that reduces ΔG‡ by just 5.7 kJ/mol speeds the reaction tenfold at room temperature.

The main limitation of TST is the quasi-equilibrium assumption itself. In reality, molecules do not always equilibrate before crossing the barrier — fast reactions, reactions with very flat barriers, or reactions involving quantum tunneling can violate this assumption. The transmission coefficient κ partially corrects for dynamical recrossing, but a full treatment requires molecular dynamics simulations that follow actual trajectories across the potential energy surface. Despite these limitations, TST remains the workhorse framework for interpreting and predicting reaction rates because it connects observables (rate constants, temperature dependence) to computable molecular properties (transition state geometry, vibrational frequencies, moments of inertia) through rigorous statistical mechanics.
