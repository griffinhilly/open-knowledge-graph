---
id: potential-energy-systems
title: Electric Potential Energy in Charge Systems
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: electric-potential-definition
  type: hard
builds-toward:
- capacitance-definition
- energy-density-electric-field
tags:
- energy
- work
- configuration
stage: formal-systems
status: draft
---

# Electric Potential Energy in Charge Systems

## Core Idea
Potential energy U = qV for a charge q at potential V. For systems of multiple charges, U = ½Σᵢ qᵢVᵢ (factor of ½ avoids double counting). Energy is required to assemble charges against the field.

## Explainer

From your study of electric potential, you know that the electric potential V at a point in space is the potential energy per unit charge placed there. This gives the simplest formula in this topic: if a charge q sits at a location where the potential is V, its potential energy is U = qV. This is a direct product — no integration required. The sign matters: a positive charge at a positive potential has positive potential energy (it would release energy if allowed to move to lower potential); a positive charge at a negative potential has negative potential energy (it is in a bound configuration).

The subtlety arises with **systems of multiple charges**: what is the total potential energy stored in an assembly of N charges? You might try summing qᵢVᵢ over all charges, but this double-counts: charge 1's interaction with charge 2 is identical to charge 2's interaction with charge 1, and a naive sum counts each pair twice. The correct result is U = ½Σᵢ qᵢVᵢ, where Vᵢ is the total potential at the location of charge i due to all other charges. The factor of ½ is the fix for double-counting, and it appears throughout electrostatics whenever you move from pairwise interactions to a self-consistent sum.

Think of assembling the system step by step, bringing charges in from infinity one at a time. The first charge costs no energy (no existing field to work against). The second charge must be brought in against the field of the first, costing U₁₂ = kq₁q₂/r₁₂. The third charge must be brought in against the fields of both previous charges, costing U₁₃ + U₂₃. The total is the sum over all unique pairs — which is exactly what the ½Σᵢ qᵢVᵢ formula computes. This assembly energy equals the energy stored in the electric field throughout all space, a deep connection that becomes explicit when you study energy density of the electric field.

The practical consequence is that **energy is required to assemble like charges and is released when opposite charges are brought together**. The binding energy of charge distributions — from capacitors (charges on two plates held at a potential difference) to atomic electron shells — is computed from exactly this accounting. For a capacitor, the stored energy U = ½QV = ½CV² emerges directly from this framework: the ½ has the same origin as the ½ in the charge assembly formula.

