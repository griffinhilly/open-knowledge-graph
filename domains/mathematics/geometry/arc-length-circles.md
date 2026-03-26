---
id: arc-length-circles
title: Arc Length of Circles
domain: mathematics
course: geometry
prerequisites:
  - id: central-angles-and-arcs
    type: hard
  - id: proportions
    type: hard
builds-toward:
  - sector-area
  - radian-measure
tags: [circles, arc-length, circumference, proportionality]
stage: abstract-reasoning
status: validated
---

# Arc Length

## Core Idea
Arc length is the linear distance along a portion of a circle's circumference. Since the circumference of a circle is 2*pi*r, an arc of measure theta degrees has length (theta/360) * 2*pi*r. Arc length is proportional to the central angle. This formula bridges angular measurement and linear measurement, laying groundwork for radian measure in later courses.

## How It's Best Learned
Derive the formula from proportional reasoning: the arc is the same fraction of the circumference as the central angle is of 360 degrees. Practice computing arc lengths for various angles and radii. Give problems where students must find the angle given the arc length, or the radius given both.

## Common Misconceptions
- Confusing arc length (a linear measurement in units like cm) with arc measure (in degrees).
- Forgetting to use the radius in the formula (using diameter instead, or omitting it).
- Not including pi in exact answers.

## Questions

```yaml
- question: "Circle A has radius 2 cm and Circle B has radius 6 cm. A 90° arc is drawn on each circle. Which arc is longer, and by how much?"
  type: multiple-choice
  options:
    - "Both arcs are equal — they share the same 90° central angle"
    - "Circle B's arc is twice as long as Circle A's"
    - "Circle B's arc is 3 times as long as Circle A's"
    - "Circle B's arc is 9 times as long because the radius difference is squared"
  answer: 2
  explanation: "Arc length = (θ/360) × 2πr. For 90°: Circle A gives (1/4) × 2π(2) = π cm; Circle B gives (1/4) × 2π(6) = 3π cm. Circle B's arc is exactly 3 times longer — arc length scales linearly with radius. The angle sets the fraction of the circle; the radius sets how large that circle is. Option A is the core misconception: equal angles do not imply equal arc lengths when radii differ."

- question: "A circle has radius 10 cm. What is the length of the arc intercepted by a central angle of 45°?"
  type: multiple-choice
  options:
    - "2.5π cm"
    - "5π cm"
    - "10π cm"
    - "45π cm"
  answer: 0
  explanation: "Arc length = (45/360) × 2π(10) = (1/8) × 20π = 2.5π cm. A common error is using the diameter (20) instead of the radius (10), giving 5π — option B. Another error is multiplying the angle directly by π without applying the fraction, yielding 45π — option D."

- question: "Two arcs with the same central angle measurement generally have the same arc length."
  type: true-false
  answer: false
  explanation: "Arc length depends on both the central angle AND the radius. Two 60° arcs with radii of 3 cm and 9 cm have arc lengths of π cm and 3π cm respectively. The angle determines the fraction of the circumference traveled; the radius determines how large that circumference is. Arc measure (degrees) and arc length (linear distance) are fundamentally different quantities."

- question: "Arc length is a linear measurement expressed in the same units as the radius of the circle."
  type: true-false
  answer: true
  explanation: "Arc length is a distance — measured in centimeters, meters, inches, or whatever unit the radius uses. This contrasts with arc measure, which is expressed in degrees (a pure number with no length units). Keeping these two quantities separate prevents the very common error of treating degree measurements as if they described a distance."

- question: "Explain in your own words why arc length depends on the radius of the circle and not just the central angle."
  type: short-answer
  answer: "The central angle determines what fraction of the full circle the arc covers, but the full circumference itself depends on the radius (C = 2πr). A larger circle has a larger circumference, so the same fraction of it is a longer distance. The formula (θ/360) × 2πr combines both: the angle provides the fraction and the radius scales the total circumference that fraction applies to."
  explanation: "A 90° arc is always one-quarter of the full circumference, but one-quarter of a small circle is a short distance and one-quarter of a large circle is a long distance. The angle and radius are independent variables — you need both to determine a unique arc length. This is why giving only the angle of an arc tells you its shape but not how far you would travel along it."
```

## Explainer

The circumference of a circle is the total distance around it: C = 2πr. An **arc** is simply a piece of that circumference — a curved segment cut off by a central angle. Arc length answers the question: if you walked along the curve instead of through the center, how far would you travel?

The key insight comes from **proportional reasoning**, which you already know. A central angle of 360° sweeps the entire circle, giving the full circumference. A central angle of 180° sweeps exactly half the circle, giving half the circumference. By the same logic, a central angle of θ degrees sweeps a fraction θ/360 of the circle. Arc length is just that fraction of the full circumference: **arc length = (θ/360) × 2πr**. The formula is not something to memorize blindly — it is proportional reasoning applied to a circle. If you understand that, you can reconstruct it from scratch.

Notice what the two variables control independently. The **angle** (θ) determines what fraction of the circle you're traveling along. The **radius** (r) scales the size of the circle itself. A 90° arc on a small circle (r = 1) has length π/2 ≈ 1.57 units. The same 90° arc on a circle ten times larger (r = 10) has length 5π ≈ 15.7 units — ten times as long. The angle alone doesn't determine length; you need the radius too.

The most important conceptual distinction is **arc measure versus arc length**. Arc measure is the degree of the central angle — a pure number between 0° and 360°, with no units of distance. Arc length is a linear distance — measured in centimeters, inches, or whatever unit the radius uses. Two arcs can have the same degree measure (say, 60°) but different lengths if their circles have different radii. Keeping these two quantities separate prevents the most common errors in circle problems.

This topic is a stepping stone to **radian measure**, which you'll encounter in later courses. Radians redefine angle measurement so that the arc length formula becomes arc length = rθ (with no 360 conversion factor), because one radian is defined as the angle for which arc length equals the radius. When you see that definition, the connection back to this formula will be immediate: radians are just the natural unit that makes the proportion come out cleanly.
