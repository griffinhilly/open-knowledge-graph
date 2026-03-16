---
id: earthquake-stress-inversion
title: Stress Inversion and Focal Mechanism Analysis
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: focal-mechanisms-and-stress-tensors
  type: hard
- id: moment-tensor-inversion
  type: hard
tags:
- earthquake
- stress
- inversion
- focal-mechanism
stage: advanced
status: draft
---

# Stress Inversion and Focal Mechanism Analysis

## Core Idea
Focal mechanisms from earthquake catalogs can be inverted for the regional stress tensor. Bootstrap and other statistical methods test solution robustness, and results reveal principal stress directions and magnitudes controlling seismicity.

## Explainer

You already know that a focal mechanism describes the geometry of fault slip for a single earthquake — the orientation of the fault plane, the direction of slip, and the pattern of compressional and dilatational first motions. You also know that moment tensor inversion recovers the full seismic source tensor from waveform data. **Stress inversion** takes the next step: given a collection of focal mechanisms from many earthquakes in a region, what is the underlying stress field that produced all of them?

The key insight is that a single focal mechanism cannot uniquely determine the stress tensor. Each focal mechanism has an inherent ambiguity (the fault plane vs. the auxiliary plane), and even if you knew which plane slipped, infinitely many stress states could have produced that particular slip direction. But when you have dozens or hundreds of focal mechanisms from a region, the problem becomes overdetermined. The assumption is that all these earthquakes occurred under the same regional stress field, and that slip on each fault was in the direction of maximum resolved shear stress on that plane. This is called the **Wallace-Bott hypothesis** — faults slip in the direction that the tectonic stress pushes them, not in some arbitrary direction.

The inversion algorithm searches for the stress tensor (specifically, the orientations of the three **principal stresses** σ₁, σ₂, σ₃ and the **stress ratio** R = (σ₂ − σ₃)/(σ₁ − σ₃)) that best predicts the observed slip directions across all focal mechanisms. The stress ratio R captures the shape of the stress ellipsoid — whether the intermediate stress is closer to the maximum or the minimum. Methods like the **Michael (1984) linear inversion** solve this efficiently by linearizing the relationship between the stress tensor and predicted slip vectors, then minimizing the angular misfit between predicted and observed slip directions across the earthquake population.

Because real data contain measurement errors and the regional stress assumption may not hold perfectly, statistical testing is essential. **Bootstrap resampling** — repeatedly solving the inversion on random subsets of the focal mechanism catalog — reveals how stable the solution is. Tight clustering of bootstrap results means the stress tensor is well constrained; a scattered distribution warns that the data may be insufficient or that multiple stress regimes are mixed in the catalog. Practitioners also check whether systematic misfits correlate with spatial location, which can indicate that the region should be subdivided into zones with distinct stress states.

The results have direct tectonic significance. The orientation of σ₁ (maximum compressive stress) reveals the direction of tectonic loading — perpendicular to a subduction trench, parallel to a transform fault, or radial to a rift zone. Changes in stress orientation with depth or across fault boundaries illuminate how stress is partitioned in the lithosphere. Stress inversion results are also essential inputs for Coulomb stress transfer calculations, which model how one earthquake changes the stress state on neighboring faults and helps forecast where future seismicity is most likely.
