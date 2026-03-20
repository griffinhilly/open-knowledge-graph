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

## Explainer

If you've worked through the mirror equation, the thin lens equation will feel immediately familiar: 1/f = 1/dₒ + 1/dᵢ. The algebra is identical. What changes is the physical geometry and the sign conventions, because a lens transmits light rather than reflecting it. The **focal length** f is positive for a converging (convex) lens and negative for a diverging (concave) lens. The **object distance** dₒ is almost always positive (real objects are on the incoming side of the lens). The **image distance** dᵢ is positive when the image forms on the far side of the lens — the transmission side — where rays actually converge, producing a **real image**. It's negative when the image appears to be on the same side as the object, producing a **virtual image** that can only be seen by looking back through the lens.

The equation is best understood through limiting cases. Place the object very far away (dₒ → ∞): then 1/dₒ → 0, so 1/dᵢ = 1/f, meaning dᵢ = f. Parallel rays from a distant object converge at the focal point — which is exactly the definition of focal length. Now place the object at the focal point (dₒ = f): 1/dᵢ = 1/f − 1/f = 0, so dᵢ = ∞. Rays exit the lens parallel — no image forms at a finite distance. Between these extremes, moving the object closer to the focal point pushes the image farther away; moving the object closer than the focal point (dₒ < f) flips dᵢ negative, producing a virtual, magnified image on the same side as the object. This is exactly how a magnifying glass works.

**Lateral magnification** m = −dᵢ/dₒ captures both size and orientation. When m is negative, the image is inverted (real images through a converging lens with dₒ > f are always inverted). When |m| > 1, the image is larger than the object; when |m| < 1, it's smaller. A camera lens forms a tiny inverted real image on the sensor (large dₒ, small dᵢ, m small and negative). A slide projector does the reverse (small dₒ just outside the focal point, large dᵢ, m large and negative — the slide is loaded upside-down on purpose so the projected image appears right-side-up).

For a diverging lens (f < 0), the equation always produces dᵢ < 0 for any positive dₒ — there is no object placement that creates a real image through a diverging lens. The image is always virtual, upright, and smaller than the object, located on the same side as the incoming light. This is why diverging lenses are used to correct nearsightedness: they make parallel incoming rays diverge slightly before they reach the eye's own converging lens, effectively moving the apparent source point to a distance the eye can focus on.
