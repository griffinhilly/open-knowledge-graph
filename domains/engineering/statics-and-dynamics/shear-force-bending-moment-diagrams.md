---
id: shear-force-bending-moment-diagrams
title: Shear Force and Bending Moment Diagrams
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: distributed-loads-beams
  type: hard
- id: support-reactions-beams
  type: hard
builds-toward:
- rigid-body-kinetics-force-acceleration
tags:
- statics
- beams
- shear force
- bending moment
- V and M diagrams
stage: formal-systems
status: draft
---

# Shear Force and Bending Moment Diagrams

## Core Idea
Shear force (V) and bending moment (M) diagrams graphically display the internal forces along a beam's length, revealing the locations and magnitudes of maximum internal loading. At any cross section, the internal shear V and moment M are found by summing forces and moments on a free body to one side of the cut. The key differential relationships are dV/dx = -w(x) and dM/dx = V, where w(x) is the distributed load intensity. These relationships mean that the shear diagram is the negative integral of the loading diagram, and the moment diagram is the integral of the shear diagram. Concentrated forces cause jumps in the shear diagram; concentrated couples cause jumps in the moment diagram. The maximum bending moment typically occurs where the shear diagram crosses zero.

## How It's Best Learned
Find all support reactions first, then move along the beam from left to right, constructing the V and M diagrams using the area method: the change in shear between two points equals the negative of the area under the load diagram, and the change in moment equals the area under the shear diagram. Check your work by verifying that V and M both return to zero at the free end (or match the known reaction at the right support).

## Common Misconceptions
- Forgetting the sign convention: the standard convention is that positive shear causes clockwise rotation of the beam element, and positive bending causes the beam to sag (concave up).
- Missing the jump in the moment diagram at the location of an applied couple (external moment).
- Assuming the maximum moment always occurs at midspan — it occurs where V = 0 or changes sign, which depends on the loading configuration.
