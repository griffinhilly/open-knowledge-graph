---
id: mirror-equation
title: The Mirror Equation and Magnification
domain: physics
course: waves-and-optics
prerequisites:
- id: spherical-mirrors
  type: hard
- id: geometric-optics-ray-approximation
  type: soft
builds-toward:
- optical-instruments
tags:
- mirror equation
- magnification
- focal length
- object distance
- image distance
stage: formal-systems
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

## Questions

```yaml
- question: "An object is placed 10 cm in front of a concave mirror with focal length f = 15 cm. Where does the image form?"
  type: multiple-choice
  options:
    - "30 cm in front of the mirror — real and inverted"
    - "30 cm behind the mirror — virtual and upright"
    - "At the focal point, 15 cm in front of the mirror"
    - "6 cm in front of the mirror — real and inverted"
  answer: 1
  explanation: "Using 1/dᵢ = 1/f − 1/dₒ = 1/15 − 1/10 = 2/30 − 3/30 = −1/30, so dᵢ = −30 cm. The negative sign means the image is behind the mirror — virtual and upright. This is the 'makeup mirror' case: when the object is closer than the focal length, the concave mirror acts as a magnifier, producing a virtual, upright, enlarged image. The most common error is forgetting that a negative dᵢ means virtual (behind the mirror), not 'no image.'"

- question: "A concave mirror produces an image with magnification m = +2. What can you conclude about this image?"
  type: multiple-choice
  options:
    - "The image is real, inverted, and twice the object's height"
    - "The image is virtual, upright, and twice the object's height"
    - "The image is real, upright, and twice the object's height — real images are always upright"
    - "The image is virtual, inverted, and half the object's height"
  answer: 1
  explanation: "Magnification m = −dᵢ/dₒ. A positive m means dᵢ is negative (image behind mirror → virtual) and the image is upright. |m| = 2 means the image is twice the object's size. Option A is wrong because negative m (not positive) indicates an inverted, real image. Option C contains a dangerous misconception: real images formed by mirrors are always inverted, never upright."

- question: "A magnification of m = −1 means no image is formed by the mirror."
  type: true-false
  answer: false
  explanation: "m = −1 means the image is real, inverted, and exactly the same size as the object. The negative sign indicates inversion (not absence), and |m| = 1 means the image height equals the object height. This occurs when dₒ = dᵢ = 2f — the object is at the center of curvature. It is one of the most instructive cases for calibrating how the mirror equation works, not a sign that something has gone wrong."

- question: "For a convex mirror, the focal length is negative, because reflected rays diverge rather than converge to a real focal point."
  type: true-false
  answer: true
  explanation: "A convex mirror's surface curves away from the incoming light, causing reflected rays to diverge. They appear to come from a point behind the mirror — the virtual focus — rather than converging to a point in front. By the sign convention (distances in front of the mirror are positive), a focal point behind the mirror gets a negative f. This is why convex mirrors always produce virtual, upright, diminished images and have positive dᵢ in the mirror equation only when... wait, actually dᵢ is negative for convex mirrors too. The key: f < 0 for convex mirrors consistently gives dᵢ < 0, confirming the image is always virtual."

- question: "Why does an object placed just inside the focal point of a concave mirror produce a large, virtual, upright image rather than a real, inverted one?"
  type: short-answer
  answer: "When dₒ < f, the denominator in dᵢ = f·dₒ/(dₒ − f) becomes negative (since dₒ − f < 0), making dᵢ negative. Negative dᵢ means the image is behind the mirror — virtual and upright. Physically, the reflected rays are diverging rather than converging: they spread out after reflection and never meet in front of the mirror. Your eye (or a lens) can trace them backward to an apparent point behind the mirror, which is where the virtual image appears. As dₒ approaches f from outside, the real image flies off to infinity; as soon as dₒ drops below f, the image 'wraps around' and appears enlarged behind the mirror."
  explanation: "This is the principle behind makeup mirrors, magnifying shaving mirrors, and dental mirrors: a concave mirror with the object close inside the focal point acts as a magnifier, producing a convenient virtual, upright, enlarged image. The sign of dᵢ from the mirror equation tells you everything: positive = real (in front), negative = virtual (behind)."
```

## Explainer

From studying spherical mirrors, you know how to locate images graphically — drawing the parallel ray, focal ray, and center ray until they converge. The **mirror equation** does the same job algebraically: given the focal length and object position, it calculates the image position precisely without a diagram. The two approaches are complementary; drawing a quick ray diagram to check the algebra is a good habit, especially when the sign of dᵢ is ambiguous.

The equation 1/f = 1/dₒ + 1/dᵢ is deceptively compact. Rearranged to solve for image distance: dᵢ = f·dₒ / (dₒ − f). Consider what happens as you move an object progressively closer to a concave mirror. When dₒ is much greater than f, the denominator is large and dᵢ is just slightly larger than f — the image forms just beyond the focal point. As dₒ approaches 2f, dᵢ also equals 2f and |m| = 1: a real, inverted image the same size as the object. As dₒ shrinks toward f, dᵢ → ∞ — the reflected rays become parallel. When dₒ < f (object inside the focal point), the denominator flips sign: dᵢ is negative, placing the image behind the mirror — **virtual, upright, and magnified**. This is exactly what you see in a makeup or shaving mirror. The mirror equation encodes this entire progression in one formula.

The **magnification** m = −dᵢ/dₒ carries both size and orientation information. The minus sign is a convention: a negative m means the image is inverted relative to the object. The magnitude |m| gives the size ratio — |m| > 1 means the image is larger, |m| < 1 means smaller. If you calculate m = −2, the image is real, inverted, and twice the object's height; if m = +0.5, the image is virtual, upright, and half the height. Both pieces of information — sign and magnitude — are needed to fully describe the image.

Sign conventions are where most errors enter. The rule is consistent: distances measured in the direction of incoming light (in front of the mirror) are positive; distances behind the mirror are negative. Focal length is positive for concave mirrors (which converge reflected rays) and negative for convex mirrors (which diverge them). These same conventions transfer directly to the **thin lens equation**, which is identical in form: 1/f = 1/dₒ + 1/dᵢ. Mastering the mirror equation and its sign system prepares you for all of geometric optics — lenses, lens combinations, and optical instruments — without needing to learn a new framework.
