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
- id: band-theory-intro
  type: soft
- id: electron-configuration-aufbau-principle
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
stage: advanced
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

## Explainer

You already know from diodes that semiconductor junctions can control current flow through the manipulation of charge carriers. A MOSFET takes this further: instead of a forward-biased junction, it uses an electric field applied through an insulating oxide layer to modulate the conductivity of a thin semiconductor channel. Because the gate is separated from the channel by oxide, virtually no DC gate current flows — the MOSFET is a **voltage-controlled device**, which is its fundamental distinction from the BJT you may have studied.

In an **enhancement-mode NMOS** device, the channel between drain and source does not exist at zero gate voltage. When you apply a positive V_GS that exceeds the **threshold voltage** V_T, the electric field beneath the oxide attracts electrons from the p-type substrate to form an n-type inversion layer — an induced channel connecting source to drain. Below V_T, the device is in **cutoff**: I_D = 0 and the MOSFET is an open switch. This is the behavior you rely on in digital logic: V_GS < V_T means off, V_GS > V_T means on.

Once V_GS > V_T, the operating region depends on V_DS. In the **triode (linear) region**, V_DS is small relative to V_GS − V_T: the channel exists uniformly from source to drain and acts like a voltage-controlled resistor. This is useful for analog switches and pass transistors. As V_DS increases and approaches V_GS − V_T, the channel begins to "pinch off" at the drain end. Beyond this point — when V_DS ≥ V_GS − V_T — the device enters **saturation**: I_D ≈ (k_n/2)(V_GS − V_T)² and becomes nearly independent of V_DS. Saturation is the amplifier region; the drain current is controlled almost entirely by the gate voltage, making it useful for transconductance amplification.

The most important application of MOSFET complementary pairing is **CMOS logic**. An NMOS transistor turns on with high gate voltage; a PMOS transistor (with opposite polarity carriers) turns on with low gate voltage. In a CMOS inverter, the NMOS and PMOS are wired so that exactly one is on at any time during steady state. When the input is high, NMOS conducts and PMOS is off, pulling the output to ground. When the input is low, PMOS conducts and NMOS is off, pulling the output to V_DD. The key insight is that in steady state, no DC path exists from V_DD to ground — power is only dissipated during switching transitions. This is why CMOS dominates digital ICs: static power dissipation is negligible, enabling billions of transistors on a single chip without melting.
