---
id: transcritical-and-supercritical-cycles
title: Transcritical and Supercritical Power Cycles
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: rankine-cycle-thermodynamic-analysis
  type: hard
- id: critical-point-behavior-substances
  type: hard
tags:
- transcritical
- supercritical
- co2
- power-cycle
- efficiency
stage: formal-systems
status: validated
---

# Transcritical and Supercritical Power Cycles

## Core Idea
Supercritical Rankine cycles operate above the critical point (T > T_c, P > P_c), avoiding two-phase expansion and allowing continuous pressure-temperature paths. Transcritical cycles compress above critical pressure but cool below critical temperature. Advantages include higher cycle efficiency (especially with heat recovery), better turbine inlet conditions, and smaller component sizes. CO₂ cycles exploit these benefits for low-grade heat recovery.

## Questions

```yaml
- question: "A conventional subcritical Rankine cycle and a supercritical Rankine cycle both receive heat from the same gas stream cooling continuously from 600°C to 200°C. Which cycle would likely achieve higher thermal efficiency, and what is the fundamental reason?"
  type: multiple-choice
  options:
    - "The subcritical cycle, because the constant-temperature boiling phase allows more efficient heat transfer than continuous heating"
    - "The supercritical cycle, because operating above the critical point allows the heat-addition profile to continuously follow the cooling heat source, minimizing the temperature difference that drives irreversibility in the heat exchangers"
    - "Both cycles achieve identical efficiency because the turbine inlet enthalpy and condenser conditions are the same"
    - "The subcritical cycle, because lower operating pressures reduce pump work and mechanical losses in the system"
  answer: 1
  explanation: "In a subcritical cycle, boiling occurs at constant temperature and pressure, creating a fixed temperature profile for heat addition that mismatches a continuously cooling heat source — generating entropy through large temperature differences in the heat exchanger. A supercritical cycle eliminates the phase boundary: the working fluid heats continuously with no isothermal plateau, allowing its temperature profile to closely track the declining heat source temperature. This better 'temperature matching' minimizes the irreversibility in heat transfer and is the fundamental thermodynamic advantage of operating above the critical point."

- question: "What distinguishes a transcritical cycle from a fully supercritical power cycle?"
  type: multiple-choice
  options:
    - "A transcritical cycle uses CO₂ as the working fluid, while supercritical cycles always use steam"
    - "A transcritical cycle operates above the critical pressure on the high-pressure side but drops below the critical temperature on the low-pressure side, so conventional condensation still occurs"
    - "A transcritical cycle only marginally exceeds the critical pressure, whereas a fully supercritical cycle greatly exceeds both critical pressure and temperature throughout"
    - "A transcritical cycle uses two separate working fluid loops, while a supercritical cycle uses a single working fluid throughout"
  answer: 1
  explanation: "Transcritical means the cycle crosses the critical-point boundary: the high-pressure side operates above critical pressure (supercritical compression and heating), but the low-pressure side cools the fluid below its critical temperature, allowing conventional two-phase condensation. The CO₂ cycle is transcritical because CO₂'s critical temperature (31°C) is close to ambient — easy to condense on the low-pressure side — while its critical pressure (7.4 MPa) is readily achievable by compression. A fully supercritical cycle would remain above both Tc and Pc throughout the high-pressure portion, never entering the two-phase region."

- question: "Operating a power cycle above the critical point eliminates the two-phase boiling dome, allowing heat addition to occur continuously without a constant-temperature plateau, which enables the cycle's temperature profile to better match a variable-temperature heat source."
  type: true-false
  answer: true
  explanation: "True. This is the fundamental thermodynamic advantage. In the subcritical two-phase region, heat addition occurs at constant pressure and temperature — a fixed horizontal line on a T-s diagram. When the heat source temperature is decreasing (as it always is, since it is transferring energy), this fixed boiling temperature creates an unavoidable mismatch. Above the critical point, there is no phase transition: the working fluid temperature rises continuously with heat addition, and the heat-addition curve on a T-s diagram can be shaped to parallel the cooling heat source, dramatically reducing entropy generation."

- question: "CO₂ is the preferred working fluid for transcritical cycles primarily because it achieves higher thermal efficiency than most other working fluids at most operating condition relevant to power generation."
  type: true-false
  answer: false
  explanation: "False. CO₂ is favored for transcritical cycles mainly because its critical point is conveniently located — critical temperature of 31°C makes condensation practical near ambient conditions, and critical pressure of 7.4 MPa is achievable with standard compression equipment. Additionally, CO₂ is non-flammable, non-toxic, inexpensive, and has low global-warming potential compared to synthetic refrigerants. Its thermodynamic efficiency advantages are real but specific to certain operating conditions (waste-heat recovery, heat pumping, geothermal); steam remains superior in high-temperature power generation applications. CO₂ is a practical choice for a specific niche, not a universally dominant working fluid."

- question: "Explain why the absence of a phase transition above the critical point improves the thermodynamic efficiency of a heat engine cycle that receives heat from a variable-temperature source."
  type: short-answer
  answer: "In a subcritical Rankine cycle, the boiling phase imposes a fixed temperature at which heat is added, regardless of the heat source temperature. When the heat source is cooling continuously, this creates large temperature differences between source and working fluid throughout much of the boiling process, generating entropy and reducing the fraction of heat that can be converted to work. Above the critical point, there is no phase boundary and no isothermal boiling — the working fluid temperature rises continuously during heat addition. The heat-addition curve on a T-s diagram can therefore be designed to closely parallel the declining temperature profile of the heat source, minimizing the average temperature difference across the heat exchanger. Smaller temperature differences mean less entropy generation and higher second-law efficiency."
  explanation: "This principle is captured by the concept of 'temperature matching' in heat exchanger design. The theoretical limit is the reversible heat engine, where heat transfers occur at infinitesimally small temperature differences. Supercritical cycles approach this limit more closely than subcritical cycles because their continuous heating profile can be tuned to match complex heat source temperature profiles — which is why modern ultra-supercritical coal plants and next-generation sCO₂ power cycles both exploit this effect."
```

## Explainer

In a conventional Rankine cycle, the working fluid is pumped as a liquid, heated until it boils, superheated as steam, and then expanded through a turbine. The two-phase boiling region — the dome on the P-v or T-s diagram — is where heat addition occurs at constant temperature and pressure. This isothermal boiling is efficient in one sense, but it creates a fixed relationship between heat-source temperature and cycle pressure that can make it hard to match the temperature profile of the heat source, and it produces wet steam at the turbine exit if care is not taken. Both of these issues disappear above the **critical point**.

At pressures above the critical pressure P_c and temperatures above the critical temperature T_c, the distinction between liquid and vapor ceases to exist. There is no dome, no phase boundary, no latent heat — just a single continuous supercritical fluid whose properties change smoothly with temperature and pressure. In a **supercritical Rankine cycle**, the pump raises pressure above P_c, and the "boiler" is replaced by a **supercritical heat exchanger** that heats the fluid from a dense, liquid-like state through the pseudocritical region (where properties change most rapidly) and into a low-density, gas-like state, all without any phase transition. This continuous heating profile allows the cycle's heat-addition curve on a T-s diagram to follow the heat source's temperature profile much more closely — reducing the temperature difference that drives irreversibility in the heat exchangers. Modern ultra-supercritical coal plants operate at ~30 MPa and ~600°C for this reason: higher pressure and temperature both raise thermal efficiency.

A **transcritical cycle** is a hybrid: the high-pressure side operates above P_c but the cooling side drops below the critical temperature, so the working fluid condenses conventionally on the low-pressure side. The CO₂ (carbon dioxide) cycle is the most important example. CO₂ has a critical point at only 31°C and 7.4 MPa — meaning it can be compressed to supercritical pressure relatively easily, but its critical temperature is close to ambient, so condensation on the low-pressure side occurs as normal liquid CO₂. The CO₂ transcritical cycle is used in heat pumps and refrigeration (it replaced CFCs in car air conditioners), and it is actively studied for waste-heat recovery from industrial processes and geothermal sources. Because CO₂ is non-flammable, non-toxic, cheap, and has a very small global-warming potential relative to synthetic refrigerants, these cycles are gaining significant commercial traction.

The main design challenge in both supercritical and transcritical cycles is the **internal heat exchanger** (or recuperator). Because the supercritical fluid's specific heat varies dramatically near the pseudocritical point, careful thermal design is needed to avoid large temperature mismatches within the recuperator itself. Poor recuperator design can undercut much of the efficiency gain. Compact high-effectiveness heat exchangers — often printed-circuit or microchannel designs — are typically required, which is why supercritical CO₂ (sCO₂) Brayton cycles for next-generation nuclear and concentrated solar power plants are physically much smaller than equivalent steam Rankine systems, even at the same power output.


