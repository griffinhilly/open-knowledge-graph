---
id: fundamentals-thermodynamic-systems
title: Fundamentals of Thermodynamic Systems
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: thermodynamic-systems-engineering
  type: hard
- id: temperature-and-thermal-equilibrium
  type: hard
builds-toward:
- control-mass-first-law-applications
- state-functions-path-functions
- steady-flow-energy-equation-engineering
tags:
- systems
- foundations
- definitions
- boundaries
stage: advanced
status: draft
---

# Fundamentals of Thermodynamic Systems

## Core Idea
A thermodynamic system is a defined region or quantity of matter chosen for analysis, with boundaries that may be rigid, movable, or semi-permeable. Systems are classified as closed (fixed mass), open (control volume with mass flow), or isolated based on energy and mass interactions with surroundings. Correctly identifying system boundaries and types is essential for applying conservation equations.

## Questions

```yaml
- question: "An engineer must analyze a centrifugal pump. She knows the inlet and outlet flow rates, pressures, and temperatures. Which system type and energy term should she use?"
  type: multiple-choice
  options:
    - "Closed system, using internal energy — the pump casing contains a fixed mass of fluid at any instant"
    - "Isolated system, since pumps are insulated and exchange no heat with the environment"
    - "Open system (control volume), using enthalpy — mass flows across the boundary and carries both internal energy and flow work"
    - "Closed system, using enthalpy — enthalpy is always the correct energy form for mechanical devices"
  answer: 2
  explanation: "When mass flows in and out, the correct system type is an open system (control volume). For flowing mass, the energy carried across the boundary includes not just internal energy u but also flow work Pv — the work done by upstream fluid pushing the mass through the boundary. The combination u + Pv = h (specific enthalpy) is the correct energy term for flowing streams. The closed system analysis using internal energy is appropriate when following a fixed parcel of fluid, but knowing inlet/outlet conditions makes the control volume approach far more natural for devices like pumps, turbines, and compressors."

- question: "Why must energy balances for open systems use enthalpy (h = u + Pv) for the energy carried by flowing mass, rather than just internal energy (u)?"
  type: multiple-choice
  options:
    - "Enthalpy is a more accurate measure of thermal energy because it accounts for pressure effects"
    - "Flowing mass must push itself across the system boundary against the local pressure, doing work equal to Pv; this flow work plus internal energy gives enthalpy h = u + Pv"
    - "Internal energy is only defined for static systems and loses meaning when mass is in motion"
    - "Enthalpy is more convenient to measure with thermocouples than internal energy"
  answer: 1
  explanation: "When a parcel of mass crosses a system boundary, it is pushed through by the fluid behind it — this takes work. The upstream fluid exerts pressure P on the parcel of specific volume v, doing flow work Pv per unit mass. This work is in addition to whatever internal energy u the parcel carries. The total energy transported across the boundary per unit mass is therefore u + Pv = h, specific enthalpy. This is not a convention or approximation — it is a precise accounting of all energy transfers when mass crosses a boundary. Omitting the Pv term would give the wrong energy balance for turbines, compressors, and all other flow devices."

- question: "The same physical apparatus (such as a pump) can be correctly analyzed using either a closed-system or an open-system framework, and both approaches yield the same physical predictions."
  type: true-false
  answer: true
  explanation: "The system boundary is a choice the engineer makes, not a property of the apparatus. A pump can be analyzed as a control volume (fixed region in space, with fluid flowing through it) using the steady-flow energy equation, or by following a fixed parcel of fluid through the pump as a closed system. Both frameworks are thermodynamically correct and yield consistent predictions for work input, pressure rise, and efficiency. The choice is purely a matter of convenience — the control volume is usually simpler when inlet/outlet conditions are known; the closed system is simpler when following the fate of a specific mass parcel."

- question: "An isolated thermodynamic system can exchange heat with its surroundings, but not work."
  type: true-false
  answer: false
  explanation: "An isolated system exchanges neither heat nor work (nor mass) with its surroundings — it has no interaction with the surroundings whatsoever. This is the definition of isolation in thermodynamics. A system that exchanges heat but not work (or work but not heat) is a closed system with specific boundary properties (adiabatic for no heat, rigid for no work). Isolated systems are mainly theoretical tools used to apply the entropy principle: for an isolated system, entropy can only increase or stay constant, never decrease. Most real engineering devices are open systems (exchanging mass, heat, and work)."

- question: "Why is defining the system boundary the essential first step in any thermodynamic analysis, rather than just a bookkeeping formality?"
  type: short-answer
  answer: "The system boundary determines which physical interactions appear as terms in the energy and mass balance equations, and which belong to the surroundings and are excluded. Choosing a rigid boundary means no boundary work appears (W_boundary = ∫P dV = 0). Choosing an open boundary means mass flow terms enter the energy balance, and those terms must use enthalpy rather than internal energy. Choosing an adiabatic boundary eliminates heat transfer terms. Getting these choices wrong means writing incorrect balance equations — the subsequent algebra will be solving the wrong problem, regardless of how carefully it's executed. The system definition is not a preliminary step before the real work begins; it is the step that determines what the real work will be."
  explanation: "The deeper point from the Explainer is that the same apparatus admits multiple valid system definitions. A competent thermodynamicist chooses the boundary that matches what is known (flow rates and inlet/outlet states → control volume; known mass and process path → closed system). The boundary is a tool for matching the mathematical framework to the available information, not a fact about the world to be discovered."
```

## Explainer

Every thermodynamic analysis starts with the same question: what exactly are you analyzing? Before applying the first or second law, before computing work or heat, you must define the **system** — the region or quantity of matter under study — and its **boundary** — the surface separating the system from its surroundings. This is not a bookkeeping formality; the choice of system boundary determines which energy and mass terms appear in your balance equations and which belong to the surroundings.

Three system types cover virtually all engineering applications. A **closed system** (or control mass) contains a fixed quantity of mass: no matter crosses its boundary, though heat or work may. A piston-cylinder device with a sealed charge of gas is the canonical example — gas can be heated, compressed, or expanded, but the amount of gas is fixed. An **open system** (or control volume) allows mass to flow across its boundary: turbines, compressors, pumps, heat exchangers, and nozzles all involve mass flowing in and out. The energy balance for an open system must account for the enthalpy carried by the flowing mass, not just internal energy. An **isolated system** exchanges neither mass nor energy with its surroundings — a theoretical limit useful for applying the entropy principle, since entropy of an isolated system can only increase. Most real engineering devices are open systems; the closed-system analysis is a stepping stone that clarifies the physics before adding the complexity of flow.

The boundary itself carries important properties. A **rigid boundary** transmits no boundary work (W = ∫P dV = 0 when volume is fixed). A **movable boundary** transmits work as it displaces against external pressure. A **diathermal boundary** allows heat transfer; an **adiabatic boundary** does not. Real devices often combine types — an insulated tank (adiabatic wall) with an inlet pipe (open boundary) and a weighted piston (movable boundary). Each section of the boundary contributes a distinct term to the energy balance, and correctly cataloguing those contributions before writing any equation is what separates clean analyses from algebra errors.

The most important lesson is that the system boundary is a design decision, not a physical fact. The same apparatus can be analyzed as a closed system (following a parcel of fluid as it passes through a pump) or as an open system (treating the pump casing as a fixed control volume with fluid flowing through). Both are correct; they lead to the same physical predictions but use different mathematical forms. The choice should be driven by what is known: if you know what is happening to a fixed mass over time, choose a closed system; if you know flow rates and inlet/outlet conditions, choose a control volume. This judgment is the foundational skill in engineering thermodynamics — everything else builds on getting the system definition right.
