---
id: turbulent-boundary-layers
title: Turbulent Boundary Layers
domain: engineering
course: fluid-mechanics
prerequisites:
- id: boundary-layer-theory
  type: hard
- id: turbulent-pipe-flow
  type: soft
tags:
- turbulent boundary layer
- log law
- power law
- wall shear stress
- viscous sublayer
- buffer layer
- law of the wall
stage: formal-systems
status: draft
---
# Turbulent Boundary Layers

## Core Idea
When a boundary layer transitions from laminar to turbulent (typically at Re_x ≈ 5×10⁵ for a flat plate), the velocity profile changes from the smooth Blasius shape to a much fuller profile characterized by vigorous mixing. The turbulent boundary layer has a universal inner structure described by the law of the wall: in wall units (y⁺ = yuτ/ν, u⁺ = u/uτ, where uτ = √(τ_w/ρ) is the friction velocity), the profile follows u⁺ = y⁺ in the viscous sublayer (y⁺ < 5), transitions through the buffer layer (5 < y⁺ < 30), and obeys the logarithmic law u⁺ = (1/κ)ln(y⁺) + B in the log layer (y⁺ > 30), with von Karman constant κ ≈ 0.41 and B ≈ 5.0. The outer region follows a velocity defect law. Engineering approximations use the 1/7th power law u/U∞ = (y/δ)^(1/7), which gives skin friction coefficient C_f ≈ 0.027/Re_x^(1/7) and boundary layer growth δ/x ≈ 0.16/Re_x^(1/7).

## How It's Best Learned
Plot the law of the wall (u⁺ vs. y⁺) on semi-log axes and identify the viscous sublayer, buffer layer, and log region. Compare experimental data from flat-plate boundary layers against the log law and power law to see where each approximation succeeds and fails. Compute the skin friction drag on a flat plate using both the laminar (Blasius) and turbulent (power law) correlations and observe that the turbulent boundary layer produces several times more drag per unit area but resists separation far better.

## Common Misconceptions
- The 1/7th power law is an engineering approximation, not a physical law. It works well for 5×10⁵ < Re_x < 10⁷ but deviates at very high Reynolds numbers where the exponent decreases.
- The viscous sublayer is not stagnant — it is a region where viscous stress dominates over Reynolds stress, but the fluid velocity varies linearly and can still be significant. Turbulent fluctuations penetrate into this layer.
- Transition location is not fixed at Re_x = 5×10⁵. It depends on free-stream turbulence intensity, surface roughness, pressure gradient, and surface curvature. Favorable pressure gradients stabilize laminar flow; adverse gradients promote earlier transition.
