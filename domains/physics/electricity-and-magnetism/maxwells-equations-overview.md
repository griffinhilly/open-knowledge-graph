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
stage: advanced
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

## Explainer

Each of Maxwell's four equations is a law you have already studied. What Maxwell did was assemble them, notice an inconsistency in one of them, fix it with a single added term, and discover — to his apparent astonishment — that the corrected system predicted the existence of electromagnetic waves traveling at the speed of light. The synthesis is one of the great achievements in the history of physics.

The first two equations are the Gauss's laws. **Gauss's law for E**, ∮ E⃗ · dA⃗ = Q_enc/ε₀, says electric field lines begin on positive charges and end on negative ones — field lines have sources and sinks. **Gauss's law for B**, ∮ B⃗ · dA⃗ = 0, says magnetic field lines never begin or end: there are no magnetic monopoles, and every field line is a closed loop. These two equations constrain the divergence (source structure) of the two fields.

The next two equations are the curl laws — they describe how the fields circulate and how they generate each other. **Faraday's law**, ∮ E⃗ · dL⃗ = −dΦ_B/dt, says a changing magnetic flux induces a circulating electric field. This is the principle behind generators, transformers, and inductors. The original **Ampère's law**, ∮ B⃗ · dL⃗ = μ₀I_enc, says a current produces a circulating magnetic field. Maxwell noticed a problem: apply the divergence theorem to Ampère's law and you get a statement that only holds for steady currents. At a charging capacitor, current flows in the wire but not between the plates — yet charge is accumulating, meaning electric flux is changing. Maxwell added the **displacement current** term, ε₀ dΦ_E/dt, to give: ∮ B⃗ · dL⃗ = μ₀(I_enc + ε₀ dΦ_E/dt). This term completes the symmetry: just as a changing B creates E (Faraday), a changing E creates B (Ampère-Maxwell).

That symmetry has profound consequences. In free space with no charges or currents, the four equations reduce to two coupled equations relating E⃗ and B⃗. Take the curl of Faraday's law, substitute Ampère-Maxwell, and the result is ∇²E⃗ = μ₀ε₀ ∂²E⃗/∂t² — a **wave equation**. The predicted speed is 1/√(μ₀ε₀), which when computed from the known values of μ₀ and ε₀ gives exactly the measured speed of light. This was not a coincidence; it was the discovery that light is an electromagnetic wave. The unification of electricity, magnetism, and optics into four equations is the moment classical physics reached its apex — and the tension those equations would later create with Newtonian mechanics set the stage for special relativity and quantum mechanics.
