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

## Explainer

From your study of flux integrals and curl, you know that ∬_S F · dS measures how much of a vector field passes through a surface, and that ∇×F (the curl) captures the local rotational tendency of a vector field at each point in space. **Stokes' theorem** says these two ideas are connected by a boundary relationship: the total circulation of F around the boundary curve C of a surface S equals the flux of the curl of F through S. The closed curve C does not enclose a region in the plane (as in Green's theorem) — it bounds a surface in 3D space.

To build intuition, extend the argument from Green's theorem to three dimensions. Tile the surface S with tiny parallelogram patches. Each patch has a tiny boundary loop, and the line integral of F around that tiny loop measures local circulation — approximately (∇×F)·n̂ times the area of the patch, where n̂ is the unit normal. Sum these contributions over all patches: adjacent interior edges cancel (they're traversed in opposite directions by neighboring patches), and what remains is the line integral around the outer boundary C. So the global circulation equals the sum of local circulations — which is exactly the surface integral ∬_S (∇×F) · dS. Stokes' theorem is this cancellation argument made rigorous.

The orientation conventions matter here and deserve careful attention. The boundary curve C must be oriented **consistently** with the surface normal: if the normal points according to the right-hand rule when you curl your fingers in the direction of traversal of C, then the signs in the theorem work out correctly. Reversing the orientation of C changes the sign of the left side; reversing the orientation of the surface (flipping the normal) changes the sign of the right side. Stokes' theorem holds for either consistent choice, but mixing orientations introduces a sign error.

A powerful corollary: for a **conservative field** (one where ∇×F = 0 everywhere), the right side is zero, so ∮_C F · dr = 0 for any closed curve C that bounds a surface in the domain. This is stronger than just knowing the field is irrotational at a point — it says the entire circulation around any bounding loop vanishes. Stokes' theorem also explains why the specific surface spanning C doesn't matter for conservative fields: if two surfaces S₁ and S₂ share the same boundary C, then ∬_{S₁} (∇×F) · dS = ∬_{S₂} (∇×F) · dS (both equal the same boundary circulation). The theorem reveals that curl flux through a surface is a property of the boundary, not the interior surface chosen.
