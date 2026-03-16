---
id: lens-image-formation-ray-diagrams
title: Lens Image Formation and Ray Diagrams
domain: physics
course: waves-and-optics
prerequisites:
- id: thin-lens-equation
  type: hard
builds-toward:
- optical-instruments
tags:
- image-formation
- lens
- ray-diagram
stage: formal-systems
status: draft
---

# Lens Image Formation and Ray Diagrams

## Core Idea
Thin lens equation (1/f = 1/do + 1/di) and magnification (m = -di/do) predict image location, size, and orientation. Converging lenses form real, inverted images when objects are beyond the focal point, and virtual, upright magnified images when objects are closer than f. Diverging lenses always form virtual, upright, diminished images. Ray diagrams using principal rays visualize these relationships.

## Explainer

You already know the thin lens equation: 1/f = 1/do + 1/di, where f is focal length, do is object distance, and di is image distance. The equation gives you numbers, but **ray diagrams** give you the geometry that makes those numbers make sense. A ray diagram traces three special rays through the lens to locate the image visually.

For a **converging lens** (positive f), the three principal rays are: (1) a ray parallel to the optical axis, which bends through the far focal point after the lens; (2) a ray through the lens center, which passes straight without bending; (3) a ray through the near focal point, which emerges parallel to the axis. Where all three rays meet on the far side of the lens is where the **real image** forms — inverted and projectable onto a screen. This geometry applies whenever the object is farther than one focal length from the lens (do > f). When the object is closer than f, the three rays diverge after the lens; tracing them backward, they appear to originate from a point on the same side as the object — a **virtual image**, upright and magnified, like what you see through a magnifying glass.

A **diverging lens** (negative f) always bends rays outward, spreading them apart. The principal rays for a diverging lens, traced backward on the exit side, always converge to a virtual, upright, diminished image on the same side as the object — regardless of where the object is. This is why a diverging lens cannot project an image but is used in corrective lenses for nearsightedness: it spreads incoming light so the eye's own lens can focus it on the retina.

The magnification equation m = −di/do ties the geometry to numbers. A negative m means the image is inverted (real image from a converging lens); positive m means upright (virtual image). |m| > 1 means larger than the object; |m| < 1 means smaller. A slide projector uses a converging lens with film placed just beyond one focal length: di is much larger than do, so |m| is large and negative — the projected image is greatly enlarged and inverted, which is why film must be loaded upside-down. A camera does the reverse: the subject is far away (do >> f), so di is only slightly larger than f, giving a small, real, inverted image on the sensor.
