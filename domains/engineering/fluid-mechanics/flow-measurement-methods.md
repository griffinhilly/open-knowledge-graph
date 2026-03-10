---
id: flow-measurement-methods
title: 'Flow Measurement: Venturi, Orifice, and Pitot Tube'
domain: engineering
course: fluid-mechanics
prerequisites:
- id: bernoullis-equation
  type: hard
- id: continuity-equation-fluid
  type: hard
- id: manometry-and-pressure-measurement
  type: soft
tags:
- venturi meter
- orifice plate
- Pitot tube
- flow rate measurement
- discharge coefficient
stage: formal-systems
status: draft
---

# Flow Measurement: Venturi, Orifice, and Pitot Tube

## Core Idea
Flow meters exploit the Bernoulli-continuity relationship between pressure and velocity. The venturi meter uses a gradual contraction and expansion to minimize losses; flow rate Q = C_d·A₂·√(2ΔP/ρ(1−(A₂/A₁)²)). The orifice plate is simpler but causes higher pressure loss. The Pitot tube measures stagnation pressure and, combined with a static tap, yields local velocity: V = √(2(P_stag − P_static)/ρ). A discharge coefficient C_d corrects for real-fluid effects.

## How It's Best Learned
Compare all three devices: which has lowest cost, lowest pressure loss, highest accuracy? Calibrate a venturi or orifice by measuring flow with a weighing tank and plotting C_d vs. Re. Use a Pitot traverse to measure velocity profile across a duct and integrate to find Q.

## Common Misconceptions
- The Pitot tube measures stagnation pressure, not static pressure — the two pressure taps must be distinguished carefully.
- The theoretical (ideal) flow rate overestimates actual flow; C_d < 1 corrects for vena contracta and friction effects.
- Venturi and orifice meters measure volumetric flow rate indirectly through pressure difference, not directly.
