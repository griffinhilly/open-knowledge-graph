---
id: moment-of-inertia
title: Moment of Inertia
domain: physics
course: classical-mechanics
prerequisites:
- id: torque
  type: hard
- id: definite-integral-definition
  type: soft
- id: center-of-mass
  type: soft
- id: triple-integrals
  type: soft
builds-toward:
- rotational-dynamics
- angular-momentum
tags:
- moment-of-inertia
- rotational-inertia
- mass-distribution
stage: formal-systems
status: validated
---
# Moment of Inertia

## Core Idea
The moment of inertia I = Σmᵢrᵢ² (or ∫r² dm for continuous bodies) is the rotational analog of mass — it measures resistance to angular acceleration. Unlike mass, I depends on how mass is distributed relative to the rotation axis: mass farther from the axis contributes more. Standard results include: I = MR² (ring), I = ½MR² (solid disk), I = ⅔MR² (solid sphere shell), I = ⅖MR² (solid sphere). The parallel axis theorem I = I_cm + Md² allows computing I about any axis.

## How It's Best Learned
Memorize key moments of inertia for standard shapes, then apply the parallel axis theorem for off-center axes. Develop physical intuition: a hollow cylinder has greater I than a solid one of the same mass because its mass is farther from the axis.

## Common Misconceptions
- Thinking moment of inertia is a fixed property of an object — it depends entirely on the chosen rotation axis.
- Applying parallel axis theorem with d measured from the wrong axis: d must be measured from the center-of-mass axis.

## Questions

```yaml
- question: "A solid disk and a hollow ring have identical mass M and radius R. Which has the greater moment of inertia about its central axis?"
  type: multiple-choice
  options: ["The solid disk (I = ½MR²)", "The hollow ring (I = MR²)", "They are equal", "It depends on the angular velocity"]
  answer: 1
  explanation: "The hollow ring concentrates all its mass at radius R, giving I = MR². The solid disk spreads mass from 0 to R, so the average r² is less than R², yielding I = ½MR². Because I = ∫r² dm, mass farther from the axis contributes disproportionately more (it scales as r²), so the ring wins."

- question: "The moment of inertia of an object is a fixed property of that object, independent of the chosen rotation axis."
  type: true-false
  answer: false
  explanation: "I depends on both the mass distribution and the choice of rotation axis. The same rod has I = (1/12)ML² when spun about its center but I = (1/3)ML² when spun about one end — a factor of four difference. Moment of inertia is always defined relative to a specific axis."

- question: "You know a solid disk's moment of inertia about its central axis is I_cm = ½MR². Using the parallel axis theorem, what is I about an axis parallel to the center but passing through the rim?"
  type: short-answer
  answer: "(3/2)MR²"
  explanation: "The parallel axis theorem states I = I_cm + Md², where d is the perpendicular distance from the center-of-mass axis to the new axis. Here d = R, so I = ½MR² + MR² = (3/2)MR². A common error is applying the theorem with d measured from an arbitrary axis rather than specifically from the center-of-mass axis."
```

## Explainer

When you learned about torque, you saw that a larger force or a longer lever arm produces more angular acceleration. Moment of inertia is the other side of that relationship: it measures how strongly a body resists angular acceleration. The rotational analog of Newton's second law is τ = Iα, which mirrors F = ma exactly. Just as a heavier object accelerates less for a given force, a larger I means less angular acceleration for a given torque.

The key departure from linear inertia is that I depends not just on total mass but on how that mass is distributed relative to the rotation axis. Each bit of mass dm at distance r from the axis contributes r² dm to the total — the r² means mass farther from the axis matters disproportionately. This is why a figure skater pulls in their arms to spin faster: reducing r reduces I, and since angular momentum Iω is conserved, ω must increase to compensate.

For standard shapes, the integrals ∫r² dm have been worked out. A ring about its central axis gives I = MR² because all mass sits exactly at distance R. A solid disk gives I = ½MR² because mass is spread from 0 to R, pulling the average r² below R². A solid sphere gives I = ⅖MR² for a similar reason. When you encounter a new shape, the right intuition is to ask where the bulk of the mass sits relative to the axis.

The parallel axis theorem extends this toolkit: if you know I_cm about the center-of-mass axis, you can find I about any parallel axis displaced by distance d by adding Md². The theorem follows from expanding the squared-distance term in the integral — it is not a separate postulate but a consequence of the definition. The critical constraint is that the reference axis must pass through the center of mass; you cannot chain the theorem arbitrarily from axis to axis.

Moment of inertia is always relative to a specific axis, not an intrinsic property of the object. A thin rod spun about its center has I = (1/12)ML², but spun about one end it has I = (1/3)ML² — four times larger, because on average the mass is now farther away. Recognizing which axis is relevant, and whether the parallel axis theorem can simplify the calculation, is usually the decisive step in solving rotational dynamics problems.
