---
id: energy-conservation-methods
title: Energy Conservation Methods for Systems
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: potential-energy-conservative-forces
  type: hard
- id: work-energy-particles
  type: hard
builds-toward:
- vibrations-simple-harmonic
- collision-analysis-restitution
tags:
- energy-conservation
- mechanical-energy
- systems
stage: formal-systems
status: draft
---

# Energy Conservation Methods for Systems

## Core Idea
When all forces acting on a system are conservative (or non-conservative forces do zero work), total mechanical energy is conserved. This provides a powerful method to relate velocities and positions without finding accelerations. Energy methods are especially useful for finding velocities at different points and for analyzing systems with multiple degrees of freedom.

## Explainer

You already know the **work-energy theorem**: the net work done on a particle equals its change in kinetic energy, W_net = ΔKE. And you know that conservative forces — gravity, springs, electrostatic forces — can be represented as **potential energy** functions PE, where the work done by the force equals the negative change in PE: W_conservative = −ΔPE. Combining these two ideas gives you energy conservation. If every force in the problem is conservative, then W_net = W_conservative = −ΔPE = ΔKE, which rearranges to ΔKE + ΔPE = 0, or equivalently KE₁ + PE₁ = KE₂ + PE₂. Total mechanical energy is constant.

The power of this approach is what it lets you skip. Newton's second law (F = ma) requires you to write equations of motion, integrate to find velocity as a function of time, and evaluate at specific moments. Energy conservation skips all of that: you directly relate the state at position 1 to the state at position 2, using only the heights and speeds at those two points. A ball thrown upward, a roller coaster dropping through a valley, a spring launching a block — in each case you can find the speed at any height without ever computing acceleration or time. The trade-off is that energy methods only tell you speed (the magnitude of velocity), not direction; for direction you still need vector analysis.

Non-conservative forces complicate the picture. Friction, drag, and applied motors do work that cannot be stored as potential energy — it is dissipated as heat or added from an external source. When these forces act and do nonzero work on the system, you extend the equation: KE₁ + PE₁ + W_nc = KE₂ + PE₂, where W_nc is the work done by all non-conservative forces. If friction acts over distance d with force f_k, then W_nc = −f_k · d (negative because friction opposes motion). This gives you the same two-state relationship but now accounting for energy lost or gained at the boundaries.

For systems with multiple connected bodies — a pulley with two hanging masses, a wheel rolling without slipping — energy methods generalize naturally. Write the total kinetic energy of the system (summing over all masses and rotational inertias) and total potential energy, then apply conservation. The constraint that bodies are connected collapses the multiple unknowns into one. A block sliding down a ramp connected via a rope over a pulley to a hanging mass can be analyzed in a single energy equation, where the single unknown is the common speed at the final state. This is where energy methods decisively outperform Newton's laws applied body-by-body.
