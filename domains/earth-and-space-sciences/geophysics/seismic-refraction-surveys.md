---
id: seismic-refraction-surveys
title: Seismic Refraction Surveys and Interpretation
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: seismic-waves
  type: hard
- id: elastic-wave-propagation-in-solids
  type: hard
builds-toward:
- seismic-reflection-surveys
- near-surface-geophysics-methods
tags:
- seismic
- survey
- refraction
- velocity
stage: advanced
status: validated
---

# Seismic Refraction Surveys and Interpretation

## Core Idea
Seismic refraction surveys image subsurface layering using refracted waves that travel along velocity boundaries. The critical angle determines when waves refract back to the surface, allowing velocity-depth relationships to be inverted from travel-time curves.

## How It's Best Learned
Work through examples of calculating critical angles and forward-modeling arrival times. Practice interpreting synthetic time-distance curves for multi-layer models.

## Common Misconceptions
- Assuming refraction only occurs at horizontal boundaries; refracted waves occur at any velocity increase. - Confusing the refracted wave with the reflected wave; refracted waves travel along the boundary, not through the layer above.

## Questions

```yaml
- question: "A seismic refraction survey produces a travel-time curve with two straight-line segments. The first segment has slope 1/500 s/m, and the second has slope 1/2000 s/m. What do these two segments represent?"
  type: multiple-choice
  options:
    - "The first segment is the reflected wave off the top of the lower layer; the second is the refracted wave returning through the upper layer"
    - "The first segment is the direct wave traveling through the upper layer at V₁ = 500 m/s; the second is the head wave (refracted wave) that traveled along the faster lower-layer boundary at V₂ = 2000 m/s"
    - "Both segments are direct waves — the first through soil, the second through bedrock — and no refraction is occurring"
    - "The first segment is the P-wave arrival; the second is the S-wave arrival at a slower apparent velocity"
  answer: 1
  explanation: "In a refraction travel-time curve, the slope of each segment equals 1/V for that wave type. The first arrivals at short source-receiver offsets are direct waves through the upper layer — slope = 1/V₁ = 1/500, so V₁ = 500 m/s. At greater offsets, refracted head waves that traveled along the faster layer overtake the direct wave — their shallower slope 1/V₂ = 1/2000 gives V₂ = 2000 m/s. The velocity of each layer is read from slopes; layer depth is calculated from the intercept time where the refracted-wave line extrapolates back to zero offset."

- question: "A geologist conducts a refraction survey searching for a buried soft-clay layer sandwiched between two harder, faster rock layers. Despite careful fieldwork, the survey reveals only two straight-line segments. Why might the clay layer be invisible?"
  type: multiple-choice
  options:
    - "The clay layer is too thin to produce a detectable head wave at the geophone spacing used"
    - "Refracted head waves only form when seismic velocity increases across a boundary; the clay has lower velocity than the overlying rock, so no head wave forms at its upper surface — it is a hidden low-velocity zone"
    - "Soft materials like clay absorb seismic energy completely before it can return to the surface"
    - "The clay layer would only be detected with S-waves, not P-waves"
  answer: 1
  explanation: "This is the fundamental limitation of seismic refraction: it requires velocity to increase with depth to generate head waves at each boundary. A head wave forms when the incident ray hits the boundary at the critical angle — which only exists when the lower layer is faster. If the clay (low velocity) is sandwiched between faster rocks, the lower boundary (clay-to-fast rock) does produce a head wave, but the upper boundary (fast rock-to-slow clay) does not. The clay layer goes undetected — it is a 'hidden layer' or low-velocity zone. Surveyors must consider this possibility when interpreting refraction data."

- question: "In a seismic refraction survey, the velocity of each subsurface layer can be determined directly from the slope of the corresponding travel-time segment without knowing the layer depths."
  type: true-false
  answer: true
  explanation: "Layer velocity is encoded in the slope of the travel-time segment: slope = 1/V, so V = 1/slope. This is independent of layer depth. The depth to each interface is then calculated separately using the intercept time — where the refracted-wave line, extrapolated back to zero source-receiver offset, crosses the time axis. This separation of velocity determination (from slope) and depth determination (from intercept) is what makes refraction surveys analytically tractable: you can extract velocities and depths sequentially using a layer-stripping approach."

- question: "A seismic refraction survey can detect any subsurface boundary, regardless of whether velocity increases or decreases across it."
  type: true-false
  answer: false
  explanation: "Refraction surveys require velocity to increase with depth across each boundary to generate detectable head waves. When a seismic wave hits a boundary at the critical angle, a head wave travels along the boundary in the faster lower medium and continuously radiates energy back upward into the slower upper layer. If the lower layer is slower than the upper layer, no critical angle exists — the wave is refracted downward away from the boundary rather than along it, and no head wave returns to the surface. Low-velocity zones sandwiched between faster layers are therefore invisible to refraction methods, which is the technique's most important limitation."

- question: "Explain why seismic refraction surveys require that velocity increases with depth at each layer boundary, and describe what happens to seismic energy that encounters a boundary where the lower layer is slower."
  type: short-answer
  answer: "A refracted head wave forms only when a seismic ray hits the boundary at the critical angle (sin θ_c = V₁/V₂). This angle exists only when V₂ > V₁ — the lower layer must be faster. When the ray hits at this angle, it travels along the boundary at V₂, continuously shedding energy back upward at angle θ_c to reach the surface at progressively greater distances. If V₂ < V₁, Snell's law predicts no critical angle exists: the transmitted ray always bends away from vertical rather than along the boundary. Energy is transmitted into the lower layer (and partly reflected), but no wave propagates along the interface and returns to the surface. The boundary is therefore acoustically invisible to refraction methods. This is why a slow layer (e.g., clay, weathered rock) between two faster layers creates a 'hidden layer' that refraction surveys cannot resolve."
  explanation: "Understanding this limitation is essential for correct interpretation of refraction data. A two-segment travel-time curve that appears to show only two layers may actually be hiding intermediate slow layers. Surveys in areas with potential velocity inversions require complementary methods — seismic reflection, borehole measurements, or gravity surveys — to avoid missing critical subsurface features."
```

## Explainer

From your understanding of seismic waves and elastic wave propagation, you know that P-waves and S-waves travel through rock at velocities determined by the material's elastic properties and density, and that when a wave hits a boundary between materials with different velocities, it can reflect, refract, or both. A **seismic refraction survey** is a field technique that exploits refracted waves — specifically head waves that travel along subsurface velocity boundaries — to determine the depth and velocity of subsurface layers.

The setup is straightforward: a seismic source (a sledgehammer for shallow work, explosives or a vibroseis truck for deeper targets) generates waves at one end of a line of **geophones** (ground-motion sensors) spaced at regular intervals along the surface. Each geophone records the arrival time of the first seismic energy to reach it. At short distances from the source, the first arrival is the **direct wave**, traveling straight through the uppermost layer at velocity V₁. At greater distances, the first arrival is a **refracted wave** (head wave) that traveled down to a deeper, faster layer at velocity V₂, raced along the interface at V₂, and returned to the surface. The crossover distance — where the refracted wave overtakes the direct wave — depends on the layer velocities and the depth to the interface.

The primary interpretation tool is the **travel-time curve**: a plot of first-arrival time versus source-receiver distance. For a simple two-layer case, this plot shows two straight-line segments. The first segment, from the direct wave, has slope 1/V₁. The second segment, from the refracted wave, has a shallower slope 1/V₂ (since V₂ > V₁). The velocity of each layer is read directly from the slope, and the depth to the interface is calculated from the **intercept time** — where the refracted-wave line, extrapolated back, crosses the time axis. For multiple layers, each producing its own head wave, the travel-time curve has additional segments with progressively shallower slopes, and a layer-stripping procedure recovers the thickness and velocity of each layer in sequence.

Real surveys go beyond this simple picture. **Reversed shooting** — firing sources from both ends of the geophone line — is essential for detecting dipping layers, which cause the forward and reverse travel-time slopes to differ. The **plus-minus method** and **generalized reciprocal method (GRM)** handle irregular interfaces by using travel times from reciprocal shot points to map undulating boundary topography. Refraction surveys excel at determining velocity structure and depth to bedrock in engineering and environmental investigations, and at imaging crustal-scale layering in academic studies, though they require that velocity increases with depth — a hidden layer (a low-velocity zone sandwiched between faster layers) produces no head wave and can go undetected, which is the method's most important limitation.
