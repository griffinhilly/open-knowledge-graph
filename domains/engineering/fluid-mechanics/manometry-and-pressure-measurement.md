---
id: manometry-and-pressure-measurement
title: Manometry and Pressure Measurement
domain: engineering
course: fluid-mechanics
prerequisites:
- id: fluid-statics-pressure
  type: hard
builds-toward:
- flow-measurement-methods
tags:
- manometer
- pressure gauge
- U-tube
- differential pressure
stage: formal-systems
status: validated
---

# Manometry and Pressure Measurement

## Core Idea
Manometers use columns of fluid to measure pressure differences by balancing hydrostatic pressure heads. A simple U-tube manometer relates the pressure difference between two points to the height difference of a manometer fluid of known density. Differential manometers compare pressures at two locations in a system, while inclined manometers improve resolution for small pressure differences.

## How It's Best Learned
Trace the pressure path from one known end to the unknown, adding ρgh when moving down and subtracting when moving up in each fluid segment. Draw the manometer systematically and label each fluid interface before writing the equation.

## Common Misconceptions
- You must track every fluid layer in the manometer path, not just the manometer fluid.
- The manometer fluid must be immiscible with and denser than the process fluid.
- Connected fluid columns at the same elevation have equal pressure only if they are in the same continuous fluid.

## Questions

```yaml
- question: "A U-tube manometer uses mercury (ρ = 13,600 kg/m³) to measure pressure in a water pipe (ρ = 1,000 kg/m³). The water fills both manometer arms above the mercury. To find the pressure difference, you should:"
  type: multiple-choice
  options:
    - "Use only the mercury column height, since water is so much less dense that its contribution is negligible in all cases"
    - "Multiply the total tube length of each arm by the respective fluid density"
    - "Account for the vertical height of every fluid segment in the path — both the water columns and the mercury column"
    - "Use the cross-sectional area of the tube to convert the mercury height into a force"
  answer: 2
  explanation: "Every fluid layer in the manometer path contributes a pressure head of ρgh. Ignoring the water columns introduces a systematic error proportional to the water column heights. If the water columns are tall relative to the mercury displacement, the error is significant. The correct approach is to trace the pressure from one port to the other, adding ρgh for each downward fluid segment and subtracting ρgh for each upward segment, for every fluid present. Tube shape and cross-section are irrelevant — only vertical heights and densities matter."

- question: "The left arm of a U-tube manometer is widened to twice the diameter of the right arm. How does this change the pressure measurement?"
  type: multiple-choice
  options:
    - "The left arm now reads a higher pressure because it holds more fluid per unit height"
    - "The pressure calculation must be corrected by the area ratio to account for the different cross-sections"
    - "The measurement is unchanged — pressure depends only on vertical height of fluid columns, not on tube geometry"
    - "The measurement becomes invalid because unequal cross-sections violate the hydrostatic balance assumption"
  answer: 2
  explanation: "This tests the core principle of fluid statics: pressure is determined by the vertical height of the fluid column above a reference point, not by the volume, shape, or cross-section of the container. P = ρgh. A wide tube and a narrow tube containing the same fluid to the same height exert identical pressure at the bottom. This is the hydrostatic paradox — the result that surprised early natural philosophers. Tube geometry affects the volume of fluid, not the pressure. The manometer equation P₁ − P₂ = ρ_m g Δh is independent of tube cross-section."

- question: "An inclined manometer tilted at 5° from horizontal provides better resolution than a vertical manometer for the same pressure difference, because a given vertical rise corresponds to a much larger displacement along the inclined tube."
  type: true-false
  answer: true
  explanation: "The geometric gain is 1/sin θ. At θ = 5°, a vertical rise of 1 mm requires a 1/sin(5°) ≈ 11.5 mm movement along the tube — readable on a scale where 1 mm increments would be invisible. This amplification is purely geometric: the pressure difference still equals ρgh (vertical height only), but the human-readable displacement is 11.5× larger. The inclined manometer is the earliest analog amplifier — using geometry to convert a small, hard-to-read signal into a large, easy-to-read one. The principle appears in every precision pressure transducer design."

- question: "In a connected fluid system, two points at the same elevation always have equal pressure, regardless of which fluids or structures lie above them."
  type: true-false
  answer: false
  explanation: "Equal pressure at equal elevation holds only within the same continuous fluid. If two points at the same elevation are connected through different fluid columns above them — for example, one arm has mercury and water, the other has only water — the pressures at that elevation can differ significantly. The equal-pressure principle applies within a single uninterrupted fluid at rest, not across fluid interfaces or separate fluid columns. This is the most common conceptual error in manometer problems: students assume that equal elevation means equal pressure, then fail to account for the different density columns above each point."

- question: "Explain why you must trace every fluid layer in a manometer path — not just the manometer fluid — when calculating a pressure difference. What error results from ignoring process fluid in the manometer arms?"
  type: short-answer
  answer: "Each fluid layer contributes a pressure head ρgh proportional to its density and vertical height. When process fluid (e.g., water) rises into the manometer arms above the mercury, it exerts pressure that partially offsets or adds to the mercury column's contribution. Ignoring the water columns means neglecting their pressure heads. If the water column on the high-pressure side is taller than on the low-pressure side, the true pressure difference is less than the mercury displacement alone would suggest. The error equals ρ_water × g × (Δh_water), which can be substantial when process fluid fills tall manometer arms. Systematic path tracing — adding ρgh going down and subtracting going up for every fluid — is the only way to account for all contributions correctly."
  explanation: "The key insight is that the manometer path traverses multiple fluids, and each one contributes to the hydrostatic balance. The mercury column is typically the largest term (high density, large displacement), but the process fluid terms are systematic corrections that cannot be ignored in precision measurements. Drawing the manometer and labeling every fluid interface before writing the equation is the procedure that prevents errors — it forces you to identify all the layers before performing the calculation."
```

## Explainer

You know from fluid statics that pressure increases with depth in a fluid: ΔP = ρgh. A **manometer** turns this hydrostatic relationship into a measurement instrument. By balancing an unknown pressure against a column of fluid of known density and height, you can read pressure without any mechanical moving parts — only equilibrium. This simplicity is why manometers remained the standard pressure measurement tool for centuries and why they still appear as the calibration reference for electronic transducers.

The simplest instrument is the **U-tube manometer**. Connect one arm to the system at unknown pressure P₁ and the other to a reference (often open atmosphere, P₂ = P_atm). Fill the bottom of the U with a dense, immiscible **manometer fluid** — mercury, colored oil, or a heavy brine. The unknown pressure displaces the manometer fluid until hydrostatic equilibrium is reached. Tracing the pressure path from the reference arm to the system arm — adding ρgh when moving downward through a fluid layer, subtracting when moving upward — gives P₁ − P₂ = ρ_m × g × Δh, where ρ_m is the manometer fluid density and Δh is the height difference between the two manometer fluid surfaces. Crucially, pressure depends only on the vertical height of fluid columns, not on tube shape, cross-section, or horizontal runs.

When the process fluid (water, oil) extends into the manometer arms, you must account for every fluid layer in the path, not just the manometer fluid. Trace the pressure from one open end to the other, accumulating a ρgh term for each vertical segment in each fluid. A systematic approach — label every fluid interface, identify every vertical rise and fall, then write the equation — prevents the most common error of forgetting a layer. For a **differential manometer** comparing pressures at two points in a flowing system, the same path-tracing method applies: start at one port, traverse through the system fluid and manometer fluid to the other port, and set the total pressure drop equal to ρ_m × g × Δh minus any process-fluid head contributions.

For measuring very small pressure differences, the **inclined manometer** amplifies resolution by tipping the tube at angle θ from horizontal. A small vertical rise h = L sin θ corresponds to a large movement L along the inclined tube. At θ = 5°, a 10 mm vertical rise produces a 115 mm column displacement — a factor of 1/sin 5° ≈ 11.5 amplification. This geometric gain is read directly off the tube, converting an imperceptibly small pressure difference into a clearly legible scale reading. The principle — using geometry to amplify a small signal into a large readable one — is the earliest analog of sensor gain and reappears in every precision pressure transducer design.
