---
id: support-reactions-classification
title: Support Reactions and Classifications
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: free-body-diagram-method
  type: hard
- id: moment-of-force-2d
  type: soft
builds-toward:
- equilibrium-rigid-bodies
- shear-force-bending-moment-diagrams
- statically-determinate-indeterminate
tags:
- supports
- reactions
- pins
- rollers
- fixed
stage: formal-systems
status: draft
---

# Support Reactions and Classifications

## Core Idea
Supports provide constraints that generate reaction forces and moments. Common supports include pinned connections (providing two force reactions), rollers (providing one perpendicular force), and fixed supports (providing two forces and one moment). The type of support determines how many unknowns must be solved for in equilibrium equations.

## Explainer

Every support you encounter in statics corresponds to a physical constraint on motion — and every constraint prevents a degree of freedom, which means the support must exert a reaction to do so. The recipe is simple: **if a support prevents translation in a direction, it exerts a force in that direction; if it prevents rotation, it exerts a moment.** You already know how to draw free-body diagrams; classifying supports correctly is what tells you what to draw at each attachment point.

A **roller** sits on a surface and can slide freely along it, but it cannot pass through the surface. Because it prevents only the perpendicular translation, it generates exactly one reaction force — perpendicular (normal) to the surface. A smooth roller on a horizontal floor gives you a vertical reaction only; on an inclined surface, the reaction is normal to that surface. One unknown: one equation needed to solve it.

A **pin** (or hinge) prevents the attached point from translating in any direction, but it allows free rotation. Because it prevents both horizontal and vertical translation, it generates two force reactions — one horizontal and one vertical, whose directions are initially unknown. You draw them both as unknowns with assumed directions, then solve. Two unknowns: the sign of the solution tells you if your assumed direction was right. A pin does *not* prevent rotation, which is why a simply-supported beam (pin at one end, roller at the other) can bend freely at both supports.

A **fixed support** (cantilever wall connection) prevents all motion: translation in both directions *and* rotation. It therefore generates three reactions: two force components and a **reaction moment**. This moment is what distinguishes a fixed support from a pin — if you tried to rotate the attached beam at its root, the wall must resist that rotation, and it does so through a couple. Three unknowns: this is the maximum a single support can introduce in 2D statics, and it is also exactly the number of equilibrium equations available (ΣFx = 0, ΣFy = 0, ΣM = 0). A beam with only one fixed support is thus statically determinate from the support equations alone.

Counting unknowns before writing equations is a critical habit. A statically determinate structure has exactly as many unknown reactions as equilibrium equations; a statically indeterminate structure has more unknowns than equations, requiring additional compatibility conditions. The table is: roller = 1 unknown, pin = 2 unknowns, fixed = 3 unknowns (in 2D). Add up the total for your structure, compare to the number of equilibrium equations available, and you immediately know whether the problem is solvable by statics alone — before you ever write a single equation.
