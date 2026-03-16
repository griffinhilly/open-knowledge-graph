---
id: half-angle-identities
title: Half Angle Identities
domain: mathematics
course: precalculus
prerequisites:
  - id: double-angle-identities
    type: hard
builds-toward:
  - solving-trigonometric-equations
  - trigonometric-integrals
tags: [trigonometry, identities, half-angle]
stage: formal-systems
status: validated
---

# Half Angle Identities

## Core Idea
Half angle identities express sin(A/2), cos(A/2), and tan(A/2) in terms of cos(A). They are derived by solving the double angle formulas for the half-angle. For example, sin(A/2) = +/- sqrt((1 - cos(A))/2). The sign depends on the quadrant of A/2. These identities are useful for finding exact values at angles like 15 or 22.5 degrees and appear in certain integration techniques.

## How It's Best Learned
Derive from the double angle identity for cosine by replacing A with A/2. Practice determining the correct sign based on the quadrant of the half angle. Use them to find exact values that cannot be obtained from sum/difference identities alone.

## Common Misconceptions
- Forgetting the +/- sign and not checking the quadrant.
- Confusing half-angle identities with simply dividing the full-angle value by 2.
- Mixing up which double angle form to start from for each half-angle identity.

## Explainer

The double-angle identity for cosine comes in three forms, and the most useful for deriving half-angle identities is cos(2A) = 1 - 2sin²(A). To get a half-angle identity, substitute θ = 2A, so A = θ/2: cos(θ) = 1 - 2sin²(θ/2). Solving for sin(θ/2): sin²(θ/2) = (1 - cos θ)/2, so **sin(θ/2) = ±√((1 - cos θ)/2)**. The parallel derivation from the form cos(2A) = 2cos²(A) - 1 gives **cos(θ/2) = ±√((1 + cos θ)/2)**. Both follow in one algebraic step from the double-angle formulas you already know — there is nothing to memorize separately beyond recognizing which double-angle form to start from.

The ± sign is not optional or cosmetic — it carries essential information. The half-angle θ/2 lies in a specific quadrant, and that quadrant determines the sign of sin(θ/2) and cos(θ/2) independently. For example, to find sin(15°), write it as sin(30°/2). Since 15° lies in the first quadrant, sin(15°) > 0, so the + sign applies: sin(15°) = +√((1 - cos 30°)/2) = √((1 - √3/2)/2) = √((2 - √3)/4) = √(2 - √3)/2. This exact value cannot be reached using sum-or-difference identities because 15° does not decompose as a sum of standard angles in a useful way. Half-angle identities open up a new class of exact values, including 22.5°, 67.5°, and others that are halves of familiar angles.

For **tan(θ/2)**, divide the half-angle formulas: sin(θ/2)/cos(θ/2) = √((1 - cos θ)/(1 + cos θ)). But there are two cleaner sign-free forms: multiplying numerator and denominator strategically (and using sin θ = 2sin(θ/2)cos(θ/2)) yields tan(θ/2) = sin θ/(1 + cos θ) and equivalently tan(θ/2) = (1 - cos θ)/sin θ. These are sign-free because the sign of sin θ and the sign of tan(θ/2) already agree automatically. These forms matter in calculus: the **Weierstrass substitution** t = tan(θ/2) converts any rational expression in sin θ and cos θ into a rational expression in t, enabling integration by substitution. The half-angle identities are the algebraic foundation for that technique.

The key habit: never apply a half-angle identity without determining the quadrant of θ/2 first. A wrong sign produces an answer that is the exact negative of the correct value — numerically plausible but wrong. Sketch the angle θ/2 on the unit circle, confirm which quadrant it occupies, and assign the sign before computing. This takes seconds and eliminates a persistent class of errors.
