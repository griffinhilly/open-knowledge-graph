---
id: lens-equation-magnification-formula
title: Thin Lens Equation and Image Formation
domain: physics
course: waves-and-optics
prerequisites:
- id: lens-focal-length-diopters
  type: hard
- id: concave-convex-mirror-image
  type: soft
builds-toward:
- combined-optical-system-magnification
tags:
- lenses
- optics
- image
stage: formal-systems
status: draft
---

# Thin Lens Equation and Image Formation

## Core Idea
The thin lens equation 1/s_o + 1/s_i = 1/f relates object distance, image distance, and focal length. Magnification m = -s_i/s_o is positive (upright image) when m > 0 and negative (inverted) when m < 0. Real images form when s_i > 0 (converging lens with s_o > f); virtual images form when s_i < 0. These relationships are identical to mirror equations, reflecting the mathematical duality between reflection and refraction.

## Explainer

From your work on focal length and diopters, you know that a converging lens bends parallel incoming rays to converge at the focal point, a distance f behind the lens. The thin lens equation extends this: what happens when light doesn't come from infinity? When an object sits at a finite distance s_o, the rays arriving at the lens are slightly diverging rather than parallel. The lens still bends them toward a focus, but that focus lands further away than f. The **thin lens equation**, 1/s_o + 1/s_i = 1/f, captures this relationship precisely.

A useful way to read the equation: think of 1/f as the converging power the lens provides, and 1/s_o as the "divergence penalty" from the object being at a finite distance. The image distance s_i is what's left after the lens overcomes that divergence. As s_o decreases toward f, s_i increases toward infinity — the image "goes to infinity" when the object sits exactly at the focal point, which means outgoing rays are parallel. This is how a slide projector works: place the slide just outside the focal point, and the image forms far away on a distant screen.

**Magnification** m = −s_i / s_o captures two things at once. The magnitude |m| is the size ratio: if |m| = 3, the image is three times taller than the object. The sign tells you orientation. The negative sign convention means that **real images** — formed on the far side of a converging lens when s_o > f — are inverted (m is negative). A **virtual image** — formed on the same side as the object when s_o < f, as with a magnifying glass held close — is upright (m is positive). When you hold a magnifying glass over text and see a larger upright image, you're looking at a virtual image; when a projector casts an inverted image on a screen, that's a real image.

If you studied the concave mirror equation (1/d_o + 1/d_i = 1/f), you'll recognize the identical structure. The mathematical duality between lenses and mirrors is not a coincidence — both redirect rays using a surface characterized by a focal length, and the geometry produces the same algebraic form. The key difference in application: for a converging lens, real images form on the far (transmission) side, s_i > 0; for a concave mirror, real images form on the front (reflection) side. Track the sign conventions carefully for each geometry, and the same equation does all the work.
