---
id: statically-determinate-analysis
title: Statically Determinate Systems Analysis
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: rigid-body-equilibrium-planar
  type: hard
- id: constraint-forces-and-reactions
  type: soft
builds-toward:
- truss-joint-and-section-methods
- frame-and-machine-components
tags:
- static determinacy
- reactions
- internal forces
- constraints
stage: formal-systems
status: validated
---
# Statically Determinate Systems Analysis

## Core Idea
A structure or system is statically determinate if all support reactions and internal forces can be found from equilibrium equations alone, without additional information about material properties or deformations. The number of unknown forces must equal the number of independent equilibrium equations available, enabling unique solution.

## Questions

```yaml
- question: "A bridge beam is supported by a pin at the left end, a roller at the middle, and a roller at the right end. How many unknown reaction forces does this create, and what does that imply about the beam?"
  type: multiple-choice
  options:
    - "3 unknowns (pin = 2, two rollers = 1 each = 2, total = 4) — wait, that's 4: statically indeterminate"
    - "4 unknowns (pin = 2, roller = 1, roller = 1) — statically indeterminate to the first degree"
    - "3 unknowns (pin = 1, two rollers = 1 each) — statically determinate"
    - "5 unknowns — requires material stiffness properties to solve"
  answer: 1
  explanation: "A pin provides two unknown reactions (horizontal and vertical force components); each roller provides one (perpendicular force only). So: 2 + 1 + 1 = 4 unknowns, but a 2D structure has only 3 equilibrium equations (ΣFx = 0, ΣFy = 0, ΣM = 0). With 4 unknowns and 3 equations, the beam is statically indeterminate to the first degree — you cannot solve for all reactions from equilibrium alone. Option C is the most common error: students undercount the pin's contribution, assigning it only one unknown instead of two."

- question: "A structural engineer calculates member forces in a statically determinate truss and then switches to using steel that is twice as stiff as originally planned. How does this affect the calculated member forces?"
  type: multiple-choice
  options:
    - "The member forces double, because stiffer members attract more load through the structure"
    - "The member forces are unchanged — in a statically determinate structure, forces depend only on geometry and loading, not on material stiffness"
    - "The member forces halve, because the stiffer structure deflects less and therefore absorbs less energy"
    - "The engineer must redo the analysis using the stiffness matrix method to account for the material change"
  answer: 1
  explanation: "This is the defining practical property of static determinacy: all reactions and internal forces follow from equilibrium equations alone. Equilibrium only involves geometry (member directions, loading positions) and applied loads — material stiffness does not appear in ΣF = 0 or ΣM = 0. Option A describes the behavior of a statically indeterminate structure, where stiffer members do attract more load because the load distribution depends on relative stiffnesses. Choosing between determinate and indeterminate analysis is therefore not just a math question — it's a question about what information you actually need."

- question: "Converting a statically determinate beam from a pin-and-roller support to a pin-and-pin support makes it statically indeterminate, requiring the beam's flexural stiffness to find all support reactions."
  type: true-false
  answer: true
  explanation: "Pin-and-roller gives 2 + 1 = 3 unknowns, matching the 3 equilibrium equations exactly — determinate. Replacing the roller with a pin adds one more unknown (now 2 + 2 = 4), exceeding the 3 available equations. The extra reaction force cannot be found from statics alone; it depends on how the beam flexes under load, which depends on the material's stiffness EI. This is the transition from statics (forces from equilibrium) to mechanics of materials (forces from compatibility of deformations)."

- question: "A statically determinate structure is always stronger and safer than a statically indeterminate structure with the same loading, because its forces can be uniquely solved from equilibrium."
  type: true-false
  answer: false
  explanation: "Determinacy refers to analytical tractability, not structural performance. Statically indeterminate structures have multiple load paths — if one member fails, others can redistribute the load. Determinate structures lack redundancy: if one critical member or support fails, the entire structure can collapse. Indeterminate structures are typically stronger and more robust under overload or partial failure. Determinacy is valuable for analysis simplicity and for understanding how forces flow, not as a measure of structural quality."

- question: "Explain why statically determinate structures can be analyzed without knowing material properties, and what additional information is needed to analyze a statically indeterminate structure."
  type: short-answer
  answer: "Equilibrium equations (ΣF = 0, ΣM = 0) express balance of forces and moments — they contain only geometric quantities (distances, angles) and force magnitudes. Material properties like Young's modulus or cross-sectional moment of inertia do not appear in the equilibrium equations. A statically determinate structure has exactly as many unknowns as equations, so the system is solvable from equilibrium alone. A statically indeterminate structure has more unknowns than equilibrium equations, so some unknowns cannot be resolved by statics. The additional equations needed come from compatibility conditions — constraints on how the structure deforms — which depend on material stiffness (EI for beams, AE for axial members). You must solve equilibrium and compatibility simultaneously."
  explanation: "This is why engineering curricula introduce statics before mechanics of materials: determinate structures can be fully analyzed with Newton's laws alone, providing a clean foundation. Indeterminate analysis adds deformation compatibility, requiring the material constitutive law (stress = E × strain) to close the system of equations."
```

## Explainer

From rigid-body equilibrium, you have three equations for any 2D structure: ΣFₓ = 0, ΣFᵧ = 0, and ΣM = 0. These give exactly three scalar equations. Static determinacy is a counting argument: if the number of unknown reaction forces equals three, you can solve; if it's more, you cannot without additional information about material behavior.

Each **support type** contributes a known number of unknowns. A **roller** allows rotation and movement parallel to its surface, so it can only push or pull perpendicular to the surface — one unknown. A **pin** prevents translation in both directions but allows rotation, giving two unknowns (horizontal and vertical reaction forces). A **fixed support** prevents all motion including rotation, providing three unknowns (two force components and a reaction moment). For a simple beam with a pin at the left end and a roller at the right: 2 + 1 = 3 unknowns, matching the 3 equations exactly. Solve directly. Replace the roller with a second pin: 2 + 2 = 4 unknowns with only 3 equations — statically **indeterminate** to the first degree. You would need the beam's flexural stiffness EI to solve (a topic in mechanics of materials).

The determinacy condition for a **truss** generalizes this: for a truss with m members, r external reaction components, and j joints, the condition for determinacy is m + r = 2j. Each joint provides two equilibrium equations (ΣFₓ = 0 and ΣFᵧ = 0), so there are 2j equations total. The m member forces and r reactions are the unknowns. If m + r < 2j, the truss is a **mechanism** — it can deform without stretching any member, meaning it's not a valid structure. If m + r > 2j, it's indeterminate. This counting rule is the gateway to the method of joints and method of sections, which build directly on it.

The practical importance of determinacy is this: a statically determinate structure's reactions and internal forces depend only on the geometry and loading, not on how stiff or flexible the members are. This makes design straightforward — you can size members for the internal forces you calculated without those forces changing due to stiffness choices. Indeterminate structures are stronger (more load paths exist) but harder to analyze, because the load distribution depends on the relative stiffnesses of the members. Recognizing determinacy before attempting analysis is the first step in any structural problem.
