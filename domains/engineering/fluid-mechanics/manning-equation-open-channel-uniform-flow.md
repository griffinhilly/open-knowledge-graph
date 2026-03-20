---
id: manning-equation-open-channel-uniform-flow
title: Manning Equation for Open Channel Uniform Flow
domain: engineering
course: fluid-mechanics
prerequisites:
- id: open-channel-flow
  type: hard
tags:
- open-channel
- manning-equation
- uniform-flow
stage: advanced
status: draft
---

# Manning Equation for Open Channel Uniform Flow

## Core Idea
The Manning equation, V = (n⁻¹)R_h^(2/3)S^(1/2), relates average velocity in open channels to hydraulic radius R_h, slope S, and Manning roughness coefficient n. Manning's n is empirical and depends on channel material, vegetation, and alignment. The equation is widely used in engineering practice despite having dimensional inconsistency because it correlates well with field data for typical channel flows.

## Explainer

From open-channel flow fundamentals, you know the key distinction from pipe flow: the water surface is free, and flow is driven by gravity acting on the sloping free surface. The Manning equation describes the special case of **uniform flow** — where depth, velocity, and cross-sectional shape are constant all along the channel reach. Uniform flow is the channel's steady-state equilibrium: gravitational driving force exactly balances friction resistance. Just as a terminal velocity exists for a falling body when drag equals weight, uniform flow depth (called **normal depth**) is the depth at which these forces balance for a given discharge and channel geometry.

The three governing quantities each play a distinct physical role. **Slope** S (dimensionless: vertical drop per unit length) is the gravitational engine — steeper channels flow faster, all else equal. The **hydraulic radius** R_h = cross-sectional flow area / wetted perimeter measures channel efficiency. Wetted perimeter is the length of channel boundary in contact with water (the source of friction); dividing area by it gives the average "thickness" of flow per unit of friction surface. A deep, narrow channel has a small wetted perimeter relative to its area (high R_h) and flows faster than a wide, shallow channel with identical area. For a circular pipe running full, R_h = D/4. For a wide, shallow channel, R_h ≈ depth. The **Manning roughness coefficient** n captures boundary friction: smooth concrete (n ≈ 0.012) is nearly three times less resistive than a weedy natural channel (n ≈ 0.035), which can be several times less resistive than a heavily vegetated floodplain (n > 0.10).

The 2/3 power on R_h and 1/2 power on S were not derived from first principles — they were fit empirically to field measurements by Robert Manning in the 1880s. This is why n carries implicit dimensions: the equation as written assumes SI units (velocity in m/s, lengths in meters). In US customary units, the equation becomes V = (1.486/n) R_h^(2/3) S^(1/2). This dimensional inconsistency is a known historical artifact, not an algebraic error. The equation works because natural channel flows occupy a narrow range of Reynolds numbers where this empirical power-law is a reliable approximation to the more rigorous (but less tractable) Darcy-Weisbach approach.

The practical workflow is to multiply V by cross-sectional area A to get discharge: Q = V · A = (1/n) A R_h^(2/3) S^(1/2). Given a target Q, you choose channel slope, cross-section shape (rectangular, trapezoidal, circular), and lining material, then solve for the required normal depth. Rearranging for depth requires iteration (since A and R_h both depend on depth) but converges quickly. This calculation underlies the design of every engineered open channel: irrigation canals, highway culverts, storm sewers, and drainage ditches. The **most hydraulically efficient section** — maximum Q for a given area — minimizes wetted perimeter; for a trapezoid this is the half-hexagon. Real design adds freeboard, velocity constraints (minimum to prevent sedimentation, maximum to prevent erosion), and safety margins on top of this baseline uniform-flow calculation.
