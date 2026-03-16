---
id: seismic-migration-techniques
title: Seismic Migration and Depth Imaging
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: seismic-data-processing-and-filtering
  type: hard
- id: seismic-velocity-depth-models
  type: hard
builds-toward:
- seismic-interpretation-structural-mapping
tags:
- seismic
- migration
- imaging
- depth-conversion
stage: advanced
status: draft
---

# Seismic Migration and Depth Imaging

## Core Idea
Seismic migration repositions reflected events to their true subsurface locations by accounting for dipping layers and velocity variations. Time migration assumes constant velocity, while depth migration uses accurate velocity models to correct for lateral velocity changes. Modern pre-stack depth migration (PSDM) produces depth-converted images essential for exploration and accurate structural interpretation.

## Explainer

After seismic data have been acquired and processed — noise removed, amplitudes corrected, traces stacked — you have a seismic section that shows reflections plotted against two-way travel time and surface position. But this image is not a faithful picture of the subsurface. Reflections from dipping layers appear displaced in the down-dip direction, diffraction hyperbolas spread energy from point scatterers (faults, pinch-outs) across the section, and the vertical axis is time rather than depth. **Seismic migration** is the processing step that corrects these distortions, collapsing diffractions to points, moving dipping reflectors to their true positions, and — in depth migration — converting the vertical axis to true depth.

The simplest way to understand migration is geometrically. When a wave reflects off a dipping surface, the reflection point is not directly below the midpoint between source and receiver — it is shifted up-dip. On an unmigrated section, the reflector therefore appears at the wrong lateral position and with the wrong dip (too shallow). Migration corrects this by tracing each recorded reflection backward through the velocity model to find where the reflecting surface must actually be. **Diffraction hyperbolas** provide the clearest illustration: a point scatterer produces a hyperbolic pattern on the unmigrated section because receivers at different offsets record the same reflection at different travel times. Migration collapses this hyperbola back to a point, concentrating the energy where it belongs.

**Time migration** assumes that velocities vary vertically but not laterally — a reasonable approximation when layers are fairly flat and velocity contrasts are mild. It uses the stacking velocity (derived from NMO analysis you learned in data processing) and works well for gentle structures. But when the geology involves strong lateral velocity variations — salt bodies, overthrust belts, steep dips — time migration breaks down because rays bend laterally through the velocity field in ways that a 1D velocity function cannot capture. **Depth migration** uses a full 2D or 3D velocity model to trace rays or propagate wavefields accurately through complex structure, producing an output in depth rather than time.

The most powerful modern approach is **pre-stack depth migration (PSDM)**, which migrates individual traces before stacking rather than migrating the stacked section. This matters because stacking implicitly assumes flat layers and mild lateral velocity variation — the same assumptions that depth migration is designed to overcome. PSDM handles all offsets independently, honoring the true ray paths for each source-receiver pair, and produces the most accurate images in complex geological settings. The trade-off is computational cost: PSDM requires an accurate velocity model (often built iteratively through **tomographic velocity analysis**) and vastly more processing power than post-stack time migration. But for exploration targets beneath salt, in fold-and-thrust belts, or anywhere the geology is structurally complex, PSDM is now the standard.
