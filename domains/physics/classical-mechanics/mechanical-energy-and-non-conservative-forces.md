---
id: mechanical-energy-and-non-conservative-forces
title: Mechanical Energy and Non-Conservative Forces
domain: physics
course: classical-mechanics
prerequisites:
- id: conservation-of-energy
  type: hard
- id: work-by-non-conservative-forces
  type: hard
builds-toward:
- energy-dissipation-in-damped-oscillations
tags:
- energy
- conservation
- non-conservative
- dissipation
stage: formal-systems
status: draft
---

# Mechanical Energy and Non-Conservative Forces

## Core Idea
Mechanical energy (KE + PE) is conserved only when all forces are conservative. With non-conservative forces present, the modified conservation law is E_mech,i + W_nc = E_mech,f, where W_nc is the work done by non-conservative forces (negative if they dissipate energy). Total energy including heat is always conserved, but mechanical energy decreases.

## Explainer

From conservation of energy, you know that the total energy of an isolated system is conserved — energy is neither created nor destroyed, only transformed. From work done by non-conservative forces, you know that forces like friction and air resistance do net negative work on an object and don't store that energy in any recoverable potential energy form. This topic combines those two ideas into the **modified conservation law**: a precise accounting tool for systems where not all forces are conservative.

Start with the ideal case you already know. When only conservative forces act — gravity, ideal springs, electrostatic forces — mechanical energy (KE + PE) is perfectly conserved. A ball tossed upward trades kinetic energy for gravitational potential energy and back, with no loss. You can solve for speeds and heights at any point using energy accounting alone, without tracking force and acceleration at every instant. This is the power of the energy method.

Now introduce **non-conservative forces** such as sliding friction. Friction does negative work on the object it acts on — it opposes motion and removes mechanical energy from the system. But total energy is still conserved: the mechanical energy that disappears reappears as **thermal energy** — the microscopic random motion of atoms in the contacting surfaces. The modified law captures this precisely: E_mech,f = E_mech,i + W_nc, where W_nc is the work done by non-conservative forces. Since friction's work is negative, final mechanical energy is less than initial. The gap is exactly the thermal energy generated.

The practical skill is correctly identifying which forces are conservative (include their contribution through potential energy terms) and which are non-conservative (compute their work separately as W_nc), then applying the equation. For a block sliding down a rough ramp, you know the initial height and thus initial PE, you calculate frictional work from the friction force and path length, and you solve for the final speed. The critical error to avoid is treating friction as though it merely slows the object while conserving mechanical energy — friction *permanently converts* mechanical energy to heat, which cannot spontaneously reconvert. Total energy bookkeeping always balances; it is only the mechanical portion that decreases when non-conservative forces are present.
