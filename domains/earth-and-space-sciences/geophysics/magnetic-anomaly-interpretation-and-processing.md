---
id: magnetic-anomaly-interpretation-and-processing
title: Magnetic Anomaly Interpretation and Reduction
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: potential-field-methods-gravity-magnetics
  type: hard
- id: magnetic-dipole-approximation-earths-field
  type: hard
tags:
- geomagnetism
- anomaly
- processing
- interpretation
stage: advanced
status: draft
---

# Magnetic Anomaly Interpretation and Reduction

## Core Idea
Magnetic anomalies are differences in the total magnetic field from the dipole background. Anomaly amplitude, shape, and direction depend on source depth, magnetization direction, and geographic latitude. Processing techniques such as reduction to the pole, analytic signal calculation, and vertical derivatives enhance anomalies and suppress regional field variations, improving source identification and depth estimation.

## How It's Best Learned
Compare total field anomalies with reduced-to-pole maps from the same region. Practice applying analytic signal and upward continuation filters to synthetic and real magnetic data.

## Common Misconceptions
Magnetic anomalies directly indicate mineral deposits (they indicate density of magnetic minerals, which correlates with but does not uniquely determine ore grade). Reduction to pole produces the same anomaly regardless of latitude (it depends on magnetization direction and geographic location).

## Explainer

From your work with potential field methods and the magnetic dipole approximation, you know that Earth's main magnetic field resembles that of a giant bar magnet, and that rocks containing magnetic minerals (primarily magnetite) acquire magnetizations that add to or subtract from this background field. A **magnetic anomaly** is simply the difference between the total field you measure at a point and the predicted regional field at that location. These anomalies carry information about the depth, shape, and magnetization of subsurface sources — but extracting that information requires careful processing because of a complication that gravity surveys do not share.

The complication is **directionality**. Gravity always points straight down, so a buried sphere produces a symmetric anomaly centered directly above it. Magnetization, however, has a direction — it aligns with Earth's field, which is vertical at the poles but nearly horizontal at the equator. This means the same buried magnetic body produces different anomaly shapes at different latitudes: a symmetric peak at the magnetic pole, an asymmetric dipolar pattern at mid-latitudes, and a symmetric trough at the magnetic equator. The technique called **reduction to the pole (RTP)** mathematically transforms the data to what the anomaly would look like if the field were vertical everywhere, centering anomalies directly over their sources and making interpretation far more intuitive. RTP is performed in the Fourier domain by applying a phase-shifting filter derived from the inclination and declination of the local field.

Beyond RTP, several other processing tools sharpen the image. The **analytic signal** (or total gradient) computes the amplitude of the gradient of the magnetic field, producing peaks directly over source edges regardless of magnetization direction — useful when RTP is unstable, as it is near the magnetic equator where the field is nearly horizontal. **Vertical derivatives** enhance shallow, short-wavelength features while suppressing broad regional trends, effectively sharpening the boundaries of near-surface bodies. Conversely, **upward continuation** simulates what the field would look like if measured at a greater altitude, smoothing out shallow noise and emphasizing deeper, larger-scale structures. Together these filters act like adjustable lenses: you can zoom in on shallow detail or step back to see deep architecture.

Interpreting the processed anomalies involves estimating source parameters — depth, geometry, and magnetization contrast. **Euler deconvolution** provides rapid depth estimates by exploiting Euler's homogeneity equation, which relates the anomaly's spatial derivatives to source depth through a structural index that encodes source geometry (0 for a contact, 1 for a thin dike, 2 for a horizontal cylinder, 3 for a sphere). The method is fast and automatic, but results must be filtered critically because noise and interfering sources produce spurious solutions. More sophisticated forward modeling and inversion approaches — analogous to those used in gravity interpretation — fit observed profiles or grids with parameterized source bodies, iterating toward models that are geologically plausible and consistent with other geophysical and geological constraints.
