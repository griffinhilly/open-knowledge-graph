---
id: double-integrals-polar
title: Double Integrals in Polar Coordinates
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: double-integrals-general-regions
  type: hard
- id: polar-coordinates
  type: hard
builds-toward:
- applications-double-integrals
- triple-integrals-cylindrical-spherical
tags:
- polar-coordinates
- jacobian
- change-of-variables
stage: formal-systems
status: draft
---

# Double Integrals in Polar Coordinates

## Core Idea
In polar coordinates (r, θ), ∬_R f dA = ∬_R f(r cos θ, r sin θ) r dr dθ. The extra factor r (the Jacobian) appears because polar area elements dA = r dr dθ. Polar coordinates simplify integrals over disks and annuli.
