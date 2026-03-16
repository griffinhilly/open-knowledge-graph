---
id: mirror-image-formation-ray-diagrams
title: Mirror Image Formation and Ray Diagrams
domain: physics
course: waves-and-optics
prerequisites:
- id: reflection-and-law-of-reflection
  type: hard
- id: geometric-optics-ray-approximation
  type: hard
builds-toward:
- spherical-mirrors
tags:
- mirror
- image-formation
- ray-diagram
stage: formal-systems
status: draft
---

# Mirror Image Formation and Ray Diagrams

## Core Idea
The mirror equation (1/f = 1/do + 1/di) and magnification (m = -di/do) apply to both converging (concave) and diverging (convex) mirrors, with sign conventions: concave mirrors have positive f and can form real or virtual images, while convex mirrors have negative f and always form virtual images. Ray diagrams showing three principal rays predict image properties.

## Explainer

You already know that reflection obeys a simple rule: the angle of incidence equals the angle of reflection, measured from the normal to the surface. For a flat mirror, every reflected ray can be traced backward to a single apparent point behind the mirror — the virtual image of the source. Curved mirrors do the same thing, but because the normal direction changes across the mirror surface, different parts of the mirror redirect light differently. This controlled redirection is what allows curved mirrors to focus light or spread it, producing images that flat mirrors cannot.

The **ray diagram** is the tool that makes image location predictable without tracing every possible ray. For any curved mirror, three special rays from an object point are easy to draw: (1) a ray parallel to the optical axis reflects through the focal point; (2) a ray passing through the focal point reflects parallel to the axis; (3) a ray aimed at the center of curvature reflects straight back. Where any two of these three rays converge after reflection — that is the image. If the reflected rays diverge, you extend them backward; they appear to come from a point behind the mirror, forming a **virtual image** (not a real intersection of light, but a perceived source location).

The **mirror equation** 1/f = 1/d_o + 1/d_i encodes this geometry algebraically. The sign convention is: distances measured in front of the mirror (where light actually travels) are positive; distances behind the mirror are negative. A **concave mirror** — like the inside of a bowl — has a positive focal length because the focal point is in front of the surface. It can form real images (d_i > 0) when the object is beyond the focal point, and virtual images (d_i < 0) when the object is inside the focal point. A **convex mirror** — like the outside of a sphere — has a negative focal length; its focal point is behind the surface, so it always forms virtual, diminished, upright images. This is why convex mirrors are used for wide-field surveillance — they show a broad scene, though the images are smaller than reality.

Magnification m = −d_i / d_o tells you both size and orientation. A negative magnification means the image is inverted; positive means upright. Magnification greater than 1 in absolute value means the image is enlarged; less than 1 means diminished. For a concave makeup mirror, you place your face inside the focal length — the image appears virtual, upright, and magnified, precisely because d_i is negative and larger in magnitude than d_o. Learning to read the signs fluently is the key skill: each sign carries physical meaning about whether light really converges there or merely appears to.
