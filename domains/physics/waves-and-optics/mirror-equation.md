---
id: mirror-equation
title: The Mirror Equation and Magnification
domain: physics
course: waves-and-optics
prerequisites:
- id: spherical-mirrors
  type: hard
builds-toward:
- optical-instruments
tags:
- mirror equation
- magnification
- focal length
- object distance
- image distance
stage: abstract-reasoning
status: validated
---

# The Mirror Equation and Magnification

## Core Idea
The mirror equation 1/f = 1/dₒ + 1/dᵢ relates focal length f, object distance dₒ, and image distance dᵢ. Magnification m = −dᵢ/dₒ gives the size ratio; a negative m means the image is inverted. Sign conventions: distances are positive in front of the mirror (real) and negative behind (virtual); focal length is positive for concave and negative for convex. These same conventions extend directly to the thin lens equation.

## How It's Best Learned
Set up a concave mirror with a lamp as the object, find the real image on a screen, and measure dₒ and dᵢ. Compute f from the mirror equation and compare to the labeled value. Then predict the image location for a different dₒ.

## Common Misconceptions
- Sign errors are extremely common; always define the sign convention explicitly and apply it consistently before substituting numbers.
- m = −1 means the image is real, inverted, and the same size as the object — not that the image is absent.

## Explainer

From studying spherical mirrors, you know how to locate images graphically — drawing the parallel ray, focal ray, and center ray until they converge. The **mirror equation** does the same job algebraically: given the focal length and object position, it calculates the image position precisely without a diagram. The two approaches are complementary; drawing a quick ray diagram to check the algebra is a good habit, especially when the sign of dᵢ is ambiguous.

The equation 1/f = 1/dₒ + 1/dᵢ is deceptively compact. Rearranged to solve for image distance: dᵢ = f·dₒ / (dₒ − f). Consider what happens as you move an object progressively closer to a concave mirror. When dₒ is much greater than f, the denominator is large and dᵢ is just slightly larger than f — the image forms just beyond the focal point. As dₒ approaches 2f, dᵢ also equals 2f and |m| = 1: a real, inverted image the same size as the object. As dₒ shrinks toward f, dᵢ → ∞ — the reflected rays become parallel. When dₒ < f (object inside the focal point), the denominator flips sign: dᵢ is negative, placing the image behind the mirror — **virtual, upright, and magnified**. This is exactly what you see in a makeup or shaving mirror. The mirror equation encodes this entire progression in one formula.

The **magnification** m = −dᵢ/dₒ carries both size and orientation information. The minus sign is a convention: a negative m means the image is inverted relative to the object. The magnitude |m| gives the size ratio — |m| > 1 means the image is larger, |m| < 1 means smaller. If you calculate m = −2, the image is real, inverted, and twice the object's height; if m = +0.5, the image is virtual, upright, and half the height. Both pieces of information — sign and magnitude — are needed to fully describe the image.

Sign conventions are where most errors enter. The rule is consistent: distances measured in the direction of incoming light (in front of the mirror) are positive; distances behind the mirror are negative. Focal length is positive for concave mirrors (which converge reflected rays) and negative for convex mirrors (which diverge them). These same conventions transfer directly to the **thin lens equation**, which is identical in form: 1/f = 1/dₒ + 1/dᵢ. Mastering the mirror equation and its sign system prepares you for all of geometric optics — lenses, lens combinations, and optical instruments — without needing to learn a new framework.
