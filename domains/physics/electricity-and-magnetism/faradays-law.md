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
status: draft
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
