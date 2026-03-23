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
status: validated
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

## Questions

```yaml
- question: "You apply the section method to find the bending moment at a cut section of a beam. When you take moments about the cut point, what happens to N and V in the equation?"
  type: multiple-choice
  options:
    - "N and V both appear in the moment equation and must be solved first before finding M"
    - "N and V are zero at the cut because the beam is in equilibrium, so they vanish automatically"
    - "N and V are eliminated because their lines of action pass through the cut point, contributing zero moment"
    - "N creates a moment but V does not, so only V is eliminated when taking moments about the cut"
  answer: 2
  explanation: "Taking moments about the cut point is powerful precisely because N and V both act *at* the cut face — their lines of action pass through the moment center. A force acting through the moment center contributes zero moment (moment = force × perpendicular distance = force × 0). Both N and V vanish from the moment equation, leaving a single equation with M as the only unknown. This is why the section method always recommends summing moments about the cut point."

- question: "What must be done before making an imaginary cut to find internal forces at a section of a beam?"
  type: multiple-choice
  options:
    - "Identify the material properties and cross-sectional dimensions of the beam"
    - "Choose the simpler side of the cut — the side with fewer loads — to isolate"
    - "Determine all external support reactions by applying equilibrium to the entire structure"
    - "Draw shear force and bending moment diagrams for the entire beam first"
  answer: 2
  explanation: "The section method requires knowing all forces and moments acting on the isolated portion before solving for N, V, and M. The external support reactions are part of those forces. If reactions are unknown, you have too many unknowns and cannot solve the equilibrium equations. The correct sequence is always: (1) solve the whole structure for reactions, then (2) make cuts to find internal forces at specific sections."

- question: "Taking moments about the cut point when applying the section method eliminates both N and V from the moment equation, allowing M to be solved directly as the only unknown."
  type: true-false
  answer: true
  explanation: "N (axial force) and V (shear force) both act at the cut cross-section — their lines of action pass through the cut point. A force through the moment center produces zero moment. Therefore both N and V drop out of the ΣM equation, leaving M as the sole unknown. This makes the moment equation the most efficient route to M in problems where all three internal resultants are unknown."

- question: "The sign convention used for internal forces (N, V, M) at a cut section follows the same rules as the sign convention for external reactions and applied loads."
  type: true-false
  answer: false
  explanation: "External reactions are defined relative to a fixed global coordinate system. Internal force sign conventions are defined relative to the cut face orientation: positive N means tension (faces pulling apart); positive V follows a specific face-direction convention; positive M produces concave-up curvature. These conventions ensure consistency when building shear and moment diagrams from multiple cuts. Mixing them up leads to incorrect signs throughout the analysis."

- question: "Explain why a bending moment M must always be included at an imaginary cut section of a loaded beam, even if no external moment loads are applied anywhere on the beam."
  type: short-answer
  answer: "A bending moment at the cut is the internal moment the material exerts to prevent rotation of the isolated portion. Even without applied external moments, the external forces on the isolated portion (reactions and applied loads) typically do not all pass through the cut point — they create a net moment about the cut. For rotational equilibrium (ΣM_cut = 0), an internal bending moment M must exist at the cut to balance this net moment. Omitting M leaves the free body out of rotational equilibrium."
  explanation: "The only exception is a two-force member — forces applied only at two points with no loads in between, where forces must be collinear and M = 0 at every interior section. For any beam with transverse loads, the forces on the isolated portion create a moment about the cut that must be balanced by internal M. This is precisely why beams deflect under load: M varies along the length, and that variation drives bending stress and curvature."
```

## Explainer

When you draw a free-body diagram of an entire structure, you can find the support reactions — the external forces and moments the supports exert on the structure. But this tells you nothing about what is happening *inside* the structure. A beam carrying a heavy load might be about to snap at its midpoint even though it's perfectly balanced as a whole. To find the internal forces, you need the **section method**: mentally cut through the member and ask, "what forces must exist at this cut to keep the piece I'm holding in equilibrium?"

At any 2D cross section, three internal resultants act: the **normal force** N (along the member axis — tension or compression), the **shear force** V (perpendicular to the axis — tends to slide one face past the other), and the **bending moment** M (the tendency to rotate about the cross section). These three quantities fully characterize the internal state of the member at that point. After making the cut, isolate either portion and apply the three equilibrium equations: ΣFₓ = 0, ΣFy = 0, ΣMcut = 0. Taking moments about the cut point is particularly powerful because it eliminates N and V from the moment equation, solving directly for M.

Always begin by finding all *external* support reactions before making any cuts. The reactions are found from equilibrium of the whole structure and are prerequisites to finding internal forces at any section. Once reactions are known, choose the simpler side of the cut — the side with fewer loads — to minimize algebra. Assume the standard positive sign convention (tension positive for N, specific shear direction positive for V, concave-up bending positive for M) before you start. Consistent sign convention is what allows you to build **shear force and bending moment diagrams** from many cuts — the topic this directly leads to.

The section method is the conceptual foundation for all of mechanics of materials. Once you know V and M at a section, you can compute the stress distribution across the cross section — shear stress from V, bending (normal) stress from M. Structural failures happen when these stresses exceed material limits. The internal forces you expose here are exactly what engineers design against when they size beams and check safety factors.
