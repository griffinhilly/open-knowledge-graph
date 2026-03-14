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
