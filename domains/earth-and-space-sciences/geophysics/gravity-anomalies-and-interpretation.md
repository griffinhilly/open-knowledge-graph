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

## Questions

```yaml
- question: "A geophysicist surveys two sites at the same elevation. Site A sits over a dense mafic intrusion; Site B sits over a low-density sedimentary basin. After applying the full Bouguer correction, which site will show a higher Bouguer anomaly value?"
  type: multiple-choice
  options:
    - "Site B — sedimentary basins trap denser fluids that increase the signal"
    - "Site A — the denser-than-average mafic body produces a positive anomaly"
    - "Neither — the Bouguer correction removes all subsurface density variation"
    - "They will be equal because the same reference density is subtracted at both sites"
  answer: 1
  explanation: "The Bouguer anomaly reveals subsurface density contrasts relative to the reference crustal density (~2,670 kg/m³). A mafic intrusion is denser than this reference, so the observed gravity exceeds the reference prediction, yielding a positive anomaly. A sedimentary basin is less dense than the reference, yielding a negative anomaly. The Bouguer correction only removes the effect of topography — it does not flatten out subsurface variation; it exposes it."

- question: "Two geophysicists model the same residual Bouguer anomaly. Geophysicist A proposes a shallow, wide body with a moderate density contrast. Geophysicist B proposes a narrow, deep body with a very high density contrast. Both models fit the observed data equally well. What does this situation illustrate?"
  type: multiple-choice
  options:
    - "One of the models must be wrong — two different geometries cannot produce the same gravity field"
    - "The non-uniqueness of potential field inversion — multiple subsurface distributions can match the same surface data"
    - "That the Bouguer anomaly has not been computed correctly, since a unique solution should exist"
    - "That gravity surveys are unreliable and should be replaced by seismic methods"
  answer: 1
  explanation: "Non-uniqueness is a fundamental mathematical property of gravity (and magnetic) fields: a given surface field can be produced by infinitely many different subsurface distributions. This is not a measurement error or a modeling failure — it is inherent to potential fields. Resolving the ambiguity requires external constraints from geology, drilling, or other geophysical methods. Recognizing non-uniqueness is what separates rigorous interpretation from naive curve-fitting."

- question: "The Bouguer anomaly directly measures the absolute density of rock beneath a gravity station."
  type: true-false
  answer: false
  explanation: "The Bouguer anomaly measures the density *contrast* between the actual subsurface and the assumed reference density used in the Bouguer correction (typically 2,670 kg/m³). A positive Bouguer anomaly means the subsurface is denser than that reference; a negative anomaly means it is less dense. Absolute density cannot be determined from gravity alone without additional constraints — and even then, the non-uniqueness problem applies."

- question: "A broad, smooth gravity anomaly over a large area is more likely caused by a deep source than a narrow, sharp anomaly of similar amplitude over a small area."
  type: true-false
  answer: true
  explanation: "Anomaly wavelength (horizontal extent) scales with source depth. A shallow density contrast creates a short-wavelength anomaly — the gravity signal falls off rapidly with horizontal distance. A deep density contrast affects a broader area at the surface, producing a long-wavelength signal. This relationship between anomaly shape and source depth is a key interpretive tool, and it is the basis of regional-residual separation, which exploits wavelength differences to separate deep (regional) from shallow (residual) sources."

- question: "Why can collecting higher-quality gravity measurements not, by itself, resolve the ambiguity about the depth and shape of a subsurface body?"
  type: short-answer
  answer: "Because gravity non-uniqueness is a mathematical property of potential fields, not a measurement problem. Any surface gravity field can be reproduced by infinitely many different subsurface density distributions — making the measurement more precise does not eliminate this fundamental ambiguity. Resolving it requires independent geological or geophysical constraints (boreholes, seismic data, geological mapping) that discriminate among the infinite family of mathematically equivalent solutions."
  explanation: "Students often assume that better data yields unique answers. In potential field geophysics this is false: the inverse problem is fundamentally underdetermined regardless of data quality. More and denser measurements constrain the anomaly field better, but they still cannot uniquely determine the source geometry. This is why gravity interpretation is always combined with other methods, and why geophysicists must explicitly state what a gravity dataset constrains and what it cannot determine."
```

## Explainer

From gravity potential theory, you understand that the Earth's gravitational field at any point is the integral effect of all mass below. A gravity measurement at the surface reflects everything from the nearby soil to the core. The challenge in exploration geophysics is isolating the small signal from a local subsurface feature — a sedimentary basin, an ore body, a salt dome — from the much larger background field. That isolation is what **gravity anomalies** accomplish: they are the difference between what you measure and what you would expect from a simplified reference Earth.

The first step is computing the **free-air anomaly**, which corrects observed gravity for the station's elevation above the reference ellipsoid. This accounts for the fact that gravity decreases with distance from Earth's center (roughly 0.3086 mGal per meter of elevation). But free-air correction alone leaves a problem: if your station sits on a mountain, the mass of the mountain itself contributes to the measurement. The **Bouguer correction** removes this effect by approximating the rock between the station and the reference surface as an infinite horizontal slab of known density (typically 2,670 kg/m³ for average crustal rock). The resulting **Bouguer anomaly** reveals density contrasts within the crust — positive anomalies indicate denser-than-average material below (mafic intrusions, uplifted basement), and negative anomalies indicate lower-density material (sedimentary basins, salt bodies, granitic batholiths). In mountainous terrain, an additional **terrain correction** accounts for the irregular topography that the infinite slab assumption misses.

A Bouguer anomaly map still contains signals from many different depth sources superimposed on each other. A deep, broad density contrast like the Moho produces a smooth, long-wavelength anomaly, while a shallow ore body produces a sharp, short-wavelength one. **Regional-residual separation** decomposes the total anomaly into a **regional** component (deep, large-scale structure) and a **residual** component (shallow, local features). Techniques range from simple polynomial surface fitting — where you fit a low-order polynomial to the data and subtract it — to more sophisticated spectral filtering that exploits the relationship between anomaly wavelength and source depth. The residual anomaly map is typically what an exploration geophysicist interprets for targets of interest.

Interpreting gravity anomalies requires forward modeling and, increasingly, formal inversion. In **forward modeling**, you assume a subsurface geometry and density distribution, compute the gravity field it would produce, and compare it to the observed anomaly. You adjust the model until it fits. The fundamental limitation is **non-uniqueness**: many different density distributions can produce the same surface gravity field. A broad, shallow body of moderate density contrast can mimic a narrow, deep body of strong contrast. This ambiguity is inherent to potential fields and cannot be eliminated by better measurements alone — it requires external constraints from geology, drilling, or other geophysical methods like seismics. Understanding this non-uniqueness is not a weakness but a discipline: it forces you to state what your gravity data actually constrain and what they leave ambiguous.
