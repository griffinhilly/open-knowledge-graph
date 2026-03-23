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

## Questions

```yaml
- question: "A rectangular HVAC duct is 0.5 m wide and 0.5 m tall (a square cross-section). What is its hydraulic diameter?"
  type: multiple-choice
  options:
    - "0.354 m — the diagonal divided by √2"
    - "0.5 m — equal to the side length"
    - "0.25 m — half the side length"
    - "0.707 m — the diagonal of the square"
  answer: 1
  explanation: "D_h = 4A/P = 4(0.5 × 0.5)/(4 × 0.5) = 4(0.25)/2.0 = 0.5 m. For a square duct with side a, D_h = 4a²/4a = a. This is a useful sanity check: a square's hydraulic diameter equals its side length, not its diagonal or any other geometric mean. The hydraulic diameter formula always reduces to the actual diameter for a circle, and to the side length for a square."

- question: "An engineer applies the hydraulic diameter formula to a very flat rectangular duct (1.0 m wide, 0.02 m tall) and uses the result in the Moody chart to estimate friction losses. Compared to a compact (nearly square) duct with the same D_h, the flat duct's actual friction factor will likely:"
  type: multiple-choice
  options:
    - "Be the same — the hydraulic diameter fully captures all geometry effects"
    - "Be lower — the flat duct has less surface area per unit volume"
    - "Be higher — corner effects and non-uniform velocity profiles in elongated ducts cause greater friction than circular-pipe correlations predict"
    - "Be unpredictable — the Moody chart cannot be applied to any non-circular duct"
  answer: 2
  explanation: "The hydraulic diameter is an empirical approximation that works best for compact, nearly equilateral cross-sections. For highly elongated ducts (aspect ratio much greater than 4:1), the velocity profile near the corners differs fundamentally from the parabolic profile assumed in circular-pipe correlations, and secondary flow structures cause additional friction. The H_h correlation systematically under-predicts friction for flat ducts approaching the parallel-plate geometry. Engineers working with high-aspect-ratio ducts should use analytical solutions (which exist for parallel plates) or correction factors rather than trusting the Moody chart directly."

- question: "For a circular pipe of diameter D, the hydraulic diameter formula D_h = 4A/P gives a result equal to D."
  type: true-false
  answer: true
  explanation: "This is the required sanity check. A circle has area A = πD²/4 and perimeter P = πD. Therefore D_h = 4(πD²/4)/(πD) = πD²/(πD) = D. The factor of 4 in the formula was specifically chosen to ensure this — without the factor of 4, D_h would equal D/4 for a circle, which would make the formula useless for the intended purpose of extending circular-pipe correlations to non-circular geometries."

- question: "The hydraulic diameter of a non-circular duct should be computed as the geometric average (square root of width × height) of its cross-sectional dimensions."
  type: true-false
  answer: false
  explanation: "The hydraulic diameter is D_h = 4A/P (four times the cross-sectional area divided by the wetted perimeter), not a geometric average of dimensions. The physical reasoning is that friction scales with the ratio of area to wetted perimeter, not with any average of dimensions. For a rectangle of width W and height H: D_h = 4(WH)/(2(W+H)) = 2WH/(W+H). For a square (W=H=a): D_h = a. The geometric mean √(WH) would give √(a²) = a for a square but would give different (wrong) values for other geometries."

- question: "Explain the physical reasoning behind the formula D_h = 4A/P — specifically, why friction in a duct scales with the ratio of cross-sectional area to wetted perimeter, and why the factor of 4 is included."
  type: short-answer
  answer: "Friction loss in internal flow comes from the shear stress exerted by the walls on the fluid. Every unit of wetted perimeter (wall contact) generates friction, while cross-sectional area carries the flow. A passage with high P/A has lots of wall per unit of flow area — it's 'friction-heavy.' A passage with low P/A has less wall per unit area — less friction per unit flow. The ratio A/P (or its reciprocal) captures this balance. The factor of 4 is a normalization convention chosen so that D_h equals the actual diameter D for a circular pipe (since a circle's A/P = D/4, multiplying by 4 gives D). This ensures all existing circular-pipe correlations apply without a correction constant."
  explanation: "The hydraulic diameter is fundamentally an empirical similarity parameter: it matches the friction characteristics of non-circular passages to the best-studied case (circular pipes) by equating their A/P ratios. It works well when the velocity profile shape is similar — compact geometries where no dimension is much larger than another. It fails for highly elongated geometries where the profile differs fundamentally from the circular-pipe parabola."
```

## Explainer

You know from the continuity equation that flow rate, velocity, and cross-sectional area are linked — but engineering systems rarely use round pipes exclusively. HVAC ducts are rectangular, heat exchanger cores use triangular passages, annular gaps appear between concentric tubes. All the friction-factor correlations (Moody chart, Colebrook equation) were derived for circular pipes. The **hydraulic diameter** is the bridge that lets you use them anyway.

The definition D_h = 4A/P encodes a physical idea: friction loss in internal flow scales with the ratio of the flow area to the wetted perimeter, not just the size of the passage. Wetted perimeter P is every solid surface in contact with the fluid — it generates friction. Cross-sectional area A carries the flow. A passage with lots of wall per unit area (high P/A) is "friction-heavy" and appears hydraulically smaller than its geometric size suggests. The factor of 4 is chosen so that D_h reduces to the actual diameter D for a circular pipe: D_h = 4(πD²/4)/(πD) = D. Verify this as a sanity check on any new geometry.

For a rectangular duct of width W and height H, D_h = 2WH/(W + H). For a square duct (W = H = a), this gives D_h = a — the side length, not the diagonal. For a very flat duct (H ≪ W), D_h ≈ 2H — twice the gap height, because the two wide faces dominate the wetted perimeter. This geometry approaches flow between parallel plates, for which exact analytical solutions exist; the hydraulic diameter approximation deteriorates as the aspect ratio grows beyond about 4:1. For an annulus with outer radius r_o and inner radius r_i, D_h = 4(π(r_o² − r_i²))/(2π(r_o + r_i)) = 2(r_o − r_i) — the gap width, doubled.

Once you have D_h, use it everywhere diameter appears in circular-pipe correlations: Re = ρ V D_h / μ for the Reynolds number, f from the Moody chart or Colebrook equation, and ΔP = f (L/D_h)(ρV²/2) in the Darcy-Weisbach equation. From your dimensional analysis background, you recognize this is an empirical similarity argument — systems with the same Re (using D_h) are expected to have similar friction behavior. The approximation is best for compact, nearly equilateral cross-sections and degrades for highly elongated or irregular geometries where the velocity profile near corners differs fundamentally from the circular-pipe assumption.
