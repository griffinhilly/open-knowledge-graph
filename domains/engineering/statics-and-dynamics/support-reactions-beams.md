---
id: support-reactions-beams
title: Support Reactions and Beam Types
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: equilibrium-particles-2d
  type: hard
- id: moment-of-force-2d
  type: hard
- id: equivalent-force-systems
  type: soft
builds-toward:
- equilibrium-rigid-bodies
- truss-method-of-joints
- frames-machines-analysis
tags:
- statics
- supports
- reactions
- beams
- boundary conditions
stage: formal-systems
status: validated
---
# Support Reactions and Beam Types

## Core Idea
Different support types constrain different degrees of freedom and produce corresponding reaction forces and moments. A pin support prevents translation in x and y (two unknown force components). A roller prevents translation perpendicular to its surface (one unknown). A fixed (cantilever) support prevents all translation and rotation (two force components plus a moment reaction). Correctly identifying reaction types determines the number of unknowns and whether a structure is statically determinate.

## How It's Best Learned
Memorize the reaction components for each standard support type. Practice drawing FBDs of beams with various support combinations and counting unknowns before writing equilibrium equations. Verify the structure is determinate (3 unknowns in 2D).

## Common Misconceptions
- Assigning moment reactions to pin or roller supports (they provide none).
- Forgetting that a smooth surface provides only a normal reaction force.
- Treating a fixed support as a pin, omitting the moment reaction.

## Explainer

Every structure interacts with the world through its supports. The support conditions determine what forces and moments the structure can resist — and therefore what unknown reactions you must solve for before applying equilibrium. You already know how to write the three equilibrium equations (ΣFx = 0, ΣFy = 0, ΣM = 0) for a rigid body in 2D. Support reactions give you the unknowns that make those equations meaningful.

There are three fundamental support types and they differ in how many degrees of freedom they constrain. A **roller support** constrains motion perpendicular to its rolling surface — one unknown reaction force, always normal to the surface. A **pin support** (or hinge) prevents translation in both x and y but allows rotation — two unknown force components, Rx and Ry, but no moment. A **fixed support** (cantilever) prevents all motion: translation in x and y, and rotation — two force components plus a moment reaction M, giving three unknowns total. The pattern to remember: each constrained degree of freedom introduces one unknown reaction component.

For a structure to be statically determinate in 2D, you need exactly three unknowns total (one equation per unknown, three equilibrium equations available). A simply supported beam — one pin and one roller — gives 2 + 1 = 3 unknowns, exactly solvable. A propped cantilever — one fixed support and one roller — gives 3 + 1 = 4 unknowns, which is statically indeterminate: you cannot solve it with equilibrium alone and need compatibility equations from mechanics of materials. Counting unknowns before writing any equations tells you whether the problem is solvable.

When drawing the free-body diagram, replace each support with its reaction components in their assumed positive directions. Solve the equilibrium equations; a negative answer simply means the reaction acts in the direction opposite to what you assumed — no cause for alarm. For moment equations, pick a moment center at the location of two or more unknowns to eliminate them from the equation, leaving fewer unknowns to solve simultaneously. With a pin and roller, taking moments about the pin eliminates both pin components and lets you solve for the roller reaction directly from a single equation.

The most important habit to build is automatic attention to the support symbol. A triangle with a flat base and rollers at the bottom is a roller (one unknown). A triangle pinned to a wall is a pin (two unknowns). A solid block or wall connection with no visible rotation symbol is a fixed support (three unknowns). Misidentifying the support type before writing equations guarantees incorrect answers regardless of how carefully you apply the equilibrium equations afterward.
