---
id: bimolecular-collision-dynamics-trajectory
title: Bimolecular Collision Dynamics and Trajectory Analysis
domain: chemistry
course: physical-chemistry
prerequisites:
- id: collision-theory-advanced-kinetics
  type: hard
- id: reaction-coordinate-diagrams
  type: hard
tags:
- collision-dynamics
- reaction-mechanism
- molecular-dynamics
stage: advanced
status: draft
---

# Bimolecular Collision Dynamics and Trajectory Analysis

## Core Idea
Bimolecular collisions are characterized by impact parameter b and collision cross-section σ. Trajectory calculations solve classical equations of motion on the potential energy surface to predict reaction probability as a function of energy and orientation. Successful reactions require the collision to deliver sufficient energy in the right direction to reach the transition state.

## Explainer

From collision theory, you know that bimolecular reactions require molecules to collide with sufficient energy and proper orientation. Trajectory analysis takes this idea from a statistical average to a molecule-by-molecule simulation: you literally follow two molecules as they approach, interact, and either react or bounce apart. This gives a far richer picture than simple collision theory, revealing exactly how energy, geometry, and the shape of the potential energy surface determine the outcome of each encounter.

The starting point is the **impact parameter b** — the perpendicular distance between the centers of the two approaching molecules if they were to travel in straight lines without interacting. Think of it like aiming a bowling ball: b = 0 is a head-on collision, while large b means a glancing encounter. For each value of b, you set initial conditions (relative velocity, orientation angles) and then numerically integrate Newton's equations of motion on the **potential energy surface (PES)** you already know from reaction coordinate diagrams. The PES provides the force at every point — it tells the molecules how to accelerate, decelerate, or deflect as they approach. The resulting path through configuration space is one trajectory.

A single trajectory tells you whether that particular collision leads to reaction or not. The real power comes from running thousands of trajectories with systematically varied b, collision energy, and molecular orientations. You discover that there is a maximum impact parameter **b_max** beyond which reaction never occurs — the collision is too glancing to deliver energy to the reactive bond. The **reaction cross-section** σ_r = πb²_max gives the effective target area for reactive collisions at a given energy. By averaging the reaction probability over a thermal distribution of collision energies, you recover the macroscopic rate constant — connecting the molecular-level picture back to the kinetics you measure in the lab.

What trajectory studies reveal that simple collision theory misses is the role of **orientation and energy partitioning**. Not all of the collision energy needs to be translational — vibrational energy in the reactants can also promote reaction, sometimes more effectively. Some reactions show a strong steric requirement (only collisions hitting a specific atom lead to products), while others are surprisingly insensitive to approach angle. These details, invisible in the Arrhenius equation, emerge naturally from trajectory calculations and explain why the simple collision theory steric factor is often much less than one.
