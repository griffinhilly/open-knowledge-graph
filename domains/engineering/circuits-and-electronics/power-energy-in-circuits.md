---
id: power-energy-in-circuits
title: Power and Energy Conservation
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: electric-potential-and-voltage
  type: hard
- id: charge-and-current-flow
  type: hard
builds-toward:
- ohms-law-and-conductance
- ideal-voltage-and-current-sources
tags:
- power
- energy
- conservation
- dissipation
stage: formal-systems
status: draft
---

# Power and Energy Conservation

## Core Idea
Instantaneous power P = VI represents the rate of energy transfer. Power is positive when energy flows into a component, negative when energy flows out. Energy conservation requires that total power supplied by sources equals total power dissipated in resistors plus power stored in reactive elements, a direct consequence of Kirchhoff's voltage law.

## Explainer

You already know that voltage is energy per unit charge and that current is charge per unit time. Multiply them and you get energy per unit time — that is, power. The relation **P = V · I** is not a new law but a logical consequence of the definitions you already have. If 5 volts is the energy cost per coulomb of charge passing through a component, and 2 amperes is 2 coulombs passing per second, then 10 joules are transferred per second — 10 watts of power.

The sign convention — positive power means energy flows into the component, negative means energy flows out — is a bookkeeping choice that makes the conservation law clean. By convention, if you define current entering the positive terminal of a component's voltage reference as positive, then P = +VI means the component absorbs power (a load: resistor, motor) and P = −VI means it supplies power (a source: battery, generator). This **passive sign convention** keeps the accounting consistent: sum all the P = VI products around a circuit, and the total must be zero by energy conservation. Sources supply exactly as much as loads absorb.

For resistors specifically, Ohm's law (V = IR) lets you write power in two equivalent forms: P = V²/R = I²R. Both are always positive for a resistor because resistors can only dissipate (convert to heat), never supply, energy. The I²R form is particularly intuitive for wires: even a small resistance in a high-current path dissipates significant power, which is why power lines operate at high voltage (and therefore low current) to minimize resistive losses over long distances.

Energy is simply power integrated over time: E = ∫P dt. For constant power, E = P · t. This integral form connects circuit behavior to physical reality: the heat generated in a resistor, the charge stored in a capacitor, the mechanical work done by a motor — all are energy quantities, computed by integrating the instantaneous power. Kirchhoff's voltage law, which you know as the constraint that voltages around any loop sum to zero, is mathematically equivalent to saying total power in the loop is zero — the voltage law and energy conservation are two views of the same underlying constraint.
