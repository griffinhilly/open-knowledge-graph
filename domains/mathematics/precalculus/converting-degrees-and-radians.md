---
id: converting-degrees-and-radians
title: Converting Between Degrees and Radians
domain: mathematics
course: precalculus
prerequisites:
  - id: radian-measure
    type: hard
builds-toward:
  - unit-circle
  - graphing-sine-and-cosine
tags: [trigonometry, radians, degrees, conversion]
stage: formal-systems
status: validated
---

# Converting Between Degrees and Radians

## Core Idea
Since 360 degrees = 2*pi radians, converting between the two systems uses the factor pi/180 (degrees to radians) or 180/pi (radians to degrees). Fluency in conversion is necessary because many real-world problems use degrees while all calculus uses radians. You should eventually recognize common conversions (30 = pi/6, 45 = pi/4, etc.) without computing.

## How It's Best Learned
Derive the conversion factor from the fundamental relationship. Practice converting standard angles in both directions. Build a reference table of common angles and their radian equivalents. Eventually move to instant recognition rather than calculation.

## Common Misconceptions
- Multiplying by the wrong conversion factor (using 180/pi when pi/180 is needed, or vice versa).
- Leaving answers in decimal approximations instead of exact multiples of pi.
- Believing that pi in radian measure is approximately 3.14 degrees.

## Explainer

The key to converting between degrees and radians is a single foundational equivalence: one full revolution equals both 360 degrees and 2π radians. This is not a definition to memorize blindly — it follows from what **radian measure** means. One radian is the angle that subtends an arc equal in length to the radius. Going all the way around a circle covers an arc of length 2πr (the circumference), so a full revolution sweeps 2π radians. That's it: 360° = 2π rad.

From this single fact, all conversions follow. To go from degrees to radians, multiply by (2π / 360) = π/180. To go from radians to degrees, multiply by (360 / 2π) = 180/π. You can always rederive these factors if you forget them — just start from 360° = 2π and cross-multiply. For example, to convert 90°: multiply by π/180 to get 90π/180 = π/2 radians. To convert 3π/4 radians: multiply by 180/π to get 3 × 180/4 = 135°.

The common angles are worth internalizing as direct associations rather than computed results. 30° = π/6, 45° = π/4, 60° = π/3, 90° = π/2, 180° = π, 270° = 3π/2, 360° = 2π. Once you see these often enough, you should recognize them the way you recognize that 1/4 = 0.25 — not by dividing each time, but instantly. The pattern helps: the denominator tells you what fraction of 180° (= π) you have, so π/6 is one-sixth of a half-turn (= 30°).

Notice that radian answers should generally be left as **exact multiples of π**, not decimal approximations. Writing π/4 is exact and clean; writing 0.785 is an approximation that loses information and makes further calculations messier. The decimal form of pi (3.14159...) is a number, not an angle unit — saying "π radians ≈ 3.14 degrees" is a category error. Fluency in this conversion is essential because calculus uses radians exclusively: the derivative of sin(x) is cos(x) only when x is in radians. Every trigonometric formula from here on assumes radian input.
