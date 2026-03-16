---
id: activation-energy-catalysis-reaction-pathways
title: Activation Energy and Catalysts
domain: chemistry
course: general-chemistry
prerequisites:
- id: factors-affecting-reaction-rates
  type: hard
- id: arrhenius-equation
  type: soft
builds-toward:
- reaction-mechanisms-elementary-steps
tags:
- activation-energy
- catalyst
- reaction-pathway
- kinetics
stage: formal-systems
status: draft
---

# Activation Energy and Catalysts

## Core Idea
Activation energy (Ea) is the minimum energy reactants need to overcome to form products. Only molecules with kinetic energy equal to or greater than Ea react. A catalyst provides an alternative reaction pathway with lower Ea, increasing reaction rate without being consumed. Enzymes are biological catalysts with extraordinary specificity and efficiency.

## How It's Best Learned
Sketch reaction coordinate diagrams showing Ea and ΔH for both uncatalyzed and catalyzed pathways. Relate Ea to temperature dependence via the Arrhenius equation.

## Explainer

From your study of factors affecting reaction rates, you know that temperature and concentration both influence how fast a reaction proceeds. Activation energy explains *why* temperature matters so much. Picture a **reaction coordinate diagram**: the x-axis tracks the progress of reactants transforming into products, and the y-axis shows potential energy. Reactants sit at one energy level, products at another, and between them rises an energy hill. The height of that hill above the reactants is the **activation energy (Ea)** — the minimum energy that colliding molecules must possess for their collision to break existing bonds and form new ones. Most collisions between reactant molecules fail to produce a reaction, not because the molecules miss each other, but because they collide without enough energy to climb over this barrier.

Temperature connects to activation energy through the distribution of molecular kinetic energies. At any temperature, molecules have a range of speeds — some slow, some fast — described by the Maxwell-Boltzmann distribution. Raising the temperature shifts this distribution so that a larger fraction of molecules carry energy equal to or greater than Ea. This is why even a modest temperature increase can dramatically accelerate a reaction: you are not just making molecules collide more often, you are making a much larger proportion of those collisions energetically successful. The Arrhenius equation, k = Ae^(−Ea/RT), captures this relationship quantitatively — the rate constant k increases exponentially as temperature rises or as Ea decreases.

A **catalyst** exploits this exponential sensitivity by providing an alternative reaction pathway with a lower activation energy. Crucially, the catalyst does not change the reactants or the products, and it does not change ΔH — the energy difference between reactants and products remains the same. What changes is the route: the catalyzed pathway might involve the formation of a temporary intermediate or a surface interaction that stabilizes the transition state, effectively lowering the energy hill that molecules must climb. Because the fraction of molecules exceeding Ea depends exponentially on the barrier height, even a small reduction in Ea produces a large increase in rate. A catalyst that lowers Ea by just 10 kJ/mol can increase the reaction rate by roughly 50-fold at room temperature.

Catalysts are classified as **homogeneous** (same phase as the reactants, like an acid catalyst dissolved in a reaction solution) or **heterogeneous** (different phase, like a platinum surface catalyzing gas-phase reactions). Biological catalysts — **enzymes** — are a special case of extraordinary efficiency: they can lower activation energies so dramatically that reactions which would take years uncatalyzed occur in milliseconds. Enzymes achieve this through precise molecular complementarity with the transition state, effectively stabilizing the highest-energy configuration along the reaction path. In all cases, the catalyst emerges unchanged at the end of the reaction, ready to facilitate another cycle — which is why catalysts are effective in tiny quantities relative to the reactants they accelerate.
