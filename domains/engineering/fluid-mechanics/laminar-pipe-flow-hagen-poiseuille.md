---
id: laminar-pipe-flow-hagen-poiseuille
title: Laminar Pipe Flow (Hagen-Poiseuille)
domain: engineering
course: fluid-mechanics
prerequisites:
- id: laminar-pipe-flow
  type: hard
- id: entrance-region-developing-flow-pipe
  type: soft
builds-toward:
- friction-factor-darcy-weisbach-equation
tags:
- laminar
- pipe-flow
- analytical
stage: formal-systems
status: draft
---

# Laminar Pipe Flow (Hagen-Poiseuille)

## Core Idea
In fully developed laminar pipe flow, the velocity profile is parabolic: V(r) = V_max(1 − (r/R)²), resulting in a volumetric flow rate Q = πR⁴ΔP/(8μL). For laminar flow (Re < 2,300), the friction factor f = 64/Re is independent of surface roughness, and head loss varies linearly with velocity.

## How It's Best Learned
Measure pressure drop in laminar flow through tubes of different diameters and lengths at various flow rates. Verify that pressure drop is inversely proportional to the fourth power of diameter and proportional to flow rate.

## Common Misconceptions
- The maximum velocity in laminar pipe flow occurs at the wall (it occurs at the centerline due to the no-slip condition and parabolic profile).
- Friction factor depends on surface roughness in laminar flow (it depends only on Reynolds number; roughness has no effect in laminar flow because viscous forces dominate).
