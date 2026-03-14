---
id: friction-factor-darcy-weisbach-equation
title: Friction Factor and the Darcy-Weisbach Equation
domain: engineering
course: fluid-mechanics
prerequisites:
- id: moody-diagram-friction-factor
  type: hard
- id: turbulent-flow-structure-properties
  type: soft
builds-toward:
- pipe-flow-network-analysis
tags:
- friction
- pressure-drop
- pipe-flow
stage: formal-systems
status: draft
---

# Friction Factor and the Darcy-Weisbach Equation

## Core Idea
The Darcy-Weisbach equation h_f = f(L/D)(V²/2g) relates head loss to friction factor, pipe length and diameter, and velocity. The friction factor f depends on Reynolds number and surface roughness (relative roughness ε/D); the Moody diagram presents this relationship. For laminar flow f = 64/Re; for turbulent flow, the Colebrook equation implicitly defines f and accounts for both viscous and form effects.
