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
status: draft
---

# Potential Field Methods: Gravity and Magnetics

## Core Idea
Potential field methods interpret gravity and magnetic anomalies to map subsurface density and magnetization contrasts. Forward modeling computes fields from assumed geometries and properties; inverse problems recover density/magnetization distributions from observed fields. Filtering and analytical continuation enhance anomalies and separate regional from residual components; derivatives (first, second, analytic signal) highlight edges and delineate structural boundaries.

## Explainer

From gravity potential theory, you understand that the gravitational field at any point is the superposition of contributions from all subsurface masses, and from Earth's magnetic field basics, you know that the dipolar field varies systematically with position. Potential field methods build on these foundations to extract geological information from measured gravity and magnetic anomalies — deviations from the expected background field that reveal lateral variations in density and magnetization within the Earth.

Both gravity and magnetic fields are **potential fields**, meaning they satisfy Laplace's equation in source-free regions. This mathematical property has powerful practical consequences. First, if you know the field on one surface (say, the ground), you can compute it on any other surface above the sources — a technique called **upward continuation**, which smooths data by emphasizing deep, broad sources, or **downward continuation**, which sharpens data to enhance shallow sources (though at the cost of amplifying noise). Second, potential fields can be decomposed into wavelength components using spectral analysis, and the relationship between wavelength and source depth is systematic: deeper sources produce broader, longer-wavelength anomalies. This allows you to separate the regional field (from deep crustal or mantle structure) from the residual field (from local, shallow targets).

**Forward modeling** is the process of computing the gravity or magnetic field produced by an assumed subsurface geometry with specified density or magnetization contrasts. For simple shapes — spheres, horizontal cylinders, vertical prisms, thin sheets — analytical formulas exist. For complex geology, numerical approaches discretize the subsurface into cells and sum their contributions. You adjust the model geometry and properties until the computed field matches the observed anomaly. The **inverse problem** reverses this: given the observed field, recover the subsurface property distribution. Inversion is inherently non-unique for potential fields — many different source distributions can produce identical surface measurements — so constraints from geology, drilling, or other geophysical data are essential.

**Derivative-based enhancement** is a suite of techniques that sharpen anomaly maps to highlight geological boundaries. The **first vertical derivative** emphasizes shallow sources and sharpens edges. The **horizontal gradient** peaks directly over steep density or magnetization contacts, making it ideal for mapping faults and formation boundaries. The **analytic signal** (the total gradient) combines horizontal and vertical derivatives into a quantity that peaks over source edges regardless of the magnetization direction — particularly useful for magnetic data, where the anomaly shape depends on the ambient field inclination and the rock's remanent magnetization. Together, these tools transform broad, overlapping anomaly patterns into crisp boundary maps that can be directly compared with geological mapping and used to guide drilling or further geophysical surveys.
