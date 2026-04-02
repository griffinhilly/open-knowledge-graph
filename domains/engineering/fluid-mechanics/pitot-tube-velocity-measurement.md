---
id: pitot-tube-velocity-measurement
title: Pitot Tube and Velocity Measurement
domain: engineering
course: fluid-mechanics
prerequisites:
- id: absolute-gauge-atmospheric-pressure
  type: hard
- id: bernoullis-equation
  type: hard
builds-toward:
- streamlines-and-flow-visualization
tags:
- measurement
- instruments
- flow
stage: expert
status: validated
---

# Pitot Tube and Velocity Measurement

## Core Idea
A Pitot tube measures flow velocity by converting dynamic pressure into a height difference in a manometer. The stagnation pressure (total pressure where flow stops) minus static pressure equals the dynamic pressure: q = ½ρV². Pitot tubes are widely used for measuring airspeed in aircraft and water velocity in open channels because they cause minimal flow disturbance.

## Questions

```yaml
- question: "A Pitot tube is inserted into a flow. The stagnation port and static port register identical pressures. What does this tell you about the flow at that location?"
  type: multiple-choice
  options:
    - "The fluid density is too low to generate a measurable pressure difference"
    - "The flow velocity at that point is zero or negligible"
    - "There is a blockage in the stagnation port preventing pressure buildup"
    - "The tube is misaligned with the flow, so stagnation is incomplete"
  answer: 1
  explanation: "Dynamic pressure = stagnation pressure − static pressure = ½ρV². If both ports read the same pressure, the difference is zero, meaning ½ρV² = 0, hence V = 0. This is the direct consequence of the operating principle: the entire measurement relies on the pressure rise that results from stagnating the moving fluid and converting its kinetic energy into pressure. No velocity means no kinetic energy to convert, so no pressure difference. A misaligned tube would reduce (not zero out) the stagnation pressure."

- question: "In a water-filled manometer connected to a Pitot tube immersed in water flow, the velocity formula simplifies to V = √(2gΔh), where Δh is the height difference. Why does fluid density not appear in this result?"
  type: multiple-choice
  options:
    - "Water is incompressible, so density does not affect pressure in any liquid measurement"
    - "Dynamic pressure ½ρV² and the manometer pressure ρgΔh both contain ρ, which cancels when they are set equal"
    - "This formula is a special approximation valid only at low flow speeds where density effects are small"
    - "Gravity acts equally on both sides of the manometer, eliminating the density term"
  answer: 1
  explanation: "Setting the dynamic pressure equal to the manometer pressure rise: ½ρV² = ρgΔh. Since ρ appears on both sides and is the same fluid (manometer fluid = flowing fluid), it cancels, giving V = √(2gΔh). This elegant result means velocity can be read directly from a ruler measurement of liquid height, with no need to know the fluid density. If the manometer uses a different fluid (e.g., mercury), the two densities are unequal and both must be accounted for."

- question: "A Pitot tube directly measures the velocity of the fluid flowing past it."
  type: true-false
  answer: false
  explanation: "A Pitot tube measures pressure — specifically the difference between stagnation (total) pressure and static pressure. Velocity is then derived from this measurement using V = √(2ΔP/ρ), which requires knowing the fluid density. The device converts kinetic energy into a measurable pressure rise; the velocity is inferred, not directly sensed. This distinction matters: errors in the assumed fluid density propagate directly into the velocity calculation."

- question: "The stagnation point at the Pitot tube's front face creates a pressure higher than the surrounding static pressure because the fluid's kinetic energy is converted into pressure energy there."
  type: true-false
  answer: true
  explanation: "This is the core physical principle. Bernoulli's equation along the stagnation streamline gives P_static + ½ρV² = P_stagnation (with elevation terms equal at both points). At the stagnation point, V = 0, so all kinetic energy ½ρV² has been converted into additional pressure. The stagnation pressure therefore exceeds the static pressure by exactly the dynamic pressure ½ρV², which is what the instrument measures. This is an energy trade-off: kinetic energy → pressure energy."

- question: "What physical principle does a Pitot tube exploit to measure flow velocity, and what two pressures must it measure to do so?"
  type: short-answer
  answer: "A Pitot tube exploits Bernoulli's equation, which states that pressure and kinetic energy trade off along a streamline: P + ½ρV² = constant. By facing a port directly into the flow, fluid is brought to rest (stagnated), converting all kinetic energy into a pressure rise. The stagnation port measures total pressure P_total = P_static + ½ρV². A flush static port measures P_static (the ambient pressure undisturbed by flow). The difference ΔP = P_total − P_static = ½ρV² is the dynamic pressure, from which velocity is calculated as V = √(2ΔP/ρ)."
  explanation: "The key insight is that the Pitot tube doesn't sense velocity directly — it senses the pressure consequence of stopping the flow. The two-port design (stagnation + static) isolates exactly the dynamic pressure term from Bernoulli's equation. Knowing fluid density then completes the velocity calculation. This simplicity (one pressure difference measurement) is why Pitot tubes are widely used from aircraft cockpits to introductory fluid mechanics labs."
```

## Explainer

Bernoulli's equation, which you know from prerequisites, states that along a streamline in steady, inviscid, incompressible flow: P + ½ρV² + ρgz = constant. This is an energy statement — the sum of pressure energy, kinetic energy, and potential energy per unit volume is conserved. The **dynamic pressure** ½ρV² represents the kinetic energy of the moving fluid. A Pitot tube exploits this relationship by creating a controlled stagnation point: a small hole facing directly into the flow brings the fluid momentarily to rest, converting all of its kinetic energy into a measurable pressure increase.

The device in practice consists of two pressure ports. The **stagnation port** faces upstream and measures total pressure P_total = P_static + ½ρV². The **static port** is flush with the tube wall and measures P_static, the ambient pressure at that location. The difference is exactly the dynamic pressure: P_total − P_static = ½ρV². Solving for velocity gives V = √(2(P_total − P_static)/ρ). You only need to measure a pressure difference and know the fluid density — no other information about the flow is required.

From your understanding of pressure measurement, you know that pressure differences can be read directly with a manometer or differential pressure transducer. In a water-filled manometer connected to the two ports, the height difference Δh satisfies ΔP = ρ_fluid · g · Δh. Substituting back gives V = √(2gΔh) for the special case where the manometer fluid is the same as the flowing fluid. This clean result is why Pitot tubes are popular in introductory lab courses — the velocity comes directly from a ruler measurement of liquid height.

On aircraft, the **Pitot-static system** connects one probe facing the airstream (for stagnation pressure) and one set of flush ports on the fuselage (for static pressure). The difference drives the airspeed indicator. One critical limitation: the classical Bernoulli derivation assumes incompressible flow. At low aircraft speeds this is fine, but above roughly Mach 0.3 the compressibility correction becomes important. For subsonic aircraft the correction is a modest factor; for supersonic flight, a normal shock forms ahead of the probe and the analysis must account for the entropy rise across the shock — the Rayleigh Pitot tube formula applies instead. But the core physical idea — measure the pressure rise from stagnating a moving fluid — remains unchanged across all these regimes.
