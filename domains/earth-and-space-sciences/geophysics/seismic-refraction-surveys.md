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
status: draft
---

# Seismic Refraction Surveys and Interpretation

## Core Idea
Seismic refraction surveys image subsurface layering using refracted waves that travel along velocity boundaries. The critical angle determines when waves refract back to the surface, allowing velocity-depth relationships to be inverted from travel-time curves.

## How It's Best Learned
Work through examples of calculating critical angles and forward-modeling arrival times. Practice interpreting synthetic time-distance curves for multi-layer models.

## Common Misconceptions
- Assuming refraction only occurs at horizontal boundaries; refracted waves occur at any velocity increase. - Confusing the refracted wave with the reflected wave; refracted waves travel along the boundary, not through the layer above.

## Explainer

From your understanding of seismic waves and elastic wave propagation, you know that P-waves and S-waves travel through rock at velocities determined by the material's elastic properties and density, and that when a wave hits a boundary between materials with different velocities, it can reflect, refract, or both. A **seismic refraction survey** is a field technique that exploits refracted waves — specifically head waves that travel along subsurface velocity boundaries — to determine the depth and velocity of subsurface layers.

The setup is straightforward: a seismic source (a sledgehammer for shallow work, explosives or a vibroseis truck for deeper targets) generates waves at one end of a line of **geophones** (ground-motion sensors) spaced at regular intervals along the surface. Each geophone records the arrival time of the first seismic energy to reach it. At short distances from the source, the first arrival is the **direct wave**, traveling straight through the uppermost layer at velocity V₁. At greater distances, the first arrival is a **refracted wave** (head wave) that traveled down to a deeper, faster layer at velocity V₂, raced along the interface at V₂, and returned to the surface. The crossover distance — where the refracted wave overtakes the direct wave — depends on the layer velocities and the depth to the interface.

The primary interpretation tool is the **travel-time curve**: a plot of first-arrival time versus source-receiver distance. For a simple two-layer case, this plot shows two straight-line segments. The first segment, from the direct wave, has slope 1/V₁. The second segment, from the refracted wave, has a shallower slope 1/V₂ (since V₂ > V₁). The velocity of each layer is read directly from the slope, and the depth to the interface is calculated from the **intercept time** — where the refracted-wave line, extrapolated back, crosses the time axis. For multiple layers, each producing its own head wave, the travel-time curve has additional segments with progressively shallower slopes, and a layer-stripping procedure recovers the thickness and velocity of each layer in sequence.

Real surveys go beyond this simple picture. **Reversed shooting** — firing sources from both ends of the geophone line — is essential for detecting dipping layers, which cause the forward and reverse travel-time slopes to differ. The **plus-minus method** and **generalized reciprocal method (GRM)** handle irregular interfaces by using travel times from reciprocal shot points to map undulating boundary topography. Refraction surveys excel at determining velocity structure and depth to bedrock in engineering and environmental investigations, and at imaging crustal-scale layering in academic studies, though they require that velocity increases with depth — a hidden layer (a low-velocity zone sandwiched between faster layers) produces no head wave and can go undetected, which is the method's most important limitation.
