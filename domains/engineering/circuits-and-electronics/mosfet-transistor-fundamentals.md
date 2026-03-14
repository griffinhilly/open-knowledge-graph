---
id: mosfet-transistor-fundamentals
title: MOSFET Fundamentals
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: diode-fundamentals
  type: hard
- id: bjt-transistor-fundamentals
  type: soft
- id: electrical-properties-of-materials
  type: soft
builds-toward:
- operational-amplifier-fundamentals
tags:
- MOSFET
- NMOS
- PMOS
- enhancement-mode
- threshold-voltage
- CMOS
- digital-switch
- triode
- saturation
stage: formal-systems
status: validated
---

# MOSFET Fundamentals

## Core Idea
A MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor) controls drain current with gate-to-source voltage V_GS; virtually no gate current flows because the oxide layer provides near-infinite DC input impedance. Enhancement-mode NMOS devices turn on when V_GS exceeds threshold voltage V_T; drain current in saturation is I_D = (k_n/2)(V_GS − V_T)². Three operating regions exist: cutoff (V_GS < V_T, I_D = 0), triode/linear (switch on, V_DS < V_GS − V_T), and saturation (amplifier, V_DS ≥ V_GS − V_T). Complementary NMOS/PMOS pairs form CMOS logic, which dominates digital ICs due to negligible static power dissipation.

## How It's Best Learned
Compare MOSFET and BJT operation side by side: MOSFET is voltage-controlled with essentially zero input current; BJT is current-controlled. Practice computing I_D and V_DS for both triode and saturation regions. Analyze a CMOS inverter to understand how NMOS and PMOS switch in complementary fashion.

## Common Misconceptions
- Confusing MOSFET operating region names with BJT names — MOSFET triode ≠ BJT active; MOSFET saturation ≠ BJT saturation; the terms are not interchangeable.
- Assuming gate current flows — the oxide insulation provides near-infinite DC input impedance, though gate capacitance matters at high frequencies.
- Assuming all MOSFETs are enhancement-mode — depletion-mode devices are normally on at V_GS = 0 and require negative gate voltage to turn off.
