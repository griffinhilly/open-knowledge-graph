---
id: static-equilibrium
title: Static Equilibrium
domain: physics
course: classical-mechanics
prerequisites:
- id: free-body-diagrams
  type: hard
- id: torque
  type: hard
- id: newtons-first-law
  type: hard
- id: systems-elimination
  type: soft
- id: vectors-in-two-dimensions
  type: soft
builds-toward:
- rotational-dynamics
tags:
- equilibrium
- static
- torque
- force-balance
stage: formal-systems
status: validated
---

# Static Equilibrium

## Core Idea
A rigid body is in static equilibrium when both the net force and the net torque on it are zero: ΣF = 0 and Στ = 0. The torque equation provides additional constraints beyond force balance and is essential for determining where forces act (e.g., normal force position under a beam). The choice of pivot for computing torques is arbitrary — any convenient point may be chosen, often one where unknown forces are applied to eliminate them from the equation.

## How It's Best Learned
Solve beam and ladder problems: draw the FBD, write ΣFx = 0, ΣFy = 0, and Στ = 0 about a strategic pivot. Practice choosing the pivot wisely — placing it at the point of application of an unknown force often simplifies algebra.

## Common Misconceptions
- Thinking the torque pivot must be a physical support point: it can be any point.
- Setting up torque equations without specifying the sign convention for clockwise vs. counterclockwise.

## Questions

```yaml
- question: "A uniform horizontal beam is pinned at its left end and rests against a smooth wall at its right end. A student places the torque pivot at the wall contact point. Which forces drop out of the torque equation?"
  type: multiple-choice
  options:
    - "Only gravity drops out because it acts at the center"
    - "The pin reaction at the left end drops out"
    - "The wall's normal force drops out because it acts right at the pivot and has zero moment arm"
    - "All forces drop out, making the torque equation useless at that pivot"
  answer: 2
  explanation: "Torque = force × perpendicular moment arm. When the pivot is placed at the point where the wall's normal force acts, that force has a zero moment arm and contributes zero torque — it drops out of the equation entirely. This leaves an equation involving only the pin reaction and gravity, making it straightforward to solve. Strategic pivot selection is the central technique in static equilibrium analysis."

- question: "Two equal but opposite forces act at the two ends of a horizontal beam, one pushing up on the left and one pushing down on the right. The net force on the beam is zero, so the beam is in static equilibrium."
  type: true-false
  answer: false
  explanation: "False. Static equilibrium requires BOTH conditions: ΣF = 0 AND Στ = 0. In this scenario, the net force is indeed zero, but the two forces form a couple that produces a net torque, causing the beam to rotate. Satisfying the force condition alone is insufficient for equilibrium of an extended object — the torque condition is a separate, independent requirement."

- question: "The pivot point used in the torque equation for static equilibrium must be located at an actual physical support or hinge."
  type: true-false
  answer: false
  explanation: "False. The torque equilibrium condition Στ = 0 must hold about any point — this is a consequence of equilibrium itself. You are free to choose whichever pivot makes the algebra simplest. The standard strategy is to place the pivot at the location of an unknown force, which makes that force's torque contribution zero and removes it from the equation. There is no requirement that the pivot be a physical support."

- question: "A ladder leans against a frictionless wall. To find the wall's normal force, a student writes Στ = 0 about the base of the ladder. Which forces appear in this torque equation?"
  type: multiple-choice
  options:
    - "The wall normal force and gravity only — base forces have zero moment arm at the base pivot"
    - "All four forces: gravity, wall normal, base normal, and base friction"
    - "Only gravity, since it is the only downward force"
    - "Base friction and gravity only — the wall force is too far away"
  answer: 0
  explanation: "With the pivot at the base, the two base forces (normal and friction) act right at the pivot — their moment arms are zero and they contribute zero torque. The torque equation then contains only the wall's normal force and gravity (each with nonzero moment arms from the base). This allows the wall force to be solved immediately, after which the force equations ΣFx = 0 and ΣFy = 0 yield the base forces."

- question: "Explain why ΣF = 0 alone is not sufficient to guarantee static equilibrium of an extended object, and what additional condition is required."
  type: short-answer
  answer: "ΣF = 0 ensures the center of mass has no translational acceleration — the object won't slide or accelerate in any direction. But extended objects can also rotate. Forces can produce torques even when they balance: two equal and opposite forces applied at different points create zero net force but nonzero net torque, causing rotation. The additional condition is Στ = 0 about any point, ensuring no rotational acceleration. Both conditions together — zero net force and zero net torque — guarantee true static equilibrium."
  explanation: "A particle (point mass) only needs ΣF = 0. But rigid bodies have spatial extent, so forces applied at different points can cause rotation without causing translation. The torque equation is an independent constraint that the force equation cannot capture, which is why equilibrium problems with extended objects have three independent scalar equations (ΣFx, ΣFy, Στ) rather than two."
```

## Explainer

From your study of free-body diagrams, torque, and Newton's first law, you have all the tools needed to analyze rigid objects that are not moving. Newton's first law tells you that an object in equilibrium has zero net force. Your study of torque adds a second, independent condition: an object that is not rotating — one in rotational equilibrium — has zero net torque. **Static equilibrium** requires *both*: ΣF = 0 and Στ = 0. Neither condition alone is sufficient, and understanding why is the key to mastering this topic.

The reason ΣF = 0 is not enough is that forces can cause rotation without causing linear acceleration of the center of mass. Imagine two equal and opposite forces applied to opposite ends of a beam — the net force is zero, but the beam will spin. The torque equation adds the rotational constraint. In two-dimensional problems, this gives three independent scalar equations: ΣF_x = 0, ΣF_y = 0, and Στ = 0 about any chosen pivot. Three equations allow you to solve for up to three unknowns — typically the magnitudes of unknown support forces and where they act. When you have exactly three unknowns and three equations, the system is **statically determinate** and has a unique solution.

The most powerful technique in static equilibrium is **strategic pivot selection**. Since the torque condition Στ = 0 must hold about *any* point you choose, you can pick whichever pivot makes the algebra simplest. The standard strategy is to place the pivot at the point where an unknown force acts: because torque equals force times perpendicular moment arm, an unknown force acting right at the pivot has a zero moment arm and contributes zero torque — it drops out of the equation entirely. For a beam supported at one end and resting against a wall at the other, placing the pivot at the base support eliminates the base reaction from the torque equation, leaving only the wall force and gravity, which is typically trivial to solve.

Consider the classic ladder problem: a uniform ladder of mass *m* leans against a frictionless wall, its base resting on rough ground. Four forces act on the ladder — gravity at the center of mass, the wall's normal force (horizontal), the ground's normal force (vertical), and friction from the ground (horizontal). The procedure is: draw a complete free-body diagram, write ΣF_x = 0 and ΣF_y = 0, then write Στ = 0 about the base of the ladder. Placing the pivot at the base eliminates both ground forces from the torque equation, leaving an equation containing only the wall normal force and gravity — solvable immediately for the wall force. Substituting back into the force equations then gives the ground forces. This sequence — FBD, force equations, strategic torque equation — applies to every static equilibrium problem you will encounter.
