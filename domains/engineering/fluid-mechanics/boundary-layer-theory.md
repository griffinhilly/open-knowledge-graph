---
id: boundary-layer-theory
title: Boundary Layer Theory
domain: engineering
course: fluid-mechanics
prerequisites:
- id: reynolds-number
  type: hard
- id: navier-stokes-equations
  type: soft
- id: dimensional-analysis-and-similarity
  type: soft
- id: partial-derivatives
  type: soft
- id: differential-equations-intro-separable
  type: soft
builds-toward:
- drag-and-lift-aerodynamics
tags:
- boundary layer
- Prandtl
- displacement thickness
- momentum thickness
- skin friction
stage: formal-systems
status: draft
---

# Boundary Layer Theory

## Core Idea
Prandtl's boundary layer theory resolves the conflict between viscous no-slip and inviscid outer flow: near a solid wall, viscous effects are confined to a thin boundary layer of thickness δ ~ L/√Re_L. Outside this layer, flow behaves as nearly inviscid. For a flat plate (Blasius solution), δ/x = 5/√Re_x for laminar flow. The boundary layer can transition to turbulent at Re_x ≈ 5×10⁵, causing a thicker, fuller profile and higher wall shear stress. Displacement thickness δ* and momentum thickness θ characterize the effect of the boundary layer on outer flow and wall drag.

## How It's Best Learned
Solve the Blasius problem numerically to see the self-similar laminar profile. Compute displacement and momentum thickness from their integral definitions. Then explore the consequences of laminar vs. turbulent boundary layers: which has higher skin friction? Which separates sooner on a curved surface?

## Common Misconceptions
- Boundary layer thickness is not sharply defined; δ is conventionally taken at the point where u = 0.99U∞, which is an approximation.
- A turbulent boundary layer has higher skin friction than laminar but is more resistant to separation — relevant to golf ball dimples and airfoil design.
- The boundary layer equations are simpler than full Navier-Stokes because the pressure gradient across the boundary layer thickness is negligible.
