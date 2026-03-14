---
id: langevin-equation-stochastic
title: Langevin Equation
domain: physics
course: statistical-mechanics
prerequisites:
- id: brownian-motion
  type: hard
- id: newton-second-law
  type: hard
builds-toward:
- fokker-planck-equation
tags:
- stochastic
- dynamics
- noise
stage: advanced
status: draft
---

# Langevin Equation

## Core Idea
The Langevin equation m(dv/dt) = F - γv + ξ(t) describes particle motion with damping and random thermal noise. The friction coefficient γ and noise variance are related through the fluctuation-dissipation theorem, making this equation fundamental to modeling thermal motion, molecular dynamics, and response to external forces.
