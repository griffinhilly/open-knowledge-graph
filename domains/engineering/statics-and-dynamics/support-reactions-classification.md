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

## Questions

```yaml
- question: "A simply-supported beam rests on a pin at its left end and a roller at its right end. How many unknown reaction components must be solved for in total?"
  type: multiple-choice
  options:
    - "Two — one vertical force at each support"
    - "Three — two at the pin and one at the roller"
    - "Four — two at each support"
    - "Five — two at the pin, one at the roller, and two from the beam's self-weight"
  answer: 1
  explanation: "A pin prevents translation in both directions and introduces two unknown force components (horizontal and vertical). A roller prevents only perpendicular translation and introduces one unknown (the normal reaction). Total: 3 unknowns. This matches exactly the three equilibrium equations available in 2D (ΣFx = 0, ΣFy = 0, ΣM = 0), making this structure statically determinate. Note that the beam's self-weight is a known applied load, not an unknown reaction."

- question: "A cantilever beam is embedded in a wall at one end (fixed support) with the other end free. Compared to a pin support, what additional reaction does the fixed support introduce?"
  type: multiple-choice
  options:
    - "An additional vertical force component to resist bending"
    - "A reaction moment that resists rotation of the beam at the wall"
    - "A horizontal tension force along the beam's axis"
    - "Two additional force components, bringing the total to four unknowns"
  answer: 1
  explanation: "A pin prevents translation (2 force components) but allows free rotation — it cannot resist a moment. A fixed support prevents both translation and rotation, adding a reaction moment (couple) to the two force components. This moment physically represents the wall's resistance to the beam rotating at its root. The fixed support therefore has 3 unknowns (Rx, Ry, M), compared to 2 for a pin. This reaction moment is what makes cantilever structures possible: the wall must absorb not just force but also the rotational tendency from the applied loads."

- question: "A pin support prevents the connected beam from rotating at the support point, just as a fixed (cantilever) support does."
  type: true-false
  answer: false
  explanation: "This is the most important distinction between pins and fixed supports. A pin allows free rotation — the beam can rotate about the pin. It only prevents translation (movement in any direction). A fixed support prevents both translation and rotation, which is why it generates a reaction moment in addition to the two force components. Getting this wrong leads to incorrectly modeling structures: a pin-roller beam can deflect and rotate freely at both ends, whereas a fixed support locks the beam's end slope."

- question: "A roller placed on an inclined surface at 30° to horizontal provides a reaction force that is perpendicular to that inclined surface, not necessarily vertical."
  type: true-false
  answer: true
  explanation: "A roller can slide freely along the surface it sits on but cannot pass through it. The reaction force is always perpendicular (normal) to the contact surface, opposing the tendency to penetrate it. If the surface is inclined at 30°, the reaction is perpendicular to that incline — at 60° from horizontal, not vertical. This is why the orientation of the roller's surface matters for free-body diagrams: the direction of the reaction force changes with the surface angle."

- question: "Explain how counting support unknowns before writing equilibrium equations tells you whether a structure is statically determinate, and why this step matters."
  type: short-answer
  answer: "Each support type introduces a fixed number of unknown reactions: roller = 1, pin = 2, fixed = 3 (in 2D). Sum these across all supports to get the total unknowns. In 2D statics, there are exactly 3 equilibrium equations (ΣFx = 0, ΣFy = 0, ΣM = 0). If total unknowns = 3, the structure is statically determinate — solvable by equilibrium alone. If unknowns > 3, it is statically indeterminate and requires additional compatibility equations. If unknowns < 3, it is a mechanism. This check costs nothing and immediately reveals whether the problem is solvable before any equations are written."
  explanation: "Students often jump to writing equations and get stuck, not realizing the structure was indeterminate from the start. The degree of static indeterminacy = (unknowns − 3), which tells you how many additional conditions (deformation compatibility, material properties) are needed. For a simply-supported beam: pin (2) + roller (1) = 3 = 3 equations → determinate. For a beam fixed at both ends: fixed (3) + fixed (3) = 6 unknowns, degree 3 indeterminate."
```

## Explainer

Every support you encounter in statics corresponds to a physical constraint on motion — and every constraint prevents a degree of freedom, which means the support must exert a reaction to do so. The recipe is simple: **if a support prevents translation in a direction, it exerts a force in that direction; if it prevents rotation, it exerts a moment.** You already know how to draw free-body diagrams; classifying supports correctly is what tells you what to draw at each attachment point.

A **roller** sits on a surface and can slide freely along it, but it cannot pass through the surface. Because it prevents only the perpendicular translation, it generates exactly one reaction force — perpendicular (normal) to the surface. A smooth roller on a horizontal floor gives you a vertical reaction only; on an inclined surface, the reaction is normal to that surface. One unknown: one equation needed to solve it.

A **pin** (or hinge) prevents the attached point from translating in any direction, but it allows free rotation. Because it prevents both horizontal and vertical translation, it generates two force reactions — one horizontal and one vertical, whose directions are initially unknown. You draw them both as unknowns with assumed directions, then solve. Two unknowns: the sign of the solution tells you if your assumed direction was right. A pin does *not* prevent rotation, which is why a simply-supported beam (pin at one end, roller at the other) can bend freely at both supports.

A **fixed support** (cantilever wall connection) prevents all motion: translation in both directions *and* rotation. It therefore generates three reactions: two force components and a **reaction moment**. This moment is what distinguishes a fixed support from a pin — if you tried to rotate the attached beam at its root, the wall must resist that rotation, and it does so through a couple. Three unknowns: this is the maximum a single support can introduce in 2D statics, and it is also exactly the number of equilibrium equations available (ΣFx = 0, ΣFy = 0, ΣM = 0). A beam with only one fixed support is thus statically determinate from the support equations alone.

Counting unknowns before writing equations is a critical habit. A statically determinate structure has exactly as many unknown reactions as equilibrium equations; a statically indeterminate structure has more unknowns than equations, requiring additional compatibility conditions. The table is: roller = 1 unknown, pin = 2 unknowns, fixed = 3 unknowns (in 2D). Add up the total for your structure, compare to the number of equilibrium equations available, and you immediately know whether the problem is solvable by statics alone — before you ever write a single equation.
