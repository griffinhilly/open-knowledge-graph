---
id: gravity-anomaly-separation-residual-regional
title: 'Gravity Anomaly Separation: Regional and Residual'
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: gravity-surveys-and-data-inversion
  type: hard
- id: gravity-anomalies-and-interpretation
  type: hard
builds-toward:
- crustal-thickness-determination-gravity
tags:
- gravity
- anomaly
- separation
- processing
stage: advanced
status: draft
---

# Gravity Anomaly Separation: Regional and Residual

## Core Idea
Gravity anomalies measured at the surface reflect contributions from sources at all depths. Regional anomalies arise from deep crustal and mantle density variations, while residual anomalies originate from shallow sources. Separation techniques such as filtering, upward continuation, and polynomial fits isolate regional and residual components to match interpreted targets to specific depth ranges.

## Explainer

From your work with gravity surveys and gravity anomaly interpretation, you know that a Bouguer anomaly map shows all the density variations beneath the surface superimposed on one another. A massive ore body at 500 meters depth, a sedimentary basin at 5 km, and crustal thinning at 30 km all contribute to the same measured gravity field. The problem is that these signals overlap spatially — you cannot simply look at the map and tell which features come from which depth. **Anomaly separation** is the set of techniques that disentangles these overlapping contributions.

The key physical principle is that deep sources produce broad, smooth (long-wavelength) anomalies, while shallow sources produce sharp, localized (short-wavelength) anomalies. This follows directly from the inverse-square law of gravity: as distance from a source increases, its gravity signal spreads out and becomes smoother. The **regional anomaly** is the long-wavelength component attributed to deep crustal or mantle structure. The **residual anomaly** is whatever remains after removing the regional — it highlights shallower targets like ore bodies, salt domes, or fault-bounded basins.

The simplest separation method is **polynomial fitting**: fit a low-order polynomial surface (linear, quadratic, or cubic) to the gravity data, call that surface the regional field, and subtract it to get the residual. This works when the regional trend is simple and smooth, but breaks down if deep structures have complex geometry. **Spectral filtering** is more rigorous: transform the gravity data into the frequency domain using a Fourier transform, then apply a low-pass filter to extract the regional or a high-pass filter to extract the residual. The cutoff wavelength is chosen based on the expected depth of the target — longer wavelengths pass through for deeper targets. **Upward continuation** is a particularly elegant technique: it mathematically recalculates what the gravity field would look like if measured at a higher elevation. Since short-wavelength signals attenuate faster with altitude, continuing the field upward progressively removes shallow contributions, leaving the regional field.

No separation method is perfect — they all require the interpreter to make choices about cutoff wavelengths, polynomial order, or continuation height, and those choices influence the result. The best practice is to apply multiple methods and look for features that appear consistently across all of them. When the residual anomaly from a polynomial fit, a bandpass filter, and an upward continuation all show the same localized high, you can be confident that a real shallow density contrast exists at that location. This iterative, multi-method approach is what transforms raw gravity data into geologically interpretable maps.
