---
id: laminar-entrance-length-development
title: Laminar Entrance Length and Velocity Profile Development
domain: engineering
course: fluid-mechanics
prerequisites:
- id: laminar-pipe-flow
  type: hard
- id: boundary-layer-theory
  type: soft
tags:
- laminar
- entrance
- development
stage: formal-systems
status: draft
---

# Laminar Entrance Length and Velocity Profile Development

## Core Idea
In developing laminar flow, the velocity profile evolves from uniform at the inlet to the parabolic Hagen-Poiseuille profile over an entrance length typically L_e ≈ 0.05 Re D. Friction factors in this region exceed fully-developed values (4/Re) due to the accelerating boundary layer. Hydrodynamic entrance effects are critical for short pipes and must be accounted for in energy balance calculations.

## How It's Best Learned
Numerically solve the Navier-Stokes equations in the entrance region using CFD, or use existing correlations to estimate entrance length for given Reynolds numbers. Compare pressure drops in short versus long pipe sections to observe the entrance effect diminishing.
