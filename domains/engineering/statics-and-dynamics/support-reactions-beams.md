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

## Questions

```yaml
- question: "A beam is supported by a pin at one end and a roller at the other. Before writing any equilibrium equations, how many unknown reaction components does this system have, and is it statically determinate?"
  type: multiple-choice
  options:
    - "2 unknowns (one from each support) — statically indeterminate because there aren't enough equations"
    - "4 unknowns (two from each support) — statically indeterminate, requiring additional equations"
    - "3 unknowns (two from the pin, one from the roller) — statically determinate"
    - "3 unknowns (two from the pin, one from the roller) — statically indeterminate"
  answer: 2
  explanation: "A pin provides two reaction components (Rx and Ry); a roller provides one (normal to its surface). Total: 3 unknowns. In 2D, there are exactly 3 equilibrium equations (ΣFx = 0, ΣFy = 0, ΣM = 0), so the system is statically determinate — solvable with equilibrium alone. Option B is the classic error of assigning a moment reaction to the pin, giving 3 + 1 = 4 unknowns. Pins allow free rotation and provide no moment reaction."

- question: "A wall-mounted cantilever beam has a fixed (cantilever) support at the wall and a roller support under the free end. How many total unknown reaction components must be solved for?"
  type: multiple-choice
  options:
    - "3 — one from the roller and two from the fixed support"
    - "4 — two force components and one moment from the fixed support, plus one force from the roller"
    - "2 — only the vertical forces matter in beam problems"
    - "3 — the moment at the fixed support cancels the roller reaction, leaving three independent unknowns"
  answer: 1
  explanation: "A fixed support provides three unknowns: two force components (Rx, Ry) and a moment reaction (M). A roller provides one unknown force. Total: 4 unknowns. With only 3 equilibrium equations available, this is statically indeterminate — you cannot solve it with equilibrium alone and need compatibility equations from mechanics of materials. Option A is the most common error: omitting the moment reaction at the fixed support, which is the defining feature that distinguishes it from a pin."

- question: "A pin support can resist forces in both the x and y directions, as well as rotational moments about its contact point."
  type: true-false
  answer: false
  explanation: "A pin support constrains translation in x and y (two force reactions) but allows free rotation — it provides NO moment reaction. This is the definition of a pin (hinge): it permits rotation at the connection point. Only a fixed support resists all three: Rx, Ry, and moment M. Incorrectly assigning a moment reaction to a pin gives 4 unknowns instead of 3 for a simply supported beam, making a determinate problem appear indeterminate."

- question: "A roller support on a horizontal surface provides only a vertical reaction force, with no horizontal force component and no moment reaction."
  type: true-false
  answer: true
  explanation: "A roller constrains motion perpendicular to its rolling surface and allows free motion parallel to that surface. On a horizontal surface, the roller prevents vertical displacement (one unknown: the normal force, vertical), allows horizontal sliding, and allows rotation. There is no horizontal reaction and no moment reaction. This is why a simply supported beam (pin + roller) has exactly 3 unknowns total. If the roller surface were inclined, the single reaction force would be normal to that inclined surface."

- question: "Why should you count unknown reaction components before writing equilibrium equations, and what does the count tell you about your solution approach?"
  type: short-answer
  answer: "Counting unknowns tells you whether the problem is statically determinate before you commit to a solution approach. In 2D, you have exactly 3 equilibrium equations. If you have exactly 3 unknowns, the system is determinate and solvable with equilibrium alone. If you have more than 3 unknowns, the system is statically indeterminate and requires additional equations from material behavior (compatibility conditions). Discovering indeterminacy after you've written and tried to solve the equations wastes time and causes confusion — the count is a prerequisite check."
  explanation: "The count also guides how you set up the equations strategically. With 3 unknowns, you can eliminate two at once by taking moments about a point where two unknowns act — leaving one equation with one unknown. For a pin-roller beam, taking moments about the pin location eliminates both pin force components, letting you solve directly for the roller reaction from a single equation. This strategic use of moment equations is only possible when you know the count and locations of unknowns before you start writing. Identifying support type → counting unknowns → checking determinacy → writing equations is the correct sequence."
```

## Explainer

Every structure interacts with the world through its supports. The support conditions determine what forces and moments the structure can resist — and therefore what unknown reactions you must solve for before applying equilibrium. You already know how to write the three equilibrium equations (ΣFx = 0, ΣFy = 0, ΣM = 0) for a rigid body in 2D. Support reactions give you the unknowns that make those equations meaningful.

There are three fundamental support types and they differ in how many degrees of freedom they constrain. A **roller support** constrains motion perpendicular to its rolling surface — one unknown reaction force, always normal to the surface. A **pin support** (or hinge) prevents translation in both x and y but allows rotation — two unknown force components, Rx and Ry, but no moment. A **fixed support** (cantilever) prevents all motion: translation in x and y, and rotation — two force components plus a moment reaction M, giving three unknowns total. The pattern to remember: each constrained degree of freedom introduces one unknown reaction component.

For a structure to be statically determinate in 2D, you need exactly three unknowns total (one equation per unknown, three equilibrium equations available). A simply supported beam — one pin and one roller — gives 2 + 1 = 3 unknowns, exactly solvable. A propped cantilever — one fixed support and one roller — gives 3 + 1 = 4 unknowns, which is statically indeterminate: you cannot solve it with equilibrium alone and need compatibility equations from mechanics of materials. Counting unknowns before writing any equations tells you whether the problem is solvable.

When drawing the free-body diagram, replace each support with its reaction components in their assumed positive directions. Solve the equilibrium equations; a negative answer simply means the reaction acts in the direction opposite to what you assumed — no cause for alarm. For moment equations, pick a moment center at the location of two or more unknowns to eliminate them from the equation, leaving fewer unknowns to solve simultaneously. With a pin and roller, taking moments about the pin eliminates both pin components and lets you solve for the roller reaction directly from a single equation.

The most important habit to build is automatic attention to the support symbol. A triangle with a flat base and rollers at the bottom is a roller (one unknown). A triangle pinned to a wall is a pin (two unknowns). A solid block or wall connection with no visible rotation symbol is a fixed support (three unknowns). Misidentifying the support type before writing equations guarantees incorrect answers regardless of how carefully you apply the equilibrium equations afterward.
