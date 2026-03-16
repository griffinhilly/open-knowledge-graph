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

## Explainer

From your prerequisites — support reaction classification and rigid body equilibrium — you know that three equilibrium equations are available for a 2D problem (ΣFx = 0, ΣFy = 0, ΣM = 0) and six for a 3D problem. Each support type contributes a fixed number of unknown reaction forces: a pin gives two unknowns, a roller gives one, a fixed wall gives three. Counting those unknowns and comparing them to available equations tells you whether the problem is solvable using equilibrium alone.

When unknowns equal equations, the structure is **statically determinate** — every reaction force follows directly from equilibrium. A simply-supported beam with one pin (2 unknowns) and one roller (1 unknown) has 3 unknowns and 3 equations: exactly solvable. This is the world that first-year statics inhabits. When unknowns exceed equations, the structure is **statically indeterminate**, with a degree of **static indeterminacy** (DSI) equal to the excess: DSI = unknowns − equations. Adding a second pin to the simply-supported beam creates DSI = 1: you have 4 unknowns and 3 equations, so one reaction cannot be determined from equilibrium alone. To resolve it, you need a **compatibility equation** — a constraint on how the structure must deform. Specifically, the deflection at the redundant support must equal zero (or some prescribed value), which couples the force to the geometry through material stiffness.

Redundancy has physical meaning: it represents multiple load paths. If one support fails in an indeterminate structure, loads redistribute to the remaining supports and the structure may survive. A determinate structure has no such reserve; losing one support produces a mechanism. This is why real civil structures — bridges, building frames, foundation systems — are deliberately designed to be indeterminate. The engineering trade-off is that indeterminacy adds safety but makes analysis more complex, requiring methods from mechanics of materials (virtual work, force method, stiffness method) that you will study later.

The third case — fewer unknowns than equations — is **geometric instability**: not enough constraints to prevent rigid-body motion. A beam supported only by parallel rollers can carry vertical loads but offers no horizontal resistance; an applied horizontal force produces no equilibrium, and the beam slides. Instability can also be **improper** rather than numerical: three parallel roller supports all contribute only vertical reactions, giving 3 unknowns and 3 equations (determinacy by count), yet the structure is still unstable because no support resists horizontal forces. Numerical counting is necessary but not sufficient — the geometry of constraint directions must also span all required load directions.
