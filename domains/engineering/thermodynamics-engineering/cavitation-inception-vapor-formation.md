---
id: cavitation-inception-vapor-formation
title: Cavitation, Vapor Formation, and Flow Choking
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: two-phase-homogeneous-flow-equilibrium
  type: hard
- id: clausius-clapeyron-vapor-pressure
  type: hard
tags:
- cavitation
- vapor-formation
- choking
- sonic-flow
- critical-pressure
stage: formal-systems
status: validated
---

# Cavitation, Vapor Formation, and Flow Choking

## Core Idea
Cavitation occurs when local static pressure falls below saturation pressure, causing liquid to vaporize suddenly. In pumps and turbines, vapor bubbles collapse on higher-pressure regions, causing erosion and noise. Critical pressure for choking (sonic flow) in a nozzle occurs when dP/dM = 0, limiting mass flow rate. Cavitation number σ = (P - P_sat)/(0.5ρV²) predicts inception conditions.

## Questions

```yaml
- question: "A pump engineer reports that after increasing rotational speed, the impeller blades developed pitting damage even though the fluid temperature never changed. What is the most likely cause?"
  type: multiple-choice
  options:
    - "Higher speed overheated the bearings and conducted heat into the fluid, raising it above boiling point"
    - "Higher rotational speed reduced local static pressure at the impeller eye below P_sat, causing cavitation; the vapor bubbles subsequently collapsed violently against the blade surfaces"
    - "Higher speed increased fluid viscosity through shear, causing abrasive wear on the blades"
    - "The impeller entered mechanical resonance with the pump casing at the new speed"
  answer: 1
  explanation: "This is the classic cavitation damage scenario. Bernoulli's equation shows that higher velocity means lower static pressure. As impeller tip speed increases, local pressure at the suction side of the blades drops. If it falls below P_sat at the current fluid temperature, vaporization occurs — not from heat, but from pressure reduction. The resulting vapor bubbles collapse as they enter higher-pressure regions downstream, generating microscopic liquid jets that pit the metal surface over time. No temperature change is required; the driver is entirely the local pressure field."

- question: "The cavitation number is σ = (P_ref − P_sat) / (½ρV²). If inlet velocity doubles while P_ref and fluid temperature remain constant, what happens to σ and to cavitation risk?"
  type: multiple-choice
  options:
    - "σ doubles — higher velocity increases the pressure margin against cavitation"
    - "σ decreases by a factor of four (denominator quadruples) — cavitation risk increases as σ approaches zero"
    - "σ remains constant because the pressure difference in the numerator also increases with velocity"
    - "σ increases because higher velocity cools the fluid, lowering P_sat"
  answer: 1
  explanation: "The denominator ½ρV² scales as V², so doubling velocity quadruples the denominator. With P_ref and P_sat constant (temperature unchanged), σ drops to one-quarter of its original value. Since σ = 0 is the inception threshold, a lower σ means the system is closer to cavitation onset — higher velocity increases cavitation risk. This is counterintuitive to engineers accustomed to thinking more flow = more performance; above a certain flow rate, cavitation breakdown actually reduces pump performance dramatically."

- question: "The primary damage mechanism in cavitation is the rapid formation of large vapor bubbles that block flow passages and reduce pump output."
  type: true-false
  answer: false
  explanation: "While vapor bubble formation does reduce pump performance (head drops, efficiency falls), the structural damage — metal pitting and erosion — is caused by bubble *collapse*, not formation. As bubbles travel downstream into higher-pressure regions where P > P_sat, the vapor condenses almost instantaneously. The implosion drives inward-rushing liquid into a microscopic jet that strikes adjacent solid surfaces at extremely high local stresses, pitting the metal over repeated cycles. The crackling noise from a cavitating pump is the acoustic signature of these implosions. Engineers worry about both effects: performance loss from formation and structural damage from collapse."

- question: "Cavitation can occur in cold water at room temperature if local flow velocity is high enough, even without any external heating."
  type: true-false
  answer: true
  explanation: "Cavitation is triggered by local static pressure falling below P_sat at the fluid's *current temperature* — not by temperature rising above the atmospheric boiling point. From Bernoulli's equation, high local velocity means low local static pressure. If that pressure drop is large enough to bring P_local < P_sat(T_fluid), vaporization occurs regardless of the absolute temperature. Room-temperature water at 20°C has P_sat ≈ 2.3 kPa. A pump or propeller blade that accelerates water enough to create pressures below 2.3 kPa at that temperature will cause cold-water cavitation — well below the 100°C atmospheric boiling point."

- question: "Explain the concept of Net Positive Suction Head (NPSH) and why engineers must ensure NPSHA exceeds NPSHR to prevent cavitation."
  type: short-answer
  answer: "NPSH measures how far the absolute pressure at the pump inlet exceeds the fluid's vapor pressure P_sat — it is the available margin against cavitation inception. NPSHA (available) is a system property: it depends on the absolute pressure at the supply source (tank or reservoir), the vertical distance from the supply to the pump inlet (head loss from elevation), and friction losses in the suction piping. NPSHR (required) is a pump property: the minimum NPSH at the pump inlet at which the pump can operate without significant cavitation-induced performance loss, specified by the manufacturer from impeller testing. If NPSHA < NPSHR, the pressure at the lowest-pressure point inside the pump (typically the impeller eye) falls below P_sat, vapor bubbles form and collapse, and the pump experiences cavitation breakdown — a sharp drop in head and efficiency on the performance curve. Engineers prevent this by maximizing suction pressure (raising supply tank level, using pressurized supply), minimizing suction piping friction (shorter, wider pipe, fewer bends), or selecting a pump with a lower NPSHR for the application."
```

## Explainer

From the Clausius-Clapeyron relation you already know, the saturation pressure P_sat is the pressure at which liquid and vapor coexist at a given temperature — it is a property of the fluid, not the flow. Cavitation exploits this fact in a destructive way: if you accelerate a liquid fast enough, Bernoulli's equation tells you the local static pressure must drop. If that local pressure drops below P_sat for the liquid's current temperature, the liquid has no choice but to begin forming vapor — it is effectively boiling, not from heat, but from a pressure drop. The vapor forms as **cavitation bubbles** that nucleate at surface defects or dissolved gas pockets.

The danger is not the bubble formation itself — it is the collapse. As the bubbles travel downstream into higher-pressure regions, the surrounding liquid pressure exceeds P_sat again and the vapor condenses almost instantaneously. The implosion is violent: inward-rushing liquid forms microscopic jets that strike adjacent solid surfaces at extremely high local stresses, pitting metal over time and generating audible crackling noise. Pump impellers, propeller blades, and turbine runners are the classic victims. The **cavitation number** σ = (P_ref − P_sat)/(½ρV²) quantifies the margin above inception: σ > σ_critical means you are safe; as σ approaches zero, cavitation begins. Engineers design to keep σ high by raising system pressure, reducing flow velocity, or selecting fluids with lower P_sat.

Flow **choking** is a related but distinct phenomenon that occurs in compressible or two-phase flows through converging nozzles. At the throat, flow reaches a critical condition (Mach 1 for gas flow; a critical void fraction in two-phase flow) beyond which the mass flow rate cannot increase regardless of how much the downstream pressure is reduced. The condition dP/dM = 0 — pressure gradient vanishes with respect to Mach number — marks this limit. In two-phase flows, choking is even more complex because the presence of vapor dramatically lowers the effective sonic velocity of the mixture, so choking can occur at velocities far below the liquid sonic speed.

Connecting both phenomena: in a pump operating near cavitation inception, vapor formation in the suction passage can choke the flow path, causing a sudden collapse in pump performance called **cavitation breakdown**. The head-flow curve shows a sharp knee where efficiency drops rapidly. This is why the **Net Positive Suction Head Available (NPSHA)** must exceed the **NPSH Required (NPSHR)** by a design margin — the engineer ensures that even at the lowest-pressure point in the suction line, P_local remains comfortably above P_sat.
