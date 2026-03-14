---
id: boltzmann-transport-equation
title: Boltzmann Transport Equation
domain: physics
course: statistical-mechanics
prerequisites:
- id: kinetic-theory-of-gases
  type: hard
- id: partial-derivatives
  type: hard
builds-toward:
- h-theorem-irreversibility
tags:
- transport
- kinetic-theory
- non-equilibrium
stage: advanced
status: draft
---

# Boltzmann Transport Equation

## Core Idea
The Boltzmann equation ∂f/∂t + v·∇f + F/m·∇_v f = (∂f/∂t)_{coll} describes the evolution of the single-particle distribution f(r,v,t) under external forces F and collisions. The collision term (∂f/∂t)_{coll} is typically approximated as −(f − f^eq)/τ (relaxation-time approximation). It governs viscosity, thermal conductivity, and electrical conductivity in gases and weakly-coupled plasmas.
