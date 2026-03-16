---
id: thin-lenses-focal-length
title: Thin Lenses and Focal Length
domain: physics
course: waves-and-optics
prerequisites:
- id: geometric-optics-ray-approximation
  type: hard
- id: refraction-and-snells-law
  type: hard
builds-toward:
- thin-lens-equation
- lensmakers-equation
tags:
- thin-lens
- focal-length
- converging-diverging
stage: formal-systems
status: draft
---

# Thin Lenses and Focal Length

## Core Idea
A thin lens is a transparent optical element that refracts light at two surfaces. A converging lens (positive f) bends rays toward the focal point; a diverging lens (negative f) bends rays away. Focal length f is the distance from the lens where parallel rays converge (or appear to diverge). Lens power P = 1/f (in diopters) quantifies the strength of focusing.

## Explainer

You already know two things that are all you need to understand thin lenses: the geometric optics ray approximation (light travels in straight rays, bending only at interfaces) and Snell's law (rays bend toward the normal when entering a denser medium and away from it when exiting). A lens is simply two curved refracting surfaces in close succession. Each surface bends the ray a little according to Snell's law; the combined effect determines where parallel incoming rays end up.

Consider a **converging (convex) lens** with both surfaces curving outward. A ray entering near the top of the lens strikes the first surface tilted toward the normal, bends downward (toward the optical axis), crosses the lens, and bends downward again at the exit surface. A ray entering at the center passes through without bending because it hits both surfaces at normal incidence. The result: all rays entering the lens parallel to the axis converge to a single point on the other side — the **focal point**. The distance from the lens center to this point is the **focal length** *f*. The focal length is positive for a converging lens: parallel light comes to a real focus on the far side.

A **diverging (concave) lens** curves inward. The same analysis reverses: parallel rays entering the lens are bent *away* from the axis and emerge spreading outward. Tracing those diverging rays backward (just as you did with virtual images in plane mirrors) reveals that they appear to diverge from a point on the *same* side as the incoming light — a virtual focal point. The focal length is negative for a diverging lens. The sign convention is consistent: positive *f* means converging power, real focus on the transmission side; negative *f* means diverging power, virtual focus on the incoming side.

**Lens power** P = 1/f measured in diopters (m⁻¹) quantifies how strongly a lens bends light. A short focal length means strong bending — high power. A long focal length means gentle bending — low power. This is why your optometrist prescribes lenses in diopters: +2.0 D is a converging lens with f = 0.5 m used to correct farsightedness; −3.0 D is a diverging lens with f ≈ 0.33 m used to correct nearsightedness. Powers add when lenses are placed in contact, which is why compound lenses in cameras and telescopes combine multiple elements to achieve a desired total power with fewer aberrations than a single thick lens could provide.
