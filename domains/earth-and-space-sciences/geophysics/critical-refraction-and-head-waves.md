---
id: critical-refraction-and-head-waves
title: Critical Angle Refraction and Head Waves
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: seismic-ray-tracing-methods
  type: hard
builds-toward:
- reflection-seismic-survey-design
tags:
- seismic
- refraction
- head-waves
- critical-angle
stage: advanced
status: draft
---

# Critical Angle Refraction and Head Waves

## Core Idea
When a seismic ray encounters a velocity increase at a boundary, it reaches a critical angle of incidence beyond which total internal reflection occurs. At the critical angle, refracted waves travel horizontally along the interface and generate head waves that arrive at large distances before direct rays. Head waves provide important constraints on velocity structure and are widely used in refraction seismic surveys.

## Explainer

From seismic ray tracing, you know that a seismic wave crossing a boundary between two layers bends according to Snell's law: sin(θ₁)/V₁ = sin(θ₂)/V₂, where θ is the angle of incidence or refraction and V is the wave velocity in each layer. When V₂ > V₁ — the deeper layer is faster — the refracted ray bends away from the normal. As the incidence angle increases, the refracted angle grows faster. At one specific angle, called the **critical angle** (θ_c = arcsin(V₁/V₂)), the refracted ray bends to exactly 90° and travels horizontally along the interface between the two layers.

This horizontally traveling wave is the key to the whole phenomenon. As it races along the top of the faster layer at velocity V₂, it continuously radiates energy back upward into the slower layer at the critical angle — like a boat creating a wake. These upward-radiating waves are called **head waves** (sometimes called refraction arrivals or conical waves). They propagate back to the surface where geophones can record them. The geometry is distinctive: the ray goes down at the critical angle, runs along the interface, and comes back up at the critical angle, forming a characteristic "V" path with a horizontal segment.

The practical importance of head waves becomes clear when you consider travel times. The direct wave travels straight from source to receiver through the slower upper layer at velocity V₁. The head wave takes a longer path — down, along, and back up — but the horizontal segment travels at the faster velocity V₂. At short source-receiver distances, the direct wave arrives first because its path is shorter. But beyond a certain distance called the **crossover distance**, the head wave overtakes the direct wave because its speed advantage along the interface more than compensates for the extra path length. On a time-distance plot, the direct arrival forms a line with slope 1/V₁, while the head wave arrival forms a line with slope 1/V₂ (shallower, since V₂ > V₁). The intercept time of the head-wave line encodes the depth to the interface.

This is why head waves are so valuable in exploration and crustal geophysics: the slope of the refraction arrival directly gives the velocity of the deeper layer, and the intercept time gives the layer depth. For a simple two-layer case, the math is straightforward. For multiple layers, each velocity boundary produces its own head wave, and the travel-time curve becomes a series of line segments with progressively shallower slopes — each segment revealing the velocity of a deeper layer. The entire framework of seismic refraction surveying is built on detecting and interpreting these arrivals.
