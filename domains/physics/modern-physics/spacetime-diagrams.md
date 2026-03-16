---
id: spacetime-diagrams
title: Spacetime Diagrams and Minkowski Geometry
domain: physics
course: modern-physics
prerequisites:
- id: special-relativity-postulates
  type: hard
- id: kinematics-2d
  type: soft
builds-toward:
- simultaneity-different-reference-frames
- time-dilation-clock-rates
tags:
- special-relativity
- visualization
- spacetime
stage: advanced
status: draft
---

# Spacetime Diagrams and Minkowski Geometry

## Core Idea
Spacetime diagrams represent events in a coordinate system where time and space are plotted on orthogonal axes, allowing visual representation of relativity concepts. Worldlines—the paths of objects through spacetime—become straight or curved lines depending on acceleration. The Minkowski metric reveals that proper distances in spacetime are conserved across reference frames, providing geometric insight into Lorentz invariance.

## Explainer

You already know from kinematics that you can draw a position-time graph: horizontal axis is space, vertical axis is time, and a moving object traces a line whose slope is 1/v. A **spacetime diagram** (also called a Minkowski diagram) does exactly this, but it takes special relativity seriously. We conventionally plot *ct* on the vertical axis (so that light, traveling at speed c, always traces a 45° line) and *x* on the horizontal. Every physical event is a point on this diagram. Every object carves out a continuous path through spacetime called its **worldline** — a stationary object traces a vertical line; a moving object tilts its worldline; a light ray moves at exactly 45°.

The postulates of special relativity — that light speed is the same in every inertial frame, and that no object travels faster than light — translate directly into a geometric constraint: **no worldline can be tilted more than 45° from vertical**. This gives rise to the **light cone**, the set of 45° lines emanating from any event. Events inside the cone (closer to vertical) are timelike-separated: they can causally influence each other. Events outside the cone are spacelike-separated: no signal can reach one from the other, which is why their temporal ordering is frame-dependent. The light cone is the boundary of causality, made visible.

The deeper geometry is encoded in the **Minkowski metric**: the spacetime interval s² = c²t² − x² (in one spatial dimension) is an invariant. Ordinary spatial distance is not conserved under Lorentz boosts — different observers disagree on lengths and times separately. But they all agree on s². This is the relativistic analogue of how spatial rotations change x and y individually, but preserve x² + y². Lorentz boosts are "rotations" in spacetime — hyperbolic rotations that mix the time and space coordinates while preserving s². A worldline with s² > 0 is **timelike** (can be traversed by a massive particle), s² = 0 is **lightlike** (photon), and s² < 0 is **spacelike** (cannot be traversed causally).

Spacetime diagrams make several hard concepts visually immediate. **Time dilation** appears as a stretched vertical axis for a moving frame: the moving clock ticks fewer times over the same coordinate-time interval. **Length contraction** appears as compressed horizontal lengths. Most strikingly, **relativity of simultaneity** — the fact that two spatially separated events that are simultaneous in one frame are not simultaneous in another — is visible as a tilting of the simultaneity lines (lines of constant t' in the moving frame are not horizontal). These are not illusions or paradoxes; they are the geometry of spacetime working exactly as the postulates demand.
