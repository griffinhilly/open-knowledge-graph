---
id: constraint-forces-and-reactions
title: Constraint Forces and Reaction Forces
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: free-body-diagram-methodology
  type: hard
- id: holonomic-and-nonholonomic-constraints
  type: soft
builds-toward:
- support-reactions-classification
- principle-of-virtual-work-advanced
tags:
- constraints
- reactions
- free-body-diagrams
stage: formal-systems
status: draft
---

# Constraint Forces and Reaction Forces

## Core Idea
Constraint forces (normal forces, support reactions, tension in strings) arise from constraints that prevent certain motions. Unlike applied forces, constraint forces adjust their magnitude to maintain the constraint—they do no work during motion satisfying the constraint, making them invisible to energy-based analysis methods like the principle of virtual work.

## Explainer

You already know how to draw a free-body diagram — you isolate a body, cut away everything connected to it, and replace those connections with forces. **Constraint forces** are the forces that appear in those cuts. They are not applied by an agent with intent; they are the physical reality of a boundary condition. A floor pushes up on a block because the block cannot pass through it. A hinge pushes back because the pin prevents translation at that joint. In each case, the constraint comes first — the force is whatever value it needs to be to maintain it.

The key property that makes constraint forces special is that they do no work when the motion is consistent with the constraint. Consider a block sliding along a smooth horizontal surface: the normal force is perpendicular to the velocity, so the dot product F·v is zero — no work done. Or a bead on a wire: the reaction force from the wire is always perpendicular to the wire (and thus to the bead's velocity along it), contributing nothing to the energy budget. This is not a coincidence. It is a theorem: a smooth, **holonomic constraint** — one you can express as an equation in coordinates — always produces a reaction force perpendicular to the allowed motion. The constraint, in effect, redirects motion without adding or removing energy.

This observation is the bridge to energy-based methods. In Newton-Euler analysis, you must explicitly solve for constraint forces alongside accelerations — they appear in ΣF = ma and must be found. In energy methods (work-energy theorem, Lagrangian mechanics), constraint forces drop out entirely because they do no virtual work. This is why the Lagrangian formulation is so powerful: by choosing generalized coordinates that automatically satisfy the constraints, you eliminate the constraint forces from your equations and work only with the degrees of freedom that actually move.

**Reaction forces** at supports follow the same logic. A pin support prevents translation in two directions but allows rotation — so it exerts two force components but no moment. A fixed (clamped) support prevents all motion — it exerts two forces and a moment. A roller prevents translation only perpendicular to the rolling surface — one force component. In each case, the number and direction of reaction force components equals the number of constrained degrees of freedom. Recognizing what a support constrains tells you exactly what to draw in the free-body diagram — and what you'll need to solve for when applying equilibrium or the equations of motion.
