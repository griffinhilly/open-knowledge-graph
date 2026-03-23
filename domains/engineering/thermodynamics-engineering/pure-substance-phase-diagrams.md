---
id: pure-substance-phase-diagrams
title: Pure Substance Phase Diagrams
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: thermodynamic-properties-and-equations-of-state
  type: hard
builds-toward:
- saturated-superheated-property-regions
- critical-point-behavior-substances
- psychrometrics-humid-air-properties
tags:
- phase-diagrams
- phases
- saturation
stage: formal-systems
status: draft
---

# Pure Substance Phase Diagrams

## Core Idea
Pure substances exist in distinct phase regions (solid, liquid, gas) separated by phase boundaries on P-T diagrams. The phase diagram shows where phases coexist and where transitions occur; the critical point marks the end of the liquid-gas boundary. Engineering applications use P-T and P-v diagrams to identify the phase of a substance and determine which properties apply.

## How It's Best Learned
Sketch the P-T and P-v diagrams for water from memory, labeling regions and boundary curves. For any given state, practice identifying which phase and which part of a property table applies. Understand that saturation curves converge at the critical point where liquid and gas become indistinguishable.

## Common Misconceptions
- The triple point and critical point are the same; they define different phase equilibrium conditions.
- Above the critical point, you can never liquefy the fluid by increasing pressure alone.
- The saturation curve is a single line on a P-T diagram but a curve in P-v space because volume changes during phase change.

## Questions

```yaml
- question: "Steam tables give you properties for steam at a given pressure P and temperature T. You are told a steam sample is at P = 500 kPa and T = 151.8°C (which happens to be the saturation temperature at that pressure). What additional information do you need to fully specify the state?"
  type: multiple-choice
  options:
    - "Nothing — pressure and temperature always fully specify the state of a pure substance"
    - "The specific enthalpy h, which is always needed alongside P and T"
    - "The quality x (vapor mass fraction), because at saturation conditions liquid and vapor coexist"
    - "The density ρ, which determines whether the substance is liquid or gas at this point"
  answer: 2
  explanation: "At saturation conditions (T = Tₛₐₜ at that pressure), the substance is inside the two-phase dome, where liquid and vapor coexist. In the two-phase region, pressure and temperature are not independent — they both lie on the saturation curve — so specifying both still leaves the state underdetermined. You need the quality x (mass fraction vapor) to locate the state between the saturated liquid line (x = 0) and the saturated vapor line (x = 1). This is invisible on a P-T diagram but clearly shown by the saturation dome in P-v space."

- question: "Water at 400°C is gradually compressed at constant temperature from very low pressure. Starting as a vapor, what phase does it become if pressure is raised well above 22.1 MPa (the critical pressure for water)?"
  type: multiple-choice
  options:
    - "It becomes a compressed liquid — sufficient pressure always liquefies any gas"
    - "It remains a supercritical fluid — above the critical temperature, no phase boundary separates liquid from gas no matter how much pressure is applied"
    - "It becomes a solid — sufficient pressure at high temperature always drives solidification"
    - "It passes through the saturation dome and emerges as liquid, just as at lower temperatures"
  answer: 1
  explanation: "Above the critical temperature (374°C for water), the vapor-pressure curve no longer exists — there is no liquid-gas phase boundary to cross. Compressing water above 374°C produces a supercritical fluid that transitions continuously between gas-like and liquid-like behavior with no distinct phase change. Option A describes behavior below the critical temperature; above it, you can apply any amount of pressure and no condensation (visible phase boundary) will occur."

- question: "The triple point and the critical point both represent conditions where liquid and gas coexist in equilibrium."
  type: true-false
  answer: false
  explanation: "The triple point is where ALL THREE phases — solid, liquid, and gas — coexist simultaneously. It is the unique P-T point where all three phase boundary curves meet. The critical point is where the distinction between liquid and gas DISAPPEARS — it is the end of the vapor-pressure curve, not a coexistence point. Above the critical point, there is no phase boundary at all, so 'coexistence' doesn't apply. These are fundamentally different phenomena."

- question: "At the critical point of a pure substance, the specific volumes of the saturated liquid and saturated vapor become equal."
  type: true-false
  answer: true
  explanation: "The critical point is the apex of the saturation dome in P-v space. Moving up the saturation envelope, the saturated liquid specific volume (vₗ) increases and the saturated vapor specific volume (vᵥ) decreases as pressure and temperature rise. They converge and become identical at the critical point — which is why the dome closes there. Beyond the critical point, the distinction between liquid and vapor vanishes precisely because there is no longer a difference in their properties."

- question: "Why is specifying both pressure and temperature alone insufficient to determine the thermodynamic state of a substance inside the saturation dome? How is the state fully specified in that region?"
  type: short-answer
  answer: "Inside the saturation dome, liquid and vapor coexist in equilibrium. Pressure and temperature are not independent there — once you fix one, the other is determined by the saturation curve. So stating P and T gives you the same information twice; you've only specified one independent variable, not two. To fully specify the state, you need the quality x (the mass fraction of the mixture that is vapor), which locates you between the saturated liquid line (x = 0) and the saturated vapor line (x = 1). Specific volume (or specific enthalpy or entropy) can substitute for quality, since all of these vary continuously across the two-phase region."
  explanation: "This is why engineers learn to first check whether a state is inside the dome before looking up properties. If you use superheated steam tables for a two-phase state, you will find no valid entry — or worse, interpolate to a nonsensical result. The P-v diagram makes this visual: the saturation dome shows exactly which states are two-phase and reminds you that volume (not just T and P) varies within it."
```

## Explainer

From your study of thermodynamic properties and equations of state, you know that a substance's state is described by properties like pressure, temperature, and specific volume. But these properties don't vary smoothly everywhere — at phase transitions, properties change discontinuously, and two phases can coexist at fixed pressure and temperature while volume spans a wide range. **Phase diagrams** are maps that show where each phase exists and where transitions occur, making them essential navigational tools for locating the correct property tables in engineering calculations.

The **P-T diagram** (pressure-temperature diagram) for a pure substance reveals three regions — solid, liquid, and gas — separated by boundary curves. The **sublimation curve** separates solid from gas. The **melting curve** separates solid from liquid; for water, this curve tilts slightly left (higher pressure lowers the melting point), an anomaly tied to water's unusual density behavior when freezing. The **vapor-pressure curve** separates liquid from gas and slopes upward: higher pressure requires higher temperature to maintain liquid-vapor equilibrium. All three curves meet at the **triple point**, where all three phases coexist in equilibrium simultaneously. The vapor-pressure curve terminates at the **critical point**: beyond this state, no distinct boundary separates liquid from gas, and the fluid is called supercritical.

The **P-v diagram** (pressure-specific volume diagram) tells a richer story. The vapor-pressure curve, which appeared as a single line in P-T space, now expands into a dome-shaped **saturation envelope**. The left edge of the dome is the **saturated liquid curve** (quality x = 0) and the right edge is the **saturated vapor curve** (x = 1). Inside the dome, liquid and vapor coexist in proportions described by **quality** x — the mass fraction that is vapor. A state with x = 0.4 is 40% vapor, 60% liquid by mass, and its specific volume lies at 40% of the way between vₗ and vᵥ at that pressure. Outside the dome to the left is compressed (subcooled) liquid; to the right is superheated vapor. The apex of the dome is the critical point; for water this is 374°C and 22.1 MPa. Above this temperature, cooling the fluid from vapor phase will never produce a visible phase boundary — the substance transitions continuously between gas-like and liquid-like behavior.

Engineering calculations depend on correctly identifying which region a given state occupies before looking up any property. The algorithm is: at the given pressure, find the saturation temperature Tₛₐₜ. If the substance's actual temperature exceeds Tₛₐₜ, you have superheated vapor. If temperature is below Tₛₐₜ and pressure is not too high, you have compressed liquid. If temperature equals Tₛₐₜ, you are inside the saturation dome and need quality to fully specify the state. Getting this identification wrong — for example, using superheated vapor tables inside the dome where those tables don't apply — produces physically meaningless answers. The P-T and P-v diagrams together give the mental picture that makes this identification automatic rather than something requiring a new thought process every time.
