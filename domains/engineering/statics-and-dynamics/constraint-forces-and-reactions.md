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

## Questions

```yaml
- question: "A bead slides frictionlessly along a curved wire. As the bead moves along the wire, how much work does the wire's reaction force do on the bead?"
  type: multiple-choice
  options:
    - "Positive work — the wire supports the bead against gravity and therefore transfers energy to it"
    - "Negative work — the wire resists the bead's motion and acts like friction"
    - "Zero — the reaction force is always perpendicular to the bead's velocity along the wire"
    - "It depends on whether the wire curves upward or downward at that point"
  answer: 2
  explanation: "The wire's reaction force constrains the bead to stay on the wire — it is always directed perpendicular to the wire at the bead's current position, and the bead's velocity is always tangent to the wire. Since force and velocity are perpendicular, their dot product is zero and no work is done. This is the fundamental theorem: smooth holonomic constraints produce reaction forces perpendicular to the allowed motion, contributing nothing to the energy budget. This is why energy methods can ignore constraint forces entirely."

- question: "A structural support at a joint in a bridge truss prevents translation in two directions but allows free rotation. What type of support is this, and how many unknown reaction components must be solved for?"
  type: multiple-choice
  options:
    - "A roller — it prevents translation in one direction, so there is one unknown reaction"
    - "A fixed (clamped) support — it prevents all motion, so there are three unknowns (two forces, one moment)"
    - "A pin (hinge) — it prevents two-directional translation but allows rotation, so there are two unknown force components"
    - "A rope — it provides tension along its length, one unknown"
  answer: 2
  explanation: "A pin or hinge support prevents translation in both the horizontal and vertical directions (two constrained DOF) but allows rotation freely (one unconstrained DOF). Therefore it exerts two force components (one horizontal, one vertical) and no moment. This is the rule: the number of reaction force/moment components equals the number of constrained degrees of freedom. A fixed support (no translation, no rotation) adds a moment reaction for the constrained rotational DOF, giving three unknowns."

- question: "In Lagrangian mechanics, constraint forces are automatically eliminated from the equations of motion when generalized coordinates are chosen to satisfy the constraints."
  type: true-false
  answer: true
  explanation: "This is the central power of the Lagrangian formulation. By choosing generalized coordinates whose values automatically respect the constraints (e.g., the angle of a pendulum rather than the Cartesian x, y coordinates of the bob), every virtual displacement is consistent with the constraints. Constraint forces do no virtual work on such displacements, so they vanish from the equations. You work only with the degrees of freedom that actually move, and you never need to find the constraint forces explicitly — unless you specifically need them (e.g., to check if a string goes slack)."

- question: "A constraint force does positive work on a body whenever the body is accelerating in the direction of the constraint force."
  type: true-false
  answer: false
  explanation: "Constraint forces are always perpendicular to the motion allowed by the constraint — this is a geometric property of the constraint, not a function of acceleration. Even if the body accelerates (because other forces act on it), the constraint force direction is dictated by the constraint geometry, not the acceleration direction. For example, a block accelerating down a ramp still has a normal force perpendicular to the ramp surface, doing zero work. Work is force dotted with velocity, and velocity is always tangent to the constrained motion — which is perpendicular to the reaction force."

- question: "Why do constraint forces not appear in energy-based analyses such as the work-energy theorem or Lagrangian mechanics, even though they are real physical forces that appear in free-body diagrams?"
  type: short-answer
  answer: "Constraint forces do no work during motion that is consistent with the constraint, because they are always perpendicular to the allowed displacement. Work is the integral of F·ds, and since the constraint force is perpendicular to ds at every instant, the integral is zero. Energy methods track energy changes through work, so forces that do no work are invisible to them. In Newton-Euler analysis, constraint forces must be found explicitly because ΣF = ma cares about all forces regardless of their work. In the Lagrangian formulation, generalized coordinates are chosen to satisfy constraints, so all virtual displacements are constraint-compatible and constraint forces drop out of the principle of virtual work entirely."
  explanation: "This distinction explains why Lagrangian mechanics is often dramatically simpler than Newton-Euler analysis for constrained systems. A double pendulum written in Cartesian coordinates requires 6 equations and 4 constraint forces; written in two angles (generalized coordinates), it requires just 2 equations with no constraint forces. The physics is identical; the choice of coordinates determines how much bookkeeping is needed."
```

## Explainer

You already know how to draw a free-body diagram — you isolate a body, cut away everything connected to it, and replace those connections with forces. **Constraint forces** are the forces that appear in those cuts. They are not applied by an agent with intent; they are the physical reality of a boundary condition. A floor pushes up on a block because the block cannot pass through it. A hinge pushes back because the pin prevents translation at that joint. In each case, the constraint comes first — the force is whatever value it needs to be to maintain it.

The key property that makes constraint forces special is that they do no work when the motion is consistent with the constraint. Consider a block sliding along a smooth horizontal surface: the normal force is perpendicular to the velocity, so the dot product F·v is zero — no work done. Or a bead on a wire: the reaction force from the wire is always perpendicular to the wire (and thus to the bead's velocity along it), contributing nothing to the energy budget. This is not a coincidence. It is a theorem: a smooth, **holonomic constraint** — one you can express as an equation in coordinates — always produces a reaction force perpendicular to the allowed motion. The constraint, in effect, redirects motion without adding or removing energy.

This observation is the bridge to energy-based methods. In Newton-Euler analysis, you must explicitly solve for constraint forces alongside accelerations — they appear in ΣF = ma and must be found. In energy methods (work-energy theorem, Lagrangian mechanics), constraint forces drop out entirely because they do no virtual work. This is why the Lagrangian formulation is so powerful: by choosing generalized coordinates that automatically satisfy the constraints, you eliminate the constraint forces from your equations and work only with the degrees of freedom that actually move.

**Reaction forces** at supports follow the same logic. A pin support prevents translation in two directions but allows rotation — so it exerts two force components but no moment. A fixed (clamped) support prevents all motion — it exerts two forces and a moment. A roller prevents translation only perpendicular to the rolling surface — one force component. In each case, the number and direction of reaction force components equals the number of constrained degrees of freedom. Recognizing what a support constrains tells you exactly what to draw in the free-body diagram — and what you'll need to solve for when applying equilibrium or the equations of motion.
