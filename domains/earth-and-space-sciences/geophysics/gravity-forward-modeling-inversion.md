---
id: gravity-forward-modeling-inversion
title: Gravity Forward Modeling and Density Inversion
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: gravity-data-reduction
  type: hard
- id: gravity-potential-theory-earths-field
  type: hard
- id: linear-transformations
  type: soft
- id: fundamental-theorem-of-calculus-part-1
  type: soft
- id: pratt-isostasy-model
  type: soft
- id: crustal-thickness-determination-gravity
  type: soft
- id: seismic-velocity-density-relationships
  type: soft
- id: synthetic-seismogram-modeling
  type: soft
tags:
- gravity
- modeling
- inversion
- density
stage: expert
status: validated
---
# Gravity Forward Modeling and Density Inversion

## Core Idea
Forward modeling computes gravity anomalies from 2D or 3D density distributions. Iterative inversion adjusts densities to fit observed anomalies while minimizing model complexity (Occam's razor). Tikhonov regularization stabilizes inversions for underdetermined problems.

## Questions

```yaml
- question: "A gravity survey shows a positive anomaly over a region. A geologist proposes a shallow, dense body and runs a forward model that matches the observed anomaly perfectly. She concludes the shallow dense body must exist. What is wrong with this conclusion?"
  type: multiple-choice
  options:
    - "Forward modeling can only be done for spherical or cylindrical bodies, so irregular geometries cannot be tested"
    - "Gravity inversion is non-unique — a deeper, larger, lower-density body could produce an identical surface anomaly"
    - "A positive anomaly always indicates a shallow body; dense deeper bodies produce negative anomalies"
    - "Perfect data fit means the model is verified; non-uniqueness only applies when the fit is imperfect"
  answer: 1
  explanation: "Non-uniqueness is a mathematical property of potential field inversion, not a data quality issue. Infinitely many density models produce the same surface gravity signal — a shallow, small, dense body and a deeper, larger, less dense body are indistinguishable from gravity data alone. A perfect fit to observations does not uniquely confirm a model; it only shows the model is consistent with the data. Eliminating alternatives requires additional constraints: seismic data, well logs, geological knowledge. This is why gravity interpretation always carries irreducible ambiguity without independent constraints."

- question: "In gravity inversion expressed as d = Gm, what does the underdetermination of the system mean for the solution?"
  type: multiple-choice
  options:
    - "The system has no solution because the number of equations exceeds the number of unknowns"
    - "There is exactly one solution, but it requires very long computation to find"
    - "There are infinitely many density models m that fit the data d equally well"
    - "The sensitivity matrix G must be inverted, which is only possible if it is square"
  answer: 2
  explanation: "In gravity inversion, there are far more unknown cell densities (model parameters m) than gravity measurements (data d). The system has more unknowns than equations — it is underdetermined. The null space of G (density models that produce zero predicted gravity everywhere) is non-trivial, meaning you can add any null-space component to a fitting solution and still fit the data perfectly. Regularization selects one solution from this infinite family by imposing a preference (e.g., smallest total density contrast, or smoothest spatial variation). Without regularization, the inversion is ill-posed and returns no useful result."

- question: "Given a sufficiently dense grid of surface gravity measurements, it is theoretically possible to uniquely determine the density distribution throughout the entire subsurface."
  type: true-false
  answer: false
  explanation: "Non-uniqueness in gravity inversion is a fundamental mathematical property, not a sampling problem. Even with infinitely many perfectly precise surface measurements, the gravity field at the surface constrains only certain combinations of subsurface density — the projection of the density model onto the sensitivity matrix. The null space of that operator is infinite-dimensional: there are always infinitely many density distributions consistent with any set of surface observations. Adding more measurement points improves resolution and reduces some uncertainty, but cannot eliminate non-uniqueness. This contrasts with seismic travel-time tomography, which does approach uniqueness with sufficient coverage."

- question: "Increasing the regularization parameter in Tikhonov regularization produces a smoother, simpler density model that may not fit the observed gravity anomalies as closely as a lower regularization parameter."
  type: true-false
  answer: true
  explanation: "Tikhonov regularization minimizes a combined objective: data misfit + λ × model complexity. The parameter λ controls the tradeoff. High λ heavily penalizes model complexity (roughness or magnitude), pushing the solution toward smooth, featureless models that may not reproduce sharp anomalies in the data. Low λ prioritizes data fit, allowing geologically implausible spiky or oscillatory models. Neither extreme is useful: too little regularization overfits (noise is 'interpreted' as geology); too much underfits (real features are smoothed away). Choosing λ — via the L-curve, cross-validation, or geological judgment — is a central practical decision in applied geophysics."

- question: "Explain why a density model that perfectly fits the observed gravity anomaly is not necessarily the correct representation of the subsurface, and how Tikhonov regularization addresses this problem."
  type: short-answer
  answer: "Perfect data fit is necessary but not sufficient for a correct model — this is the non-uniqueness problem. Because the sensitivity matrix G maps infinitely many density models to the same surface gravity, any particular fitting model has infinitely many equivalent alternatives. Without additional constraints, the mathematically 'best fit' model may be geologically meaningless (e.g., alternating high- and low-density cells that cancel to produce the right anomaly). Tikhonov regularization adds a penalty term that favors models with small density contrasts or smooth spatial variations, selecting the 'simplest' fitting model according to a chosen criterion. This does not resolve non-uniqueness — there are still infinitely many models — but it replaces an arbitrary choice with a principled one guided by geological plausibility. Independent geological or geophysical constraints (seismic reflectors, well data) are needed to further narrow the space of plausible models."
  explanation: "The philosophical principle is Occam's razor applied to geophysics: prefer the simplest model consistent with observations. Regularization operationalizes this preference mathematically. But choosing what 'simple' means (smooth? compact? minimum norm?) implicitly encodes geological assumptions that must be justified."
```

## Explainer

You have already learned how to reduce raw gravity measurements to Bouguer anomalies — removing the predictable effects of latitude, elevation, and surrounding terrain to isolate the signal from unknown subsurface density variations. The next step is interpreting those anomalies: what underground structure could produce the gravity pattern you observe? This is where **forward modeling** and **inversion** come in, and they represent two complementary directions of reasoning.

**Forward modeling** is the "what if" direction. You propose a subsurface geometry — say, a granite pluton of known density and estimated shape buried at some depth — and calculate the gravity anomaly it would produce at the surface. The calculation uses Newton's law of gravitation, integrating the gravitational attraction of every small element of the body. For simple shapes (spheres, horizontal cylinders, infinite slabs), closed-form solutions exist from your calculus background. For realistic geology, the subsurface is discretized into polygonal cross-sections (2D) or prismatic cells (3D), and each cell's contribution is summed numerically. You then compare the computed anomaly with the observed one: if they match, your model is consistent with the data; if not, you adjust the geometry or density and try again.

**Inversion** automates and formalizes this trial-and-error process. Instead of manually tweaking a model, you set up a system of equations relating the observed gravity at each measurement point to the unknown densities in a grid of subsurface cells. In matrix form, this is **d = Gm**, where **d** is the data vector, **m** is the model vector of cell densities, and **G** is the sensitivity matrix encoding how each cell contributes to each measurement. The problem is almost always **underdetermined** — there are far more unknown cell densities than data points — meaning infinitely many density models can fit the data equally well. This is the fundamental **non-uniqueness** of potential field inversion: a shallow, small, dense body can produce the same anomaly as a deeper, larger, less dense body.

To pick a single useful solution from the infinite possibilities, you impose additional constraints through **regularization**. **Tikhonov regularization** adds a penalty term that discourages models that are overly complex — either in magnitude (favoring small density contrasts) or in roughness (favoring smooth spatial variations). The trade-off between fitting the data closely and keeping the model simple is controlled by a regularization parameter: too little regularization produces a noisy, geologically implausible model that overfits the data; too much produces a bland, featureless model that underfits it. Choosing this balance — often guided by the L-curve method or cross-validation — is one of the most important practical decisions in gravity inversion. The result is a density model that honors the data while respecting the principle that the simplest explanation consistent with observations is preferred.
