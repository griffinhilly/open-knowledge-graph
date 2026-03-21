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

## Questions

```yaml
- question: "A MOSFET is operating in saturation. Which variable primarily controls the drain current I_D in this region?"
  type: multiple-choice
  options:
    - "V_DS, the drain-to-source voltage"
    - "V_GS − V_T, the gate overdrive voltage"
    - "The channel resistance, which depends on V_DS"
    - "The gate current I_G flowing through the oxide"
  answer: 1
  explanation: "In saturation (V_DS ≥ V_GS − V_T), the drain current is I_D = (k_n/2)(V_GS − V_T)² and is nearly independent of V_DS. The current is controlled by the gate overdrive voltage (V_GS − V_T), not by V_DS. This makes the MOSFET behave like a voltage-controlled current source in saturation — the gate voltage sets the current, and the drain-source voltage simply maintains the saturation condition. This is why saturation is the amplifier region: small changes in V_GS produce predictable changes in I_D regardless of what's happening at the drain."

- question: "A digital designer claims that a CMOS inverter wastes significant power even when its output is held static (not switching). Is this correct?"
  type: multiple-choice
  options:
    - "Yes — both NMOS and PMOS are always partially on, creating a constant current path from V_DD to ground"
    - "No — in steady state, one transistor is fully on and the other is fully off, so there is no DC path from V_DD to ground"
    - "Yes — the gate capacitance of the transistors continuously draws current from the supply"
    - "No — CMOS logic does not use transistors in steady state; it only activates them during switching"
  answer: 1
  explanation: "In a CMOS inverter at steady state, NMOS and PMOS are designed to be complementary: when the input is high, NMOS is on and PMOS is off; when the input is low, PMOS is on and NMOS is off. In either case, one transistor is in cutoff (essentially an open circuit), so no DC current path exists from V_DD to ground. Power is only dissipated during switching transitions, when both transistors may be partially on momentarily, and when charging/discharging load capacitance. This negligible static power dissipation is the fundamental reason CMOS enables billions of transistors on a chip — if every transistor drew DC current, the chip would instantly overheat."

- question: "When a MOSFET enters saturation (V_DS ≥ V_GS − V_T), it behaves like a BJT in saturation: both devices are fully switched on and act as low-resistance paths."
  type: true-false
  answer: false
  explanation: "This is the most dangerous naming confusion in transistor circuits. MOSFET saturation and BJT saturation are entirely different operating regimes. MOSFET saturation is the *amplifier* region, where the channel is pinched off at the drain end and I_D depends on V_GS but not V_DS — the device acts as a voltage-controlled current source. BJT saturation is the *switch-fully-on* region, where both junctions are forward biased and V_CE is very small. The MOSFET equivalent of 'BJT saturation' is the *triode (linear) region*, where V_DS is small and the device acts as a voltage-controlled resistor. The terms were chosen independently and unfortunately share the word 'saturation' for opposite reasons."

- question: "The gate of a MOSFET draws essentially no DC current because an insulating oxide layer physically separates the gate terminal from the semiconductor channel."
  type: true-false
  answer: true
  explanation: "This is the MOSFET's defining structural advantage over the BJT. The gate is formed from a conductor (metal or polysilicon) separated from the semiconductor channel by a thin layer of silicon dioxide (SiO₂), which is an excellent insulator. Because there is no DC conduction path between the gate and the channel, gate current is essentially zero at DC. The input impedance looking into the gate is effectively infinite at low frequencies — orders of magnitude higher than a BJT base. This means MOSFET gates draw negligible power from the driving circuit and can control large drain currents with virtually no input current, a critical advantage for digital logic density."

- question: "Why does CMOS logic consume negligible static power, and why does this matter for modern integrated circuit design?"
  type: short-answer
  answer: "CMOS uses complementary NMOS and PMOS transistors wired so that exactly one is off (in cutoff, drawing no current) in every static logic state. When the input is high, NMOS conducts and PMOS is off; when the input is low, PMOS conducts and NMOS is off. In either case, the off transistor presents a near-open circuit between V_DD and ground, so no static current flows and no static power is dissipated. Power is consumed only during switching transitions (charging/discharging gate capacitances) and briefly when both transistors are simultaneously partially on. This matters enormously for chip design: a chip with a billion transistors all drawing even 1 μA each would dissipate 1,000 watts at idle. CMOS's near-zero static dissipation is what makes dense, battery-powered computing physically possible."
  explanation: "As transistor feature sizes have shrunk, leakage currents through the oxide have increased, making static power dissipation a growing concern in modern CMOS — one of the major challenges for the semiconductor industry below 10 nm. But the fundamental CMOS principle of complementary switching remains the basis of essentially all digital logic, from microcontrollers to server chips."
```

## Explainer

You already know from diodes that semiconductor junctions can control current flow through the manipulation of charge carriers. A MOSFET takes this further: instead of a forward-biased junction, it uses an electric field applied through an insulating oxide layer to modulate the conductivity of a thin semiconductor channel. Because the gate is separated from the channel by oxide, virtually no DC gate current flows — the MOSFET is a **voltage-controlled device**, which is its fundamental distinction from the BJT you may have studied.

In an **enhancement-mode NMOS** device, the channel between drain and source does not exist at zero gate voltage. When you apply a positive V_GS that exceeds the **threshold voltage** V_T, the electric field beneath the oxide attracts electrons from the p-type substrate to form an n-type inversion layer — an induced channel connecting source to drain. Below V_T, the device is in **cutoff**: I_D = 0 and the MOSFET is an open switch. This is the behavior you rely on in digital logic: V_GS < V_T means off, V_GS > V_T means on.

Once V_GS > V_T, the operating region depends on V_DS. In the **triode (linear) region**, V_DS is small relative to V_GS − V_T: the channel exists uniformly from source to drain and acts like a voltage-controlled resistor. This is useful for analog switches and pass transistors. As V_DS increases and approaches V_GS − V_T, the channel begins to "pinch off" at the drain end. Beyond this point — when V_DS ≥ V_GS − V_T — the device enters **saturation**: I_D ≈ (k_n/2)(V_GS − V_T)² and becomes nearly independent of V_DS. Saturation is the amplifier region; the drain current is controlled almost entirely by the gate voltage, making it useful for transconductance amplification.

The most important application of MOSFET complementary pairing is **CMOS logic**. An NMOS transistor turns on with high gate voltage; a PMOS transistor (with opposite polarity carriers) turns on with low gate voltage. In a CMOS inverter, the NMOS and PMOS are wired so that exactly one is on at any time during steady state. When the input is high, NMOS conducts and PMOS is off, pulling the output to ground. When the input is low, PMOS conducts and NMOS is off, pulling the output to V_DD. The key insight is that in steady state, no DC path exists from V_DD to ground — power is only dissipated during switching transitions. This is why CMOS dominates digital ICs: static power dissipation is negligible, enabling billions of transistors on a single chip without melting.
