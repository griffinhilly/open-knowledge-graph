---
id: legendre-transformations-potentials
title: Legendre Transformations and Thermodynamic Potentials
domain: physics
course: thermodynamics
prerequisites:
- id: exact-and-inexact-differentials
  type: hard
- id: free-energy-thermodynamic-relations
  type: soft
builds-toward:
- maxwell-relations-thermodynamics
- thermodynamic-availability-exergy
tags:
- potentials
- transformations
- natural-variables
stage: formal-systems
status: draft
---

# Legendre Transformations and Thermodynamic Potentials

## Core Idea
Legendre transformations are mathematical operations that exchange variables in a function—for example, replacing volume V with pressure P in the internal energy U(S,V) to obtain the enthalpy H(S,P). Different thermodynamic potentials (internal energy, enthalpy, Helmholtz free energy, Gibbs free energy) are Legendre transforms of each other and are useful under different experimental conditions. Choosing the right potential simplifies problem-solving by making the natural variables match the constraints of the system.

## How It's Best Learned
Construct each potential from the others via Legendre transformation. Identify which potential is natural for different experimental conditions (constant T vs constant S, constant P vs constant V).

## Common Misconceptions
- Thinking all potentials contain the same information (they do, but natural variables differ).
- Confusing the potential (e.g., H) with its differential form.
- Applying Gibbs free energy without recognizing when H and TS terms are separately meaningful.
