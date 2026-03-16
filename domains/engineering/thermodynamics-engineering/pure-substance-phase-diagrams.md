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
stage: advanced
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

## Explainer

From your study of thermodynamic properties and equations of state, you know that a substance's state is described by properties like pressure, temperature, and specific volume. But these properties don't vary smoothly everywhere — at phase transitions, properties change discontinuously, and two phases can coexist at fixed pressure and temperature while volume spans a wide range. **Phase diagrams** are maps that show where each phase exists and where transitions occur, making them essential navigational tools for locating the correct property tables in engineering calculations.

The **P-T diagram** (pressure-temperature diagram) for a pure substance reveals three regions — solid, liquid, and gas — separated by boundary curves. The **sublimation curve** separates solid from gas. The **melting curve** separates solid from liquid; for water, this curve tilts slightly left (higher pressure lowers the melting point), an anomaly tied to water's unusual density behavior when freezing. The **vapor-pressure curve** separates liquid from gas and slopes upward: higher pressure requires higher temperature to maintain liquid-vapor equilibrium. All three curves meet at the **triple point**, where all three phases coexist in equilibrium simultaneously. The vapor-pressure curve terminates at the **critical point**: beyond this state, no distinct boundary separates liquid from gas, and the fluid is called supercritical.

The **P-v diagram** (pressure-specific volume diagram) tells a richer story. The vapor-pressure curve, which appeared as a single line in P-T space, now expands into a dome-shaped **saturation envelope**. The left edge of the dome is the **saturated liquid curve** (quality x = 0) and the right edge is the **saturated vapor curve** (x = 1). Inside the dome, liquid and vapor coexist in proportions described by **quality** x — the mass fraction that is vapor. A state with x = 0.4 is 40% vapor, 60% liquid by mass, and its specific volume lies at 40% of the way between vₗ and vᵥ at that pressure. Outside the dome to the left is compressed (subcooled) liquid; to the right is superheated vapor. The apex of the dome is the critical point; for water this is 374°C and 22.1 MPa. Above this temperature, cooling the fluid from vapor phase will never produce a visible phase boundary — the substance transitions continuously between gas-like and liquid-like behavior.

Engineering calculations depend on correctly identifying which region a given state occupies before looking up any property. The algorithm is: at the given pressure, find the saturation temperature Tₛₐₜ. If the substance's actual temperature exceeds Tₛₐₜ, you have superheated vapor. If temperature is below Tₛₐₜ and pressure is not too high, you have compressed liquid. If temperature equals Tₛₐₜ, you are inside the saturation dome and need quality to fully specify the state. Getting this identification wrong — for example, using superheated vapor tables inside the dome where those tables don't apply — produces physically meaningless answers. The P-T and P-v diagrams together give the mental picture that makes this identification automatic rather than something requiring a new thought process every time.
