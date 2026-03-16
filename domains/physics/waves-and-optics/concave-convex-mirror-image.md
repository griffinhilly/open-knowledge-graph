---
id: concave-convex-mirror-image
title: 'Spherical Mirrors: Focal Length and Image Formation'
domain: physics
course: waves-and-optics
prerequisites:
- id: reflection-angle-geometry
  type: hard
builds-toward:
- lens-equation-magnification-formula
tags:
- mirrors
- optics
stage: formal-systems
status: draft
---

# Spherical Mirrors: Focal Length and Image Formation

## Core Idea
A spherical mirror's focal length f = R/2 (R = radius of curvature) is the distance from the mirror where parallel rays converge (concave) or appear to diverge (convex). The mirror equation 1/s_o + 1/s_i = 1/f relates object and image distances. Magnification m = -s_i/s_o. Concave mirrors form real images (inverted) when s_o > f; convex mirrors form only virtual images (upright).

## How It's Best Learned
Trace rays for objects at different distances to understand when real vs. virtual images form and their orientation.

## Common Misconceptions
A convex mirror cannot form a real image—it always forms a virtual, upright, diminished image.

## Explainer

You already know from reflection-angle geometry that the angle of incidence equals the angle of reflection. Spherical mirrors apply that law to a curved surface, and the curvature introduces something powerful: parallel incoming rays no longer reflect randomly — they all converge toward (or diverge away from) a single point called the **focal point**. For a concave mirror, parallel rays reflect inward and meet at the focal point in front of the mirror. For a convex mirror, they reflect outward and appear to come from a focal point behind the mirror. In both cases, the focal length f = R/2, where R is the radius of the sphere the mirror's surface belongs to — half the radius of curvature.

The **mirror equation** 1/s_o + 1/s_i = 1/f ties together three quantities: the object distance s_o (how far the object sits from the mirror), the image distance s_i (how far the resulting image sits from the mirror), and the focal length. When you solve for s_i, you immediately learn two things: where the image forms and whether it is real or virtual. Positive s_i means the image forms in front of the mirror — where light actually goes after reflecting — and is therefore a **real image**. Negative s_i means the image appears to be behind the mirror, where no light actually travels, making it a **virtual image**.

**Magnification** m = −s_i/s_o tells you both size and orientation. A negative m means the image is inverted; positive m means upright. A |m| > 1 means the image is larger than the object; |m| < 1 means smaller. For a concave mirror, the character of the image depends entirely on where the object sits relative to the focal point: when s_o > f, light has room to converge and a real, inverted image forms. Move the object inside the focal length (s_o < f), and the reflected rays diverge — they never cross in front of the mirror, so you trace them backward and find a virtual, upright, magnified image behind it. This is exactly how a makeup mirror works.

Convex mirrors have a negative focal length (the focal point is behind the mirror), so s_i always comes out negative regardless of where you place the object. The image is always virtual, upright, and smaller than the object — but it covers a wide field of view, which is why convex mirrors are used for security corners and vehicle side mirrors. The key discipline when working these problems is tracking sign conventions rigorously: front of the mirror is positive, back is negative, and the sign of s_i tells you immediately whether the image is real or virtual.
