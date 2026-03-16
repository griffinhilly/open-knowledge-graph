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
- id: linear-algebra
  type: soft
- id: calculus
  type: soft
tags:
- gravity
- modeling
- inversion
- density
stage: advanced
status: draft
---

# Gravity Forward Modeling and Density Inversion

## Core Idea
Forward modeling computes gravity anomalies from 2D or 3D density distributions. Iterative inversion adjusts densities to fit observed anomalies while minimizing model complexity (Occam's razor). Tikhonov regularization stabilizes inversions for underdetermined problems.

## Explainer

You have already learned how to reduce raw gravity measurements to Bouguer anomalies — removing the predictable effects of latitude, elevation, and surrounding terrain to isolate the signal from unknown subsurface density variations. The next step is interpreting those anomalies: what underground structure could produce the gravity pattern you observe? This is where **forward modeling** and **inversion** come in, and they represent two complementary directions of reasoning.

**Forward modeling** is the "what if" direction. You propose a subsurface geometry — say, a granite pluton of known density and estimated shape buried at some depth — and calculate the gravity anomaly it would produce at the surface. The calculation uses Newton's law of gravitation, integrating the gravitational attraction of every small element of the body. For simple shapes (spheres, horizontal cylinders, infinite slabs), closed-form solutions exist from your calculus background. For realistic geology, the subsurface is discretized into polygonal cross-sections (2D) or prismatic cells (3D), and each cell's contribution is summed numerically. You then compare the computed anomaly with the observed one: if they match, your model is consistent with the data; if not, you adjust the geometry or density and try again.

**Inversion** automates and formalizes this trial-and-error process. Instead of manually tweaking a model, you set up a system of equations relating the observed gravity at each measurement point to the unknown densities in a grid of subsurface cells. In matrix form, this is **d = Gm**, where **d** is the data vector, **m** is the model vector of cell densities, and **G** is the sensitivity matrix encoding how each cell contributes to each measurement. The problem is almost always **underdetermined** — there are far more unknown cell densities than data points — meaning infinitely many density models can fit the data equally well. This is the fundamental **non-uniqueness** of potential field inversion: a shallow, small, dense body can produce the same anomaly as a deeper, larger, less dense body.

To pick a single useful solution from the infinite possibilities, you impose additional constraints through **regularization**. **Tikhonov regularization** adds a penalty term that discourages models that are overly complex — either in magnitude (favoring small density contrasts) or in roughness (favoring smooth spatial variations). The trade-off between fitting the data closely and keeping the model simple is controlled by a regularization parameter: too little regularization produces a noisy, geologically implausible model that overfits the data; too much produces a bland, featureless model that underfits it. Choosing this balance — often guided by the L-curve method or cross-validation — is one of the most important practical decisions in gravity inversion. The result is a density model that honors the data while respecting the principle that the simplest explanation consistent with observations is preferred.
