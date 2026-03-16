---
id: couple-moment
title: Couple and Moment of a Couple
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: moment-of-force-2d
  type: hard
builds-toward:
- equivalent-force-systems
tags:
- statics
- couple
- pure moment
- free vector
stage: formal-systems
status: validated
---

# Couple and Moment of a Couple

## Core Idea
A couple consists of two parallel forces of equal magnitude but opposite direction separated by a perpendicular distance d. The net force of a couple is zero, but it produces a pure moment M = F·d that tends to rotate a body without translating it. Critically, the moment of a couple is a free vector — its rotational effect is identical regardless of where the couple is applied on the rigid body. Couples can be added algebraically in 2D or as vectors in 3D.

## How It's Best Learned
Recognize when a loading condition reduces to a pure couple (zero net force). Practice identifying couples embedded within larger force systems before applying superposition to find the total resultant moment.

## Common Misconceptions
- Thinking the moment of a couple depends on the chosen moment point — it does not.
- Confusing a force-couple system (force plus moment at a point) with a pure couple.
- Forgetting that couples can be freely moved anywhere on the body without changing their mechanical effect.

## Explainer

You already know how to compute the moment of a single force about a point: M = r × F, where r is the position vector from the moment center to the force. Notice that this moment depends on *which point you choose* — move the moment center, and r changes, so M changes. This is the normal behavior of a force. A **couple** is special precisely because it escapes this dependence entirely.

A couple consists of two forces: equal in magnitude, parallel, opposite in direction, and separated by a perpendicular distance d. Think of turning a steering wheel with both hands, or twisting a jar lid — two forces, no net push in any direction. The net force is zero (they cancel), so the couple cannot translate the body. But the forces are offset, so they do create rotation. Computing the total moment about *any* point P reveals something remarkable: all the terms involving P's position cancel out. What remains is M = F·d regardless of where P is. The couple's moment is the same no matter what reference point you use.

This is what makes the couple's moment a **free vector**: it has a magnitude and direction, but no fixed point of application. You can move it anywhere on — or off — the rigid body and its mechanical effect is unchanged. This is in sharp contrast to a force, which is a **sliding vector** (it can slide along its line of action but not move off it) or a force-moment pair at a specific point. The freedom of the couple vector is what makes it so useful in analyzing equivalent force systems: when you replace a distributed loading by its resultant, the result is typically a single force plus a free couple moment at any convenient point.

In 2D, couples add algebraically: counterclockwise is positive. In 3D, they add as vectors with direction given by the right-hand rule. When you encounter a loading configuration with zero net force but nonzero net moment, you are looking at a pure couple — recognizing this immediately simplifies the analysis of any problem involving wrench loads, torsion, or gear pairs.
