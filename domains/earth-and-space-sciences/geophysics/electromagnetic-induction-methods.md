---
id: electromagnetic-induction-methods
title: Electromagnetic Induction and Transient Methods
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: potential-field-methods-gravity-magnetics
  type: soft
- id: electromagnetic-waves
  type: soft
builds-toward:
- magnetotelluric-methods-em-induction
tags:
- electromagnetic
- induction
- tem
- methods
stage: advanced
status: draft
---

# Electromagnetic Induction and Transient Methods

## Core Idea
Time-domain (TEM) and frequency-domain electromagnetic methods measure electrical conductivity through induced currents and transient responses. Data are inverted for 1D/2D/3D conductivity-depth models.

## Explainer

From your background in electromagnetic waves, you know that a changing magnetic field induces an electric field, and that electric field can drive currents in any conductive material. Electromagnetic induction methods in geophysics exploit exactly this principle: they use a controlled or natural electromagnetic source to induce electrical currents in the subsurface, then measure the resulting secondary fields to map how **electrical conductivity** varies with depth. This gives access to a physical property — conductivity — that is exquisitely sensitive to fluid content, salinity, temperature, and mineralogy, making EM methods complementary to the density and magnetization contrasts you studied in potential field methods.

In **time-domain electromagnetic (TEM)** methods, a transmitter loop carries a steady current that is abruptly shut off. The sudden change in magnetic flux induces eddy currents in the ground that initially concentrate near the surface, then diffuse downward over time — a phenomenon called **smoke-ring diffusion**. The receiver measures how the secondary magnetic field decays after the transmitter switches off. Early-time signals reflect shallow conductivity structure; late-time signals, which arrive from deeper-propagating currents, reveal conductivity at greater depths. The decay curve's shape encodes the conductivity-depth profile: a highly conductive layer produces a slow, sustained decay because induced currents persist longer in good conductors.

**Frequency-domain methods** take a different approach. Instead of pulsing and watching the decay, they transmit a continuous sinusoidal signal and measure the amplitude and phase of the secondary field relative to the transmitted primary field. Low frequencies penetrate deeper because the **skin depth** — the distance over which the field amplitude decays to 1/e — increases as frequency decreases (skin depth ∝ 1/√(frequency × conductivity)). By sweeping through a range of frequencies, you effectively sample different depths. The ratio of secondary to primary field, expressed as apparent conductivity or mutual impedance, can be inverted for a layered conductivity model.

Both approaches ultimately produce a model of how conductivity varies with depth, but they have different practical strengths. TEM is excellent for detecting conductive targets (ore bodies, saline aquifers, clay layers) because the late-time response is dominated by the most conductive features. Frequency-domain systems are often more portable and provide continuous spatial coverage, making them ideal for mapping lateral variations in shallow conductivity — groundwater contamination plumes, for instance. In either case, the measured data are **inverted** using forward models that compute the expected response for a given conductivity structure, iteratively adjusting the model until it fits the observations. The non-uniqueness of this inverse problem — different conductivity distributions can produce similar responses — is managed through regularization, prior constraints, and, increasingly, joint inversion with other geophysical datasets.
