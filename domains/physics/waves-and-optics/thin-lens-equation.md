---
id: thin-lens-equation
title: The Thin Lens Equation
domain: physics
course: waves-and-optics
prerequisites:
- id: thin-lenses
  type: hard
- id: mirror-equation
  type: soft
- id: solving-rational-equations
  type: soft
builds-toward:
- lens-combinations
- optical-instruments
- lensmakers-equation
tags:
- lens equation
- magnification
- focal length
- image distance
stage: formal-systems
status: validated
---

# The Thin Lens Equation

## Core Idea
The thin lens equation 1/f = 1/dₒ + 1/dᵢ is identical in form to the mirror equation and uses the same sign convention: dᵢ positive for a real image on the opposite side of the lens from the object, negative for a virtual image on the same side. Lateral magnification m = −dᵢ/dₒ. For a diverging lens f < 0, and the equation consistently predicts dᵢ < 0 (virtual image) for all positive object distances.

## How It's Best Learned
Measure image distances for a converging lens at five different object distances, plot 1/dᵢ vs 1/dₒ, and extract f from the y-intercept. This graphical approach builds deep intuition for how the variables relate.

## Common Misconceptions
- The lens equation and mirror equation look identical but the sign conventions for dᵢ differ (real image is positive for lenses on the transmission side, for mirrors on the reflection side).
- Students forget that for a virtual image through a lens, the image and object are on the same side.

## Questions

```yaml
- question: "An object is placed 10 cm from a converging lens with a focal length of 15 cm. Where does the image form?"
  type: multiple-choice
  options:
    - "30 cm on the far (transmission) side of the lens — a real, inverted image"
    - "30 cm on the same side as the object — a virtual, upright image"
    - "6 cm on the far side of the lens — a real, inverted image"
    - "No image forms because the object is inside the focal length"
  answer: 1
  explanation: "Using 1/dᵢ = 1/f − 1/dₒ = 1/15 − 1/10 = 2/30 − 3/30 = −1/30, so dᵢ = −30 cm. The negative sign means the image is on the same side as the object — a virtual image. This is the magnifying glass configuration: when the object is closer than the focal length (dₒ < f), dᵢ goes negative, producing an upright, magnified virtual image. Option D is wrong because an image does form — it's just virtual."

- question: "What happens to the image distance dᵢ as an object is moved from far away toward the focal point of a converging lens (approaching from dₒ > f)?"
  type: multiple-choice
  options:
    - "dᵢ decreases toward zero as the image gets closer to the lens"
    - "dᵢ remains constant at twice the focal length"
    - "dᵢ increases without bound — the image recedes toward infinity"
    - "dᵢ becomes negative, indicating the image flips to virtual before dₒ reaches f"
  answer: 2
  explanation: "As dₒ → f from above, 1/dₒ → 1/f, so 1/dᵢ = 1/f − 1/dₒ → 0, meaning dᵢ → ∞. The image races away from the lens indefinitely. At exactly dₒ = f, the rays exit parallel and no image forms at a finite distance. Option D describes what happens when dₒ passes through f and becomes less than f — the image then flips to virtual — but that is not what happens as dₒ approaches f from above."

- question: "A diverging lens can form a real image if the object is placed far enough from the lens."
  type: true-false
  answer: false
  explanation: "For a diverging lens, f < 0. Substituting into 1/dᵢ = 1/f − 1/dₒ: since both 1/f and −1/dₒ are negative (for any positive dₒ), dᵢ is always negative. A diverging lens always produces a virtual image — upright, reduced, and on the same side as the object — regardless of object distance. There is no object placement that produces a real image through a single diverging lens."

- question: "The lateral magnification m = −dᵢ/dₒ predicts that real images formed by a single converging lens are always inverted."
  type: true-false
  answer: true
  explanation: "For a real image formed by a converging lens, the image is on the far (transmission) side, so dᵢ > 0. Object distance dₒ is also positive. Therefore m = −dᵢ/dₒ is negative, indicating an inverted image. This is always true for real images through a single lens: real images are inverted. Virtual images (dᵢ < 0) have positive m and are upright — this is why a magnifying glass and the human eye both produce upright virtual images when used normally."

- question: "A student holds a converging lens close to a page of text and sees an upright, enlarged image of the letters. Explain using the thin lens equation why this image must be virtual."
  type: short-answer
  answer: "For the image to be upright and magnified through a single converging lens, the object must be inside the focal length (dₒ < f). Substituting into 1/dᵢ = 1/f − 1/dₒ: when dₒ < f, 1/dₒ > 1/f, so 1/dᵢ < 0, meaning dᵢ < 0. A negative image distance means the image forms on the same side as the object — not where light actually converges, but where diverging rays appear to come from when you look through the lens. That is the definition of a virtual image."
  explanation: "The sign of dᵢ is the key: positive means a real image (rays actually converge on the far side), negative means a virtual image (rays diverge, and the image is where they appear to originate). For a magnifying glass, the lens is too close to the object for rays to converge on the far side — instead they exit the lens still diverging, and your eye traces them back to an apparent source that is upright and enlarged. The thin lens equation automatically captures this: whenever dₒ < f for a converging lens, dᵢ turns negative."
```

## Explainer

If you've worked through the mirror equation, the thin lens equation will feel immediately familiar: 1/f = 1/dₒ + 1/dᵢ. The algebra is identical. What changes is the physical geometry and the sign conventions, because a lens transmits light rather than reflecting it. The **focal length** f is positive for a converging (convex) lens and negative for a diverging (concave) lens. The **object distance** dₒ is almost always positive (real objects are on the incoming side of the lens). The **image distance** dᵢ is positive when the image forms on the far side of the lens — the transmission side — where rays actually converge, producing a **real image**. It's negative when the image appears to be on the same side as the object, producing a **virtual image** that can only be seen by looking back through the lens.

The equation is best understood through limiting cases. Place the object very far away (dₒ → ∞): then 1/dₒ → 0, so 1/dᵢ = 1/f, meaning dᵢ = f. Parallel rays from a distant object converge at the focal point — which is exactly the definition of focal length. Now place the object at the focal point (dₒ = f): 1/dᵢ = 1/f − 1/f = 0, so dᵢ = ∞. Rays exit the lens parallel — no image forms at a finite distance. Between these extremes, moving the object closer to the focal point pushes the image farther away; moving the object closer than the focal point (dₒ < f) flips dᵢ negative, producing a virtual, magnified image on the same side as the object. This is exactly how a magnifying glass works.

**Lateral magnification** m = −dᵢ/dₒ captures both size and orientation. When m is negative, the image is inverted (real images through a converging lens with dₒ > f are always inverted). When |m| > 1, the image is larger than the object; when |m| < 1, it's smaller. A camera lens forms a tiny inverted real image on the sensor (large dₒ, small dᵢ, m small and negative). A slide projector does the reverse (small dₒ just outside the focal point, large dᵢ, m large and negative — the slide is loaded upside-down on purpose so the projected image appears right-side-up).

For a diverging lens (f < 0), the equation always produces dᵢ < 0 for any positive dₒ — there is no object placement that creates a real image through a diverging lens. The image is always virtual, upright, and smaller than the object, located on the same side as the incoming light. This is why diverging lenses are used to correct nearsightedness: they make parallel incoming rays diverge slightly before they reach the eye's own converging lens, effectively moving the apparent source point to a distance the eye can focus on.
