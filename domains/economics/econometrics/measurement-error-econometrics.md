---
id: measurement-error-econometrics
title: Measurement Error and Its Consequences
domain: economics
course: econometrics
prerequisites:
- id: ols-assumptions
  type: hard
- id: omitted-variable-bias
  type: soft
tags:
- measurement-error
- attenuation-bias
- iv
stage: formal-systems
status: draft
---

# Measurement Error and Its Consequences

## Core Idea
Measurement error in a regressor causes classical attenuation bias, shrinking OLS coefficients toward zero. Measurement error in the outcome increases standard errors. Instrumental variables can address measurement error if valid instruments exist.

## How It's Best Learned
Simulate data with known measurement error and observe how coefficients shrink. Consider IV estimation or instrumental variable techniques if measurement error is suspected.
