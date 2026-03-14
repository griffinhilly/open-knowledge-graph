---
id: drag-coefficient-bluff-bodies
title: Drag Coefficient for Bluff Bodies
domain: engineering
course: fluid-mechanics
prerequisites:
- id: drag-and-lift-aerodynamics
  type: hard
- id: reynolds-number
  type: hard
tags:
- drag coefficient
- bluff body
- pressure drag
- friction drag
- streamlining
- drag crisis
stage: formal-systems
status: draft
---
# Drag Coefficient for Bluff Bodies

## Core Idea
The drag coefficient C_D of a bluff body (one whose shape causes flow separation and a large wake) is dominated by pressure drag rather than skin friction drag. For canonical shapes — spheres, circular cylinders, flat plates — C_D depends primarily on Reynolds number and body geometry. At low Re, C_D decreases monotonically (Stokes drag gives C_D = 24/Re for a sphere). At intermediate Re, C_D plateaus (roughly 0.4–0.5 for a sphere, ~1.2 for a long cylinder). At the critical Reynolds number (~3×10⁵ for a smooth sphere), the boundary layer transitions to turbulent before separation, the wake narrows dramatically, and C_D drops by a factor of 3–5 — the drag crisis. Streamlining a bluff body delays separation and reduces pressure drag, though it increases wetted area and therefore friction drag; the net effect is almost always a large reduction in total drag.

## How It's Best Learned
Plot C_D vs. Re for a sphere, cylinder, and flat plate on the same log-log chart and compare the curves. Identify the Stokes regime, the plateau, and the drag crisis on each. Calculate the terminal velocity of a falling sphere at different sizes to see how the drag coefficient regime changes the answer. Then compare the drag of a streamlined strut to a circular cylinder of the same frontal area to quantify the benefit of streamlining.

## Common Misconceptions
- The drag crisis is not caused by turbulence increasing drag — it is caused by the turbulent boundary layer delaying separation, which shrinks the low-pressure wake and reduces pressure drag.
- Surface roughness (like dimples on a golf ball) can trigger the drag crisis at lower Re by promoting early transition; this reduces drag in the critical range but increases it at very high Re where transition would have occurred anyway.
- Drag coefficient is not a fixed property of a shape — it varies with Reynolds number, surface roughness, free-stream turbulence intensity, and aspect ratio. Quoting a single C_D without the Re range is incomplete.
