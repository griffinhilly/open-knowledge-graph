---
id: vp-vs-ratio-interpretation
title: Vp/Vs Ratio and Rock Properties
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: seismic-body-waves-p-and-s
  type: hard
- id: rock-forming-minerals
  type: soft
- id: seismic-interpretation-structural-mapping
  type: soft
- id: earthquake-magnitude-frequency-gutenberg-richter
  type: soft
- id: seismic-signal-processing
  type: soft
builds-toward:
- seismic-velocity-depth-models
tags:
- seismic
- rock-properties
- interpretation
stage: expert
status: validated
---
# Vp/Vs Ratio and Rock Properties

## Core Idea
The Vp/Vs ratio (ratio of P-wave to S-wave velocity) is a sensitive indicator of rock composition, porosity, and fluid content. Dry rocks typically have Vp/Vs ratios around 1.7–1.8, while water-saturated rocks exceed 1.9. This ratio is independent of pressure and stress, making it a robust diagnostic tool in seismic interpretation and subsurface characterization.

## How It's Best Learned
Examine Vp/Vs values from well logs and compare them to core samples and laboratory measurements. Practice computing Vp/Vs from multichannel seismic data using seismic inversion techniques.

## Common Misconceptions
Vp/Vs uniquely determines rock type (multiple lithologies can have identical ratios). The ratio is constant across all rock types (it varies significantly with composition, porosity, and fluids).

## Questions

```yaml
- question: "A seismic survey reveals a sandstone reservoir zone with Vp/Vs = 1.55. Laboratory measurements on dry sandstone cores from the same formation give Vp/Vs ≈ 1.65–1.70. What does the anomalously low ratio most likely indicate?"
  type: multiple-choice
  options:
    - "Water saturation — water increases both Vp and Vs proportionally, reducing their ratio"
    - "Gas saturation — gas dramatically reduces Vp (gas is highly compressible) while Vs is nearly unchanged, lowering the ratio below the dry-rock value"
    - "Higher clay content — clay-rich rocks consistently have lower Vp/Vs than clean sandstone"
    - "Greater burial depth — increased confining pressure reduces the Vp/Vs ratio"
  answer: 1
  explanation: "Gas is highly compressible, so saturating the rock with gas sharply lowers Vp by reducing the effective bulk modulus. Meanwhile, S-waves depend only on the shear modulus of the rock frame, not on the pore fluid (gas contributes no shear strength), so Vs stays nearly the same. The result is a Vp/Vs ratio that falls below the dry-rock value. Water saturation does the opposite — water increases the bulk modulus (and therefore Vp) while Vs is barely affected, pushing Vp/Vs above the dry value."

- question: "Two identical sandstone cores are measured in the lab — one at the confining pressure equivalent to 1 km depth, the other at 4 km depth. What would you expect for their Vp/Vs ratios?"
  type: multiple-choice
  options:
    - "The deeper sample has much higher Vp/Vs because pressure increases Vp more than Vs"
    - "The shallower sample has higher Vp/Vs because near-surface rocks contain more pore fluid"
    - "Both samples have similar Vp/Vs because pressure increases both Vp and Vs at comparable rates, so the effect largely cancels in the ratio"
    - "The deeper sample has lower Vp/Vs because compaction at depth reduces porosity and disproportionately affects P-wave velocity"
  answer: 2
  explanation: "Both Vp and Vs increase with confining pressure at similar rates because pressure closes cracks and stiffens the rock frame — affecting both wave types. Because the pressure effect applies similarly to both velocities, their ratio stays relatively stable. This is the key diagnostic advantage of Vp/Vs over individual velocities: by taking the ratio, you cancel out the dominant pressure effect and isolate the signal from fluid content and lithology. A Vp/Vs anomaly at depth almost certainly reflects composition or fluids, not just burial depth."

- question: "A water-saturated rock will have a higher Vp/Vs ratio than the same rock when dry, because water increases Vp while leaving Vs nearly unchanged."
  type: true-false
  answer: true
  explanation: "Water has a bulk modulus (~2.2 GPa) that adds to the rock frame's resistance to compression, increasing Vp. Water has zero shear modulus — it cannot resist shear deformation — so it contributes nothing to Vs. The result is a higher Vp with nearly the same Vs, meaning Vp/Vs rises. For typical sandstones, dry Vp/Vs ≈ 1.6–1.7 and water-saturated Vp/Vs ≈ 1.9–2.1. Gas saturation does the opposite, reducing Vp/Vs below the dry value."

- question: "Because Vp/Vs is relatively independent of pressure, knowing a formation's Vp/Vs ratio uniquely identifies its lithology."
  type: true-false
  answer: false
  explanation: "Vp/Vs cancels out the pressure effect but does NOT uniquely determine lithology. Multiple rock types can have overlapping or identical Vp/Vs values. For example, some shales and carbonates can have similar ratios despite being completely different lithologies. Porosity, clay content, cementation, and fluid saturation all shift the ratio, and their effects can partially offset each other. Vp/Vs is a powerful diagnostic indicator — especially for fluid detection — but it must be interpreted alongside other information such as absolute velocities, impedance, and geological context."

- question: "Explain why the Vp/Vs ratio is a more useful indicator of pore fluid content than either Vp or Vs measured individually."
  type: short-answer
  answer: "P-wave velocity (Vp) increases with both burial depth (pressure closes cracks, stiffening the rock) and water saturation. If you observe a high Vp, you cannot tell whether it is because the rock is deep or because it is water-saturated. S-wave velocity (Vs) is similarly affected by pressure. The ratio Vp/Vs cancels out the pressure effect because both velocities respond to pressure at similar rates. What remains in the ratio is the differential response to fluids: water raises Vp (adds bulk modulus) but barely changes Vs (no shear strength), pushing Vp/Vs up. Gas lowers Vp (high compressibility) but barely changes Vs, pushing Vp/Vs down. The ratio isolates the fluid signal from the confounding depth/pressure signal."
  explanation: "This is why seismic interpreters use Vp/Vs (or equivalently, Poisson's ratio derived from it) for fluid discrimination rather than plotting Vp alone. In a depth-varying subsurface, absolute velocities change with pressure even in uniform rock. The ratio corrects for this, making anomalies in Vp/Vs strong candidates for fluid or lithology changes rather than depth effects."
```

## Explainer

From your study of P- and S-wave body waves, you know that these two wave types travel at different speeds determined by different elastic properties of the rock. **P-waves** depend on both the bulk modulus (resistance to compression) and shear modulus, while **S-waves** depend only on the shear modulus. The **Vp/Vs ratio** exploits this difference: because P- and S-waves respond differently to changes in rock properties, their ratio isolates information that neither velocity alone can provide.

For a simple elastic solid, the Vp/Vs ratio relates directly to **Poisson's ratio** (ν), a fundamental elastic constant: Vp/Vs = √((2 − 2ν)/(1 − 2ν)). For most common minerals and dry rocks, Poisson's ratio falls between 0.20 and 0.30, yielding Vp/Vs values of about 1.63 to 1.87. The theoretical minimum for a stable elastic solid is √2 ≈ 1.414 (when ν = 0), and values approaching infinity occur as ν approaches 0.5 — the condition of a fluid, which has zero shear modulus and therefore zero S-wave velocity. This is why the Vp/Vs ratio is so sensitive to fluids.

The practical diagnostic power shows up clearly in **fluid detection**. Dry sandstone might have Vp/Vs ≈ 1.6–1.7. Saturate the same rock with water, and Vp increases (because water's bulk modulus adds to the rock frame's resistance to compression) while Vs barely changes (because water has no shear strength), pushing Vp/Vs above 1.9 or even 2.0. Replace the water with gas, and Vp drops sharply (gas is highly compressible) while Vs remains nearly the same — Vp/Vs may fall below 1.6. This is why seismic interpreters in hydrocarbon exploration watch Vp/Vs closely: a zone with anomalously low Vp/Vs in a sandstone reservoir is a strong indicator of gas saturation.

Beyond fluids, Vp/Vs varies systematically with **lithology and composition**. Quartz-rich rocks (sandstones, quartzites) tend to have lower ratios (~1.6–1.7) because quartz has an unusually low Poisson's ratio. Carbonate rocks (limestones, dolomites) cluster around 1.8–1.9. Mafic igneous rocks and clay-rich shales push higher, often above 1.8. At crustal and mantle scales, Vp/Vs helps distinguish between felsic and mafic compositions — a valuable constraint when direct rock sampling is impossible. The key advantage of the ratio over absolute velocities is that it **cancels out the dominant effect of pressure**: both Vp and Vs increase with confining pressure at similar rates, so their ratio remains relatively stable, isolating the effects of composition and fluid content from the effect of burial depth.
