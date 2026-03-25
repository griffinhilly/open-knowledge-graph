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
- id: statically-determinate-analysis
  type: soft
builds-toward:
- truss-method-of-joints
- frames-machines-analysis
tags:
- static-determinacy
- redundancy
- constraints
stage: formal-systems
status: validated
---
# Statically Determinate vs. Indeterminate Structures

## Core Idea
A structure is statically determinate if the number of unknown reactions equals the number of available equilibrium equations (3 for 2D, 6 for 3D). If there are more unknowns, the structure is indeterminate (redundant) and requires additional equations from deformation. If there are fewer unknowns, the structure is unstable. Determinacy is essential for solving reactions using only equilibrium.

## Questions

```yaml
- question: "A 2D beam is supported by a pin at A (2 unknowns) and a fixed wall at B (3 unknowns), giving 5 unknown reactions. How many equilibrium equations are available, and what is the degree of static indeterminacy?"
  type: multiple-choice
  options:
    - "3 equations available; DSI = 5 − 3 = 2"
    - "5 equations available; DSI = 0 (exactly determinate)"
    - "6 equations available; the structure is over-constrained"
    - "3 equations available; the structure is unstable because the fixed wall provides too many constraints"
  answer: 0
  explanation: "For a 2D structure, exactly 3 equilibrium equations are always available (ΣFx = 0, ΣFy = 0, ΣM = 0). With 5 unknown reactions and 3 equations, DSI = 5 − 3 = 2 — the structure is statically indeterminate to the second degree. Two additional compatibility equations (from deformation constraints) are needed to solve all reactions. The number of equations available is always 3 for 2D problems; it does not scale with the number of supports."

- question: "A 2D structure has exactly 3 unknown reactions (one at each of three roller supports), matching the 3 equilibrium equations. A student concludes the structure is stable and determinate. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — if unknowns equal equations, the structure is always stable and solvable"
    - "The structure may still be geometrically unstable if all supports provide reactions in the same direction, leaving one load direction unresisted"
    - "The student should have 6 equations for a structure with 3 supports"
    - "Roller supports each provide 2 unknowns, so the count is actually 6 unknowns"
  answer: 1
  explanation: "Numerical counting (unknowns = equations) is necessary but not sufficient for stability. If all three rollers are oriented vertically, every reaction is vertical — no support resists horizontal forces. A horizontal load has no equilibrium, and the structure slides. This is geometric (improper) instability: the directions of constraint don't span the full space of possible loads. The lesson: after counting, always verify that the constraint directions cover all required load directions."

- question: "A statically indeterminate structure requires additional equations derived from deformation compatibility — not just equilibrium — to find all support reactions."
  type: true-false
  answer: true
  explanation: "When there are more unknowns than equilibrium equations, the extra unknowns are called 'redundant' reactions. To solve them, you impose compatibility conditions: geometric constraints on how the structure must deform. For example, the deflection at a redundant support must be zero (or a prescribed value). These compatibility equations relate forces to displacements through material stiffness (from mechanics of materials), providing the additional equations needed to make the system solvable."

- question: "Statically indeterminate structures are less safe than determinate ones because the extra constraints add complexity and increase the risk of structural failure."
  type: true-false
  answer: false
  explanation: "The opposite is generally true: indeterminate structures are safer because redundancy provides multiple load paths. If one support fails, loads redistribute to the remaining supports and the structure may survive. A determinate structure has exactly enough supports — losing any one produces a mechanism (uncontrolled motion). This is why real bridges, building frames, and foundations are deliberately designed to be indeterminate. The greater analysis complexity is the price paid for greater structural resilience."

- question: "What is the physical meaning of static indeterminacy, and why do civil engineers deliberately design indeterminate structures rather than determinate ones?"
  type: short-answer
  answer: "Static indeterminacy means a structure has more supports (or internal constraints) than the minimum required for equilibrium — it has redundant load paths. Physically, redundancy means that if one support is removed or fails, the remaining supports can carry the load. Determinate structures have no redundancy: removing any support produces collapse. Engineers favor indeterminate structures for safety: buildings, bridges, and frames must survive partial support failures, seismic shifts, and uneven settlements."
  explanation: "The trade-off is real: analyzing an indeterminate structure requires compatibility equations and knowledge of material stiffness, which makes the math significantly more complex. But the safety benefit justifies the complexity in any structure where failure has serious consequences. Understanding this trade-off is why statics teaches determinacy before jumping to indeterminate analysis — you need to understand what each additional constraint is buying you structurally."
```

## Explainer

From your prerequisites — support reaction classification and rigid body equilibrium — you know that three equilibrium equations are available for a 2D problem (ΣFx = 0, ΣFy = 0, ΣM = 0) and six for a 3D problem. Each support type contributes a fixed number of unknown reaction forces: a pin gives two unknowns, a roller gives one, a fixed wall gives three. Counting those unknowns and comparing them to available equations tells you whether the problem is solvable using equilibrium alone.

When unknowns equal equations, the structure is **statically determinate** — every reaction force follows directly from equilibrium. A simply-supported beam with one pin (2 unknowns) and one roller (1 unknown) has 3 unknowns and 3 equations: exactly solvable. This is the world that first-year statics inhabits. When unknowns exceed equations, the structure is **statically indeterminate**, with a degree of **static indeterminacy** (DSI) equal to the excess: DSI = unknowns − equations. Adding a second pin to the simply-supported beam creates DSI = 1: you have 4 unknowns and 3 equations, so one reaction cannot be determined from equilibrium alone. To resolve it, you need a **compatibility equation** — a constraint on how the structure must deform. Specifically, the deflection at the redundant support must equal zero (or some prescribed value), which couples the force to the geometry through material stiffness.

Redundancy has physical meaning: it represents multiple load paths. If one support fails in an indeterminate structure, loads redistribute to the remaining supports and the structure may survive. A determinate structure has no such reserve; losing one support produces a mechanism. This is why real civil structures — bridges, building frames, foundation systems — are deliberately designed to be indeterminate. The engineering trade-off is that indeterminacy adds safety but makes analysis more complex, requiring methods from mechanics of materials (virtual work, force method, stiffness method) that you will study later.

The third case — fewer unknowns than equations — is **geometric instability**: not enough constraints to prevent rigid-body motion. A beam supported only by parallel rollers can carry vertical loads but offers no horizontal resistance; an applied horizontal force produces no equilibrium, and the beam slides. Instability can also be **improper** rather than numerical: three parallel roller supports all contribute only vertical reactions, giving 3 unknowns and 3 equations (determinacy by count), yet the structure is still unstable because no support resists horizontal forces. Numerical counting is necessary but not sufficient — the geometry of constraint directions must also span all required load directions.
