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
- id: energy-dissipation-in-damped-oscillations
  type: soft
builds-toward:
- energy-dissipation-in-damped-oscillations
tags:
- energy
- conservation
- non-conservative
- dissipation
stage: formal-systems
status: validated
---
# Mechanical Energy and Non-Conservative Forces

## Core Idea
Mechanical energy (KE + PE) is conserved only when all forces are conservative. With non-conservative forces present, the modified conservation law is E_mech,i + W_nc = E_mech,f, where W_nc is the work done by non-conservative forces (negative if they dissipate energy). Total energy including heat is always conserved, but mechanical energy decreases.

## Questions

```yaml
- question: "A block slides down a rough ramp with friction. Compared to a frictionless ramp of identical height, which of the following is true at the bottom?"
  type: multiple-choice
  options:
    - "Total energy (mechanical + thermal) is less on the rough ramp because friction removed energy from the system"
    - "The block has less kinetic energy on the rough ramp, and the 'lost' mechanical energy has been permanently converted to thermal energy"
    - "The block has less kinetic energy on the rough ramp, but this energy is stored temporarily in the rough surface and can be recovered"
    - "The block has the same kinetic energy on both ramps because gravity converts the same potential energy in both cases"
  answer: 1
  explanation: "Friction does negative work on the block, permanently converting mechanical energy to thermal energy (microscopic random motion of atoms in the contacting surfaces). The block arrives with less kinetic energy — by exactly the amount of thermal energy generated. Total energy is conserved: the mechanical energy that disappeared reappears as heat. Option C is incorrect: friction-generated heat cannot spontaneously reconvert to mechanical energy."

- question: "Using the modified conservation law E_mech,f = E_mech,i + W_nc, what is the sign of W_nc for a block sliding along a rough horizontal surface that comes to rest?"
  type: multiple-choice
  options:
    - "W_nc = 0 because no conservative forces act on the horizontal surface"
    - "W_nc > 0 because friction adds energy to the system from the surface"
    - "W_nc < 0 because friction does negative work on the block, removing mechanical energy"
    - "W_nc is undefined because the block stops, meaning there is no net displacement"
  answer: 2
  explanation: "Friction opposes motion, so the friction force and displacement point in opposite directions — their dot product is negative. W_nc = F_friction · d · cos(180°) = −F_friction · d < 0. The negative W_nc means final mechanical energy is less than initial, accounting for the kinetic energy converted to heat as the block decelerates. The block has displacement (it slides before stopping), so W_nc is well-defined and negative."

- question: "When non-conservative forces like friction act on a system, the total energy of the universe (including thermal energy) decreases."
  type: true-false
  answer: false
  explanation: "Total energy is ALWAYS conserved — this is the first law of thermodynamics. What decreases is the mechanical energy (KE + PE) of the system, not the total energy. The mechanical energy that disappears converts to thermal energy: the random kinetic energy of atoms in the surfaces in contact. The total energy (mechanical + thermal) remains constant. Only the form changes."

- question: "Non-conservative forces are called 'non-conservative' because the work they do on an object depends on the path taken, not just the starting and ending positions."
  type: true-false
  answer: true
  explanation: "Conservative forces (gravity, springs) do work that depends only on initial and final positions — you can define a potential energy function for them. Non-conservative forces like friction do work that depends on the entire path: a longer or rougher path means more friction work, even between the same two endpoints. This path-dependence is precisely why we cannot assign a potential energy to friction, and why the standard conservation equation (using only potential energy) is insufficient."

- question: "Explain why total energy is conserved when friction acts on a sliding block, even though the block slows down and loses mechanical energy."
  type: short-answer
  answer: "Total energy is conserved because the mechanical energy lost by the block is not destroyed — it is converted into thermal energy in the surfaces in contact. Friction generates heat through microscopic deformation and vibration of atoms at the sliding interface. The kinetic energy the block loses equals exactly the thermal energy gained by the surfaces. Mechanical energy decreases; thermal energy increases by the same amount; their sum remains constant."
  explanation: "This is the key distinction between 'energy conservation' (always true) and 'mechanical energy conservation' (only true for conservative-force systems). The modified law E_mech,f = E_mech,i + W_nc is careful bookkeeping: W_nc is negative (energy leaves the mechanical account) and that amount is deposited into the thermal account. Total balance is always zero change."
```

## Explainer

From conservation of energy, you know that the total energy of an isolated system is conserved — energy is neither created nor destroyed, only transformed. From work done by non-conservative forces, you know that forces like friction and air resistance do net negative work on an object and don't store that energy in any recoverable potential energy form. This topic combines those two ideas into the **modified conservation law**: a precise accounting tool for systems where not all forces are conservative.

Start with the ideal case you already know. When only conservative forces act — gravity, ideal springs, electrostatic forces — mechanical energy (KE + PE) is perfectly conserved. A ball tossed upward trades kinetic energy for gravitational potential energy and back, with no loss. You can solve for speeds and heights at any point using energy accounting alone, without tracking force and acceleration at every instant. This is the power of the energy method.

Now introduce **non-conservative forces** such as sliding friction. Friction does negative work on the object it acts on — it opposes motion and removes mechanical energy from the system. But total energy is still conserved: the mechanical energy that disappears reappears as **thermal energy** — the microscopic random motion of atoms in the contacting surfaces. The modified law captures this precisely: E_mech,f = E_mech,i + W_nc, where W_nc is the work done by non-conservative forces. Since friction's work is negative, final mechanical energy is less than initial. The gap is exactly the thermal energy generated.

The practical skill is correctly identifying which forces are conservative (include their contribution through potential energy terms) and which are non-conservative (compute their work separately as W_nc), then applying the equation. For a block sliding down a rough ramp, you know the initial height and thus initial PE, you calculate frictional work from the friction force and path length, and you solve for the final speed. The critical error to avoid is treating friction as though it merely slows the object while conserving mechanical energy — friction *permanently converts* mechanical energy to heat, which cannot spontaneously reconvert. Total energy bookkeeping always balances; it is only the mechanical portion that decreases when non-conservative forces are present.
