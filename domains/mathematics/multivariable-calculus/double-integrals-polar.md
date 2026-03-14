---
id: double-integrals-polar
title: Double Integrals in Polar Coordinates
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: double-integrals-cartesian
  type: hard
- id: polar-coordinates
  type: hard
- id: iterated-integrals
  type: hard
builds-toward:
- jacobian-change-of-variables
tags:
- polar-coordinates
- double-integral
- area-element
- change-of-variables
stage: formal-systems
status: validated
---

# Double Integrals in Polar Coordinates

## Core Idea
In polar coordinates, the area element is dA = r dr dθ (not just dr dθ). Double integrals over circular or radially symmetric regions become ∬_R f(x,y) dA = ∫∫ f(r cosθ, r sinθ) r dr dθ, where the extra factor of r accounts for the non-uniform stretching of the coordinate system. Polar coordinates simplify integrals over circles, annuli, and regions bounded by polar curves. The classic example is ∫_{−∞}^{∞} e^{−x²} dx = √π, which is computed by squaring the integral and converting to polar.

## How It's Best Learned
The extra r factor is the hardest part. Derive it geometrically: the area of a small polar sector is approximately r ΔrΔθ, not ΔrΔθ. Then practice converting Cartesian integrals to polar when the region is circular. The Gaussian integral computation (∫e^{-x²}dx = √π) is an unforgettable application that demonstrates the power of the method.

## Common Misconceptions
- The area element is r dr dθ, not dr dθ. Forgetting the r factor is the most common error.
- The limits on r can be functions of θ (for non-circular polar regions); they are not always constants.
- x² + y² = r², not (x+y)²; the substitution x = r cosθ, y = r sinθ must be applied carefully.
