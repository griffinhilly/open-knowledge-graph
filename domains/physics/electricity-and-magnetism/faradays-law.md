---
id: faradays-law
title: Faraday's Law of Electromagnetic Induction
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: magnetic-flux-and-induction
  type: hard
- id: derivative-notation
  type: hard
- id: flux-integrals
  type: soft
- id: curl-and-divergence
  type: soft
builds-toward:
- lenzs-law
- inductance-and-inductors
- maxwells-equations-overview
tags:
- Faraday-law
- induced-EMF
- induction
- generators
stage: formal-systems
status: validated
---

# Faraday's Law of Electromagnetic Induction

## Core Idea
Faraday's law states that the induced EMF in a closed loop equals the negative rate of change of magnetic flux through the loop: ε = −dΦ_B/dt. For a coil of N turns, ε = −N dΦ_B/dt. This law unifies motional EMF (moving conductor in B) and transformer EMF (changing B through a stationary conductor) under one principle. It is one of Maxwell's four fundamental equations of electromagnetism.

## How It's Best Learned
Apply Faraday's law to three cases: (1) changing B with fixed area, (2) changing area with fixed B (sliding rod), and (3) rotating coil in fixed B (AC generator). For each, compute dΦ_B/dt explicitly and find the induced EMF.

## Common Misconceptions
- The negative sign is not optional — it encodes Lenz's law and energy conservation.
- Faraday's law applies even when no physical conductor is present; it describes a fundamental property of changing magnetic fields.
- The induced EMF is distributed around the loop, not localized to one point.

## Explainer

You already know that **magnetic flux** Φ_B = ∫ **B** · d**A** measures how much magnetic field threads through a surface — it is the "amount of B passing through" a loop. Faraday's discovery was that whenever this flux changes, nature responds by driving an electric current around the loop, as if a battery had been inserted. The harder the flux changes, the stronger the drive. Quantitatively: **ε = −dΦ_B/dt**. The EMF (electromotive force, measured in volts) equals the negative rate at which flux is changing.

The three routes to changing flux help build physical intuition. First, you can change **B** while keeping the loop stationary — place a loop near a magnet and pull the magnet away, or switch on a nearby current. Second, you can move or reshape the loop while **B** stays fixed — a conducting rod sliding along rails sweeps out new area, cutting through field lines. Third, you can rotate the loop in a fixed field — this is how every AC generator works, turning mechanical rotation into oscillating EMF. All three routes are unified by the single equation ε = −dΦ_B/dt, because all three change Φ_B.

The **negative sign** carries deep physical meaning. It enforces energy conservation: the induced current creates its own magnetic field that *opposes* the change in flux that created it. If you push a north pole into a loop, the induced current flows so as to create a north pole facing your magnet — it resists the insertion. This is **Lenz's law**, and it is not a separate rule but a consequence of the minus sign in Faraday's law. Without it, a slight perturbation would cause self-amplifying currents and free energy, violating thermodynamics.

For a coil of N turns, each turn contributes its own EMF, so the total becomes ε = −N dΦ_B/dt. This is the transformer principle: more turns means more induced voltage for the same changing flux. In the differential (curl) form of Maxwell's equations, Faraday's law reads ∇ × **E** = −∂**B**/∂t, which reveals something profound: a changing magnetic field *directly generates* a circulating electric field, even in empty space with no conductor present. The conductor just provides a path for the current — the field is there regardless. This field-level view is how electromagnetic waves propagate through vacuum, carrying energy without any material medium.
