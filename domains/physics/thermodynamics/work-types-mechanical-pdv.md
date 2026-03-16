---
id: work-types-mechanical-pdv
title: 'Types of Work: Mechanical PdV and Beyond'
domain: physics
course: thermodynamics
prerequisites:
- id: first-law-of-thermodynamics
  type: hard
builds-toward:
- polytropic-process-index
- otto-cycle-internal-combustion
tags:
- work
- energy-transfer
- first-law
stage: formal-systems
status: draft
---

# Types of Work: Mechanical PdV and Beyond

## Core Idea
While PdV work (mechanical work against external pressure) is the most common form in thermodynamics, other work types include electrical work, surface work, and magnetic work. The first law generalizes as dU = đQ - đW_total, where W includes all forms of work done by the system; for a closed system with only PdV work, this simplifies to dU = đQ - PdV. Understanding which work terms apply is essential for applying the first law correctly to diverse physical systems.

## How It's Best Learned
Solve problems with multiple work terms: a gas expanding against external pressure plus electrical work. Compare systems where PdV work dominates versus those where other work matters.

## Common Misconceptions
- Assuming the only work is PdV work in all contexts.
- Confusing sign conventions: W as work by the system vs. on the system.
- Forgetting that surface work γdA can be significant at small scales.

## Explainer

The first law says dU = đQ - đW. You've already learned that a system's internal energy changes when it receives heat or does work. But what counts as "work"? In introductory thermodynamics, work usually means **PdV work** — the mechanical work done when a gas expands against external pressure. When a piston pushes outward against pressure P, the work done by the gas is W = ∫P dV. This arises directly from the force-times-displacement picture you know from mechanics: pressure is force per area, and volume change is area times displacement, so P·dV is force times distance.

The first law is more general than any single work type, however. A battery discharging through a resistor does **electrical work** — charge moving through a potential difference. A soap bubble growing does **surface work** against surface tension — γ dA, where γ is the surface tension coefficient and dA is the change in area. A magnetized material does **magnetic work** — μ₀ H dM, where H is the applied field and M is the magnetization. In each case the work term has the same mathematical structure: an intensive variable (pressure, voltage, surface tension, magnetic field) multiplied by the differential of an extensive variable (volume, charge, area, magnetization). The total work is the sum of all applicable terms: đW_total = P dV + electrical + surface + magnetic + ....

For most large-scale gas problems, PdV dominates and all other terms are negligible — which is why introductory courses start there. But at small scales, the calculus changes. Inside a living cell, surface tension at membrane interfaces contributes meaningfully. Inside a lithium-ion battery, electrical work is the whole story. Inside a ferromagnet being magnetized, magnetic work is the relevant term. Knowing which work terms belong in a given situation is the first step in correctly applying the first law; including irrelevant terms wastes effort, while omitting relevant ones produces wrong answers.

Sign convention is a persistent source of confusion. The **physics convention** writes dU = đQ - đW, so work done *by* the system is positive (an expanding gas does positive work, losing internal energy). The **engineering convention** writes dU = đQ + đW, so work done *on* the system is positive (a compressor putting energy into a gas does positive work). Both conventions are self-consistent — they define đW with opposite signs. Always identify which convention a textbook or problem is using, and never mix them within a single calculation. When in doubt, state your convention explicitly before solving.
