---
id: boltzmann-transport-equation
title: The Boltzmann Transport Equation
domain: physics
course: statistical-mechanics
prerequisites:
- id: kinetic-theory-of-gases
  type: hard
- id: grand-canonical-ensemble
  type: soft
builds-toward:
- h-theorem-reversibility
- non-equilibrium-basics-statmech
tags:
- boltzmann-equation
- kinetic-theory
- transport
stage: advanced
status: draft
---

# The Boltzmann Transport Equation

## Core Idea
The Boltzmann transport equation ∂f/∂t + v·∇f + (F/m)·∇_v f = C[f] describes how the one-particle distribution function f(r,v,t) evolves under advection and forces, with collisions represented by the collision integral C[f]. It bridges microscopic dynamics and macroscopic transport properties (viscosity, conductivity, diffusion) and is fundamental to kinetic theory.
