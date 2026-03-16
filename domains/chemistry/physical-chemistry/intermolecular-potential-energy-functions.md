---
id: intermolecular-potential-energy-functions
title: Intermolecular Potential Energy Surfaces
domain: chemistry
course: physical-chemistry
prerequisites:
- id: intermolecular-forces-overview
  type: hard
- id: molecular-polarity
  type: hard
builds-toward:
- van-der-waals-equation-of-state-advanced
- hydrogen-bonding-energetics
tags:
- intermolecular-forces
- potential
- interactions
- van-der-waals
stage: advanced
status: draft
---

# Intermolecular Potential Energy Surfaces

## Core Idea
Intermolecular interactions are quantified by pair potential functions U(r), which combine attractive terms (London dispersion, dipole-dipole, hydrogen bonding) and repulsive core interactions. The Lennard-Jones potential U(r) = 4ε[(σ/r)¹² − (σ/r)⁶] exemplifies this competition; the balance determines equilibrium intermolecular distance and intermolecular binding energy. These potentials are inputs to molecular dynamics simulations and solution models.

## Explainer

From your study of intermolecular forces, you know the qualitative picture: molecules attract each other through London dispersion, dipole-dipole, and hydrogen bonding interactions, but repel when they get too close and their electron clouds overlap. **Intermolecular potential energy functions** make this picture quantitative by expressing the interaction energy U as a mathematical function of the distance r between two molecules (or atoms). The shape of U(r) — a curve that plunges to a minimum and then rises steeply — encodes everything about how two molecules interact.

The most widely used model is the **Lennard-Jones (LJ) potential**: U(r) = 4ε[(σ/r)¹² − (σ/r)⁶]. This deceptively simple equation has two terms and two parameters. The attractive term (σ/r)⁶ captures **London dispersion forces**, which arise from instantaneous dipole-induced dipole interactions and fall off as 1/r⁶ — this is well-grounded in quantum mechanical perturbation theory. The repulsive term (σ/r)¹² models the steep wall of **Pauli repulsion** when electron clouds overlap. The exponent 12 is chosen for computational convenience (it is the square of 6) rather than from first principles, but it reproduces the essential physics: a hard, short-range repulsion. The parameter **ε** (epsilon) is the depth of the energy well — the strength of the attraction at the optimal distance. The parameter **σ** (sigma) is the distance at which U = 0, roughly the "size" of the molecule. The equilibrium distance (the minimum of U) occurs at r = 2^(1/6)σ ≈ 1.12σ.

The shape of the LJ curve explains many bulk properties. The well depth ε determines boiling points — deeper wells mean stronger attractions and higher boiling points. The equilibrium distance sets molecular packing in liquids and solids. The steepness of the repulsive wall explains why liquids are nearly incompressible. The asymmetry of the curve (steep repulsion, gentle attraction) explains thermal expansion: as temperature increases, molecules vibrate more broadly across the asymmetric well, and the average distance shifts outward.

Beyond the LJ potential, more sophisticated functions exist for specific interactions. The **Morse potential** adds an exponential form that better captures bond-like interactions. **Electrostatic terms** (Coulomb's law) are added for charged or polar species. **Buckingham potentials** use an exponential repulsion instead of r⁻¹². In molecular dynamics simulations, these functions are evaluated billions of times to compute forces between every pair of molecules, propagating their trajectories through time. The accuracy of any simulation — whether predicting protein folding, liquid viscosity, or gas solubility — ultimately depends on how well these potential functions represent the true intermolecular interactions.
