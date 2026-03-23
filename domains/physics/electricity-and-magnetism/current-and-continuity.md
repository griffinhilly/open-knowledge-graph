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
status: validated
---

# Electric Current and Continuity Equation

## Core Idea
Electric current I = dQ/dt is charge flow rate. Current density is J⃗ = nqv⃗_d where n is carrier density and v⃗_d is drift velocity. The continuity equation, ∂ρ/∂t + ∇·J⃗ = 0, expresses charge conservation: charge density decreases at points where current diverges. In steady state, ∇·J⃗ = 0, so current is conserved at circuit junctions (Kirchhoff's current law).

## Questions

```yaml
- question: "A wire narrows from a wide section to a thin section while carrying a steady current. What happens to the current density J in the thin section?"
  type: multiple-choice
  options:
    - "J decreases, because fewer carriers fit in the thin section"
    - "J increases, because the same charge flow must pass through a smaller cross-sectional area"
    - "J stays the same, because current is conserved"
    - "J doubles, because the resistance doubles"
  answer: 1
  explanation: "Current I = J·A is conserved along the wire in steady state. If I is constant and the cross-sectional area A decreases, then J = I/A must increase proportionally. The same charge per second is being forced through a smaller cross-section, so the charge density of flow (current density) must be higher. This is why current density is a vector field — it varies spatially even when the total current is constant."

- question: "Kirchhoff's Current Law (the sum of currents into a junction equals the sum leaving) is best understood as which of the following?"
  type: multiple-choice
  options:
    - "An empirical rule discovered by measuring hundreds of circuits"
    - "A consequence of charge conservation (continuity equation) in steady state, where ∇·J = 0"
    - "A consequence of Ohm's Law at junctions"
    - "A rule that applies only to resistive circuits, not to capacitive or inductive ones"
  answer: 1
  explanation: "KCL follows directly from the continuity equation ∂ρ/∂t + ∇·J = 0 in steady state. Setting ∂ρ/∂t = 0 gives ∇·J = 0 — current has no sources or sinks inside the conductor. Integrating over a small volume surrounding a junction, the divergence theorem converts this to: net charge flow out = 0, which is precisely KCL. It is not empirical but derived from charge conservation, and it applies to any circuit element in steady state, not just resistors."

- question: "In a metal wire, conventional current flows in the same direction as the drift velocity of the electrons."
  type: true-false
  answer: false
  explanation: "Conventional current is defined as the direction positive charges would flow — historically established before the discovery that electrons (negative charges) carry current in metals. In a metal, electrons drift opposite to the electric field direction. Since conventional current is opposite to electron drift, conventional current and electron drift velocity point in opposite directions. This is a persistent source of sign errors; always distinguish between carrier motion and conventional current direction."

- question: "The continuity equation ∂ρ/∂t + ∇·J = 0 implies that in steady state, no charge accumulates or depletes at any point inside the conductor."
  type: true-false
  answer: true
  explanation: "In steady state, all quantities are time-independent, so ∂ρ/∂t = 0. The continuity equation then requires ∇·J = 0 everywhere inside the conductor — the current field has no divergence. Any point where more current flowed out than in would see charge depletion (∂ρ/∂t < 0), violating steady state. This confirms that charge distribution is static in a DC circuit, and any current entering a region must equal current leaving it."

- question: "Why does the continuity equation reduce to Kirchhoff's Current Law in the context of a DC circuit junction?"
  type: short-answer
  answer: "In steady state, ∂ρ/∂t = 0, so the continuity equation becomes ∇·J = 0. Integrating over a small closed volume surrounding the junction and applying the divergence theorem converts this into a surface integral: the net charge flux out of the surface is zero. This means the sum of currents entering the junction equals the sum leaving — which is KCL."
  explanation: "The derivation shows KCL is not an independent empirical law but a macroscopic consequence of the local charge conservation law. The continuity equation holds at every point in space; KCL is what you get when you apply it to the specific geometry of a circuit junction. Understanding this connection reveals that all of circuit theory ultimately rests on conservation laws, not just convenient approximations."
```

## Explainer

Electric current is simply charge in motion — but to understand it precisely, you need to connect it to your prerequisite: charge conservation. When charge flows through a wire, total charge doesn't appear or disappear; it moves. **Electric current** I = dQ/dt measures how fast charge crosses a surface: if 1 coulomb passes a point per second, that's 1 ampere. The direction of conventional current follows positive charge flow (or, equivalently, opposite to electron motion in a metal).

The microscopic picture makes this more concrete. Imagine a wire filled with free electrons, each drifting slowly in response to an electric field. The **current density** J⃗ = nqv⃗_d packages three quantities: n (charge carriers per unit volume), q (the charge of each carrier), and v⃗_d (their average drift velocity). A thick wire can carry the same current as a thin wire if the drift velocity adjusts accordingly — J⃗ is higher in the thinner section because the same charge must squeeze through a smaller cross-section. Current density is a vector field: it varies in space and encodes both magnitude and direction of charge flow at every point.

The **continuity equation** ∂ρ/∂t + ∇·J⃗ = 0 is the mathematical expression of charge conservation in differential form. Read it as: the rate at which charge density decreases at a point equals the net outward current flow from that point. If more current flows out of a small volume than flows in, charge must be depleting inside it. This is the divergence theorem applied to charge — the same mathematics that appears in Gauss's law, but now tracking current flow rather than field lines.

In **steady state**, nothing changes with time, so ∂ρ/∂t = 0 and the continuity equation reduces to ∇·J⃗ = 0. This means current has no sources or sinks anywhere inside the conductor — it is divergence-free. Apply this to a wire junction: all the current flowing in must equal all the current flowing out. This is Kirchhoff's current law — not a separate empirical rule invented for circuits, but a direct consequence of charge conservation in steady state. The continuity equation thus unifies macroscopic circuit rules with the underlying field description.
