---
id: airy-isostasy-model
title: Airy Isostasy and Crustal Thickness Variation
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: isostasy-and-crustal-balance
  type: hard
- id: gravity-potential-theory-earths-field
  type: soft
builds-toward:
- pratt-isostasy-model
- elastic-plate-flexure
tags:
- gravity
- isostasy
- crustal-structure
stage: advanced
status: validated
---

# Airy Isostasy and Crustal Thickness Variation

## Core Idea
The Airy model assumes isostatic equilibrium is maintained by variations in crustal thickness: mountains have thick crustal roots while ocean basins have thin crust. A column of rock at any location has the same total gravitational weight if integrated to a constant reference depth. Airy isostasy predicts the crustal thickness needed to balance observed topography.

## Questions

```yaml
- question: "Seismic imaging beneath a 2 km plateau in East Africa shows that crustal thickness is nearly uniform — the same as the surrounding lowlands. What does this imply about the mechanism of isostatic compensation?"
  type: multiple-choice
  options:
    - "The Airy model correctly explains the plateau: uniform crust is consistent with surface elevation"
    - "The plateau must have an unusually deep root that the seismic survey failed to detect"
    - "Compensation is likely achieved through lateral density variations (Pratt-style), not crustal thickness"
    - "Isostasy does not apply to plateaus; only mountain ranges achieve gravitational equilibrium"
  answer: 2
  explanation: "The Airy model predicts that elevation differences are compensated by crustal thickness — a high plateau should have a deep root. If seismic evidence shows no root, the compensating mass deficit must come from lower-density material at constant crustal thickness, which is the Pratt model's mechanism. This is a real-world situation in the East African Rift, where hot, low-density mantle material provides isostatic support without varying crustal thickness."

- question: "In the Airy model, why does a 1 km mountain require roughly 5 km of crustal root rather than a 1:1 ratio?"
  type: multiple-choice
  options:
    - "Because the crust is approximately 5 times denser than the mantle, so 1 km of mountain displaces 5 km of mantle"
    - "Because the density contrast between crust and mantle is small relative to crustal density, so a large volume of crust must displace mantle to compensate for the added surface mass"
    - "Because mountain erosion removes surface material faster than roots can grow, requiring a larger initial root"
    - "Because the compensation depth is defined as exactly 5 times the surface elevation by convention"
  answer: 1
  explanation: "The formula r = h × ρ_c / (ρ_m − ρ_c) gives root depth. With ρ_c ≈ 2,700 kg/m³ and ρ_m ≈ 3,300 kg/m³, the density contrast is only 600 kg/m³. The root displaces dense mantle and replaces it with lighter crust, so a large volume of crustal root is needed to offset a relatively small surface elevation. Numerically: r ≈ h × 2,700 / 600 ≈ 4.5h. The ratio is determined entirely by the density contrast, not by convention."

- question: "In the Airy model, a mountain range with twice the elevation of another has approximately twice the crustal root depth."
  type: true-false
  answer: true
  explanation: "The Airy formula r = h × ρ_c / (ρ_m − ρ_c) is linear in surface elevation h — root depth scales directly with elevation. Doubling the surface load doubles the required subsurface mass deficit, which in the Airy model means doubling the root thickness. This linear prediction is broadly confirmed by seismic studies comparing mountain ranges of different heights."

- question: "The Airy isostasy model explains topographic compensation through lateral variations in crustal density."
  type: true-false
  answer: false
  explanation: "This describes the Pratt model, not Airy. The Airy model assumes uniform crustal density everywhere and explains all elevation differences through variations in crustal thickness — mountains have thick roots, basins have thin crust, but the density of the crust is the same everywhere. The Pratt model holds crustal thickness constant and varies density. Both achieve isostasy through different means; confusing them reverses the core assumption of each model."

- question: "What physical principle requires that all vertical columns must weigh the same in Airy isostasy, and what would happen if they did not?"
  type: short-answer
  answer: "The principle is equal pressure at the compensation depth: at a horizontal surface deep in the mantle, pressure must be the same everywhere. Pressure at depth equals the weight of the overlying column per unit area. If two adjacent columns had different total weights, they would exert different pressures at the compensation depth, creating a horizontal pressure gradient. Since the mantle behaves as a viscous fluid over geological timescales, this gradient would drive lateral flow from the high-pressure column toward the low-pressure one, redistributing mass until pressures equalized. Isostatic equilibrium is simply the state at which this flow has ceased."
  explanation: "The analogy is hydrostatics: pressure differences in a fluid drive flow until equilibrium. The mantle is solid on short timescales but flows on timescales of thousands to millions of years. Isostasy describes the equilibrium toward which this slow flow converges."
```

## Explainer

From your study of isostasy, you know that Earth's crust floats on the denser mantle much like ice floats on water, and that topographic highs must be compensated by mass deficits at depth to maintain gravitational equilibrium. The **Airy isostasy model** specifies exactly how this compensation works: it assumes the crust has a uniform density everywhere, and that differences in surface elevation are explained entirely by differences in crustal thickness. Mountains stand high because they have deep roots extending into the mantle; ocean basins sit low because their crust is thin.

The analogy to icebergs is nearly exact. An iceberg floating in the ocean has most of its mass below the waterline. A taller iceberg does not have denser ice — it simply has more ice extending deeper into the water. In Airy isostasy, a 5 km mountain range might require a crustal root extending 30–35 km below the normal crustal base, because the density contrast between crust (~2,700 kg/m³) and mantle (~3,300 kg/m³) determines the ratio of root depth to surface elevation. The math follows directly from the **equal pressure at a compensation depth** principle: pick a horizontal surface deep in the mantle, and the total weight of every vertical column above that surface must be the same. If it were not, pressure differences would drive lateral flow in the mantle until balance was restored.

You can calculate the root thickness from a simple formula. If the crust has density ρ_c and the mantle has density ρ_m, then for a mountain of height h above the reference surface, the root extends to a depth r = h × ρ_c / (ρ_m − ρ_c). With typical values, this gives roughly r ≈ 5h — every kilometer of elevation requires about five kilometers of extra root. This prediction is testable: seismic studies beneath the Himalayas and the Andes confirm that crustal roots reach 60–70 km, consistent with Airy predictions for their elevations.

The Airy model works well for mountain belts and continental margins, where crustal thickness variations are the dominant mode of compensation. It works less well for broad plateaus and mid-ocean features, where lateral density variations (the subject of the Pratt model you will encounter next) may play a larger role. The model also assumes perfect local compensation — each column is independently balanced — which ignores the lateral strength of the lithosphere. Real lithosphere can support loads over some horizontal distance, which is why the related concept of elastic plate flexure eventually refines this picture. Still, Airy isostasy remains the foundational quantitative tool for predicting how topography and crustal structure relate, and gravity anomaly analysis in the field begins by comparing observations against Airy predictions.
