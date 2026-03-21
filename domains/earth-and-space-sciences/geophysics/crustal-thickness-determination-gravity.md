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

## Questions

```yaml
- question: "A regional gravity survey over a major mountain range shows strongly negative Bouguer anomalies beneath the highest peaks. A student attributes this to the large mass of rock in the mountains themselves. What does the negative anomaly actually indicate?"
  type: multiple-choice
  options:
    - "The mountain rocks are unusually low density compared to surrounding crust"
    - "A thick crustal root beneath the mountains — low-density crustal material at depth is replacing what would otherwise be denser mantle rock, producing a mass deficit"
    - "A sedimentary basin hidden beneath the mountains, filled with low-density material"
    - "The absence of volcanic intrusions that would otherwise add dense material to the crust"
  answer: 1
  explanation: "The student's intuition is backwards. Mountains have a positive topographic mass (extra rock above sea level), which would naively suggest a positive gravity anomaly. But the Bouguer correction removes the effect of topography, and what remains — the Bouguer anomaly — reflects subsurface density variations. The strongly negative residual after Bouguer correction indicates a mass deficit at depth: a thick crustal root where low-density crust (≈2800 kg/m³) extends downward into the mantle, displacing denser mantle material (≈3300 kg/m³). This is exactly the Airy isostasy model — mountains are 'floating' on roots, and those roots are what create the negative Bouguer anomaly."

- question: "Why does gravity-based crustal thickness estimation produce lower-resolution Moho maps than seismic refraction surveys, even when both cover the same area?"
  type: multiple-choice
  options:
    - "Gravity instruments are inherently less precise than seismometers and introduce more measurement noise"
    - "The gravity field smooths out with distance from its source, so sharp lateral changes in Moho depth are blurred and cannot be resolved accurately from surface measurements alone"
    - "The Moho density contrast is too small for gravity instruments to detect reliably"
    - "Gravity surveys can only be conducted on flat terrain where vehicles can travel"
  answer: 1
  explanation: "Gravity anomalies decrease in amplitude and increase in wavelength as the depth of the source increases — a phenomenon that smears out lateral variations in Moho depth when viewed from the surface. A sharp lateral step in Moho depth (say, from 35 km to 50 km over 20 km horizontally) produces a broad, smooth gravity gradient rather than a sharp edge. Seismic refraction can detect this step clearly because seismic waves travel directly through the structure and arrive with timing that precisely constrains layer depths. Gravity data cannot 'see' sharp boundaries at depth as clearly — the physics of potential fields limits resolution of deep structure."

- question: "A positive Bouguer anomaly in a continental interior generally indicates that the crust is thinner than average because denser mantle material sits closer to the surface."
  type: true-false
  answer: true
  explanation: "The relationship is symmetric: negative Bouguer anomalies correlate with thick crust (low-density crustal root displacing mantle), and positive anomalies correlate with thin crust (mantle rock at shallower depth, higher density than average). Continental cratons with ancient, thin crust, rift zones where the lithosphere has thinned, and ocean-continent transition zones often show positive or near-zero Bouguer anomalies precisely because the Moho is relatively shallow. Gravity inversion exploits this systematic relationship: measuring the Bouguer anomaly and solving for the Moho depth that would produce it."

- question: "Gravity data alone can determine absolute crustal thickness without any additional seismic or geological constraints, because the density contrast at the Moho is a fixed physical constant."
  type: true-false
  answer: false
  explanation: "The density contrast at the Moho varies depending on crustal and mantle composition — it is not a universal constant. Typical values range from about 300 to 600 kg/m³, but the exact value affects the calculated Moho depth significantly. A gravity inversion that assumes the wrong density contrast will produce systematically biased crustal thickness estimates. This is why gravity-derived Moho maps require calibration using seismic control points where Moho depth has been independently measured. The best results come from joint interpretation: gravity data provides broad spatial coverage, seismic data anchors the density contrast and absolute depth. Neither alone is as powerful as the combination."

- question: "Explain the physical relationship between Bouguer gravity anomalies and crustal thickness, specifically what creates the negative anomaly beneath mountain ranges."
  type: short-answer
  answer: "The key is the density contrast at the Moho — the boundary between crust (approximately 2800 kg/m³) and mantle (approximately 3300 kg/m³). Where crust is thick, a large volume of low-density crustal rock occupies space that would otherwise be filled by denser mantle rock. This creates a mass deficit relative to a reference model where crust has normal thickness. The Bouguer anomaly measures deviations from expected gravity after removing the effect of surface topography, so this deep mass deficit registers as a negative Bouguer anomaly. Beneath mountain ranges, the crust is thickest (isostatic compensation requires a root to support the topographic load), so the mass deficit is greatest and the Bouguer anomaly is most negative. The inverse applies at ocean basins and thin-crust regions: mantle is close to the surface, the mass excess produces positive anomalies."
  explanation: "The gravitational effect of the Moho is large because the density contrast (300–600 kg/m³) persists over a thick horizontal layer. A 10 km variation in Moho depth produces a Bouguer anomaly difference of roughly 50–80 milligals — easily detectable with modern gravimeters. This sensitivity is what makes gravity a powerful tool for crustal mapping despite its resolution limitations."
```

## Explainer

You already know from gravity anomaly separation that a measured gravity field contains contributions from sources at every depth, and that filtering techniques can isolate the regional component — the broad, long-wavelength signal produced by deep structure. You also know from the Airy isostasy model that mountains are supported by deep crustal roots: thicker crust beneath high topography, thinner crust beneath ocean basins. The method covered here connects these two ideas — it uses the regional gravity field to estimate how thick the crust is at any point.

The key physical insight is that the **Mohorovičić discontinuity** (Moho) — the boundary between crust and mantle — represents a sharp density contrast, typically around 400–600 kg/m³. Where the crust is thick, there is more low-density crustal rock replacing high-density mantle rock, producing a negative Bouguer gravity anomaly. Where the crust is thin, mantle rock sits closer to the surface, producing a less negative or even positive anomaly. This predictable relationship between Bouguer anomaly and Moho depth is the foundation of gravity-based crustal thickness estimation.

The simplest inversion approach assumes a uniform crustal density and a known density contrast at the Moho, then solves for the Moho depth that would produce the observed gravity anomaly at each point. In practice, this is done using **Parker's method**, which relates the Fourier transform of the gravity anomaly to the Fourier transform of the Moho topography through the density contrast. The calculation is iterative: you start with an initial Moho depth estimate (often from isostatic assumptions), compute the predicted gravity, compare it to the observed gravity, and adjust the Moho depth until the misfit is acceptably small.

This technique is especially powerful in places where seismic refraction surveys — the gold-standard method for measuring Moho depth — are impractical or too expensive. Satellite gravity missions like GRACE and GOCE now provide global gravity coverage, enabling crustal thickness maps even for remote continental interiors, ice-covered regions like Antarctica, and ocean basins. The trade-off is resolution: gravity data alone cannot resolve sharp lateral changes in Moho depth as precisely as seismic data, because the gravity field smooths out with distance from the source. The best results come from jointly interpreting gravity-derived Moho maps with the sparse seismic control points that do exist, using the seismic data to calibrate the density contrast and reference depth assumed in the gravity inversion.
