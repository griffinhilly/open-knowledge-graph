---
id: transfer-function-poles-zeros-interpretation
title: Transfer Function Poles and Zeros Interpretation
domain: engineering
course: control-systems
prerequisites:
- id: transfer-functions-control
  type: hard
- id: pole-zero-plot-stability-analysis
  type: hard
builds-toward:
- root-locus-method
- nyquist-plot-encirclement-criterion
tags:
- pole-location
- zero-location
- stability
- frequency-response
- time-response
stage: abstract-reasoning
status: draft
---

# Transfer Function Poles and Zeros Interpretation

## Core Idea
Poles in the left-half plane (LHP) contribute stable exponentially decaying terms; right-half plane (RHP) poles are unstable. Pole location (real part controls decay rate; imaginary part controls frequency) directly determines time response; frequency response magnitude has peaks near poles and nulls near zeros.
