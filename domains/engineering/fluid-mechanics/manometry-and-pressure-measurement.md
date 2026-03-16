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

## Explainer

You know from fluid statics that pressure increases with depth in a fluid: ΔP = ρgh. A **manometer** turns this hydrostatic relationship into a measurement instrument. By balancing an unknown pressure against a column of fluid of known density and height, you can read pressure without any mechanical moving parts — only equilibrium. This simplicity is why manometers remained the standard pressure measurement tool for centuries and why they still appear as the calibration reference for electronic transducers.

The simplest instrument is the **U-tube manometer**. Connect one arm to the system at unknown pressure P₁ and the other to a reference (often open atmosphere, P₂ = P_atm). Fill the bottom of the U with a dense, immiscible **manometer fluid** — mercury, colored oil, or a heavy brine. The unknown pressure displaces the manometer fluid until hydrostatic equilibrium is reached. Tracing the pressure path from the reference arm to the system arm — adding ρgh when moving downward through a fluid layer, subtracting when moving upward — gives P₁ − P₂ = ρ_m × g × Δh, where ρ_m is the manometer fluid density and Δh is the height difference between the two manometer fluid surfaces. Crucially, pressure depends only on the vertical height of fluid columns, not on tube shape, cross-section, or horizontal runs.

When the process fluid (water, oil) extends into the manometer arms, you must account for every fluid layer in the path, not just the manometer fluid. Trace the pressure from one open end to the other, accumulating a ρgh term for each vertical segment in each fluid. A systematic approach — label every fluid interface, identify every vertical rise and fall, then write the equation — prevents the most common error of forgetting a layer. For a **differential manometer** comparing pressures at two points in a flowing system, the same path-tracing method applies: start at one port, traverse through the system fluid and manometer fluid to the other port, and set the total pressure drop equal to ρ_m × g × Δh minus any process-fluid head contributions.

For measuring very small pressure differences, the **inclined manometer** amplifies resolution by tipping the tube at angle θ from horizontal. A small vertical rise h = L sin θ corresponds to a large movement L along the inclined tube. At θ = 5°, a 10 mm vertical rise produces a 115 mm column displacement — a factor of 1/sin 5° ≈ 11.5 amplification. This geometric gain is read directly off the tube, converting an imperceptibly small pressure difference into a clearly legible scale reading. The principle — using geometry to amplify a small signal into a large readable one — is the earliest analog of sensor gain and reappears in every precision pressure transducer design.
