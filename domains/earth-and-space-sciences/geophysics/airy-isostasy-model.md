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
status: draft
---

# Airy Isostasy and Crustal Thickness Variation

## Core Idea
The Airy model assumes isostatic equilibrium is maintained by variations in crustal thickness: mountains have thick crustal roots while ocean basins have thin crust. A column of rock at any location has the same total gravitational weight if integrated to a constant reference depth. Airy isostasy predicts the crustal thickness needed to balance observed topography.

## Explainer

From your study of isostasy, you know that Earth's crust floats on the denser mantle much like ice floats on water, and that topographic highs must be compensated by mass deficits at depth to maintain gravitational equilibrium. The **Airy isostasy model** specifies exactly how this compensation works: it assumes the crust has a uniform density everywhere, and that differences in surface elevation are explained entirely by differences in crustal thickness. Mountains stand high because they have deep roots extending into the mantle; ocean basins sit low because their crust is thin.

The analogy to icebergs is nearly exact. An iceberg floating in the ocean has most of its mass below the waterline. A taller iceberg does not have denser ice — it simply has more ice extending deeper into the water. In Airy isostasy, a 5 km mountain range might require a crustal root extending 30–35 km below the normal crustal base, because the density contrast between crust (~2,700 kg/m³) and mantle (~3,300 kg/m³) determines the ratio of root depth to surface elevation. The math follows directly from the **equal pressure at a compensation depth** principle: pick a horizontal surface deep in the mantle, and the total weight of every vertical column above that surface must be the same. If it were not, pressure differences would drive lateral flow in the mantle until balance was restored.

You can calculate the root thickness from a simple formula. If the crust has density ρ_c and the mantle has density ρ_m, then for a mountain of height h above the reference surface, the root extends to a depth r = h × ρ_c / (ρ_m − ρ_c). With typical values, this gives roughly r ≈ 5h — every kilometer of elevation requires about five kilometers of extra root. This prediction is testable: seismic studies beneath the Himalayas and the Andes confirm that crustal roots reach 60–70 km, consistent with Airy predictions for their elevations.

The Airy model works well for mountain belts and continental margins, where crustal thickness variations are the dominant mode of compensation. It works less well for broad plateaus and mid-ocean features, where lateral density variations (the subject of the Pratt model you will encounter next) may play a larger role. The model also assumes perfect local compensation — each column is independently balanced — which ignores the lateral strength of the lithosphere. Real lithosphere can support loads over some horizontal distance, which is why the related concept of elastic plate flexure eventually refines this picture. Still, Airy isostasy remains the foundational quantitative tool for predicting how topography and crustal structure relate, and gravity anomaly analysis in the field begins by comparing observations against Airy predictions.
