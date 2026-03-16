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

## Explainer

A beam is a structural element designed to carry loads perpendicular to its length. When you apply loads to a beam, the beam's cross-sections push and pull on one another internally to resist those loads. **Shear force** V at a cross-section is the internal force that prevents one part of the beam from sliding vertically past the other; **bending moment** M is the internal couple that prevents the beam from rotating at that section. These internal forces are invisible — you cannot see them — but they determine whether the beam will survive or fail. The V and M diagrams make the distribution of these internal forces visible along the beam's entire length.

The method of sections operationalizes this: pick any cross-section, make a mental cut, and apply equilibrium to the free body on one side of the cut. Your prerequisite on support reactions gives you all the external forces; the internal V and M at the cut are whatever values are required to keep the cut-off portion in equilibrium. This works but is tedious for many cross-sections. The differential relationships dV/dx = −w(x) and dM/dx = V make it systematic: the shear diagram's slope at any point equals the negative of the distributed load intensity there, and the moment diagram's slope equals the shear value there. You do not need to re-cut for every point — you can trace the entire diagram by integration.

The **area method** makes this integration concrete without calculus. Moving from left to right along the beam: the change in shear between two points equals the negative of the area under the load diagram between those points; the change in moment equals the area under the shear diagram. A concentrated force causes a sudden jump in the shear diagram equal to the force magnitude (upward forces jump V upward on the left-to-right convention). A concentrated couple causes a sudden jump in the moment diagram. The shapes are predictable: uniform load produces linearly varying shear and parabolically varying moment; no load produces constant shear and linearly varying moment. Recognizing these shapes lets you sketch diagrams quickly and catch errors.

The most structurally important point is where the maximum bending moment occurs, because bending moment drives the tensile and compressive stresses that cause beams to fracture. The maximum M occurs where dM/dx = V = 0 — where the shear diagram crosses zero. This may be at midspan for a symmetric simply-supported beam with uniform load (the familiar textbook case), but for unsymmetric loading or cantilevered beams the location shifts. Always locate the zero-crossing of the shear diagram before identifying the critical cross-section. In design, the cross-section at maximum M must be sized to carry that bending without exceeding the material's allowable stress — which connects directly to the flexure formula σ = Mc/I that you will use in mechanics of materials.
