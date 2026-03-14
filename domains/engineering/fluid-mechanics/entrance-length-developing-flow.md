---
id: entrance-length-developing-flow
title: Entrance Length and Developing Flow
domain: engineering
course: fluid-mechanics
prerequisites:
- id: laminar-pipe-flow
  type: hard
- id: boundary-layer-theory
  type: soft
tags:
- entrance length
- developing flow
- hydrodynamic entry region
- velocity profile development
- entrance effects
stage: formal-systems
status: draft
---
# Entrance Length and Developing Flow

## Core Idea
When fluid enters a pipe from a reservoir or fitting, the velocity profile is initially nearly uniform (plug flow). A boundary layer grows inward from the pipe wall, and the core flow accelerates to satisfy continuity until the boundary layers merge at the centerline — at that point the flow is fully developed and the velocity profile no longer changes with axial position. The distance required for this development is the hydrodynamic entrance length L_e. For laminar flow, L_e/D ≈ 0.05·Re_D, which can be substantial (e.g., 575 diameters at Re = 2000). For turbulent flow, the entrance length is much shorter relative to laminar scaling: L_e/D ≈ 10–60, because turbulent mixing accelerates profile development. In the entrance region, the wall shear stress and friction factor are higher than their fully developed values because the boundary layer is thinner and the velocity gradient at the wall is steeper.

## How It's Best Learned
Sketch the velocity profile evolution from uniform at the inlet to parabolic (laminar) or flattened (turbulent) at fully developed conditions. Calculate the entrance length for representative cases (e.g., water in a 2 cm pipe at Re = 1000 vs. Re = 50,000) to develop intuition for when entrance effects matter. Compare the excess pressure drop in the entrance region to the fully developed value using published correction factors (Hagenbach correction).

## Common Misconceptions
- The entrance length for laminar flow is proportional to Re, so at higher Re the pipe must be much longer before the flow develops. This is the opposite of the turbulent case, where the entrance length is relatively insensitive to Re.
- Higher pressure drop in the entrance region is not just due to friction — momentum flux change (the velocity profile is redistributing kinetic energy from uniform to peaked) also contributes to the apparent pressure drop.
- Thermal and hydrodynamic entrance lengths are different. Even if the velocity profile is fully developed, the temperature profile may still be developing, and vice versa. The two are equal only when the Prandtl number is exactly 1.
