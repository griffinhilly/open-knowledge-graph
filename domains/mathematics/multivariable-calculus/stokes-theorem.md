---
id: stokes-theorem
title: Stokes' Theorem
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: flux-integrals
  type: hard
- id: curl-divergence
  type: hard
builds-toward:
- applications-multivariable
tags:
- stokes
- curl
stage: advanced
status: draft
---

# Stokes' Theorem

## Core Idea
Stokes' theorem: ∮_C F · dr = ∬_S (∇×F) · dS. This relates circulation around a closed curve to the flux of curl through the surface, generalizing Green's theorem to 3D.

## Questions

```yaml
- question: "Two different surfaces S₁ and S₂ share the same oriented boundary curve C. The vector field F has ∇×F ≠ 0 throughout space. What can you conclude?"
  type: multiple-choice
  options:
    - "∬_{S₁}(∇×F)·dS = ∬_{S₂}(∇×F)·dS, because both equal the same boundary circulation ∮_C F·dr"
    - "The two integrals are different, because the curl field varies in space and different surfaces sample different regions"
    - "The two integrals are equal only if S₁ and S₂ have the same area"
    - "The two integrals are equal only if F is conservative"
  answer: 0
  explanation: "Stokes' theorem says ∬_S (∇×F)·dS = ∮_C F·dr for any surface S spanning C. Since both S₁ and S₂ share boundary C, both curl-flux integrals equal the same line integral ∮_C F·dr — even though ∇×F ≠ 0 and the surfaces sample different regions of space. This is the deep result: the flux of curl through a surface depends only on the boundary, not on which spanning surface is chosen."

- question: "You know ∇×F = 0 everywhere in a simply-connected region, and C is a closed loop bounding a surface S in that region. Which reasoning correctly concludes that ∮_C F·dr = 0?"
  type: multiple-choice
  options:
    - "The argument is circular — you need to verify F has a potential function before applying this reasoning"
    - "∬_S (∇×F)·dS = ∬_S 0 dS = 0, and by Stokes' theorem this equals ∮_C F·dr, so the circulation is zero"
    - "Stokes' theorem doesn't apply here because ∇×F = 0 means there is no curl field to integrate"
    - "The circulation is zero only if C is a circle — other loop shapes require a different argument"
  answer: 1
  explanation: "This is a direct application of Stokes' theorem. Because ∇×F = 0 everywhere, the surface integral ∬_S (∇×F)·dS = 0 regardless of which surface S you choose. Stokes' theorem then forces ∮_C F·dr = 0. Option A confuses the logical direction: Stokes' theorem is the tool that proves the circulation vanishes; you don't need to find a potential function first. The curl condition ∇×F = 0 is doing all the work."

- question: "Stokes' theorem implies that the flux of the curl through a surface depends only on the boundary curve of that surface, not on which particular surface spanning that curve you choose."
  type: true-false
  answer: true
  explanation: "This is the core geometric content of Stokes' theorem. For any two surfaces sharing the same oriented boundary C, both curl-flux integrals equal ∮_C F·dr — the same quantity. So the value is entirely determined by C. This has a powerful consequence: to evaluate ∬_S (∇×F)·dS, you can replace S with any other convenient surface that has the same boundary, often dramatically simplifying the computation."

- question: "Stokes' theorem states that the circulation of F around a curve C equals the flux of ∇×F through C itself."
  type: true-false
  answer: false
  explanation: "C is a curve — you cannot integrate a vector field over a curve using a surface integral. Stokes' theorem states that circulation around C equals the flux of ∇×F through a surface S whose *boundary* is C: ∮_C F·dr = ∬_S (∇×F)·dS. The surface S is a 2D object bounded by C; it is distinct from C itself. Confusing the boundary curve with the spanning surface is a common sign of misunderstanding the theorem's structure."

- question: "Explain in your own words how the tiling argument derives Stokes' theorem. Why does only the outer boundary survive when you sum the circulation contributions from all the tiny patches?"
  type: short-answer
  answer: "Divide the surface S into many tiny parallelogram patches. Each patch has a small boundary loop, and the circulation around that tiny loop is approximately (∇×F)·n̂ ΔA — the local curl dotted with the patch's normal times its area. Now sum all these tiny circulations. Every interior edge is shared by exactly two adjacent patches, and those patches traverse the shared edge in opposite directions (one clockwise, one counterclockwise relative to that edge). These contributions cancel exactly. The only edges that are not canceled are those on the outer boundary of the entire surface — each of those is traversed only once. The surviving sum is therefore the line integral ∮_C F·dr around the outer boundary. Making this argument rigorous gives Stokes' theorem: the global circulation equals the sum of local curl contributions."
```

## Explainer

From your study of flux integrals and curl, you know that ∬_S F · dS measures how much of a vector field passes through a surface, and that ∇×F (the curl) captures the local rotational tendency of a vector field at each point in space. **Stokes' theorem** says these two ideas are connected by a boundary relationship: the total circulation of F around the boundary curve C of a surface S equals the flux of the curl of F through S. The closed curve C does not enclose a region in the plane (as in Green's theorem) — it bounds a surface in 3D space.

To build intuition, extend the argument from Green's theorem to three dimensions. Tile the surface S with tiny parallelogram patches. Each patch has a tiny boundary loop, and the line integral of F around that tiny loop measures local circulation — approximately (∇×F)·n̂ times the area of the patch, where n̂ is the unit normal. Sum these contributions over all patches: adjacent interior edges cancel (they're traversed in opposite directions by neighboring patches), and what remains is the line integral around the outer boundary C. So the global circulation equals the sum of local circulations — which is exactly the surface integral ∬_S (∇×F) · dS. Stokes' theorem is this cancellation argument made rigorous.

The orientation conventions matter here and deserve careful attention. The boundary curve C must be oriented **consistently** with the surface normal: if the normal points according to the right-hand rule when you curl your fingers in the direction of traversal of C, then the signs in the theorem work out correctly. Reversing the orientation of C changes the sign of the left side; reversing the orientation of the surface (flipping the normal) changes the sign of the right side. Stokes' theorem holds for either consistent choice, but mixing orientations introduces a sign error.

A powerful corollary: for a **conservative field** (one where ∇×F = 0 everywhere), the right side is zero, so ∮_C F · dr = 0 for any closed curve C that bounds a surface in the domain. This is stronger than just knowing the field is irrotational at a point — it says the entire circulation around any bounding loop vanishes. Stokes' theorem also explains why the specific surface spanning C doesn't matter for conservative fields: if two surfaces S₁ and S₂ share the same boundary C, then ∬_{S₁} (∇×F) · dS = ∬_{S₂} (∇×F) · dS (both equal the same boundary circulation). The theorem reveals that curl flux through a surface is a property of the boundary, not the interior surface chosen.
