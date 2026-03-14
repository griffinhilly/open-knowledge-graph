---
id: divergence-theorem
title: The Divergence Theorem
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: flux-integrals
  type: hard
- id: curl-and-divergence
  type: hard
- id: triple-integrals
  type: hard
- id: greens-theorem
  type: soft
- id: stokes-theorem
  type: soft
tags:
- divergence-theorem
- Gauss-theorem
- flux
- boundary
- volume-integral
stage: formal-systems
status: validated
---
# The Divergence Theorem

## Core Idea
The divergence theorem (Gauss's theorem) states ∬_S F · dS = ∭_E div F dV, relating the outward flux of F through the closed surface S (boundary of solid E) to the total divergence of F within E. It is the 3D analogue of Green's flux theorem: divergence measures local source strength, and the total flux through the boundary equals the total source within. The theorem allows converting difficult closed-surface integrals to volume integrals, or computing volume integrals using surface geometry.

## How It's Best Learned
The physical interpretation is powerful: if div F represents fluid creation rate, the divergence theorem says total fluid leaving through the boundary equals total creation inside. Verify for simple examples (F = ⟨x, y, z⟩ over a sphere, where div F = 3 and ∭ 3 dV = 3 × volume). Practice choosing between evaluating the surface or volume integral based on which is simpler.

## Common Misconceptions
- The surface S must be closed (a complete boundary with no edges); Stokes' theorem applies to open surfaces, the divergence theorem to closed ones.
- The outward normal convention is essential; inward normals would negate the left-hand side.
- div F = 0 (incompressible field) means zero net flux through any closed surface — the field neither creates nor destroys 'fluid' anywhere inside.
