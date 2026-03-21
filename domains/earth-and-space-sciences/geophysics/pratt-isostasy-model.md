---
id: pratt-isostasy-model
title: Pratt Isostasy and Lateral Density Variations
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: isostasy-and-crustal-balance
  type: hard
- id: airy-isostasy-model
  type: soft
builds-toward:
- elastic-plate-flexure
tags:
- gravity
- isostasy
- density
stage: advanced
status: draft
---

# Pratt Isostasy and Lateral Density Variations

## Core Idea
The Pratt model achieves isostatic balance through lateral variations in density at constant crustal thickness rather than through crustal thickness variations. High topography corresponds to lower-density crust, while low topography corresponds to higher-density crust. Though less realistic than Airy isostasy, Pratt's model usefully interprets gravity anomalies in regions where crust deforms by density redistribution.

## Questions

```yaml
- question: "A mid-ocean ridge stands 2 km above the surrounding seafloor, but seismic surveys show the crustal thickness is approximately the same everywhere. Which isostasy model best explains why the ridge stands high?"
  type: multiple-choice
  options:
    - "Airy isostasy — the ridge must have a deep crustal root, and the seismic data must be incorrect"
    - "Neither model applies here — isostasy requires crustal thickness variation to support topography"
    - "Pratt isostasy — the ridge stands high because hot, less dense mantle beneath the spreading center reduces the column's average density at roughly constant crustal thickness"
    - "Flexural isostasy — the rigid lithosphere elastically supports the ridge without any density variation"
  answer: 2
  explanation: "The Airy model predicts topographic highs should have thick crustal roots. Seismic evidence at mid-ocean ridges contradicts this — crustal thickness is not anomalously large. The Pratt model explains the ridge's elevation through lower density: hot asthenosphere upwelling at the spreading center is thermally expanded and less dense, supporting the topographic high at constant (or near-constant) crustal thickness. This is a textbook case where Pratt outperforms Airy."

- question: "In the Pratt model, two crustal columns must balance at the compensation depth. Column A has density 2800 kg/m³ and height 35 km. Column B has lower density 2600 kg/m³. For isostatic balance (equal pressure at compensation depth), how tall must Column B be?"
  type: multiple-choice
  options:
    - "35 km — same height regardless of density"
    - "Approximately 37.7 km — Column B must be taller because lower density requires greater height to achieve the same pressure"
    - "Approximately 32.5 km — denser columns are taller to compensate"
    - "The height cannot be determined without knowing the mantle density"
  answer: 1
  explanation: "Pressure at compensation depth = ρ × h (per unit area). For balance: ρ_A × h_A = ρ_B × h_B. So h_B = (2800 × 35) / 2600 ≈ 37.7 km. Lower density requires proportionally greater height to generate the same pressure. This is the core Pratt mechanism: high topography is underlain by low-density crust, and the taller column of lighter material equals the shorter column of denser material in terms of total mass per unit area."

- question: "In the Pratt isostasy model, regions of higher topography have lower average crustal density than regions of lower topography, assuming all columns reach the same compensation depth."
  type: true-false
  answer: true
  explanation: "This is the defining feature of Pratt isostasy: ρh = constant at the compensation depth for all columns. Higher topography (larger h) requires smaller ρ to keep the product constant. This contrasts with the Airy model, where density is uniform and topographic support comes from varying the depth of the crustal root. In Pratt, the 'root' is replaced by laterally variable density."

- question: "The Airy and Pratt isostasy models make identical predictions about crustal thickness beneath mountain ranges, differing only in their treatment of lateral density."
  type: true-false
  answer: false
  explanation: "The two models make opposite predictions about crustal thickness under mountains. Airy predicts thick crustal roots beneath high topography — mountains float on deep keels of less-dense crust, while crustal density stays constant. Pratt predicts that crustal thickness is constant (all columns reach the same compensation depth), and topographic differences are explained by density variations. Seismic data under the Himalayas and Andes confirm deep crustal roots, strongly supporting Airy isostasy there. Under mid-ocean ridges, constant thickness supports Pratt."

- question: "Explain why mid-ocean ridges are a better example of Pratt isostasy than Airy isostasy, and what physical process drives the density variation."
  type: short-answer
  answer: "Mid-ocean ridges are elevated above the surrounding seafloor, but seismic surveys show the oceanic crust is not significantly thicker at ridges — there is no Airy-type deep root. The Pratt model applies because the underlying mantle at a spreading center is hot due to asthenospheric upwelling: thermally expanded rock is less dense than cooler mantle, so the elevated topography is supported by lower-density material at roughly constant crustal thickness. As lithosphere spreads away from the ridge and cools, it contracts, becomes denser, and subsides — the classic age-depth relationship of oceanic crust, which is the Pratt mechanism operating through thermal contraction."
  explanation: "This makes mid-ocean ridges a dynamic rather than static example of Pratt isostasy: the density varies continuously with distance from the ridge as the lithosphere cools, and the topography tracks the density change accordingly. The age-depth curve of oceanic crust (depth ∝ √age) is a direct prediction of thermally-driven Pratt isostasy."
```

## Explainer

From isostasy and crustal balance, you know that the Earth's crust floats on the denser mantle in a state of gravitational equilibrium, much like blocks of wood floating in water. You may also be familiar with the Airy model, which explains topographic differences through variations in crustal thickness — mountains have deep roots, ocean basins have thin crust. The **Pratt model** offers an alternative mechanism: instead of varying how deep the crust extends, it varies how dense the crust is, while keeping the base of the crust at a uniform depth called the **compensation depth**.

Picture a set of columns, all extending from the surface down to the same compensation depth, all exerting the same pressure on the mantle beneath them. For this to work, columns that stick up higher (mountains) must be made of less dense material, while columns that sit lower (basins) must be denser. The math is straightforward: if every column has the same pressure at the compensation depth, then ρ₁h₁ = ρ₂h₂ — the product of density and total column height must be constant. A taller column (higher topography) requires a proportionally lower density to maintain the balance.

While the Airy model generally provides a better description of continental mountain belts — where seismic data confirms the existence of deep crustal roots — the Pratt model is surprisingly effective in certain geological settings. **Mid-ocean ridges** are the classic example: the ridge stands high not because the crust is thicker there, but because the underlying mantle is hotter and therefore less dense. As lithosphere moves away from the ridge and cools, it becomes denser and subsides — exactly the Pratt mechanism at work. Thermal expansion and contraction create lateral density variations at roughly constant crustal thickness. Similarly, in some continental settings, lateral variations in crustal composition (more felsic vs. more mafic rock) produce density contrasts that contribute to topographic differences without large changes in Moho depth.

In practice, real isostatic compensation involves elements of both models — and often neither is sufficient on its own. Modern geophysics uses **flexural isostasy**, which treats the lithosphere as an elastic plate that distributes loads over a broader area than either the Airy or Pratt models predict. But the Pratt model remains valuable as a conceptual tool for interpreting gravity anomalies: when you observe high topography paired with relatively normal crustal thickness, lateral density variations — the Pratt mechanism — are likely at work. Recognizing whether Airy-type root thickening or Pratt-type density variation dominates in a given region is essential for correctly interpreting Bouguer anomaly patterns and understanding the tectonic forces at play.
