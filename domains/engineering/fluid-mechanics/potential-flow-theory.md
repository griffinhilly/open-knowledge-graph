---
id: potential-flow-theory
title: Potential Flow Theory
domain: engineering
course: fluid-mechanics
prerequisites:
- id: fluid-kinematics
  type: hard
- id: partial-derivatives
  type: hard
- id: gradient-vector
  type: soft
- id: bernoullis-equation
  type: soft
builds-toward:
- drag-and-lift-aerodynamics
tags:
- potential flow
- irrotational
- stream function
- velocity potential
- superposition
stage: formal-systems
status: draft
---

# Potential Flow Theory

## Core Idea
For irrotational, incompressible flow (∇×V = 0 and ∇·V = 0), the velocity field can be derived from a scalar potential φ: V = ∇φ, where φ satisfies Laplace's equation ∇²φ = 0. A stream function ψ can also be defined such that V = ∇×(ψk̂). Because Laplace's equation is linear, elementary flows (uniform flow, source, sink, doublet, vortex) can be superposed to construct complex flows. Potential flow gives excellent pressure distributions away from walls but fails near boundaries where viscous effects matter.

## How It's Best Learned
Build complex flows by superposing elementary solutions: uniform flow + doublet = flow past a cylinder; add a vortex to get lift. Verify with the Bernoulli equation that the pressure distribution is correct. Note the symmetric pressure distribution for the cylinder case (d'Alembert's paradox: zero drag in potential flow) and discuss why real flows differ.

## Common Misconceptions
- Potential flow is not just 'inviscid flow' — it additionally requires irrotationality. Viscous wakes and boundary layers can produce rotational regions even in high-Re flows.
- d'Alembert's paradox (zero drag in potential flow) seems to contradict reality; real drag comes from viscous effects and the separated wake not captured by potential flow.
- Streamlines and equipotential lines are always orthogonal in 2D potential flow, which helps visualize the flow but can be mistaken for a general truth.
