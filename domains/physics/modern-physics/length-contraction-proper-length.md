---
id: length-contraction-proper-length
title: Length Contraction and Proper Length
domain: physics
course: modern-physics
prerequisites:
- id: relativity-of-simultaneity
  type: hard
- id: length-contraction
  type: soft
tags:
- special-relativity
- spacetime
- length
stage: abstract-reasoning
status: draft
---

# Length Contraction and Proper Length

## Core Idea
Objects moving relative to an observer appear contracted in the direction of motion by a factor of 1/γ. The proper length (length measured in the object's rest frame) is the maximum; all other observers measure shorter lengths. Proper length is an invariant property defined only in the object's rest frame.

## Explainer

From the relativity of simultaneity, you know that two events that are simultaneous in one reference frame are not simultaneous in another frame moving relative to the first. Length contraction is a direct consequence of this, not a separate postulate. To measure the length of a moving object, you must record the positions of its two ends *at the same moment*. But "at the same moment" is frame-dependent. What counts as simultaneous in your frame is not simultaneous in the object's frame, and this mismatch is exactly what produces the disagreement about length.

Here is the argument made concrete. Imagine a rod of **proper length** L₀ at rest in frame S'. Proper length is the length measured in the rest frame — by observers who can leisurely measure both ends without worrying about the rod moving between measurements. Now in frame S, the rod moves at speed v along the x-axis. To measure its length in S, you note the position of the front end and the back end simultaneously (by S's clocks). But because of the relativity of simultaneity, those two position measurements are *not* simultaneous according to S' — the frame in which the rod is at rest. The Lorentz transformation works out to give L = L₀/γ, where γ = 1/√(1 − v²/c²) ≥ 1. The moving rod appears shorter by the factor 1/γ.

Notice that γ ≥ 1 always, so L = L₀/γ ≤ L₀. The proper length is always the *maximum* — all other observers, moving relative to the rod, measure shorter lengths. Also notice: contraction occurs *only in the direction of motion*. The rod's width and height are unchanged; only the dimension parallel to **v** is contracted. A cube moving at relativistic speed becomes a flat slab in the direction of travel, but its cross-section perpendicular to the motion remains square. This asymmetry traces directly to how the Lorentz transformation mixes space and time coordinates: only the coordinate along the motion is transformed, not the transverse coordinates.

The concept of **proper length** is what makes the physics invariant even though measured lengths are not. Every inertial observer agrees on what the proper length is — it is an intrinsic property of the object — even though they disagree on its coordinate length in their own frame. Similarly, **proper time** (your earlier prerequisite) is the time measured in the object's rest frame: the maximum time between two events on its worldline. Length contraction and time dilation are not contradictions or paradoxes; they are different facets of the same geometric fact about spacetime — that different inertial observers slice the same four-dimensional spacetime structure along different spatial and temporal hyperplanes.
