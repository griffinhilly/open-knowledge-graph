---
id: crustal-thickness-determination-gravity
title: Determining Crustal Thickness from Gravity Data
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: gravity-anomaly-separation-residual-regional
  type: hard
- id: airy-isostasy-model
  type: hard
builds-toward:
- lithosphere-thickness-and-age
tags:
- gravity
- crustal-structure
- inversion
stage: advanced
status: draft
---

# Determining Crustal Thickness from Gravity Data

## Core Idea
Regional gravity anomalies primarily reflect variations in crustal thickness and density. Using isostatic assumptions and the gravity effect of the crustal/mantle density contrast at the Mohorovičić discontinuity, crustal thickness can be inverted from Bouguer gravity anomalies. This method is especially valuable in continental regions where seismic Moho observations are sparse.

## Explainer

You already know from gravity anomaly separation that a measured gravity field contains contributions from sources at every depth, and that filtering techniques can isolate the regional component — the broad, long-wavelength signal produced by deep structure. You also know from the Airy isostasy model that mountains are supported by deep crustal roots: thicker crust beneath high topography, thinner crust beneath ocean basins. The method covered here connects these two ideas — it uses the regional gravity field to estimate how thick the crust is at any point.

The key physical insight is that the **Mohorovičić discontinuity** (Moho) — the boundary between crust and mantle — represents a sharp density contrast, typically around 400–600 kg/m³. Where the crust is thick, there is more low-density crustal rock replacing high-density mantle rock, producing a negative Bouguer gravity anomaly. Where the crust is thin, mantle rock sits closer to the surface, producing a less negative or even positive anomaly. This predictable relationship between Bouguer anomaly and Moho depth is the foundation of gravity-based crustal thickness estimation.

The simplest inversion approach assumes a uniform crustal density and a known density contrast at the Moho, then solves for the Moho depth that would produce the observed gravity anomaly at each point. In practice, this is done using **Parker's method**, which relates the Fourier transform of the gravity anomaly to the Fourier transform of the Moho topography through the density contrast. The calculation is iterative: you start with an initial Moho depth estimate (often from isostatic assumptions), compute the predicted gravity, compare it to the observed gravity, and adjust the Moho depth until the misfit is acceptably small.

This technique is especially powerful in places where seismic refraction surveys — the gold-standard method for measuring Moho depth — are impractical or too expensive. Satellite gravity missions like GRACE and GOCE now provide global gravity coverage, enabling crustal thickness maps even for remote continental interiors, ice-covered regions like Antarctica, and ocean basins. The trade-off is resolution: gravity data alone cannot resolve sharp lateral changes in Moho depth as precisely as seismic data, because the gravity field smooths out with distance from the source. The best results come from jointly interpreting gravity-derived Moho maps with the sparse seismic control points that do exist, using the seismic data to calibrate the density contrast and reference depth assumed in the gravity inversion.
