---
id: internal-forces-members
title: Internal Forces in Structural Members
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: equilibrium-rigid-bodies
  type: hard
- id: support-reactions-beams
  type: soft
builds-toward:
  - shear-force-bending-moment-diagrams
tags:
- statics
- internal forces
- section method
- normal force
- shear force
- bending moment
stage: formal-systems
status: draft
---
# Internal Forces in Structural Members

## Core Idea
When a structural member is "cut" at an imaginary section, the internal forces and moment at that section must be exposed to maintain equilibrium of the isolated portion. At any cross section, three internal resultants exist (in 2D): the normal force N acting along the member's axis, the shear force V acting perpendicular to the axis, and the bending moment M. These are found by drawing a free-body diagram of either portion of the cut member and applying the three equilibrium equations: sum of forces in x, sum of forces in y, and sum of moments about the cut point. The section method is the foundation for understanding how beams, columns, and frames carry loads internally, and it directly leads to stress analysis in mechanics of materials.

## How It's Best Learned
Always find external support reactions first, then pass an imaginary cut at the section of interest and draw the FBD of the simpler side (fewer loads). Assume positive internal forces using the standard sign convention (tension positive for N, clockwise rotation for positive V, concave-up bending for positive M). Taking moments about the cut point eliminates N and V, solving for M directly.

## Common Misconceptions
- Forgetting to include the internal moment M at the cut section, which is always present unless the member is a two-force member.
- Choosing the more complicated side of the cut for the FBD, making the algebra harder than necessary.
- Confusing the sign convention for internal forces with the sign of external reactions — internal sign conventions are defined relative to the cut face orientation.

## Explainer

When you draw a free-body diagram of an entire structure, you can find the support reactions — the external forces and moments the supports exert on the structure. But this tells you nothing about what is happening *inside* the structure. A beam carrying a heavy load might be about to snap at its midpoint even though it's perfectly balanced as a whole. To find the internal forces, you need the **section method**: mentally cut through the member and ask, "what forces must exist at this cut to keep the piece I'm holding in equilibrium?"

At any 2D cross section, three internal resultants act: the **normal force** N (along the member axis — tension or compression), the **shear force** V (perpendicular to the axis — tends to slide one face past the other), and the **bending moment** M (the tendency to rotate about the cross section). These three quantities fully characterize the internal state of the member at that point. After making the cut, isolate either portion and apply the three equilibrium equations: ΣFₓ = 0, ΣFy = 0, ΣMcut = 0. Taking moments about the cut point is particularly powerful because it eliminates N and V from the moment equation, solving directly for M.

Always begin by finding all *external* support reactions before making any cuts. The reactions are found from equilibrium of the whole structure and are prerequisites to finding internal forces at any section. Once reactions are known, choose the simpler side of the cut — the side with fewer loads — to minimize algebra. Assume the standard positive sign convention (tension positive for N, specific shear direction positive for V, concave-up bending positive for M) before you start. Consistent sign convention is what allows you to build **shear force and bending moment diagrams** from many cuts — the topic this directly leads to.

The section method is the conceptual foundation for all of mechanics of materials. Once you know V and M at a section, you can compute the stress distribution across the cross section — shear stress from V, bending (normal) stress from M. Structural failures happen when these stresses exceed material limits. The internal forces you expose here are exactly what engineers design against when they size beams and check safety factors.
