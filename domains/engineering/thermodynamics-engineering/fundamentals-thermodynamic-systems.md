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

## Explainer

Every thermodynamic analysis starts with the same question: what exactly are you analyzing? Before applying the first or second law, before computing work or heat, you must define the **system** — the region or quantity of matter under study — and its **boundary** — the surface separating the system from its surroundings. This is not a bookkeeping formality; the choice of system boundary determines which energy and mass terms appear in your balance equations and which belong to the surroundings.

Three system types cover virtually all engineering applications. A **closed system** (or control mass) contains a fixed quantity of mass: no matter crosses its boundary, though heat or work may. A piston-cylinder device with a sealed charge of gas is the canonical example — gas can be heated, compressed, or expanded, but the amount of gas is fixed. An **open system** (or control volume) allows mass to flow across its boundary: turbines, compressors, pumps, heat exchangers, and nozzles all involve mass flowing in and out. The energy balance for an open system must account for the enthalpy carried by the flowing mass, not just internal energy. An **isolated system** exchanges neither mass nor energy with its surroundings — a theoretical limit useful for applying the entropy principle, since entropy of an isolated system can only increase. Most real engineering devices are open systems; the closed-system analysis is a stepping stone that clarifies the physics before adding the complexity of flow.

The boundary itself carries important properties. A **rigid boundary** transmits no boundary work (W = ∫P dV = 0 when volume is fixed). A **movable boundary** transmits work as it displaces against external pressure. A **diathermal boundary** allows heat transfer; an **adiabatic boundary** does not. Real devices often combine types — an insulated tank (adiabatic wall) with an inlet pipe (open boundary) and a weighted piston (movable boundary). Each section of the boundary contributes a distinct term to the energy balance, and correctly cataloguing those contributions before writing any equation is what separates clean analyses from algebra errors.

The most important lesson is that the system boundary is a design decision, not a physical fact. The same apparatus can be analyzed as a closed system (following a parcel of fluid as it passes through a pump) or as an open system (treating the pump casing as a fixed control volume with fluid flowing through). Both are correct; they lead to the same physical predictions but use different mathematical forms. The choice should be driven by what is known: if you know what is happening to a fixed mass over time, choose a closed system; if you know flow rates and inlet/outlet conditions, choose a control volume. This judgment is the foundational skill in engineering thermodynamics — everything else builds on getting the system definition right.
