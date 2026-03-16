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
stage: abstract-reasoning
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

## Explainer

Your prerequisite knowledge of force resultants tells you how to handle forces that translate — push and pull — on objects. But forces also rotate. When you tighten a bolt with a wrench, you are not pushing the bolt sideways; you are rotating it. The **moment of a force** quantifies that rotational tendency. The reference point (the "pivot") is the center around which you are measuring potential rotation. Just as force is the measure of linear push, moment is the measure of rotational push about a chosen point.

The defining insight is that what matters is not where along the force's line you apply it — you could push at the handle's end or halfway down — but rather how far the force's **line of action** is from the pivot. Extend the force vector into an infinite line; drop a perpendicular from your reference point to that line. That perpendicular distance d is the **moment arm**. Moment = Force × moment arm (M = F·d). This formula is exactly what the cross product computes in 2D: if you write M = r × F, the r is any vector from the reference point to any point on the line of action, and the cross product automatically extracts the perpendicular component. Both methods give the same number; use whichever is faster given the geometry.

The critical consequence is the zero-moment case: if the force's line of action passes directly through the reference point, then d = 0, so M = 0. This is not an edge case — it is one of the most frequently used facts in statics problems. When you later analyze rigid-body equilibrium, you will choose reference points strategically to eliminate unknown forces from moment equations (picking the point where an unknown force acts eliminates that unknown, because its moment arm is zero). This makes otherwise unsolvable problems solvable. Developing intuition about which point to sum moments about is a skill that comes from practice.

Sign convention is essential and arbitrary — you just have to commit to one. The universal standard is **counterclockwise positive**. A force that would spin the body counterclockwise about the pivot gets a positive moment; clockwise gets negative. When you apply the cross product M = r × F in 2D, the resulting vector points out of the page for counterclockwise (positive z) and into the page for clockwise (negative z). In a 2D problem you typically just write the scalar result with the appropriate sign. Consistency here matters far more than which convention you pick — mixed conventions within a single problem produce sign errors that are notoriously hard to catch.
