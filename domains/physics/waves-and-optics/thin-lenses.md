---
id: thin-lenses
title: 'Thin Lenses: Converging and Diverging'
domain: physics
course: waves-and-optics
prerequisites:
- id: refraction-intro
  type: hard
- id: snells-law
  type: soft
builds-toward:
- thin-lens-equation
- lens-combinations
- optical-instruments
tags:
- thin lens
- converging lens
- diverging lens
- focal point
- principal axis
stage: abstract-reasoning
status: validated
---

# Thin Lenses: Converging and Diverging

## Core Idea
A thin lens refracts light at two surfaces such that parallel rays converge to (or diverge from) a focal point. Converging (convex) lenses have positive focal length and can form real or virtual images; diverging (concave) lenses have negative focal length and always form virtual, upright, reduced images. The three principal rays for lenses parallel the rays used for mirrors: parallel ray, focal ray, and central ray through the optical center.

## How It's Best Learned
Use a converging lens to project an image of a distant window onto a sheet of paper and measure f. Then draw ray diagrams for objects at dₒ > 2f, dₒ = 2f, f < dₒ < 2f, and dₒ < f, tabulating image properties systematically.

## Common Misconceptions
- The 'thin lens' approximation assumes lens thickness is negligible compared to focal length; thick lenses require a more complex model.
- Diverging lenses cannot form real images, ever — a common exam trap.

## Explainer

You already know from refraction that light bends when it crosses from one medium into another, with the bending angle determined by Snell's law and the refractive indices involved. A lens is simply two curved refracting surfaces working together to redirect light in a controlled and predictable way. The **thin lens approximation** treats both surfaces as coincident — valid when lens thickness is much smaller than its focal length — which lets us ignore the small displacement between entry and exit refractions and treat the whole lens as a single, instantaneous bending element.

The defining concept is the **focal point**. For a **converging lens** (thicker at center, like a magnifying glass), all rays arriving parallel to the **optical axis** are refracted and meet at a single point on the other side — the focal point F. The distance from the lens center to F is the **focal length** f, which is positive for converging lenses. A **diverging lens** (thinner at center) bends rays outward, so parallel incoming rays appear to *come from* a focal point on the same side they entered — a virtual focal point, giving a negative focal length.

Ray diagrams give you an exact geometric method for finding image location and properties. Three principal rays are sufficient: (1) a ray entering parallel to the optical axis exits through F on the far side; (2) a ray entering through F on the near side exits parallel to the axis; (3) a ray passing through the optical center is undeviated. Where any two of these rays meet is where the image forms. If they diverge after the lens and only their backward extensions meet, the image is virtual — located on the same side as the object.

For a converging lens, image character depends sharply on object distance relative to f. With the object beyond 2f, the image is real, inverted, and reduced. Between f and 2f, it's real, inverted, and magnified — the configuration used in projectors. Inside f, rays diverge after the lens, and you see a virtual, upright, magnified image on the same side as the object — exactly how a magnifying glass works. A diverging lens, by contrast, always produces virtual, upright, reduced images regardless of object distance; since it never converges rays to a point, it can never form a real image. This is a firm rule worth memorizing: diverging lens → virtual image, always.
