---
id: subcooled-liquid-and-superheated-vapor
title: Subcooled Liquid and Superheated Vapor
domain: physics
course: thermodynamics
prerequisites:
- id: phase-diagrams
  type: hard
- id: temperature-and-thermal-equilibrium
  type: soft
- id: intensive-and-extensive-properties
  type: soft
- id: molar-heat-capacities
  type: soft
tags:
- phase-state
- subcooled
- superheated
- properties
stage: advanced
status: validated
---
# Subcooled Liquid and Superheated Vapor

## Core Idea
Subcooled liquid is a liquid below its saturation temperature at a given pressure; it is compressed slightly from the saturated state. Superheated vapor is a vapor above its saturation temperature; it is further from the two-phase boundary. Both regions contain single-phase substances with unique properties that depend on temperature and pressure.

## Questions

```yaml
- question: "Water is at 250°C and a pressure of 10 MPa. The saturation temperature at 10 MPa is approximately 311°C. What is the state of the water?"
  type: multiple-choice
  options:
    - "Superheated vapor, because 250°C is a high temperature"
    - "Subcooled (compressed) liquid, because T < T_sat(P)"
    - "A saturated mixture, because 250°C far exceeds the familiar boiling point of 100°C"
    - "Superheated vapor, because the pressure is very high"
  answer: 1
  explanation: "State identification requires comparing T with T_sat at the given pressure, not with 100°C (which is only T_sat at 1 atm). At 10 MPa, T_sat ≈ 311°C. Since 250°C < 311°C, the water is below its boiling point at that pressure — subcooled (compressed) liquid. This is counterintuitive: water at 250°C feels 'hot,' but at 10 MPa it is liquid, compressed below its phase boundary. The 100°C reference is only correct at atmospheric pressure."

- question: "Steam at 400°C and 1 atm (T_sat at 1 atm = 100°C) should be described using which property table?"
  type: multiple-choice
  options:
    - "The saturated liquid table at 400°C"
    - "The saturated vapor table at 1 atm"
    - "The superheated vapor table at 400°C and 1 atm"
    - "The compressed liquid table at 400°C and 1 atm"
  answer: 2
  explanation: "Since T = 400°C > T_sat(1 atm) = 100°C, the steam is superheated. Superheated vapor properties are tabulated as functions of both T and P in the superheated vapor table. The saturated vapor table (option B) applies only to vapor exactly on the saturation curve (at T_sat), not to superheated conditions. The compressed liquid table applies to subcooled liquids, not vapors. This three-way discrimination — subcooled / saturated / superheated — determines which table to use in every thermodynamic property lookup."

- question: "A substance is known to be on the saturation curve. Specifying its pressure alone mostly determines its thermodynamic state."
  type: true-false
  answer: false
  explanation: "On the saturation curve, pressure and temperature are coupled — fixing one fixes the other. But this only locates the substance on the saturation boundary; it does not pin down where between saturated liquid and saturated vapor the state lies. To fully specify the state, you must also provide quality x = m_vapor / m_total (ranging from 0 for saturated liquid to 1 for saturated vapor). Without quality, two substances at the same saturation pressure can have wildly different specific volumes and enthalpies. By contrast, in single-phase regions (subcooled or superheated), pressure and temperature independently determine the state."

- question: "The specific volume of a subcooled liquid is best approximated by the saturated liquid value at the same temperature, not the same pressure."
  type: true-false
  answer: true
  explanation: "Because liquids are nearly incompressible, their intensive properties change little with pressure but do change meaningfully with temperature. The saturated liquid table at temperature T provides the baseline, and the small pressure correction is usually negligible. Using the saturated liquid value at the same *pressure* instead would introduce a larger error by referencing T_sat(P) — which may differ significantly from the actual subcooled liquid temperature — as the interpolation anchor. The temperature-based approximation is standard engineering practice and is explicitly justified by the incompressibility of liquids."

- question: "You are told that steam is at 250°C, but not told its pressure. Can you determine whether it is subcooled liquid, on the saturation curve, or superheated vapor? Explain."
  type: short-answer
  answer: "No — temperature alone is insufficient to determine phase state. Whether a substance at 250°C is subcooled, saturated, or superheated depends on its pressure. At 1 atm (T_sat = 100°C), 250°C steam is superheated. At 10 MPa (T_sat ≈ 311°C), a substance at 250°C is subcooled liquid. At the saturation pressure corresponding to 250°C (about 3.97 MPa), the substance is exactly on the saturation curve. The state is determined by comparing T to T_sat(P), which requires knowing P."
  explanation: "This illustrates the two-property rule: for a pure substance in a single-phase region, any two independent intensive properties completely specify the state. In single-phase regions, T and P are independent — both are needed. On the saturation curve, T and P are dependent (knowing one fixes the other), but quality x is then needed as the second property to specify the state within the two-phase region. Temperature alone is always half the information required."
```

## Explainer

From your study of phase diagrams, you know that matter can exist as a liquid, vapor, or two-phase mixture depending on its temperature and pressure. The **saturation curve** on a P-T diagram marks the boundary between single-phase liquid and single-phase vapor regions. On the saturation curve itself, liquid and vapor coexist in equilibrium, and temperature and pressure are not independent — fixing one fixes the other. Step off the saturation curve in either direction, and you enter single-phase territory where temperature and pressure are independently specifiable.

A **subcooled liquid** (also called compressed liquid) is a liquid that sits to the left of the saturation curve — at a temperature below the saturation temperature for its current pressure. Think of liquid water at 20°C and atmospheric pressure: the saturation temperature at 1 atm is 100°C, so the water is 80°C below boiling. It has no tendency to vaporize. The "sub-cooled" name emphasizes that it has been cooled below its boiling point, while "compressed" emphasizes that its pressure exceeds the saturation pressure at its current temperature. In engineering calculations, a useful approximation treats subcooled liquid properties (specific volume, internal energy, enthalpy) as equal to the corresponding saturated liquid values at the same temperature — the deviation is small because liquids are nearly incompressible and properties change slowly with pressure.

A **superheated vapor** is a vapor that sits to the right of the saturation curve — at a temperature above the saturation temperature for its current pressure. Steam at 200°C and 1 atm is superheated: at that pressure, the saturation temperature is 100°C, so the steam is 100°C hotter than needed to maintain vapor phase. It has no tendency to condense. Superheating matters enormously in engineering: steam turbines use superheated steam to avoid water droplet formation on turbine blades (which causes erosion) and to extract more work. Unlike subcooled liquids, superheated vapor properties cannot be approximated simply — they must be read from steam tables or computed using an equation of state, because real vapor behavior departs significantly from ideal gas predictions near the saturation curve.

The practical skill is locating a substance's state on the phase diagram given its temperature and pressure, then choosing the right property table. If T < T_sat(P), you have subcooled liquid; use the compressed liquid table (or approximate with saturated liquid at T). If T > T_sat(P), you have superheated vapor; use the superheated vapor table. If T = T_sat(P), you are on the saturation curve and must specify quality x = m_vapor/m_total to pin down the state. This three-way discrimination — subcooled, saturated, superheated — is the entry point for nearly every thermodynamic cycle calculation in engineering practice.
