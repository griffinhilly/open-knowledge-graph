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
stage: advanced
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

## Explainer

From boundary layer theory, you know that a laminar boundary layer grows along a flat plate with the smooth Blasius velocity profile — a gently curved shape where velocity increases steadily from zero at the wall to the freestream value U∞. This profile has low skin friction but is fragile: it separates readily under adverse pressure gradients and destabilizes at moderate Reynolds numbers. When the local Re_x ≈ 5×10⁵, infinitesimal disturbances amplify and the boundary layer transitions to turbulence. The turbulent velocity profile looks strikingly different: much fuller close to the wall, with most of the velocity defect concentrated in a thin region right at the surface. This fullness — high near-wall momentum — is what makes turbulent boundary layers so resistant to separation.

The inner structure of a turbulent boundary layer is organized into distinct layers that the **law of the wall** describes using **wall units**: the friction velocity u_τ = √(τ_w/ρ) sets the velocity scale, and the viscous length ν/u_τ sets the distance scale. In these units, y⁺ = y·u_τ/ν and u⁺ = u/u_τ. In the **viscous sublayer** (y⁺ < 5), viscous stress dominates over turbulent Reynolds stress and the velocity profile is perfectly linear: u⁺ = y⁺. This is a thin sliver of fluid — at typical engineering conditions, it may be only tens of micrometers thick — yet it carries a disproportionate share of the total shear stress and governs heat and mass transfer at the wall. Above it, the **buffer layer** (5 < y⁺ < 30) is a transition zone where neither viscous nor turbulent stresses completely dominate. In the **log layer** (y⁺ > 30), turbulent mixing dominates and the mean profile obeys the universal logarithmic law: u⁺ = (1/κ)ln(y⁺) + B, with κ ≈ 0.41 and B ≈ 5.0. This log law — also familiar from turbulent pipe flow — emerges from the physics of an energy cascade: turbulent eddies at each scale in the overlap layer produce a self-similar structure that forces the log profile.

For engineering calculations, the full inner structure is often bypassed in favor of the **1/7th power law**: u/U∞ = (y/δ)^(1/7). This simple algebraic profile integrates to give a skin friction coefficient C_f ≈ 0.027/Re_x^(1/7) and boundary layer growth δ/x ≈ 0.16/Re_x^(1/7). Comparing these to the laminar Blasius results (C_f ≈ 0.664/Re_x^0.5, δ/x ≈ 5/Re_x^0.5) shows two key differences: turbulent skin friction is several times higher at the same Re, and the turbulent boundary layer is thicker. The extra thickness and mixing are inseparable from the higher drag. The trade-off — more friction drag but separation-resistant behavior — is central to aerodynamic design choices between maintaining laminar flow (valuable on aircraft wings where friction drag dominates) and accepting turbulent flow (sometimes deliberately triggered to prevent separation).
