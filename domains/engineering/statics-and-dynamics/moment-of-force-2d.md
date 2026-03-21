---
id: moment-of-force-2d
title: Moment of a Force in 2D
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: force-systems-resultants
  type: hard
- id: torque
  type: soft
- id: cross-product
  type: soft
builds-toward:
- varignons-theorem
- couple-moment
- equilibrium-rigid-bodies
tags:
- statics
- moment
- torque
- rotation
stage: formal-systems
status: validated
---

# Moment of a Force in 2D

## Core Idea
The moment of a force about a point is the tendency of that force to cause rotation about that point, calculated as M = r × F (cross product) or equivalently M = F·d, where d is the perpendicular distance from the point to the force's line of action. In 2D, moments are scalar quantities with sign indicating direction (counterclockwise positive by convention). The moment depends on both the force magnitude and the perpendicular geometry — a force directed through the reference point produces zero moment.

## How It's Best Learned
Compute moments using both the cross product method and the perpendicular distance method and verify the answers agree. Always establish a positive direction convention before starting. Practice identifying the line of action to find the correct perpendicular distance.

## Common Misconceptions
- Using the distance to the point of force application rather than the perpendicular distance to the line of action.
- Sign errors when determining clockwise versus counterclockwise sense.
- Thinking a force that passes through the reference point has a nonzero moment.

## Questions

```yaml
- question: "A 100 N force is applied at point P, which is located 0.8 m from pivot O. However, the force's line of action passes directly through point O. What is the moment of this force about O?"
  type: multiple-choice
  options:
    - "80 N·m, because moment = force × distance to point of application"
    - "0 N·m, because the moment arm (perpendicular distance from O to the line of action) is zero"
    - "100 N·m, because the full force magnitude creates rotation"
    - "It cannot be determined without knowing the force direction"
  answer: 1
  explanation: "When a force's line of action passes through the reference point, the perpendicular distance from the point to the line of action is zero, so M = F × d = 100 × 0 = 0. The distance to the point of application (0.8 m) is irrelevant — the moment arm is always the perpendicular distance from the pivot to the LINE OF ACTION, not to the application point. This is the most common error in moment calculations."

- question: "A wrench handle is 0.4 m long and a 60 N force is applied at its tip at 30° to the handle. What is the correct moment arm to use when calculating the moment about the bolt at the other end?"
  type: multiple-choice
  options:
    - "0.4 m — the distance from the bolt to where the force is applied"
    - "0.4 × cos(30°) = 0.346 m — the component of the handle along the force direction"
    - "0.4 × sin(30°) = 0.2 m — the perpendicular distance from the bolt to the force's line of action"
    - "0.4 / sin(30°) = 0.8 m — the extended line of action length"
  answer: 2
  explanation: "The moment arm is the perpendicular distance from the pivot (bolt) to the force's line of action. When the force makes angle θ with the handle, the perpendicular distance is r × sin(θ) = 0.4 × sin(30°) = 0.2 m. So M = 60 × 0.2 = 12 N·m. Alternatively, using M = r × F with the cross product gives the same result: the cross product automatically extracts the perpendicular component."

- question: "If you slide the point of force application along the force's line of action to a different location, the moment about any given reference point remains unchanged."
  type: true-false
  answer: true
  explanation: "The moment depends only on the force magnitude and the perpendicular distance from the reference point to the LINE OF ACTION — not on where along that line the force is applied. The line of action extends infinitely in both directions; any point on it gives the same line, the same perpendicular distance to the pivot, and therefore the same moment. This principle (called the principle of transmissibility) is fundamental to rigid-body statics."

- question: "The moment of a force about a point depends on the distance from the pivot to the specific point where the force is applied to the body."
  type: true-false
  answer: false
  explanation: "This is the most common misconception in moment calculations. The moment depends on the perpendicular distance from the pivot to the force's LINE OF ACTION, not to the point of application. A force applied at the tip of a wrench versus halfway down the handle will have different moment arms only if moving the application point changes the line of action — and if the force direction stays the same, it usually does. The correct mental model is: extend the force into an infinite line, then measure the perpendicular from the pivot to that line."

- question: "Why is the moment arm defined as the perpendicular distance from the reference point to the force's line of action, rather than simply the distance from the reference point to the point of force application?"
  type: short-answer
  answer: "Rotation depends on how far 'off-center' the force is pushing — that is, what component of the force is acting tangentially rather than radially toward/away from the pivot. Only the perpendicular component creates rotation; a force aimed directly at (or away from) the pivot has zero rotational effect regardless of how far away the application point is. The moment arm captures this by measuring the perpendicular offset of the entire line of action from the pivot. The cross product M = r × F computes this automatically: the cross product of r and F extracts the perpendicular component, which equals F × d where d is the perpendicular distance to the line of action."
  explanation: "This also explains the zero-moment case: when the line of action passes through the pivot, there is no perpendicular offset and the force creates no rotation, no matter how large the force or how far away the application point. This fact is exploited constantly in equilibrium analysis to choose strategic reference points."
```

## Explainer

Your prerequisite knowledge of force resultants tells you how to handle forces that translate — push and pull — on objects. But forces also rotate. When you tighten a bolt with a wrench, you are not pushing the bolt sideways; you are rotating it. The **moment of a force** quantifies that rotational tendency. The reference point (the "pivot") is the center around which you are measuring potential rotation. Just as force is the measure of linear push, moment is the measure of rotational push about a chosen point.

The defining insight is that what matters is not where along the force's line you apply it — you could push at the handle's end or halfway down — but rather how far the force's **line of action** is from the pivot. Extend the force vector into an infinite line; drop a perpendicular from your reference point to that line. That perpendicular distance d is the **moment arm**. Moment = Force × moment arm (M = F·d). This formula is exactly what the cross product computes in 2D: if you write M = r × F, the r is any vector from the reference point to any point on the line of action, and the cross product automatically extracts the perpendicular component. Both methods give the same number; use whichever is faster given the geometry.

The critical consequence is the zero-moment case: if the force's line of action passes directly through the reference point, then d = 0, so M = 0. This is not an edge case — it is one of the most frequently used facts in statics problems. When you later analyze rigid-body equilibrium, you will choose reference points strategically to eliminate unknown forces from moment equations (picking the point where an unknown force acts eliminates that unknown, because its moment arm is zero). This makes otherwise unsolvable problems solvable. Developing intuition about which point to sum moments about is a skill that comes from practice.

Sign convention is essential and arbitrary — you just have to commit to one. The universal standard is **counterclockwise positive**. A force that would spin the body counterclockwise about the pivot gets a positive moment; clockwise gets negative. When you apply the cross product M = r × F in 2D, the resulting vector points out of the page for counterclockwise (positive z) and into the page for clockwise (negative z). In a 2D problem you typically just write the scalar result with the appropriate sign. Consistency here matters far more than which convention you pick — mixed conventions within a single problem produce sign errors that are notoriously hard to catch.
