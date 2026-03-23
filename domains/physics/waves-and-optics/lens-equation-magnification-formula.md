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
stage: advanced
status: validated
---

# Thin Lens Equation and Image Formation

## Core Idea
The thin lens equation 1/s_o + 1/s_i = 1/f relates object distance, image distance, and focal length. Magnification m = -s_i/s_o is positive (upright image) when m > 0 and negative (inverted) when m < 0. Real images form when s_i > 0 (converging lens with s_o > f); virtual images form when s_i < 0. These relationships are identical to mirror equations, reflecting the mathematical duality between reflection and refraction.

## Questions

```yaml
- question: "An object is placed 10 cm in front of a converging lens with focal length 15 cm. Which correctly describes the image?"
  type: multiple-choice
  options:
    - "Real, inverted, on the far side of the lens"
    - "Virtual, upright, on the same side as the object"
    - "Real, upright, on the far side of the lens"
    - "No image forms because the object is inside the focal length"
  answer: 1
  explanation: "When s_o < f, solving 1/s_i = 1/f − 1/s_o gives a negative s_i (here, −30 cm), meaning the image is virtual and on the same side as the object. The magnitude |m| = 30/10 = 3 and m is positive — upright and magnified. This is exactly the magnifying-glass case. Option D is wrong: an image always forms; it is simply virtual when s_o < f."

- question: "A slide projector places a slide just outside the focal length of a converging lens (s_o slightly > f). The image on the distant screen is inverted, so the slide must be loaded upside-down. Which statement best explains why the image is inverted?"
  type: multiple-choice
  options:
    - "The lens flips the image because it is a diverging lens"
    - "When s_o > f for a converging lens, s_i > 0 (real image on the far side), and the magnification m = −s_i/s_o is negative, indicating an inverted image"
    - "The image is inverted only because s_o is very large compared to f"
    - "All lenses invert images regardless of object distance"
  answer: 1
  explanation: "Real images (s_i > 0) form when s_o > f for a converging lens. The magnification formula m = −s_i/s_o is negative whenever s_i and s_o have the same sign, which is always the case for real images. Negative m means inverted. Option D is wrong: when s_o < f, a converging lens produces a virtual, upright image (m > 0)."

- question: "A converging lens always produces a real image."
  type: true-false
  answer: false
  explanation: "A converging lens produces a virtual image whenever the object is placed inside the focal length (s_o < f). In that case, 1/s_i = 1/f − 1/s_o becomes negative, giving s_i < 0 — the image is on the same side as the object and cannot be projected on a screen. This is the magnifying glass mode. 'Converging lens' describes the lens geometry, not a guarantee of image type."

- question: "A positive value of magnification (m > 0) from the formula m = −s_i/s_o always means the image is larger than the object."
  type: true-false
  answer: false
  explanation: "The sign of m encodes orientation, not size. Positive m means the image is upright (virtual); negative m means inverted (real). The magnitude |m| encodes size ratio. A virtual image could have m = +0.5 — upright and smaller than the object. Size and orientation are two independent pieces of information packed into a single signed number."

- question: "Why does the thin lens equation predict that s_i approaches infinity as the object approaches the focal point, and what practical optical device exploits this behavior?"
  type: short-answer
  answer: "As s_o → f, the term 1/f − 1/s_o → 0, so 1/s_i → 0 and s_i → ∞. Physically, rays from an object at the focal point exit the lens parallel — they never converge. A collimator or beam expander exploits this: placing a point source at the focal point produces a parallel output beam."
  explanation: "This limiting case is not a failure of the equation — it is a real physical result. Slide projectors, flashlights, and laser beam expanders all exploit it. The equation is continuous: as the object moves toward f from outside, s_i grows toward +∞ (real image pushed further away); as the object moves toward f from inside, s_i grows toward −∞ (virtual image pushed further away on the same side). The focal point is the singularity where the image 'goes to infinity.'"
```

## Explainer

From your work on focal length and diopters, you know that a converging lens bends parallel incoming rays to converge at the focal point, a distance f behind the lens. The thin lens equation extends this: what happens when light doesn't come from infinity? When an object sits at a finite distance s_o, the rays arriving at the lens are slightly diverging rather than parallel. The lens still bends them toward a focus, but that focus lands further away than f. The **thin lens equation**, 1/s_o + 1/s_i = 1/f, captures this relationship precisely.

A useful way to read the equation: think of 1/f as the converging power the lens provides, and 1/s_o as the "divergence penalty" from the object being at a finite distance. The image distance s_i is what's left after the lens overcomes that divergence. As s_o decreases toward f, s_i increases toward infinity — the image "goes to infinity" when the object sits exactly at the focal point, which means outgoing rays are parallel. This is how a slide projector works: place the slide just outside the focal point, and the image forms far away on a distant screen.

**Magnification** m = −s_i / s_o captures two things at once. The magnitude |m| is the size ratio: if |m| = 3, the image is three times taller than the object. The sign tells you orientation. The negative sign convention means that **real images** — formed on the far side of a converging lens when s_o > f — are inverted (m is negative). A **virtual image** — formed on the same side as the object when s_o < f, as with a magnifying glass held close — is upright (m is positive). When you hold a magnifying glass over text and see a larger upright image, you're looking at a virtual image; when a projector casts an inverted image on a screen, that's a real image.

If you studied the concave mirror equation (1/d_o + 1/d_i = 1/f), you'll recognize the identical structure. The mathematical duality between lenses and mirrors is not a coincidence — both redirect rays using a surface characterized by a focal length, and the geometry produces the same algebraic form. The key difference in application: for a converging lens, real images form on the far (transmission) side, s_i > 0; for a concave mirror, real images form on the front (reflection) side. Track the sign conventions carefully for each geometry, and the same equation does all the work.
