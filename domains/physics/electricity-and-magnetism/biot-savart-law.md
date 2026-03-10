---
id: biot-savart-law
title: Biot-Savart Law
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: magnetic-field-intro
  type: hard
- id: electric-current-and-resistance
  type: hard
- id: cross-product
  type: hard
builds-toward:
- amperes-law
- magnetic-flux-and-induction
tags:
- Biot-Savart
- magnetic-field-calculation
- current
- integration
stage: formal-systems
status: draft
---

# Biot-Savart Law

## Core Idea
The Biot-Savart law gives the magnetic field contribution dB from an infinitesimal current element Id l: dB = (μ₀/4π) (Id l × r̂)/r². The total field is obtained by integrating over the entire current distribution. For a long straight wire at distance r, the result is B = μ₀I/(2πr). For a circular current loop of radius R at its center, B = μ₀I/(2R). The permeability of free space μ₀ = 4π × 10⁻⁷ T·m/A.

## How It's Best Learned
First verify the formula for a long straight wire by integrating the Biot-Savart law, then use the result without re-deriving it for composite geometries. Always identify the symmetry and dominant field direction before computing the integral.

## Common Misconceptions
- Biot-Savart applies to steady currents; it cannot be directly applied to accelerating charges.
- The cross product d l × r̂ determines the direction of dB — do not just look at the magnitude.
- Unlike Coulomb's law, the Biot-Savart integrand is not radially symmetric.
