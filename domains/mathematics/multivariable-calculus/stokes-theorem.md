---
id: stokes-theorem
title: 'Stokes'' Theorem'
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: flux-integrals
  type: hard
- id: curl-and-divergence
  type: hard
- id: greens-theorem
  type: hard
- id: conservative-fields
  type: soft
- id: fundamental-theorem-line-integrals
  type: soft
builds-toward:
- divergence-theorem
tags:
- Stokes-theorem
- curl
- surface-integral
- boundary
- circulation
stage: formal-systems
status: validated
---
# Stokes' Theorem

## Core Idea
Stokes' theorem states ∮_C F · dr = ∬_S (curl F) · dS, relating the line integral of F around the boundary curve C of an oriented surface S to the flux of the curl of F through S. It is the 3D generalization of Green's theorem: Green's theorem is Stokes' theorem applied to a flat surface in the xy-plane. The orientation convention requires that walking along C with the surface on the left keeps the normal pointing upward (right-hand rule). Stokes' theorem converts difficult line integrals into surface integrals (or vice versa).

## How It's Best Learned
Begin by showing that Green's theorem is a special case of Stokes' (flat surface, normal pointing in z-direction, curl in z-direction = ∂Q/∂x − ∂P/∂y). Then generalize. Emphasize the orientation convention carefully with diagrams. Practice choosing whether to evaluate ∮ F · dr directly or ∬ curl F · dS — often one is significantly easier.

## Common Misconceptions
- The boundary curve C must be oriented consistently with the surface normal via the right-hand rule; reversing either changes the sign of both sides.
- Stokes' theorem holds for any oriented surface with the same boundary C — the value ∬ curl F · dS is the same for all such surfaces (this is why it equals the boundary integral).
- If curl F = 0 everywhere, ∮_C F · dr = 0 for every closed curve on a simply connected surface — this recovers the conservative field result.
