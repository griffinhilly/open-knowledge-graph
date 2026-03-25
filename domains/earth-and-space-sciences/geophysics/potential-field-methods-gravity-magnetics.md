---
id: potential-field-methods-gravity-magnetics
title: 'Potential Field Methods: Gravity and Magnetics'
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: gravity-potential-theory-earths-field
  type: hard
- id: earths-magnetic-dipole-field-basics
  type: soft
builds-toward:
- gravity-surveys-and-data-inversion
tags:
- potential-field
- gravity
- magnetics
- interpretation
stage: advanced
status: validated
---

# Potential Field Methods: Gravity and Magnetics

## Core Idea
Potential field methods interpret gravity and magnetic anomalies to map subsurface density and magnetization contrasts. Forward modeling computes fields from assumed geometries and properties; inverse problems recover density/magnetization distributions from observed fields. Filtering and analytical continuation enhance anomalies and separate regional from residual components; derivatives (first, second, analytic signal) highlight edges and delineate structural boundaries.

## Questions

```yaml
- question: "A geophysicist observes two gravity anomalies: one is broad and spans hundreds of kilometers; the other is narrow and spans only a few kilometers. What does spectral analysis suggest about the relative depths of their sources?"
  type: multiple-choice
  options:
    - "The broad anomaly indicates a shallow, dense source; the narrow one indicates a deep source"
    - "The broad, long-wavelength anomaly indicates a deep source; the narrow, short-wavelength anomaly indicates a shallow source"
    - "Wavelength is determined by the density contrast, not the depth — both anomalies could be at the same depth"
    - "Both anomalies must originate at the same depth since they appear on the same survey"
  answer: 1
  explanation: "A key property of potential fields is the systematic relationship between source depth and anomaly wavelength. Deep sources produce broad, long-wavelength anomalies because their gravitational (or magnetic) contribution spreads over a larger area by the time it reaches the surface. Shallow sources produce narrow, short-wavelength anomalies. Spectral analysis exploits this to separate regional (deep crustal/mantle) signals from residual (local, shallow) signals — a fundamental step in potential field data processing."

- question: "A gravity inversion produces a density model that perfectly fits all observed data. A colleague then proposes an entirely different density distribution that also perfectly reproduces the observations. What does this demonstrate?"
  type: multiple-choice
  options:
    - "One model must be wrong — a correctly solved inversion always produces a unique solution"
    - "This is the inherent non-uniqueness of potential field inversion — many different subsurface configurations produce identical surface fields, so external constraints are essential"
    - "The analytic signal can always distinguish between competing models"
    - "Denser survey coverage would uniquely determine the correct model"
  answer: 1
  explanation: "Non-uniqueness is a fundamental mathematical property of potential field inversion, not an error or a data-quality issue. Because gravity and magnetic fields measured on a surface are the integrated result of all subsurface sources, many different 3D distributions of density or magnetization can produce identical field values at the surface. Breaking this ambiguity requires independent constraints — borehole data, seismic sections, geological mapping, or other geophysical methods. Accepting this limitation is essential to responsible potential field interpretation."

- question: "Upward continuation of potential field data enhances shallow, local anomalies while suppressing signals from deep sources."
  type: true-false
  answer: false
  explanation: "It is the opposite. Upward continuation computes the field as it would appear at a greater height above the sources. Moving away from sources smooths and attenuates short-wavelength (shallow) signals while preserving long-wavelength (deep) components — it is a low-pass spatial filter. This is useful for emphasizing deep crustal structure and suppressing near-surface noise. Downward continuation does the reverse — it sharpens shallow anomalies by projecting toward the sources, but at the cost of amplifying noise and numerical instability."

- question: "The analytic signal is particularly useful for magnetic data interpretation because it peaks over source edges regardless of the direction of magnetization or the ambient field inclination."
  type: true-false
  answer: true
  explanation: "Magnetic anomaly shapes depend strongly on both the inclination of the ambient geomagnetic field (which varies with latitude) and the direction of remanent magnetization in the rocks (which may differ from the current field). This makes magnetic anomalies asymmetric and difficult to compare across regions. The analytic signal — the total gradient combining horizontal and vertical derivatives — produces a symmetric, always-positive amplitude that peaks directly over source edges regardless of these directional complications. It is a robust edge-detection tool even when magnetization direction is unknown."

- question: "Why is forward modeling an essential step even when the ultimate goal is inversion — recovering subsurface structure from observed data?"
  type: short-answer
  answer: "Forward modeling provides the mathematical link between an assumed subsurface model and the predicted surface field. Inversion cannot operate without it — the inversion process works by iteratively adjusting a model and computing its forward prediction, comparing that prediction to observed data, and minimizing the misfit. Without forward modeling there is no way to evaluate whether a candidate model is consistent with the observations. Forward modeling also builds interpretive intuition: knowing how a sphere, dyke, or prism produces specific anomaly shapes allows you to recognize those signatures in data and propose geologically reasonable starting models."
  explanation: "Forward modeling also serves as a quality-control tool: if the best-fit inverted model's forward prediction fails to match key features of the data, something is wrong — either with the model parameterization, the inversion constraints, or the data themselves. The interplay between forward modeling and inversion is iterative, with geological judgment guiding which non-unique solutions to accept as physically meaningful."
```

## Explainer

From gravity potential theory, you understand that the gravitational field at any point is the superposition of contributions from all subsurface masses, and from Earth's magnetic field basics, you know that the dipolar field varies systematically with position. Potential field methods build on these foundations to extract geological information from measured gravity and magnetic anomalies — deviations from the expected background field that reveal lateral variations in density and magnetization within the Earth.

Both gravity and magnetic fields are **potential fields**, meaning they satisfy Laplace's equation in source-free regions. This mathematical property has powerful practical consequences. First, if you know the field on one surface (say, the ground), you can compute it on any other surface above the sources — a technique called **upward continuation**, which smooths data by emphasizing deep, broad sources, or **downward continuation**, which sharpens data to enhance shallow sources (though at the cost of amplifying noise). Second, potential fields can be decomposed into wavelength components using spectral analysis, and the relationship between wavelength and source depth is systematic: deeper sources produce broader, longer-wavelength anomalies. This allows you to separate the regional field (from deep crustal or mantle structure) from the residual field (from local, shallow targets).

**Forward modeling** is the process of computing the gravity or magnetic field produced by an assumed subsurface geometry with specified density or magnetization contrasts. For simple shapes — spheres, horizontal cylinders, vertical prisms, thin sheets — analytical formulas exist. For complex geology, numerical approaches discretize the subsurface into cells and sum their contributions. You adjust the model geometry and properties until the computed field matches the observed anomaly. The **inverse problem** reverses this: given the observed field, recover the subsurface property distribution. Inversion is inherently non-unique for potential fields — many different source distributions can produce identical surface measurements — so constraints from geology, drilling, or other geophysical data are essential.

**Derivative-based enhancement** is a suite of techniques that sharpen anomaly maps to highlight geological boundaries. The **first vertical derivative** emphasizes shallow sources and sharpens edges. The **horizontal gradient** peaks directly over steep density or magnetization contacts, making it ideal for mapping faults and formation boundaries. The **analytic signal** (the total gradient) combines horizontal and vertical derivatives into a quantity that peaks over source edges regardless of the magnetization direction — particularly useful for magnetic data, where the anomaly shape depends on the ambient field inclination and the rock's remanent magnetization. Together, these tools transform broad, overlapping anomaly patterns into crisp boundary maps that can be directly compared with geological mapping and used to guide drilling or further geophysical surveys.
