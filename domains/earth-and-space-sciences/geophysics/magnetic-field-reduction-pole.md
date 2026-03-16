---
id: magnetic-field-reduction-pole
title: Magnetic Field Reduction to the Pole
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: earths-magnetic-dipole-field-basics
  type: hard
- id: potential-field-methods-gravity-magnetics
  type: hard
builds-toward:
- magnetic-dipole-anomalies
tags:
- magnetic
- reduction-to-pole
- anomaly
stage: advanced
status: draft
---

# Magnetic Field Reduction to the Pole

## Core Idea
Magnetic anomalies are displaced from their sources in non-equatorial regions. Reduction-to-the-pole transforms data as if the dipole field were vertical, relocating anomalies to their true positions and enhancing small anomalies.

## Explainer

From your study of Earth's dipole field, you know that the magnetic field is not vertical everywhere — it dips at an angle (the inclination) that varies with latitude, from horizontal at the magnetic equator to vertical at the poles. From potential field methods, you know that magnetic surveys measure anomalies caused by subsurface bodies with contrasting magnetic properties. The problem that **reduction to the pole (RTP)** solves is that these two facts interact in a way that makes magnetic maps misleading at most latitudes.

Consider a simple case: a vertically magnetized, roughly spherical ore body buried beneath the surface. If you were at the magnetic pole, where the ambient field is vertical, this body would produce a symmetric anomaly directly above it — a clean bulls-eye pattern with the peak centered over the source. Interpretation would be straightforward. But at mid-latitudes, where the field is inclined, the same body produces an **asymmetric anomaly**: the peak is displaced to one side of the source, and a negative lobe appears on the other side. The anomaly no longer sits directly over the body that causes it. At the magnetic equator, where the field is horizontal, the distortion is even more pronounced — the anomaly pattern can look completely different from what you might naively expect. This latitude-dependent distortion occurs because the magnetic anomaly depends on both the magnetization direction of the source and the direction of the ambient field in which the measurement is made.

**Reduction to the pole** is a mathematical transformation applied in the frequency domain (using Fourier transforms) that recalculates the magnetic data as if the survey had been conducted at the magnetic pole, where inclination is 90°. The transformation effectively rotates the magnetization and ambient field vectors to vertical, converting every anomaly into the symmetric, centered pattern it would have at the pole. After RTP processing, anomaly peaks sit directly above their sources, positive and negative lobes resolve into clean shapes, and the map becomes far easier to interpret geologically. Small anomalies that were partially obscured by the asymmetric lobes of nearby larger anomalies become visible.

The RTP operation does have limitations. It requires knowledge of the local magnetic field direction (inclination and declination), which is typically obtained from the International Geomagnetic Reference Field (IGRF) model. At **low magnetic latitudes** — within about 15° of the magnetic equator — the transformation becomes numerically unstable because it involves dividing by quantities that approach zero when the inclination is small. In these regions, alternative approaches such as **reduction to the equator** or **pseudogravity transformation** are used instead. Additionally, RTP assumes that all sources are magnetized parallel to the ambient field (induced magnetization only). Bodies with strong **remanent magnetization** in a different direction — common in volcanic rocks — will not be correctly repositioned by standard RTP and require modified approaches that account for the remanence direction.
