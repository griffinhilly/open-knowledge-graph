---
id: work-types-mechanical-pdv
title: 'Types of Work: Mechanical PdV and Beyond'
domain: physics
course: thermodynamics
prerequisites:
- id: first-law-of-thermodynamics
  type: hard
- id: path-functions-vs-state-functions
  type: soft
builds-toward:
- polytropic-process-index
- otto-cycle-internal-combustion
tags:
- work
- energy-transfer
- first-law
stage: formal-systems
status: validated
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

## Questions

```yaml
- question: "A lithium-ion battery discharges completely at constant volume, converting stored chemical energy into electrical energy in an external circuit. Which work term in the first law accounts for this energy transfer?"
  type: multiple-choice
  options:
    - "PdV work — all thermodynamic work transfers occur through volume changes"
    - "Electrical work (voltage × charge transferred), because the dominant energy transfer mechanism is charge moving through a potential difference"
    - "Surface work γdA, because ion transport across the electrode interface changes interfacial area"
    - "No work term — the first law only applies to systems that exchange heat"
  answer: 1
  explanation: "At constant volume, PdV = 0 — no mechanical expansion work occurs. The energy leaving the battery is electrical work: charge q moves through potential difference V, giving W_elec = V·q (or in differential form, V dq). This is the appropriate work term for this system. The first law dU = đQ − đW_total remains valid; you simply use the correct work term. Option A is the common misconception that PdV is the only work type — it applies to gas systems but not batteries. Option C (surface work) is real but negligible here."

- question: "A gas expands against external pressure, doing 100 J of work on the surroundings. A student uses the physics convention dU = đQ − đW (work done *by* system is positive). Their textbook uses the engineering convention dU = đQ + đW (work done *on* system is positive). Which statement is correct?"
  type: multiple-choice
  options:
    - "Both conventions give đW = +100 J and agree on ΔU"
    - "The student has đW = +100 J (work done by system); the textbook has đW = −100 J (work done on system is negative for expansion). Both give the same ΔU."
    - "The conventions give different values of ΔU, so one must be wrong"
    - "The engineering convention always assigns positive work to expansion; the physics convention assigns negative work"
  answer: 1
  explanation: "Both conventions are self-consistent and give the same ΔU — they just define đW with opposite signs. Physics convention: đW = +100 J (the gas does work), so ΔU = Q − 100. Engineering convention: đW = −100 J (work *on* system during expansion is negative, since the system is doing the pushing), so ΔU = Q + (−100) = Q − 100. Identical result. The danger is mixing conventions: never use the physics đW formula with the engineering sign for đW, or vice versa."

- question: "Surface tension work (γdA) is negligible in most physical systems and can safely be ignored when applying the first law."
  type: true-false
  answer: false
  explanation: "Surface tension work is negligible at macroscopic scales where PdV dominates, but it is significant at small scales — for example, in living cells where membrane surface tension affects thermodynamics, in soap films, and in microfluidic systems. The general rule is that which work terms matter depends on the system and scale. Assuming PdV is always dominant ignores important physics at small scales and in specialized systems."

- question: "Every work term in thermodynamics has the mathematical structure of an intensive variable multiplied by the differential of an extensive variable."
  type: true-false
  answer: true
  explanation: "This pattern is universal: PdV (pressure × dvolume), V dq (voltage × dcharge), γ dA (surface tension × darea), μ₀ H dM (magnetic field × dmagnetization). Intensive variables are size-independent (pressure is the same whether you have a little or a lot of gas); extensive variables scale with the amount of substance. This structure is not a coincidence — it reflects the thermodynamic definition of work as a generalized force (intensive) times a generalized displacement (differential of the conjugate extensive variable)."

- question: "Why does applying the first law correctly require identifying which work terms are relevant to a given system, rather than always defaulting to dU = đQ − PdV?"
  type: short-answer
  answer: "dU = đQ − PdV is only correct for a closed system where mechanical expansion/compression is the sole work mechanism. When a system transfers energy through other channels — electrical work in a battery, surface work in a membrane, magnetic work in a ferromagnet — those terms must be included in đW_total. Omitting a relevant work term breaks the energy balance: the equation will not close correctly, and calculated ΔU will be wrong. Including irrelevant terms is harmless (they evaluate to zero for the specific process), but missing relevant ones produces systematically incorrect thermodynamic analysis."
  explanation: "The first law's generality is its strength: dU = đQ − đW_total holds for any closed system in any process. The skill is identifying đW_total correctly for the system at hand — which requires understanding what energy transfer mechanisms are physically active. This is why thermodynamics problems begin by characterizing the system and process, not by writing equations."
```

## Explainer

The first law says dU = đQ - đW. You've already learned that a system's internal energy changes when it receives heat or does work. But what counts as "work"? In introductory thermodynamics, work usually means **PdV work** — the mechanical work done when a gas expands against external pressure. When a piston pushes outward against pressure P, the work done by the gas is W = ∫P dV. This arises directly from the force-times-displacement picture you know from mechanics: pressure is force per area, and volume change is area times displacement, so P·dV is force times distance.

The first law is more general than any single work type, however. A battery discharging through a resistor does **electrical work** — charge moving through a potential difference. A soap bubble growing does **surface work** against surface tension — γ dA, where γ is the surface tension coefficient and dA is the change in area. A magnetized material does **magnetic work** — μ₀ H dM, where H is the applied field and M is the magnetization. In each case the work term has the same mathematical structure: an intensive variable (pressure, voltage, surface tension, magnetic field) multiplied by the differential of an extensive variable (volume, charge, area, magnetization). The total work is the sum of all applicable terms: đW_total = P dV + electrical + surface + magnetic + ....

For most large-scale gas problems, PdV dominates and all other terms are negligible — which is why introductory courses start there. But at small scales, the calculus changes. Inside a living cell, surface tension at membrane interfaces contributes meaningfully. Inside a lithium-ion battery, electrical work is the whole story. Inside a ferromagnet being magnetized, magnetic work is the relevant term. Knowing which work terms belong in a given situation is the first step in correctly applying the first law; including irrelevant terms wastes effort, while omitting relevant ones produces wrong answers.

Sign convention is a persistent source of confusion. The **physics convention** writes dU = đQ - đW, so work done *by* the system is positive (an expanding gas does positive work, losing internal energy). The **engineering convention** writes dU = đQ + đW, so work done *on* the system is positive (a compressor putting energy into a gas does positive work). Both conventions are self-consistent — they define đW with opposite signs. Always identify which convention a textbook or problem is using, and never mix them within a single calculation. When in doubt, state your convention explicitly before solving.
