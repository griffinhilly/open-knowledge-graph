---
id: hydraulic-diameter-non-circular-ducts
title: Hydraulic Diameter and Non-Circular Conduits
domain: engineering
course: fluid-mechanics
prerequisites:
- id: continuity-equation-fluid
  type: hard
- id: dimensional-analysis-and-similarity
  type: soft
builds-toward:
- minor-loss-coefficients-fittings-elbows
- pipe-networks-series-parallel-analysis
tags:
- geometry
- diameter
- correlations
stage: formal-systems
status: draft
---

# Hydraulic Diameter and Non-Circular Conduits

## Core Idea
The hydraulic diameter D_h = 4A/P converts non-circular flow passages (rectangular ducts, annuli, channels) into equivalent diameters for use with circular-pipe friction-factor and Reynolds-number correlations. This empirical equivalence allows the same engineering correlations developed for pipes to apply to complex geometries. Accuracy depends on the aspect ratio and degree of eccentricity.

## Explainer

You know from the continuity equation that flow rate, velocity, and cross-sectional area are linked — but engineering systems rarely use round pipes exclusively. HVAC ducts are rectangular, heat exchanger cores use triangular passages, annular gaps appear between concentric tubes. All the friction-factor correlations (Moody chart, Colebrook equation) were derived for circular pipes. The **hydraulic diameter** is the bridge that lets you use them anyway.

The definition D_h = 4A/P encodes a physical idea: friction loss in internal flow scales with the ratio of the flow area to the wetted perimeter, not just the size of the passage. Wetted perimeter P is every solid surface in contact with the fluid — it generates friction. Cross-sectional area A carries the flow. A passage with lots of wall per unit area (high P/A) is "friction-heavy" and appears hydraulically smaller than its geometric size suggests. The factor of 4 is chosen so that D_h reduces to the actual diameter D for a circular pipe: D_h = 4(πD²/4)/(πD) = D. Verify this as a sanity check on any new geometry.

For a rectangular duct of width W and height H, D_h = 2WH/(W + H). For a square duct (W = H = a), this gives D_h = a — the side length, not the diagonal. For a very flat duct (H ≪ W), D_h ≈ 2H — twice the gap height, because the two wide faces dominate the wetted perimeter. This geometry approaches flow between parallel plates, for which exact analytical solutions exist; the hydraulic diameter approximation deteriorates as the aspect ratio grows beyond about 4:1. For an annulus with outer radius r_o and inner radius r_i, D_h = 4(π(r_o² − r_i²))/(2π(r_o + r_i)) = 2(r_o − r_i) — the gap width, doubled.

Once you have D_h, use it everywhere diameter appears in circular-pipe correlations: Re = ρ V D_h / μ for the Reynolds number, f from the Moody chart or Colebrook equation, and ΔP = f (L/D_h)(ρV²/2) in the Darcy-Weisbach equation. From your dimensional analysis background, you recognize this is an empirical similarity argument — systems with the same Re (using D_h) are expected to have similar friction behavior. The approximation is best for compact, nearly equilateral cross-sections and degrades for highly elongated or irregular geometries where the velocity profile near corners differs fundamentally from the circular-pipe assumption.
