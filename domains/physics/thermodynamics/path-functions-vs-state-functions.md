---
id: path-functions-vs-state-functions
title: Path Functions versus State Functions
domain: physics
course: thermodynamics
prerequisites:
- id: first-law-of-thermodynamics
  type: hard
- id: state-variables-and-functions
  type: hard
builds-toward:
- exact-and-inexact-differentials
- work-types-mechanical-pdv
tags:
- first-law
- energy
- process-dependence
stage: formal-systems
status: draft
---

# Path Functions versus State Functions

## Core Idea
Heat and work are path functions—their values depend on the specific process (path) followed between two states, so ∫đQ and ∫đW must be specified for a particular path. State functions like internal energy, entropy, and enthalpy are path-independent, meaning their change ΔU, ΔS, ΔH depends only on initial and final states, not the route taken. The first law of thermodynamics relates these: ΔU = Q - W, combining a state function change with two path functions.

## How It's Best Learned
Calculate Q and W for the same state change via different paths (isothermal vs. adiabatic, etc.). Verify that ΔU is path-independent while Q and W vary.

## Common Misconceptions
- Thinking work done ON a system is always positive.
- Assuming total heat content is conserved (enthalpy is conserved under certain conditions, not heat).
- Confusing path functions with irreversible processes.
