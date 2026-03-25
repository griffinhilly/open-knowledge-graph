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
- id: seismic-ray-theory
  type: soft
- id: subduction-zone-seismic-structure
  type: soft
builds-toward:
- seismic-interpretation-structural-mapping
tags:
- seismic
- migration
- imaging
- depth-conversion
stage: expert
status: validated
---
# Seismic Migration and Depth Imaging

## Core Idea
Seismic migration repositions reflected events to their true subsurface locations by accounting for dipping layers and velocity variations. Time migration assumes constant velocity, while depth migration uses accurate velocity models to correct for lateral velocity changes. Modern pre-stack depth migration (PSDM) produces depth-converted images essential for exploration and accurate structural interpretation.

## Questions

```yaml
- question: "An unmigrated seismic section shows a reflector with an apparent dip of 15°. After applying migration, the same reflector appears to dip at 28° and is shifted laterally. What does this indicate?"
  type: multiple-choice
  options:
    - "Migration introduced an error — it should have flattened the reflector, not steepened it"
    - "The true reflector is steeper than it appeared; migration moved it updip to its correct subsurface position"
    - "The stacking velocity model was too slow, causing over-migration of the reflector"
    - "The reflector was a multiple reflection that migration correctly removed from the section"
  answer: 1
  explanation: "Unmigrated dipping reflectors always appear with shallower dip and displaced in the downdip direction compared to their true position. Migration moves them updip toward the true location and restores the correct (steeper) dip. Seeing a steeper reflector after migration is exactly the expected result for a genuinely dipping interface — the migrated section is more accurate, not erroneous."

- question: "Why is pre-stack depth migration (PSDM) required for reliable imaging beneath a salt body, whereas post-stack time migration would fail?"
  type: multiple-choice
  options:
    - "Salt bodies absorb seismic energy completely, so only PSDM's higher energy input can generate reflections beneath them"
    - "Salt has very different seismic velocity from surrounding sediments, creating strong lateral velocity variation that violates the assumptions of time migration"
    - "Post-stack time migration cannot handle more than one reflection per trace, and salt creates multiple reflections"
    - "PSDM uses a denser acquisition grid that is only economically justified beneath high-value salt plays"
  answer: 1
  explanation: "Time migration assumes velocities vary only vertically — a 1D velocity model. Salt bodies have P-wave velocities (~4480 m/s) nearly twice those of surrounding sediments (~2000–2500 m/s), causing rays to refract strongly at the salt flanks and base. This lateral velocity variation bends ray paths in ways that a 1D velocity function cannot predict. Depth migration uses a full 2D or 3D velocity model to trace rays accurately through the salt geometry, producing correctly positioned subsalt images."

- question: "Diffraction hyperbolas on an unmigrated seismic section indicate that the subsurface contains curved or dome-shaped reflective interfaces."
  type: true-false
  answer: false
  explanation: "False. Diffraction hyperbolas arise from point scatterers — fault tips, pinch-outs, fractures, or any abrupt lateral discontinuity — not from curved surfaces. When a wave hits a point scatterer, it diffracts energy in all directions; receivers at varying offsets record this energy at different travel times, producing the characteristic hyperbolic pattern. Migration collapses these hyperbolas back to the point where the scatterer is actually located. A curved reflector would produce a more complex pattern, not a simple hyperbola."

- question: "Time migration is less accurate than depth migration when subsurface geology involves significant lateral velocity variation."
  type: true-false
  answer: true
  explanation: "True. Time migration uses stacking velocities that vary with depth but not laterally — a 1D velocity function. This works well when layers are flat and velocity contrasts are mild. But in structurally complex areas (salt bodies, overthrust belts, steep dips), seismic rays bend laterally through the velocity field in ways a 1D model cannot capture. Depth migration uses a full 3D velocity model, tracing rays accurately through lateral velocity contrasts to position reflectors correctly in depth."

- question: "Why does an unmigrated seismic section misrepresent the true positions of subsurface reflectors, and what information does migration use to correct this?"
  type: short-answer
  answer: "An unmigrated section plots each reflection at the midpoint between source and receiver at the recorded two-way travel time. For dipping reflectors, the actual reflection point is laterally offset from that midpoint (shifted updip), so the reflector appears at the wrong position and with the wrong (shallower) dip. Migration corrects this by tracing each recorded reflection backward through a velocity model — using the known wave speed — to determine where the reflecting surface must actually be, repositioning events to their true subsurface locations."
  explanation: "The velocity model is the critical input: an accurate model produces a correctly migrated image; a wrong model produces a migrated image that is still incorrect, just differently so. This is why velocity model building (often through tomographic analysis) is the most labor-intensive part of modern seismic processing — the migration output is only as good as the velocity model fed into it."
```

## Explainer

After seismic data have been acquired and processed — noise removed, amplitudes corrected, traces stacked — you have a seismic section that shows reflections plotted against two-way travel time and surface position. But this image is not a faithful picture of the subsurface. Reflections from dipping layers appear displaced in the down-dip direction, diffraction hyperbolas spread energy from point scatterers (faults, pinch-outs) across the section, and the vertical axis is time rather than depth. **Seismic migration** is the processing step that corrects these distortions, collapsing diffractions to points, moving dipping reflectors to their true positions, and — in depth migration — converting the vertical axis to true depth.

The simplest way to understand migration is geometrically. When a wave reflects off a dipping surface, the reflection point is not directly below the midpoint between source and receiver — it is shifted up-dip. On an unmigrated section, the reflector therefore appears at the wrong lateral position and with the wrong dip (too shallow). Migration corrects this by tracing each recorded reflection backward through the velocity model to find where the reflecting surface must actually be. **Diffraction hyperbolas** provide the clearest illustration: a point scatterer produces a hyperbolic pattern on the unmigrated section because receivers at different offsets record the same reflection at different travel times. Migration collapses this hyperbola back to a point, concentrating the energy where it belongs.

**Time migration** assumes that velocities vary vertically but not laterally — a reasonable approximation when layers are fairly flat and velocity contrasts are mild. It uses the stacking velocity (derived from NMO analysis you learned in data processing) and works well for gentle structures. But when the geology involves strong lateral velocity variations — salt bodies, overthrust belts, steep dips — time migration breaks down because rays bend laterally through the velocity field in ways that a 1D velocity function cannot capture. **Depth migration** uses a full 2D or 3D velocity model to trace rays or propagate wavefields accurately through complex structure, producing an output in depth rather than time.

The most powerful modern approach is **pre-stack depth migration (PSDM)**, which migrates individual traces before stacking rather than migrating the stacked section. This matters because stacking implicitly assumes flat layers and mild lateral velocity variation — the same assumptions that depth migration is designed to overcome. PSDM handles all offsets independently, honoring the true ray paths for each source-receiver pair, and produces the most accurate images in complex geological settings. The trade-off is computational cost: PSDM requires an accurate velocity model (often built iteratively through **tomographic velocity analysis**) and vastly more processing power than post-stack time migration. But for exploration targets beneath salt, in fold-and-thrust belts, or anywhere the geology is structurally complex, PSDM is now the standard.
