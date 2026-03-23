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
stage: expert
status: draft
---

# Gravity Anomaly Separation: Regional and Residual

## Core Idea
Gravity anomalies measured at the surface reflect contributions from sources at all depths. Regional anomalies arise from deep crustal and mantle density variations, while residual anomalies originate from shallow sources. Separation techniques such as filtering, upward continuation, and polynomial fits isolate regional and residual components to match interpreted targets to specific depth ranges.

## Questions

```yaml
- question: "A geophysicist applies upward continuation to a Bouguer anomaly map, progressively increasing the continuation height. Which feature would be most attenuated first?"
  type: multiple-choice
  options:
    - "A broad gravity low caused by crustal thinning at 30 km depth"
    - "A narrow, intense gravity high from a dense ore body at 200 m depth"
    - "A continental-scale gradient caused by lithospheric density variations"
    - "A regional anomaly from a deep sedimentary basin at 8 km depth"
  answer: 1
  explanation: "Upward continuation attenuates short-wavelength signals faster than long-wavelength ones. Shallow sources produce short-wavelength (spatially narrow) anomalies because the gravity signal spreads out little before reaching the surface. As continuation height increases, these narrow features vanish first. Deep sources produce broad, long-wavelength signals that persist to greater heights. This is exactly the property that makes upward continuation useful for isolating the regional (deep) signal."

- question: "A geologist applies a low-order polynomial fit to a Bouguer anomaly map, calls the polynomial surface the 'regional,' and subtracts it to obtain the 'residual.' A colleague claims the residual objectively represents the shallow subsurface. What is the most serious problem with this claim?"
  type: multiple-choice
  options:
    - "Polynomial fitting only works in the time domain, not on spatial gravity maps"
    - "The polynomial order is chosen by the interpreter, so features assigned to 'regional' vs. 'residual' depend on that subjective choice — the separation is not unique"
    - "The method cannot distinguish between ore bodies and faults, so the residual is geologically ambiguous"
    - "Low-order polynomials cannot fit smooth regional trends, so they always contaminate the residual with deep-source contributions"
  answer: 1
  explanation: "The key limitation of polynomial fitting is that the interpreter must choose the polynomial degree, and that choice determines which spatial wavelengths are called 'regional.' A linear fit assigns only the broadest trend to the regional; a cubic fit absorbs more medium-wavelength features. The residual is therefore not a purely objective quantity — it is the part of the signal that the interpreter decided was not regional. Best practice is to apply multiple separation methods and trust only features that appear consistently across all of them."

- question: "A shallow ore body and a deep crustal structure both contribute to the same gravity measurement at the surface — they cannot be isolated from each other without processing."
  type: true-false
  answer: true
  explanation: "Gravity is a potential field: every density contrast at every depth contributes to the measured value at the surface simultaneously. There is no way to look at a single gravity reading and know which part came from what depth. Processing — spectral filtering, upward continuation, polynomial subtraction — is required to exploit the depth-wavelength relationship and disentangle contributions from different depth ranges."

- question: "Upward continuation is used to isolate the residual (shallow) anomaly because it removes deep-source contributions from the gravity field, leaving only signals from shallow structures."
  type: true-false
  answer: false
  explanation: "This reverses the logic. Upward continuation preferentially attenuates shallow (short-wavelength) signals and preserves deep (long-wavelength) signals. Therefore, continuing the field upward produces the regional anomaly — the smooth, long-wavelength component from deep sources. To obtain the residual, you then subtract this continued (regional) field from the original data. The shallow ore body signal is what gets removed by continuation, not preserved."

- question: "Why do deep density sources produce broad, long-wavelength gravity anomalies while shallow sources produce narrow, short-wavelength anomalies, and how does this property make separation possible?"
  type: short-answer
  answer: "Gravity follows an inverse-square law: the signal from a point source spreads and weakens with distance. A deep source is far from every surface measurement point, so its gravitational pull is distributed broadly across the map — producing a wide, smooth anomaly. A shallow source is close to some measurement points and far from others, producing a sharp, localized anomaly. Separation techniques exploit this: filters that remove long spatial wavelengths highlight shallow targets; filters that remove short wavelengths (or upward continuation) reveal deep structure."
  explanation: "The depth-wavelength relationship is the physical foundation for all anomaly separation. A rule of thumb is that the horizontal half-width of an anomaly from a point source equals approximately the source depth. So a 20 km-wide anomaly suggests a source at ~20 km depth; a 500 m-wide anomaly suggests a source at ~500 m. Separation methods are essentially spatial-frequency filters tuned to target a particular depth range. The non-uniqueness arises because real sources are not points, and any finite spatial filter will bleed some contribution from one depth range into another."
```

## Explainer

From your work with gravity surveys and gravity anomaly interpretation, you know that a Bouguer anomaly map shows all the density variations beneath the surface superimposed on one another. A massive ore body at 500 meters depth, a sedimentary basin at 5 km, and crustal thinning at 30 km all contribute to the same measured gravity field. The problem is that these signals overlap spatially — you cannot simply look at the map and tell which features come from which depth. **Anomaly separation** is the set of techniques that disentangles these overlapping contributions.

The key physical principle is that deep sources produce broad, smooth (long-wavelength) anomalies, while shallow sources produce sharp, localized (short-wavelength) anomalies. This follows directly from the inverse-square law of gravity: as distance from a source increases, its gravity signal spreads out and becomes smoother. The **regional anomaly** is the long-wavelength component attributed to deep crustal or mantle structure. The **residual anomaly** is whatever remains after removing the regional — it highlights shallower targets like ore bodies, salt domes, or fault-bounded basins.

The simplest separation method is **polynomial fitting**: fit a low-order polynomial surface (linear, quadratic, or cubic) to the gravity data, call that surface the regional field, and subtract it to get the residual. This works when the regional trend is simple and smooth, but breaks down if deep structures have complex geometry. **Spectral filtering** is more rigorous: transform the gravity data into the frequency domain using a Fourier transform, then apply a low-pass filter to extract the regional or a high-pass filter to extract the residual. The cutoff wavelength is chosen based on the expected depth of the target — longer wavelengths pass through for deeper targets. **Upward continuation** is a particularly elegant technique: it mathematically recalculates what the gravity field would look like if measured at a higher elevation. Since short-wavelength signals attenuate faster with altitude, continuing the field upward progressively removes shallow contributions, leaving the regional field.

No separation method is perfect — they all require the interpreter to make choices about cutoff wavelengths, polynomial order, or continuation height, and those choices influence the result. The best practice is to apply multiple methods and look for features that appear consistently across all of them. When the residual anomaly from a polynomial fit, a bandpass filter, and an upward continuation all show the same localized high, you can be confident that a real shallow density contrast exists at that location. This iterative, multi-method approach is what transforms raw gravity data into geologically interpretable maps.
