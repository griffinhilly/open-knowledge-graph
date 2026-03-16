---
id: joule-heating
title: Joule Heating and Power Dissipation
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: ohms-law-microscopic
  type: hard
builds-toward:
- resistor-combinations
tags:
- power
- heating
- dissipation
stage: formal-systems
status: draft
---

# Joule Heating and Power Dissipation

## Core Idea
Power dissipated in a resistor is P = IV = I²R = V²/R. Microscopically, the electric field does work on charge carriers at rate p = J⃗·E⃗ = σE², which is converted to heat through collisions. Energy dissipated over time t is E = Pt. This is the principle behind resistive heating and energy loss in conductors.

## Explainer

From your study of Ohm's law at the microscopic level, you know that electrons in a conductor don't accelerate freely — they drift under the electric field and then scatter off lattice ions, losing their gained kinetic energy as heat. **Joule heating** is simply the macroscopic accounting of that energy transfer. Every time the electric field does work to accelerate a charge carrier, a collision soon after dumps that kinetic energy into the lattice as thermal vibration. The conductor's temperature rises.

At the macroscopic level, the power calculation is straightforward. Power is the rate of doing work on charges. In a time dt, a charge dq = I dt moves through a potential difference V, so the work done on it is dW = V dq = V I dt. Dividing by dt gives **P = IV** — the power delivered to any circuit element is current times voltage, regardless of whether it stores energy (as a capacitor does) or dissipates it. For a purely resistive element where V = IR, you can substitute to get two equivalent forms: P = I²R (useful when you know the current) or P = V²/R (useful when you know the voltage).

At the microscopic level, the connection is equally clean. You know that J⃗ = σE⃗ (current density is conductivity times field). The work done by the field per unit volume per unit time is the dot product p = J⃗ · E⃗ = σE². Integrating over the volume of a resistor recovers P = IV exactly. Crucially, this formula shows that doubling the current quadruples the power — a P ∝ I² relationship. This is why transmission lines operate at high voltage and low current: the same power P = IV can be transmitted with much less I²R heating by raising V and reducing I proportionally.

The three forms P = IV = I²R = V²/R are all the same equation dressed differently, and choosing the right form depends only on which two quantities you know directly. A 100 Ω resistor carrying 100 mA dissipates P = (0.1)² × 100 = 1 W — enough to get warm to the touch. The same resistor with 1 A through it dissipates 100 W and will burn out immediately. Engineering with resistive elements means designing so that the operating current stays far below the point where dissipated power would damage the component.
