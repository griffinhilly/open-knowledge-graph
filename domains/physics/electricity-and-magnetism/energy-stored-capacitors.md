---
id: energy-stored-capacitors
title: Energy Storage and Forces in Capacitors
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: capacitor-geometry
  type: hard
builds-toward:
- capacitor-networks
tags:
- energy
- force
- field-energy
stage: formal-systems
status: draft
---

# Energy Storage and Forces in Capacitors

## Core Idea
Energy stored in a capacitor is U = (1/2)QV = (1/2)CV² = (1/2)Q²/C. This energy is distributed in the electric field with density u = (ε₀/2)κᵣE². Forces between plates arise from energy changes with separation: F = −∂U/∂d. Dielectrics are attracted into capacitors because they lower the total stored energy.

## Explainer

From your study of capacitor geometry, you know that a capacitor stores separated charge Q on two conductors held at a potential difference V, with capacitance C = Q/V. But a charged capacitor also stores something more tangible: **electrical potential energy** that can be released to do work. The three equivalent expressions U = ½QV = ½CV² = ½Q²/C all say the same thing, but each is most useful in different contexts — use ½CV² when V is fixed (like a battery-connected capacitor), and ½Q²/C when Q is fixed (like an isolated charged capacitor).

Where is this energy physically located? The field picture gives the deeper answer. Between the capacitor plates, an electric field E exists with energy density u = (ε₀/2)κᵣE², where κᵣ is the dielectric constant of any material between the plates. Integrating this energy density over the volume between the plates recovers exactly U = ½CV². This tells you that **the energy is stored in the electric field itself**, not on the surface charge or in the conductors. This is not merely a bookkeeping choice — it becomes essential in electrodynamics, where fields can carry energy through empty space.

The **energy method** for calculating forces is one of the most powerful tools that flows from this picture. Rather than finding the force by computing the electric field and then integrating pressure over a surface, you can differentiate the stored energy with respect to the relevant displacement: F = −∂U/∂d, where d is the plate separation. The sign is crucial: the force is in the direction that decreases U. For a charged capacitor with fixed charge Q (isolated), increasing d increases U (since U = Q²/2C and C decreases as d increases), so F = −∂U/∂d is negative — the plates attract each other, as expected.

The same logic explains why a **dielectric is pulled into a capacitor**. When a dielectric slab partially fills the gap between the plates at fixed voltage, the dielectric increases the effective capacitance of the filled portion. This increases total stored energy (U = ½CV², and C is larger). But wait — if energy increases, why is the dielectric pulled in? The resolution is that at fixed voltage, the battery does work to maintain V as C increases; the dielectric lowers the *free energy* (the energy the system can supply as mechanical work), so the net force still draws the dielectric inward. At fixed charge, the story is simpler: the dielectric lowers U directly, and the system lowers its energy by pulling the dielectric in. Both cases illustrate that forces on dielectrics arise not from direct field forces on bulk material but from energy minimization — a theme that recurs throughout electrostatics and thermodynamics.
