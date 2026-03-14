---
id: maxwells-equations-overview
title: 'Maxwell''s Equations'
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: gauss-law
  type: hard
- id: amperes-law
  type: hard
- id: faradays-law
  type: hard
- id: dielectrics
  type: soft
- id: curl-and-divergence
  type: soft
- id: divergence-theorem
  type: soft
- id: stokes-theorem
  type: soft
- id: energy-stored-in-fields
  type: soft
builds-toward:
- electromagnetic-waves
tags:
- Maxwell
- displacement-current
- unification
- electromagnetism
stage: formal-systems
status: validated
---
# Maxwell's Equations

## Core Idea
Maxwell's four equations unify electricity and magnetism into a single coherent theory. They are: (1) Gauss's law for E, ∮ E · dA = Q_enc/ε₀; (2) Gauss's law for B, ∮ B · dA = 0 (no monopoles); (3) Faraday's law, ∮ E · dl = −dΦ_B/dt; (4) Ampère-Maxwell law, ∮ B · dl = μ₀(I_enc + ε₀ dΦ_E/dt). Maxwell's key addition was the displacement current ε₀ dΦ_E/dt, which completes the symmetry between E and B and predicts that changing electric fields create magnetic fields — leading directly to electromagnetic waves.

## How It's Best Learned
Study each equation as a previously derived result (Gauss, Faraday, Ampère), then focus specifically on what Maxwell added — the displacement current — and why it was necessary to conserve charge at a capacitor gap. Verify that the equations in vacuum predict wave solutions.

## Common Misconceptions
- Maxwell did not discover most of these laws — his contribution was the displacement current term and the synthesis.
- The displacement current is not a real current (no charge moves); it is a changing electric flux.
- These four equations, in principle, describe all classical electromagnetic phenomena.
