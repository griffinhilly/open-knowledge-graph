---
id: green-kubo-formula
title: Green-Kubo Formula
domain: physics
course: statistical-mechanics
prerequisites:
- id: response-functions-definition
  type: hard
- id: linear-response-theory-statmech
  type: hard
builds-toward:
- transport-coefficients-viscosity
- thermal-conductivity-kinetic
tags:
- response
- transport
- fluctuation-dissipation
stage: advanced
status: draft
---

# Green-Kubo Formula

## Core Idea
The Green-Kubo formula expresses transport coefficients as time integrals of equilibrium correlation functions: η = (V/kT)∫₀^∞ ⟨σ_xy(t)σ_xy(0)⟩dt. This remarkable result allows macroscopic transport properties to be computed from microscopic equilibrium fluctuations without requiring explicit non-equilibrium simulations.
