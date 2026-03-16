---
id: lens-focal-length-diopters
title: Lens Focal Length and Optical Power
domain: physics
course: waves-and-optics
prerequisites:
- id: refraction-interface-snell-relation
  type: hard
builds-toward:
- lens-equation-magnification-formula
tags:
- lenses
- optics
stage: formal-systems
status: draft
---

# Lens Focal Length and Optical Power

## Core Idea
A thin lens's focal length f is defined by where parallel rays converge (or appear to diverge from). Optical power P = 1/f (in diopters, D = m⁻¹) quantifies the lens's strength. Converging lenses have positive f; diverging lenses have negative f. The lensmaker's equation relates f to radius of curvature and refractive index.

## How It's Best Learned
Trace ray paths through a lens using refraction at both surfaces to see how focal length emerges from the surface curvatures.

## Common Misconceptions
Focal length is a property of the lens alone—it does not depend on object distance or how the lens is used.

## Explainer

From your work on refraction, you know that light bends when it crosses an interface between media of different refractive indices. A lens applies this effect twice — once at the front surface and once at the back — to redirect parallel incoming rays toward (or away from) a single point. The **focal length** f is simply the distance from the lens center to that convergence point when the incoming rays are perfectly parallel (effectively from an infinitely distant source). For a converging (convex) lens, rays meet on the far side — positive f. For a diverging (concave) lens, rays spread out and appear to come from a point on the near side — negative f.

The **lensmaker's equation** makes explicit what shapes the focal length: 1/f = (n−1)[1/R₁ − 1/R₂], where n is the glass's refractive index and R₁, R₂ are the radii of curvature of the two surfaces. A lens with more curved surfaces bends light more sharply — shorter focal length. A lens with a higher refractive index also bends light more for the same curvature. This is why high-index lens materials (used in thin eyeglass lenses) can achieve the same focal length with flatter, lighter glass.

**Optical power** P = 1/f, measured in **diopters** (D), converts focal length into a more intuitive quantity: how strongly does the lens bend light? A +2D converging lens focuses parallel rays 0.5 m away. A −4D diverging lens is twice as strong a diverger. Diopters add linearly when lenses are placed in contact — a +3D and −1D lens together give +2D — which is why your optometrist describes your prescription as a single diopter value rather than a focal length.

The most important insight is that focal length belongs to the lens, not the situation. Whether you are projecting an image far away or magnifying something close up, the lens still has the same f. What changes is where the image forms — that is governed by the thin lens equation (which you will encounter next). For now, internalize that focal length is determined entirely by geometry and glass: the curvatures of the surfaces and the refractive index of the material.
