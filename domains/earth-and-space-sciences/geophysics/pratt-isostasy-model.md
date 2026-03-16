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

## Explainer

From isostasy and crustal balance, you know that the Earth's crust floats on the denser mantle in a state of gravitational equilibrium, much like blocks of wood floating in water. You may also be familiar with the Airy model, which explains topographic differences through variations in crustal thickness — mountains have deep roots, ocean basins have thin crust. The **Pratt model** offers an alternative mechanism: instead of varying how deep the crust extends, it varies how dense the crust is, while keeping the base of the crust at a uniform depth called the **compensation depth**.

Picture a set of columns, all extending from the surface down to the same compensation depth, all exerting the same pressure on the mantle beneath them. For this to work, columns that stick up higher (mountains) must be made of less dense material, while columns that sit lower (basins) must be denser. The math is straightforward: if every column has the same pressure at the compensation depth, then ρ₁h₁ = ρ₂h₂ — the product of density and total column height must be constant. A taller column (higher topography) requires a proportionally lower density to maintain the balance.

While the Airy model generally provides a better description of continental mountain belts — where seismic data confirms the existence of deep crustal roots — the Pratt model is surprisingly effective in certain geological settings. **Mid-ocean ridges** are the classic example: the ridge stands high not because the crust is thicker there, but because the underlying mantle is hotter and therefore less dense. As lithosphere moves away from the ridge and cools, it becomes denser and subsides — exactly the Pratt mechanism at work. Thermal expansion and contraction create lateral density variations at roughly constant crustal thickness. Similarly, in some continental settings, lateral variations in crustal composition (more felsic vs. more mafic rock) produce density contrasts that contribute to topographic differences without large changes in Moho depth.

In practice, real isostatic compensation involves elements of both models — and often neither is sufficient on its own. Modern geophysics uses **flexural isostasy**, which treats the lithosphere as an elastic plate that distributes loads over a broader area than either the Airy or Pratt models predict. But the Pratt model remains valuable as a conceptual tool for interpreting gravity anomalies: when you observe high topography paired with relatively normal crustal thickness, lateral density variations — the Pratt mechanism — are likely at work. Recognizing whether Airy-type root thickening or Pratt-type density variation dominates in a given region is essential for correctly interpreting Bouguer anomaly patterns and understanding the tectonic forces at play.
