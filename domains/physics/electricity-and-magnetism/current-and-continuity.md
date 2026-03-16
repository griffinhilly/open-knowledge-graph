---
id: current-and-continuity
title: Electric Current and Continuity Equation
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: conservation-of-electric-charge
  type: hard
builds-toward:
- ohms-law-microscopic
tags:
- current
- continuity
- charge-conservation
stage: formal-systems
status: draft
---

# Electric Current and Continuity Equation

## Core Idea
Electric current I = dQ/dt is charge flow rate. Current density is J⃗ = nqv⃗_d where n is carrier density and v⃗_d is drift velocity. The continuity equation, ∂ρ/∂t + ∇·J⃗ = 0, expresses charge conservation: charge density decreases at points where current diverges. In steady state, ∇·J⃗ = 0, so current is conserved at circuit junctions (Kirchhoff's current law).

## Explainer

Electric current is simply charge in motion — but to understand it precisely, you need to connect it to your prerequisite: charge conservation. When charge flows through a wire, total charge doesn't appear or disappear; it moves. **Electric current** I = dQ/dt measures how fast charge crosses a surface: if 1 coulomb passes a point per second, that's 1 ampere. The direction of conventional current follows positive charge flow (or, equivalently, opposite to electron motion in a metal).

The microscopic picture makes this more concrete. Imagine a wire filled with free electrons, each drifting slowly in response to an electric field. The **current density** J⃗ = nqv⃗_d packages three quantities: n (charge carriers per unit volume), q (the charge of each carrier), and v⃗_d (their average drift velocity). A thick wire can carry the same current as a thin wire if the drift velocity adjusts accordingly — J⃗ is higher in the thinner section because the same charge must squeeze through a smaller cross-section. Current density is a vector field: it varies in space and encodes both magnitude and direction of charge flow at every point.

The **continuity equation** ∂ρ/∂t + ∇·J⃗ = 0 is the mathematical expression of charge conservation in differential form. Read it as: the rate at which charge density decreases at a point equals the net outward current flow from that point. If more current flows out of a small volume than flows in, charge must be depleting inside it. This is the divergence theorem applied to charge — the same mathematics that appears in Gauss's law, but now tracking current flow rather than field lines.

In **steady state**, nothing changes with time, so ∂ρ/∂t = 0 and the continuity equation reduces to ∇·J⃗ = 0. This means current has no sources or sinks anywhere inside the conductor — it is divergence-free. Apply this to a wire junction: all the current flowing in must equal all the current flowing out. This is Kirchhoff's current law — not a separate empirical rule invented for circuits, but a direct consequence of charge conservation in steady state. The continuity equation thus unifies macroscopic circuit rules with the underlying field description.
