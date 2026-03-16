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

## Explainer

You already know from current and continuity that current density J⃗ describes how much charge flows through a unit area per unit time. The key question is: what drives that flow? In a conductor, the answer is an applied electric field. But free electrons in a metal don't accelerate indefinitely — they collide with lattice ions, impurity atoms, and phonons. The **Drude model** captures this in a simple picture: electrons accelerate under the field, reach some average velocity, scatter and restart, then accelerate again. The net effect is a steady **drift velocity** proportional to the applied field.

From Newton's law for a single electron: the field exerts force qE, and the electron scatters every τ seconds (the mean collision time or **relaxation time**). At steady state the average drift velocity is v_d = qEτ/m. The current density is J = nqv_d, where n is the number of conduction electrons per unit volume. Substituting: J = (nq²τ/m)E. The quantity in parentheses is the **conductivity** σ = nq²τ/m, so J⃗ = σE⃗ — the microscopic statement of Ohm's law. The linear relationship between J and E is not obvious from first principles; it follows from the assumption that τ doesn't depend on field strength, which holds for ordinary electric fields.

To connect to the familiar macroscopic form V = IR, integrate the microscopic relationship across a cylindrical conductor of length L and cross-sectional area A. The field E = V/L (voltage per length), and J = I/A (current per area). Substituting into J = σE: I/A = σ(V/L), which rearranges to V = (L/σA)I = RI where R = L/(σA) = ρL/A with **resistivity** ρ = 1/σ. The geometry (L/A) and the material (ρ) factor cleanly. A long thin wire has high resistance; a short fat one has low resistance — exactly what intuition suggests from the analogy of water flowing through a pipe.

The conductivity formula σ = nq²τ/m reveals what makes a good conductor: high carrier density n (metals have ~10²⁸ electrons/m³) and long scattering time τ (few collisions). Temperature matters because higher temperatures mean more lattice vibrations and shorter τ, which is why metallic resistance increases with temperature. Semiconductors behave oppositely — higher temperature generates more carriers (increasing n), so conductivity increases with temperature, giving them the opposite sign of temperature coefficient.
