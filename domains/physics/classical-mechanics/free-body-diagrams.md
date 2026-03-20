---
id: free-body-diagrams
title: Free-Body Diagrams
domain: physics
course: classical-mechanics
prerequisites:
- id: newtons-second-law
  type: hard
- id: vectors-in-two-dimensions
  type: hard
- id: right-triangle-trigonometry-intro
  type: soft
- id: vector-addition-subtraction
  type: hard
builds-toward:
- friction-forces
- circular-motion-dynamics
- torque
tags:
- free-body-diagram
- force-analysis
- problem-solving
stage: formal-systems
status: validated
---

# Free-Body Diagrams

## Core Idea
A free-body diagram (FBD) is a schematic showing all forces acting on a single object, represented as vectors drawn from the object's center of mass. Drawing an accurate FBD is the essential first step in any dynamics problem. Each force must be labeled with its type, magnitude symbol, and direction. The FBD then allows direct application of ΣF = ma in each coordinate direction.

## How It's Best Learned
Practice drawing FBDs before writing any equations. Use a checklist: gravity (always), normal force (if on a surface), tension (if connected), friction (if sliding or at risk of sliding), and any applied forces. Only then apply Newton's second law.

## Common Misconceptions
- Including the object's acceleration or motion as a force in the diagram — only real forces belong in an FBD.
- Forgetting the normal force or drawing it in the wrong direction (it is always perpendicular to the surface).
- Drawing forces on multiple objects in one diagram — each FBD shows forces on one object only.

## Questions

```yaml
- question: "A 5 kg block rests on an inclined ramp. A student's free-body diagram includes four vectors: gravity, the normal force, friction, and the block's acceleration down the ramp. What is wrong with this diagram?"
  type: multiple-choice
  options: ["The normal force should point straight up, not perpendicular to the ramp", "Acceleration is not a force and should not appear in the free-body diagram", "Friction should not be included because the block is at rest", "Gravity should be split into components before drawing the diagram"]
  answer: 1
  explanation: "A free-body diagram shows only real forces — acceleration is the result of the net force, not a force itself. Including 'ma' as a vector in the FBD is one of the most common errors in dynamics. Friction is correctly included (static friction keeps a resting block from sliding), and gravity appears as a single downward vector (components are extracted during the algebra, not on the FBD itself)."

- question: "The normal force on an object always points straight up, opposing gravity."
  type: true-false
  answer: false
  explanation: "The normal force is always perpendicular to the contact surface, not necessarily straight up. On a horizontal floor it does point straight up, but on an inclined ramp it points perpendicular to the ramp surface — at an angle to the vertical. Confusing 'perpendicular to surface' with 'opposite to gravity' leads to incorrect component calculations in inclined-plane problems."

- question: "Why should a free-body diagram be drawn before writing any equations in a dynamics problem?"
  type: short-answer
  answer: "A free-body diagram makes all forces and their directions explicit, ensuring that Newton's second law (ΣF = ma) is applied with the correct signs and components in each direction — preventing errors from omitting forces or misidentifying directions."
  explanation: "The FBD is a systematic accounting tool: it forces you to identify every force before writing ΣF = ma. Without it, students frequently forget forces (especially the normal force on inclined planes) or assign wrong signs to components. Drawing the FBD first separates the physical analysis from the algebraic calculation, reducing both types of error."
```

## Explainer

Newton's second law states that ΣF = ma — the net force on an object equals its mass times its acceleration. But that equation is only as useful as your ability to correctly identify all the forces acting on the object and their directions. This is exactly what a **free-body diagram** (FBD) is for: a schematic showing only the forces on one isolated object, drawn as labeled arrows from the object's center of mass, before you write a single equation.

The procedure has a logical structure. First, **isolate the object** — mentally separate it from its surroundings. Then ask systematically: what is touching this object? Every contact interaction produces a force. A surface produces a **normal force** perpendicular to the surface and possibly a **friction force** parallel to it. A rope under tension pulls along its length toward the rope. An applied push or pull acts in its given direction. Gravity always acts straight downward, regardless of any contact. Draw each of these as a labeled arrow, then stop — the diagram is complete.

The most important rule is that **only real forces go on the FBD**. Acceleration is not a force; it is the *outcome* of the net force, computed *after* the diagram is complete. Students who draw an "ma" arrow on the FBD are confusing cause and effect. A closely related error: on an inclined surface, the normal force points perpendicular to the ramp, not straight up. These directions coincide only on a horizontal floor. Drawing the normal force vertically in an inclined-plane problem produces wrong components throughout the calculation.

A second key rule is **one object per diagram**. If you are analyzing two blocks connected by a rope, you draw one FBD for block A and a separate FBD for block B. Each diagram shows only the forces on that object — including the tension in the rope, which appears in both diagrams pointing in opposite directions (a consequence of Newton's third law). Mixing forces from multiple objects into a single diagram destroys the clean ΣF = ma relationship. Once you have separate, accurate FBDs for each object, applying Newton's second law to each one becomes a straightforward algebraic step.
