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
- id: reflection-and-law-of-reflection
  type: hard
builds-toward:
- mirror-equation
tags:
- concave mirror
- convex mirror
- focal point
- center of curvature
- real image
stage: formal-systems
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

## Questions

```yaml
- question: "A candle is placed 5 cm in front of a concave mirror with focal length 10 cm (the object is between F and the mirror). What kind of image does the mirror form?"
  type: multiple-choice
  options:
    - "Real, inverted, magnified — because concave mirrors always form real images"
    - "No image — a concave mirror cannot form an image when the object is inside the focal length"
    - "Virtual, upright, magnified — because the reflected rays diverge and appear to come from behind the mirror"
    - "Virtual, inverted, reduced — the same as a convex mirror always produces"
  answer: 2
  explanation: "When an object is between the focal point and a concave mirror, the reflected rays diverge rather than converge — they never meet in front of the mirror. Your eye traces the diverging rays backward to find a virtual image located behind the mirror: upright and larger than the object, like a magnifying mirror. The common misconception is that concave mirrors always make real images — they do only when the object is placed beyond F."

- question: "A store installs a security mirror to monitor a wide area. Which type of mirror is used, and why?"
  type: multiple-choice
  options:
    - "Concave mirror — it magnifies objects, making distant details easier to see"
    - "Convex mirror — it always produces a virtual, upright, reduced image, giving a wider field of view"
    - "Plane mirror — it produces no distortion and allows accurate size estimation"
    - "Convex mirror — because it can form real images that can be projected onto a screen for recording"
  answer: 1
  explanation: "Convex mirrors always produce virtual, upright, and reduced images regardless of object position. The reduction in image size means a wide sweep of the scene fits within the mirror's field of view — exactly what security surveillance requires. The cost is that objects appear farther away. Concave mirrors cannot serve this purpose: they produce inverted real images for most object distances and have a narrower, not wider, field of view."

- question: "A real image formed by a concave mirror is located in front of the mirror and can be projected onto a screen placed at the image location."
  type: true-false
  answer: true
  explanation: "This is what 'real' means in optics: reflected rays actually converge at the image location. A screen placed there displays a focused image because light physically arrives at that point. Real images form in front of a concave mirror — same side as the object and incoming light — not behind it. Virtual images, by contrast, form where rays only appear to diverge from; no screen can capture them."

- question: "A concave mirror usually produces a real image, regardless of where the object is placed."
  type: true-false
  answer: false
  explanation: "A concave mirror produces a real image only when the object is placed beyond the focal point F. When the object is between F and the mirror surface, the reflected rays diverge and form a virtual, upright, magnified image behind the mirror. When the object is exactly at F, the reflected rays emerge parallel and no image forms at all. Object position relative to F completely determines whether the image is real or virtual."

- question: "Explain the difference between a real image and a virtual image in terms of what the reflected light rays actually do."
  type: short-answer
  answer: "A real image forms where reflected rays actually converge — light physically arrives at that point, so a screen placed there shows a focused image. A virtual image forms where reflected rays appear to diverge from when traced backward — no light actually arrives at that point, so no screen can capture it; only an eye looking into the mirror perceives it."
  explanation: "The distinction is whether the rays actually meet or only appear to meet. For a concave mirror with object beyond F: reflected rays converge in front of the mirror — real image. For a concave mirror with object inside F, or any convex mirror: reflected rays diverge, but their backward extensions meet behind the mirror — virtual image. This determines whether the image can be projected, whether it is inverted or upright, and which sign conventions apply in the mirror equation."
```

## Explainer

You already know from the law of reflection that any incident ray bounces off a surface such that the angle of incidence equals the angle of reflection, measured from the normal. For a flat mirror, all normals are parallel, so reflected rays that originate from a single point on an object all diverge after reflection — your eye traces them backward and locates the virtual image behind the mirror. A spherical mirror takes this same law and applies it to a curved surface, where the normals point in different directions at different points. That curvature is what allows reflected rays to converge rather than diverge — and convergence is what creates a real image.

For a **concave mirror**, the reflective surface curves inward like a bowl. Rays arriving parallel to the optical axis each obey the law of reflection at their local normal — and because all normals point toward the center of curvature C, those reflected rays all pass through (or close to) the focal point F, located halfway between the mirror and C at distance f = R/2. This is the key geometry: the focal length is determined entirely by the radius of curvature, and R/2 is not an approximation for small apertures — it is exact by the geometry of reflection. An object placed beyond F will produce a **real image**: reflected rays actually converge in front of the mirror, where you could place a screen and see a focused image. An object placed between F and the mirror surface produces a **virtual image** behind the mirror, just as a flat mirror does — but larger and still upright.

For a **convex mirror**, the surface curves outward, so the normals diverge rather than converge. Reflected rays always spread apart after reflection — they never cross in front of the mirror. Your eye traces them backward and finds a virtual image located behind the mirror. The image is always upright and smaller than the object. This reduced field of view is precisely why convex mirrors appear on car side mirrors and in store security: a single convex mirror can show a wide sweep of the scene in one compact view, at the cost of making objects appear farther away than they are (hence the warning "objects in mirror are closer than they appear").

The three principal rays are a systematic tool for locating images without equations: (1) a ray parallel to the axis reflects through F; (2) a ray through F reflects parallel to the axis; (3) a ray aimed at C reflects straight back on itself (since it hits the surface perpendicular to its normal). Where any two of these reflected rays intersect — or where their backward extensions intersect — is the image location. Practicing these ray diagrams across all object positions for a concave mirror (beyond C, at C, between C and F, at F, between F and mirror) builds a complete picture of how image properties shift: from real, inverted, reduced (far away) to real, inverted, same size (at C) to real, inverted, enlarged (between C and F) to no image (at F) to virtual, upright, enlarged (inside F). The mirror equation you will derive next formalizes this entire catalog algebraically.

