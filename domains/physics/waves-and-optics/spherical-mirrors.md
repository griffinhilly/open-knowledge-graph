---
id: spherical-mirrors
title: 'Spherical Mirrors: Concave and Convex'
domain: physics
course: waves-and-optics
prerequisites:
- id: reflection-law
  type: hard
- id: plane-mirrors
  type: soft
builds-toward:
- mirror-equation
tags:
- concave mirror
- convex mirror
- focal point
- center of curvature
- real image
stage: abstract-reasoning
status: validated
---

# Spherical Mirrors: Concave and Convex

## Core Idea
A spherical mirror has a center of curvature C and a focal point F at half the radius of curvature (f = R/2). Concave (converging) mirrors can form both real and virtual images depending on object position; convex (diverging) mirrors always form virtual, upright, reduced images. The three principal rays used for ray diagrams are: parallel to axis → through F; through F → parallel to axis; through C → straight back.

## How It's Best Learned
Construct ray diagrams for object distances greater than, equal to, and less than the focal length of a concave mirror. Observe how image type (real/virtual), orientation (upright/inverted), and size (magnified/reduced) change.

## Common Misconceptions
- A real image forms in front of a concave mirror, not behind it, and can be projected on a screen.
- Convex mirrors always form virtual images — they are useful precisely because they always show an upright, wide-field view.

## Explainer

You already know from the law of reflection that any incident ray bounces off a surface such that the angle of incidence equals the angle of reflection, measured from the normal. For a flat mirror, all normals are parallel, so reflected rays that originate from a single point on an object all diverge after reflection — your eye traces them backward and locates the virtual image behind the mirror. A spherical mirror takes this same law and applies it to a curved surface, where the normals point in different directions at different points. That curvature is what allows reflected rays to converge rather than diverge — and convergence is what creates a real image.

For a **concave mirror**, the reflective surface curves inward like a bowl. Rays arriving parallel to the optical axis each obey the law of reflection at their local normal — and because all normals point toward the center of curvature C, those reflected rays all pass through (or close to) the focal point F, located halfway between the mirror and C at distance f = R/2. This is the key geometry: the focal length is determined entirely by the radius of curvature, and R/2 is not an approximation for small apertures — it is exact by the geometry of reflection. An object placed beyond F will produce a **real image**: reflected rays actually converge in front of the mirror, where you could place a screen and see a focused image. An object placed between F and the mirror surface produces a **virtual image** behind the mirror, just as a flat mirror does — but larger and still upright.

For a **convex mirror**, the surface curves outward, so the normals diverge rather than converge. Reflected rays always spread apart after reflection — they never cross in front of the mirror. Your eye traces them backward and finds a virtual image located behind the mirror. The image is always upright and smaller than the object. This reduced field of view is precisely why convex mirrors appear on car side mirrors and in store security: a single convex mirror can show a wide sweep of the scene in one compact view, at the cost of making objects appear farther away than they are (hence the warning "objects in mirror are closer than they appear").

The three principal rays are a systematic tool for locating images without equations: (1) a ray parallel to the axis reflects through F; (2) a ray through F reflects parallel to the axis; (3) a ray aimed at C reflects straight back on itself (since it hits the surface perpendicular to its normal). Where any two of these reflected rays intersect — or where their backward extensions intersect — is the image location. Practicing these ray diagrams across all object positions for a concave mirror (beyond C, at C, between C and F, at F, between F and mirror) builds a complete picture of how image properties shift: from real, inverted, reduced (far away) to real, inverted, same size (at C) to real, inverted, enlarged (between C and F) to no image (at F) to virtual, upright, enlarged (inside F). The mirror equation you will derive next formalizes this entire catalog algebraically.

