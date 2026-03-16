---
id: joint-inversion-gravity-seismics
title: Joint Inversion of Gravity and Seismic Data
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: gravity-surveys-and-data-inversion
  type: hard
- id: seismic-tomography-velocity-imaging
  type: hard
tags:
- inversion
- gravity
- seismic
- joint-inversion
stage: advanced
status: draft
---

# Joint Inversion of Gravity and Seismic Data

## Core Idea
Gravity and seismic data constrain different physical properties (density and seismic velocity) and can be combined in joint inversions to construct more robust models of subsurface structure. Gravity adds depth sensitivity beyond seismic surveys and provides independent constraints on density; seismics provides detailed velocity structure. Joint inversion reduces model ambiguity and improves interpretability.

## Explainer

From your work with gravity data inversion, you know that gravity measurements constrain density structure but suffer from severe non-uniqueness — many different subsurface density distributions can produce the same surface gravity field. From seismic tomography, you know that travel-time data constrain velocity structure with good spatial resolution but can have limited sensitivity to certain rock properties. **Joint inversion** combines these two complementary datasets into a single inversion framework, producing a model that must simultaneously satisfy both gravity and seismic observations. The result is more tightly constrained than either method alone could achieve.

The physical basis for joint inversion is the empirical relationship between seismic velocity and density. In most crustal rocks, velocity and density covary — denser rocks generally have higher seismic velocities. This correlation has been quantified through relationships like **Nafe-Drake** curves (for marine sediments), **Birch's law** (for crystalline rocks), and **Gardner's relation** (ρ ≈ aV^0.25 for sedimentary rocks). These empirical links mean that a velocity model and a density model of the same region should be mutually consistent. Joint inversion enforces this consistency by coupling the two parameter fields through a shared constraint — either a direct petrophysical relationship or a structural similarity requirement.

There are two main approaches to joint inversion. In **petrophysically coupled** inversion, the velocity-density relationship is built directly into the forward model: when the algorithm adjusts velocity in a cell, the density changes accordingly (or vice versa). This is powerful when the empirical relationship is well established, but it can fail in unusual lithologies where the standard relationships break down (e.g., gas-saturated sediments have low velocity but moderate density). In **structurally coupled** (or cross-gradient) inversion, the algorithm does not enforce a specific velocity-density relationship but instead requires that the spatial gradients of the two property fields are parallel — meaning structural boundaries appear in the same locations in both models. This is more flexible and makes fewer petrophysical assumptions, but it provides weaker coupling.

The practical benefit is a dramatic reduction in model ambiguity. Consider mapping a sedimentary basin: gravity alone might suggest either a deep basin with moderate density contrast or a shallow basin with strong contrast. Seismic refraction data resolve the basin geometry (depth to basement) but may poorly constrain absolute densities. Jointly inverting both datasets yields a model where the basin geometry is fixed by the seismics and the density distribution is consistent with the gravity — a result neither method could produce independently. Joint inversion is now standard practice in crustal-scale studies, resource exploration, and tectonic research, and the framework extends naturally to include additional datasets like magnetotelluric conductivity or magnetic susceptibility, further narrowing the space of permissible models.
