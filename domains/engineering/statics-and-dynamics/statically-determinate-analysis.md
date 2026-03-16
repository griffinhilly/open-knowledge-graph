---
id: statically-determinate-analysis
title: Statically Determinate Systems Analysis
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: rigid-body-equilibrium-planar
  type: hard
builds-toward:
- truss-joint-and-section-methods
- frame-and-machine-components
tags:
- static determinacy
- reactions
- internal forces
- constraints
stage: formal-systems
status: draft
---

# Statically Determinate Systems Analysis

## Core Idea
A structure or system is statically determinate if all support reactions and internal forces can be found from equilibrium equations alone, without additional information about material properties or deformations. The number of unknown forces must equal the number of independent equilibrium equations available, enabling unique solution.

## Explainer

From rigid-body equilibrium, you have three equations for any 2D structure: ΣFₓ = 0, ΣFᵧ = 0, and ΣM = 0. These give exactly three scalar equations. Static determinacy is a counting argument: if the number of unknown reaction forces equals three, you can solve; if it's more, you cannot without additional information about material behavior.

Each **support type** contributes a known number of unknowns. A **roller** allows rotation and movement parallel to its surface, so it can only push or pull perpendicular to the surface — one unknown. A **pin** prevents translation in both directions but allows rotation, giving two unknowns (horizontal and vertical reaction forces). A **fixed support** prevents all motion including rotation, providing three unknowns (two force components and a reaction moment). For a simple beam with a pin at the left end and a roller at the right: 2 + 1 = 3 unknowns, matching the 3 equations exactly. Solve directly. Replace the roller with a second pin: 2 + 2 = 4 unknowns with only 3 equations — statically **indeterminate** to the first degree. You would need the beam's flexural stiffness EI to solve (a topic in mechanics of materials).

The determinacy condition for a **truss** generalizes this: for a truss with m members, r external reaction components, and j joints, the condition for determinacy is m + r = 2j. Each joint provides two equilibrium equations (ΣFₓ = 0 and ΣFᵧ = 0), so there are 2j equations total. The m member forces and r reactions are the unknowns. If m + r < 2j, the truss is a **mechanism** — it can deform without stretching any member, meaning it's not a valid structure. If m + r > 2j, it's indeterminate. This counting rule is the gateway to the method of joints and method of sections, which build directly on it.

The practical importance of determinacy is this: a statically determinate structure's reactions and internal forces depend only on the geometry and loading, not on how stiff or flexible the members are. This makes design straightforward — you can size members for the internal forces you calculated without those forces changing due to stiffness choices. Indeterminate structures are stronger (more load paths exist) but harder to analyze, because the load distribution depends on the relative stiffnesses of the members. Recognizing determinacy before attempting analysis is the first step in any structural problem.
