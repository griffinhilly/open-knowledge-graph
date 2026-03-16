---
id: transition-state-geometry-activated-complex
title: Transition State Geometry and Activated Complex
domain: chemistry
course: physical-chemistry
prerequisites:
- id: transition-state-theory
  type: hard
- id: potential-energy-surfaces
  type: hard
builds-toward:
- arrhenius-equation-temperature-dependence
tags:
- transition-state
- reaction-mechanism
- activation-energy
stage: advanced
status: draft
---

# Transition State Geometry and Activated Complex

## Core Idea
The transition state is a saddle point on the potential energy surface where the system has maximum energy along the reaction coordinate but minimum energy perpendicular to it. The activated complex's geometry determines E_a and the reaction mechanism; slight changes in structure drastically alter rate. Transition state theory assumes the system crosses through this single critical point.

## Explainer

From transition state theory and potential energy surfaces, you know that a chemical reaction proceeds by climbing from a reactant minimum over an energy barrier to a product minimum. The **transition state** sits at the top of that barrier — the saddle point on the potential energy surface. But the transition state is not just an energy value; it has a specific three-dimensional geometry, and that geometry controls everything about how the reaction proceeds.

The **activated complex** is the molecular species that exists at the transition state geometry. It is not an intermediate — intermediates sit in energy minima and have measurable lifetimes. The activated complex exists for only the time it takes the system to pass through the saddle point, roughly one vibrational period (~10⁻¹³ seconds). You cannot bottle it or observe it spectroscopically under normal conditions. Mathematically, the activated complex has one imaginary vibrational frequency — the mode that corresponds to motion along the reaction coordinate. All other vibrational modes are real, meaning the complex is stable with respect to every distortion except the one that carries it forward (toward products) or backward (toward reactants).

The geometry of the transition state directly determines the **activation energy** (Eₐ). Consider an SN2 reaction where a nucleophile attacks a carbon bearing a leaving group. The transition state has a trigonal bipyramidal geometry with the nucleophile and leaving group at apical positions and partial bonds to both. If you change the nucleophile to a bulkier one, steric crowding at the transition state raises its energy relative to the reactants, increasing Eₐ and slowing the reaction. The same logic explains why small changes in substrate structure — adding a methyl group near the reaction center, for instance — can dramatically alter reaction rates. The rate does not depend on reactant stability alone; it depends on the energy difference between the reactants and this specific, fleeting geometry.

Understanding transition state geometry also explains **selectivity**. When a reactant can follow two different reaction pathways, it will preferentially follow the one whose transition state is lower in energy. The competing transition states often differ in subtle geometric ways — a bond angle that is more or less strained, a substituent that is equatorial versus axial, or a developing charge that is stabilized by a nearby group. Computational chemistry can now predict transition state geometries with remarkable accuracy, allowing chemists to calculate activation energies, predict product ratios, and even design catalysts that selectively stabilize one transition state over another. The central insight is that reaction rates are governed not by where molecules start or finish, but by the geometry of the bottleneck they must pass through.
