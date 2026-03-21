---
id: ohms-law-microscopic
title: 'Ohm''s Law: Microscopic and Macroscopic Forms'
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: current-and-continuity
  type: hard
builds-toward:
- resistor-combinations
tags:
- ohms-law
- resistivity
- conductivity
stage: formal-systems
status: draft
---

# Ohm's Law: Microscopic and Macroscopic Forms

## Core Idea
Ohm's law in microscopic form: J⃗ = σE⃗, where σ = nq²τ/m is conductivity. In macroscopic form: V = IR, where R = ρL/A is resistance (ρ = 1/σ is resistivity). Resistance depends on material (ρ) and geometry (L/A). Ohm's law emerges from drift motion of charge carriers colliding with the lattice; it is a material property that holds for linear response.

## Questions

```yaml
- question: "Two wires are made of the same copper (same resistivity ρ). Wire A is twice as long and half the cross-sectional area of Wire B. How does the resistance of A compare to B?"
  type: multiple-choice
  options:
    - "Wire A has the same resistance as B — same material means same resistance"
    - "Wire A has twice the resistance of B"
    - "Wire A has 4 times the resistance of B"
    - "Wire A has half the resistance of B"
  answer: 2
  explanation: "Resistance R = ρL/A. For Wire A: L_A = 2L, A_A = A/2, so R_A = ρ(2L)/(A/2) = 4ρL/A = 4R_B. Wire A has 4 times the resistance. The common misconception is that same material means same resistance (option A), but R depends on both material (ρ) and geometry (L/A). Doubling length doubles resistance; halving area doubles it again; the effects multiply."

- question: "In the Drude model, why does current density J depend linearly on the electric field E rather than quadratically or in some other way?"
  type: multiple-choice
  options:
    - "Because charge is defined as current times time, making the relationship linear by definition"
    - "Because the mean collision time τ is independent of field strength for ordinary electric fields, so drift velocity — and therefore J — scales linearly with E"
    - "Because the number of conduction electrons n doubles when E doubles"
    - "Because resistivity ρ is defined as E/J, making the linear relationship tautological"
  answer: 1
  explanation: "The linearity of Ohm's law is not obvious — it follows from the assumption that τ (mean time between collisions) doesn't change with field strength. Under this assumption, drift velocity v_d = qEτ/m scales linearly with E. Since J = nqv_d, J scales linearly with E too, giving J = σE. This is an empirical approximation valid for ordinary field strengths; at very high fields τ can become field-dependent and Ohm's law breaks down."

- question: "The resistance of a metallic conductor increases when temperature rises because higher temperature increases the number of conduction electrons."
  type: true-false
  answer: false
  explanation: "In metals, the number of conduction electrons n does not significantly change with temperature — metals already have a high, fixed density of free electrons. Instead, higher temperature increases lattice vibrations, which shorten the mean collision time τ. Since σ = nq²τ/m, smaller τ means lower σ and higher resistance. Resistance increases because of more collisions, not more electrons. Semiconductors are opposite: temperature promotes more electrons to the conduction band, increasing n and decreasing resistance."

- question: "The microscopic Ohm's law J⃗ = σE⃗ applies universally to all materials, while V = IR is only an approximation valid for certain geometries."
  type: true-false
  answer: false
  explanation: "Neither form of Ohm's law is universal — both describe a linear regime that holds only for *ohmic* (linear) materials. Diodes, transistors, and many other components are non-ohmic: their J–E relationships are not proportional. The distinction between the microscopic and macroscopic forms is one of generality (J = σE is local; V = IR integrates across a conductor with specific geometry), not of exactness. Both forms break down for non-ohmic materials."

- question: "Explain why a semiconductor's resistance decreases as temperature increases, while a metal's resistance increases — despite both obeying J = σE with σ = nq²τ/m."
  type: short-answer
  answer: "The conductivity formula contains two temperature-sensitive quantities: carrier density n and scattering time τ. In metals, n is approximately constant (the conduction band is full), so temperature only affects τ — more lattice vibrations cause more frequent collisions, reducing τ, decreasing σ, and increasing resistance. In semiconductors, the conduction band is mostly empty at low temperatures; increasing temperature promotes electrons across the band gap, dramatically increasing n. This increase in n dominates over the decrease in τ, so σ increases and resistance falls."
  explanation: "Both behaviors follow from the same formula, with different dominant mechanisms. In metals τ is the controlling variable; in semiconductors n is. Temperature coefficient of resistance is positive for metals and negative for semiconductors — a direct consequence. This has practical implications: superconducting metals and cooling improve metallic conductivity, while semiconductor devices conduct better when heated."
```

## Explainer

You already know from current and continuity that current density J⃗ describes how much charge flows through a unit area per unit time. The key question is: what drives that flow? In a conductor, the answer is an applied electric field. But free electrons in a metal don't accelerate indefinitely — they collide with lattice ions, impurity atoms, and phonons. The **Drude model** captures this in a simple picture: electrons accelerate under the field, reach some average velocity, scatter and restart, then accelerate again. The net effect is a steady **drift velocity** proportional to the applied field.

From Newton's law for a single electron: the field exerts force qE, and the electron scatters every τ seconds (the mean collision time or **relaxation time**). At steady state the average drift velocity is v_d = qEτ/m. The current density is J = nqv_d, where n is the number of conduction electrons per unit volume. Substituting: J = (nq²τ/m)E. The quantity in parentheses is the **conductivity** σ = nq²τ/m, so J⃗ = σE⃗ — the microscopic statement of Ohm's law. The linear relationship between J and E is not obvious from first principles; it follows from the assumption that τ doesn't depend on field strength, which holds for ordinary electric fields.

To connect to the familiar macroscopic form V = IR, integrate the microscopic relationship across a cylindrical conductor of length L and cross-sectional area A. The field E = V/L (voltage per length), and J = I/A (current per area). Substituting into J = σE: I/A = σ(V/L), which rearranges to V = (L/σA)I = RI where R = L/(σA) = ρL/A with **resistivity** ρ = 1/σ. The geometry (L/A) and the material (ρ) factor cleanly. A long thin wire has high resistance; a short fat one has low resistance — exactly what intuition suggests from the analogy of water flowing through a pipe.

The conductivity formula σ = nq²τ/m reveals what makes a good conductor: high carrier density n (metals have ~10²⁸ electrons/m³) and long scattering time τ (few collisions). Temperature matters because higher temperatures mean more lattice vibrations and shorter τ, which is why metallic resistance increases with temperature. Semiconductors behave oppositely — higher temperature generates more carriers (increasing n), so conductivity increases with temperature, giving them the opposite sign of temperature coefficient.
