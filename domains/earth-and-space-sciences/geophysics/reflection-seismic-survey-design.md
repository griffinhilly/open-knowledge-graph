---
id: reflection-seismic-survey-design
title: Reflection Seismic Survey Design and Acquisition
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: seismic-ray-tracing-methods
  type: hard
- id: potential-field-methods-gravity-magnetics
  type: soft
builds-toward:
- seismic-data-processing-and-filtering
- seismic-migration-techniques
tags:
- seismic
- survey-design
- reflection
- acquisition
stage: advanced
status: draft
---

# Reflection Seismic Survey Design and Acquisition

## Core Idea
Reflection seismic surveys use arrays of sources and receivers to record reflections from subsurface interfaces. Survey parameters such as source-receiver distance, receiver spacing, and line direction must be chosen based on target depth, expected reflection geometry, and spatial resolution requirements. Common-midpoint (CMP) gathers organize the data to enhance signals and suppress noise.

## Explainer

From seismic ray tracing, you understand how seismic waves travel through layered media, reflecting and refracting at interfaces where acoustic impedance changes. A **reflection seismic survey** applies this physics systematically: you generate seismic waves at the surface, record the echoes that bounce off subsurface layers, and use the timing and amplitude of those reflections to build an image of the geology below. The challenge is designing the survey so that the recorded data actually contain the information you need — and this is where survey design becomes critical.

The fundamental geometry involves a **source** (an explosive charge, vibrator truck, or air gun) and an array of **receivers** (geophones on land, hydrophones at sea) laid out along a line or across a grid. Each source activation produces a **shot gather** — a collection of traces recorded at different offsets (source-receiver distances). Short offsets record near-vertical reflections and are most sensitive to shallow, flat-lying layers. Long offsets capture wide-angle reflections that carry information about velocities and deeper structures but are also contaminated by surface waves and refractions. The maximum offset, receiver spacing, and source interval must be chosen to match the target: deeper targets require longer offsets and more powerful sources, while resolving thin layers or small faults demands closer receiver spacing to capture high spatial frequencies.

The key organizational concept is the **common-midpoint (CMP) gather**. Multiple source-receiver pairs share the same midpoint on the surface, meaning their reflections sample approximately the same subsurface point but at different angles. Stacking (summing) these traces after correcting for the extra travel time at longer offsets — the **normal moveout (NMO) correction** — reinforces coherent reflections while canceling random noise, dramatically improving the signal-to-noise ratio. The number of traces that contribute to each CMP is the **fold**; higher fold means more noise suppression but requires more sources and receivers, increasing cost. A typical exploration survey might aim for 60- to 120-fold coverage.

Survey design also involves practical trade-offs between resolution, coverage, cost, and logistics. **Spatial aliasing** occurs when the receiver spacing is too coarse to sample steeply dipping events — the Nyquist criterion requires at least two samples per wavelength of the steepest event. **3D surveys** extend coverage from lines to grids, using multiple parallel receiver lines and source lines to capture reflections from all azimuths, essential for imaging complex structures like salt bodies or fault networks. The design process typically begins with synthetic modeling: ray tracing or wave-equation simulations through an expected geological model predict what the recorded data should look like, allowing the geophysicist to optimize parameters before deploying expensive field equipment.
