---
id: energy-stored-capacitors
title: Energy Storage and Forces in Capacitors
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: capacitor-geometry
  type: hard
- id: capacitor-field-energy-storage
  type: soft
builds-toward:
- capacitor-networks
tags:
- energy
- force
- field-energy
stage: formal-systems
status: validated
---
# Energy Storage and Forces in Capacitors

## Core Idea
Energy stored in a capacitor is U = (1/2)QV = (1/2)CV² = (1/2)Q²/C. This energy is distributed in the electric field with density u = (ε₀/2)κᵣE². Forces between plates arise from energy changes with separation: F = −∂U/∂d. Dielectrics are attracted into capacitors because they lower the total stored energy.

## Questions

```yaml
- question: "An isolated capacitor (disconnected from any battery) holds fixed charge Q. The plates are slowly pulled farther apart. What happens to the stored energy?"
  type: multiple-choice
  options:
    - "Energy decreases, because the plates move in the direction of the attractive force between them"
    - "Energy stays the same, because charge Q is conserved"
    - "Energy increases, because C decreases and U = Q²/2C grows as C shrinks"
    - "Energy decreases, because the electric field weakens as the plate separation increases"
  answer: 2
  explanation: "With fixed charge Q, U = Q²/2C. As plates separate, capacitance C = ε₀A/d decreases (C ∝ 1/d), so U = Q²/2C increases. This tells you that an external force must do positive work to separate the plates — the system's energy increases. Meanwhile F = −∂U/∂d is negative (force opposes increasing d), confirming the plates attract each other. Option A confuses the direction of the force with the direction of energy change when an external agent does work against that force."

- question: "A capacitor is connected to a battery (fixed voltage V). A dielectric slab is slowly inserted between the plates, increasing the capacitance C and therefore the stored energy U = ½CV². Why is the dielectric nonetheless pulled inward?"
  type: multiple-choice
  options:
    - "Because the electric field exerts a direct attractive force on the bulk dielectric material"
    - "Because the battery supplies extra charge to maintain V; the work done by the battery exceeds the energy stored, and the surplus goes to mechanical work pulling the dielectric inward"
    - "Because the dielectric reduces the electric field between the plates, lowering energy"
    - "Because the dielectric is attracted by the magnetic field generated during capacitor charging"
  answer: 1
  explanation: "At fixed V, inserting the dielectric increases C, which increases U = ½CV². This seems to argue against insertion — but the battery must supply extra charge (ΔQ = V·ΔC) to maintain V. The energy supplied by the battery is V·ΔQ = V²·ΔC, which is twice the energy increase ΔU = ½ΔC·V². The excess V²·ΔC/2 provides the mechanical work pulling the dielectric inward. The dielectric is attracted not by a direct field force on bulk material but by the system's tendency to lower its free energy — the energy available as mechanical work."

- question: "The energy stored in a charged capacitor resides in the electric field between the plates, not on the surface charges themselves."
  type: true-false
  answer: true
  explanation: "The energy density in the electric field is u = (ε₀/2)κᵣE². Integrating this over the volume between the plates recovers exactly U = ½CV². This is more than bookkeeping: in electrodynamics, fields can carry energy through vacuum (as in electromagnetic waves) independently of any charges. The field-energy picture is the correct fundamental view, with charge distributions as the sources that create the fields."

- question: "The three energy expressions U = ½QV, U = ½CV², and U = ½Q²/C always give the same numerical result, so it does not matter which one you use when analyzing how energy changes as capacitor plates are separated."
  type: true-false
  answer: false
  explanation: "All three expressions are equivalent at any single moment (they all equal U), but they depend on different variables — Q, C, and V — and different quantities are held constant in different situations. When plates separate at fixed Q (isolated capacitor), use U = Q²/2C: Q is constant, C changes. Using U = ½CV² with varying V requires tracking how V changes simultaneously, which adds complexity without benefit. Choosing the form whose fixed variable matches your constraint makes the physics transparent and the algebra clean."

- question: "Explain why the energy stored in a capacitor is U = ½QV rather than U = QV, even though the charge Q was moved across potential difference V."
  type: short-answer
  answer: "The factor of ½ arises because the potential difference builds up progressively as charge is transferred. The first small element of charge dq is moved across a near-zero potential (when the capacitor is nearly uncharged). As charge accumulates, the voltage rises, and later increments of charge are moved against a higher potential. The average potential during charging is V/2, not V. Integrating dU = v·dq from 0 to Q — where v = q/C at each stage — gives U = ∫₀Q (q/C)dq = Q²/2C = ½QV. If you moved all charge Q across the full final potential V, you'd compute QV — but that's not what happens during charging."
  explanation: "The ½ factor is the hallmark of energy stored in a quadratic process (like a spring: U = ½kx²). In both cases, the restoring force grows as the system charges up, so the average force (and thus work per unit displacement) is half the final value."
```

## Explainer

From your study of capacitor geometry, you know that a capacitor stores separated charge Q on two conductors held at a potential difference V, with capacitance C = Q/V. But a charged capacitor also stores something more tangible: **electrical potential energy** that can be released to do work. The three equivalent expressions U = ½QV = ½CV² = ½Q²/C all say the same thing, but each is most useful in different contexts — use ½CV² when V is fixed (like a battery-connected capacitor), and ½Q²/C when Q is fixed (like an isolated charged capacitor).

Where is this energy physically located? The field picture gives the deeper answer. Between the capacitor plates, an electric field E exists with energy density u = (ε₀/2)κᵣE², where κᵣ is the dielectric constant of any material between the plates. Integrating this energy density over the volume between the plates recovers exactly U = ½CV². This tells you that **the energy is stored in the electric field itself**, not on the surface charge or in the conductors. This is not merely a bookkeeping choice — it becomes essential in electrodynamics, where fields can carry energy through empty space.

The **energy method** for calculating forces is one of the most powerful tools that flows from this picture. Rather than finding the force by computing the electric field and then integrating pressure over a surface, you can differentiate the stored energy with respect to the relevant displacement: F = −∂U/∂d, where d is the plate separation. The sign is crucial: the force is in the direction that decreases U. For a charged capacitor with fixed charge Q (isolated), increasing d increases U (since U = Q²/2C and C decreases as d increases), so F = −∂U/∂d is negative — the plates attract each other, as expected.

The same logic explains why a **dielectric is pulled into a capacitor**. When a dielectric slab partially fills the gap between the plates at fixed voltage, the dielectric increases the effective capacitance of the filled portion. This increases total stored energy (U = ½CV², and C is larger). But wait — if energy increases, why is the dielectric pulled in? The resolution is that at fixed voltage, the battery does work to maintain V as C increases; the dielectric lowers the *free energy* (the energy the system can supply as mechanical work), so the net force still draws the dielectric inward. At fixed charge, the story is simpler: the dielectric lowers U directly, and the system lowers its energy by pulling the dielectric in. Both cases illustrate that forces on dielectrics arise not from direct field forces on bulk material but from energy minimization — a theme that recurs throughout electrostatics and thermodynamics.
