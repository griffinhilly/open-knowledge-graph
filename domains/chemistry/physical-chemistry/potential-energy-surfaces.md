---
id: potential-energy-surfaces
title: Potential Energy Surfaces and Reaction Coordinates
domain: chemistry
course: physical-chemistry
prerequisites:
- id: born-oppenheimer-approximation
  type: hard
- id: collision-theory-advanced-kinetics
  type: soft
builds-toward:
- transition-state-theory
- unimolecular-reaction-mechanisms
tags:
- PES
- transition-state
- saddle-point
- reaction-coordinate
- IRC
- Hammond-postulate
stage: advanced
status: validated
---

# Potential Energy Surfaces and Reaction Coordinates

## Core Idea
A potential energy surface (PES) is the electronic energy of a molecular system as a function of all nuclear coordinates, obtained within the Born-Oppenheimer approximation. Reactants, products, and intermediates correspond to minima on the PES; the transition state is a first-order saddle point — a maximum along the reaction coordinate but a minimum in all perpendicular directions. The intrinsic reaction coordinate (IRC) traces the minimum-energy path from reactants through the transition state to products. Hammond's postulate states that the transition state resembles the higher-energy species (reactants or products), providing qualitative predictions of TS structure without quantum calculations.

## How It's Best Learned
Study 2D contour maps of PESs for simple reactions (e.g., H + H₂ → H₂ + H). Identify minima, saddle points, and valley-ridge inflection points. Confirm Hammond's postulate by comparing exothermic and endothermic reactions.

## Common Misconceptions
- Thinking the transition state is an intermediate — it has no lifetime and cannot be isolated.
- Confusing the reaction coordinate (a path through multidimensional space) with a single bond length.

## Explainer

From the Born-Oppenheimer approximation, you know that electrons move so much faster than nuclei that you can solve for the electronic energy at each fixed arrangement of nuclei. If you do this for every possible arrangement, you get a surface — the **potential energy surface (PES)** — where each point represents a molecular geometry and the height at that point is the total electronic energy. For a diatomic molecule, the PES is just a curve (energy versus bond length). For a triatomic system like H + H₂, the PES becomes a two-dimensional surface plotted over two bond distances, and for larger molecules it extends into many dimensions that we cannot visualize directly but can analyze mathematically.

The topology of the PES tells the entire story of a chemical reaction. **Minima** on the surface correspond to stable species — reactants, products, and intermediates — because any small displacement raises the energy. The system naturally settles into these valleys. Between two minima lies a mountain pass: the **transition state**, which is technically a first-order saddle point. A saddle point is a maximum in one direction (the reaction coordinate) but a minimum in all perpendicular directions, just like a mountain pass is the highest point on the trail between two valleys but the lowest point on the ridge connecting two peaks. The transition state has exactly one imaginary vibrational frequency, corresponding to the motion that carries the system over the barrier.

The **intrinsic reaction coordinate (IRC)** traces the minimum-energy pathway from reactants through the transition state to products. Think of it as the path a ball would follow if it rolled downhill from the saddle point in both directions with infinitesimal kinetic energy. The IRC gives you the reaction coordinate — not a single bond distance, but a composite coordinate that may involve simultaneous bond breaking and forming, angle changes, and molecular rearrangement. The energy profile along the IRC is the familiar reaction energy diagram with its activation energy barrier.

**Hammond's postulate** provides a powerful shortcut for predicting transition state structure without computing the full PES. It states that the transition state resembles whichever species — reactants or products — it is closer to in energy. For a highly exothermic reaction, the transition state is close in energy to the reactants, so it resembles the reactants structurally (early transition state with bonds only slightly stretched). For a highly endothermic reaction, the transition state resembles the products (late transition state with bonds nearly fully broken or formed). This lets you make qualitative predictions about activation energies and selectivity: if you know whether a reaction is exothermic or endothermic, Hammond's postulate tells you roughly what the transition state looks like, which in turn predicts how sensitive the rate is to structural changes in the reactants.
