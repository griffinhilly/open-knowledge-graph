---
id: statically-determinate-indeterminate
title: Statically Determinate vs. Indeterminate Structures
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: support-reactions-classification
  type: hard
- id: equilibrium-rigid-bodies
  type: hard
builds-toward:
- truss-method-of-joints
- frames-machines-analysis
tags:
- static-determinacy
- redundancy
- constraints
stage: formal-systems
status: draft
---

# Statically Determinate vs. Indeterminate Structures

## Core Idea
A structure is statically determinate if the number of unknown reactions equals the number of available equilibrium equations (3 for 2D, 6 for 3D). If there are more unknowns, the structure is indeterminate (redundant) and requires additional equations from deformation. If there are fewer unknowns, the structure is unstable. Determinacy is essential for solving reactions using only equilibrium.
