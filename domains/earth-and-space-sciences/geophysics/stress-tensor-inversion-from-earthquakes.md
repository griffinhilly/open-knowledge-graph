---
id: stress-tensor-inversion-from-earthquakes
title: Stress Tensor Inversion from Focal Mechanisms
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: focal-mechanisms-and-stress-tensors
  type: hard
- id: moment-tensor-inversion
  type: hard
builds-toward:
- coulomb-stress-transfer-faults
tags:
- seismic
- stress
- inversion
- focal-mechanisms
stage: advanced
status: draft
---

# Stress Tensor Inversion from Focal Mechanisms

## Core Idea
Focal mechanisms from earthquake populations can be inverted to determine the regional stress tensor (principal stress orientations and relative magnitudes). Methods like the Michael method assume earthquakes occur on planes optimally oriented for slip given the stress state. Stress tensors inferred from seismicity illuminate plate boundary mechanics and lithospheric stress states.

## Explainer

From your work with focal mechanisms, you know that each earthquake's radiation pattern reveals the geometry of faulting — the orientation of the fault plane and the direction of slip. From moment tensor inversion, you know how to extract this information from seismic waveforms. **Stress tensor inversion** asks the inverse question: given many earthquakes, each with its own focal mechanism, what single stress field could have caused all of them to slip the way they did?

The physical foundation is the **Wallace-Bott hypothesis**: slip on a fault occurs in the direction of maximum resolved shear stress on that fault plane. Imagine you have a regional stress field — three principal stress axes (σ₁ > σ₂ > σ₃) with fixed orientations. Any fault plane sitting in this stress field will experience a shear traction that points in a specific direction on that plane, determined by the fault's orientation relative to the stress axes. The Wallace-Bott assumption says the earthquake slip vector should parallel this shear traction direction. So each focal mechanism is an observation of the shear traction direction on one particular fault plane, and the collection of many such observations constrains the stress tensor that generated them all.

The **Michael (1984) method** is the most widely used approach. It formulates the problem as a linear inverse problem: given N focal mechanisms (each providing a fault plane orientation and a slip direction), find the four parameters that define the reduced stress tensor — the orientations of σ₁, σ₂, and σ₃ plus the **stress ratio** R = (σ₂ − σ₃)/(σ₁ − σ₃). Note that the inversion cannot determine absolute stress magnitudes, only the principal directions and the relative shape of the stress ellipsoid. The method minimizes the angular misfit between the observed slip directions and those predicted by the best-fitting stress tensor. Because each focal mechanism has a fault-plane ambiguity (two nodal planes, only one of which actually slipped), the algorithm must either try both planes or use external information to select the correct one.

Robustness testing is essential because real focal mechanism catalogs contain errors and may span regions with non-uniform stress. **Bootstrap resampling** randomly resamples the catalog thousands of times, solving the inversion each time, and the scatter in results reveals confidence intervals on the principal stress orientations. If the bootstrap solutions cluster tightly, the stress tensor is well resolved. If they scatter broadly, the data may be too noisy, too few, or the region may contain multiple stress domains that need to be analyzed separately. Some advanced methods (like the Hardebeck and Michael 2006 approach) allow the stress field to vary spatially, solving for a smoothly varying stress tensor on a grid — a damped inversion that balances spatial resolution against data constraints.

The practical payoff is substantial. Stress tensor inversions reveal the tectonic forces driving seismicity: compressional, extensional, or strike-slip regimes become quantitatively characterized. Changes in stress orientation across fault systems, with depth, or over time (before and after large earthquakes) illuminate how the lithosphere partitions and transfers stress. These results feed directly into **Coulomb stress transfer models** that forecast where future earthquakes are more likely — making stress inversion a bridge between observational seismology and seismic hazard assessment.
