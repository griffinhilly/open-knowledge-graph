---
id: gravity-anomalies-and-interpretation
title: Gravity Anomalies and Interpretation
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: gravity-potential-theory-earths-field
  type: hard
builds-toward:
- isostasy-and-crustal-balance
- potential-field-methods-gravity-magnetics
- gravity-surveys-and-data-inversion
tags:
- gravity
- anomalies
- crustal-structure
- interpretation
stage: advanced
status: draft
---

# Gravity Anomalies and Interpretation

## Core Idea
A gravity anomaly is the observed gravitational acceleration minus a reference value (usually the International Gravity Reference Field for a spherical, non-rotating Earth). The Bouguer anomaly corrects for elevation and rock density between the station and a reference surface, revealing subsurface density contrasts. Residual anomalies isolate local features from regional trends, enabling interpretation of basin geometry, ore deposits, and deep crustal structure.

## Explainer

From gravity potential theory, you understand that the Earth's gravitational field at any point is the integral effect of all mass below. A gravity measurement at the surface reflects everything from the nearby soil to the core. The challenge in exploration geophysics is isolating the small signal from a local subsurface feature — a sedimentary basin, an ore body, a salt dome — from the much larger background field. That isolation is what **gravity anomalies** accomplish: they are the difference between what you measure and what you would expect from a simplified reference Earth.

The first step is computing the **free-air anomaly**, which corrects observed gravity for the station's elevation above the reference ellipsoid. This accounts for the fact that gravity decreases with distance from Earth's center (roughly 0.3086 mGal per meter of elevation). But free-air correction alone leaves a problem: if your station sits on a mountain, the mass of the mountain itself contributes to the measurement. The **Bouguer correction** removes this effect by approximating the rock between the station and the reference surface as an infinite horizontal slab of known density (typically 2,670 kg/m³ for average crustal rock). The resulting **Bouguer anomaly** reveals density contrasts within the crust — positive anomalies indicate denser-than-average material below (mafic intrusions, uplifted basement), and negative anomalies indicate lower-density material (sedimentary basins, salt bodies, granitic batholiths). In mountainous terrain, an additional **terrain correction** accounts for the irregular topography that the infinite slab assumption misses.

A Bouguer anomaly map still contains signals from many different depth sources superimposed on each other. A deep, broad density contrast like the Moho produces a smooth, long-wavelength anomaly, while a shallow ore body produces a sharp, short-wavelength one. **Regional-residual separation** decomposes the total anomaly into a **regional** component (deep, large-scale structure) and a **residual** component (shallow, local features). Techniques range from simple polynomial surface fitting — where you fit a low-order polynomial to the data and subtract it — to more sophisticated spectral filtering that exploits the relationship between anomaly wavelength and source depth. The residual anomaly map is typically what an exploration geophysicist interprets for targets of interest.

Interpreting gravity anomalies requires forward modeling and, increasingly, formal inversion. In **forward modeling**, you assume a subsurface geometry and density distribution, compute the gravity field it would produce, and compare it to the observed anomaly. You adjust the model until it fits. The fundamental limitation is **non-uniqueness**: many different density distributions can produce the same surface gravity field. A broad, shallow body of moderate density contrast can mimic a narrow, deep body of strong contrast. This ambiguity is inherent to potential fields and cannot be eliminated by better measurements alone — it requires external constraints from geology, drilling, or other geophysical methods like seismics. Understanding this non-uniqueness is not a weakness but a discipline: it forces you to state what your gravity data actually constrain and what they leave ambiguous.
