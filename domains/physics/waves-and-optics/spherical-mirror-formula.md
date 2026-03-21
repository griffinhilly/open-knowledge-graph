---
id: spherical-mirror-formula
title: Spherical Mirror Formula and Sign Conventions
domain: physics
course: waves-and-optics
prerequisites:
- id: mirror-equation
  type: soft
- id: paraxial-ray-approximation
  type: hard
builds-toward:
- mirror-image-formation-ray-diagrams
tags:
- spherical-mirrors
- mirror-equation
- focal-length
stage: formal-systems
status: draft
---

# Spherical Mirror Formula and Sign Conventions

## Core Idea
The mirror equation 1/f = 1/o + 1/i applies to spherical mirrors with focal length f = R/2 (R is radius of curvature). Sign conventions matter: concave mirrors have positive f; convex mirrors have negative f. Real objects have positive o; virtual objects (uncommon) have negative o.

## Questions

```yaml
- question: "An object is placed 10 cm in front of a concave mirror with focal length 15 cm (the object is inside the focal length). Using 1/f = 1/o + 1/i, what type of image does the mirror form?"
  type: multiple-choice
  options:
    - "Real, inverted, and magnified — concave mirrors always form real images"
    - "Virtual, upright, and magnified — the formula gives a negative image distance"
    - "Virtual, inverted, and reduced — the object is too close to form a proper image"
    - "No image forms — the formula is only valid when the object is beyond the focal point"
  answer: 1
  explanation: "Substituting: 1/15 = 1/10 + 1/i → 1/i = 1/15 − 1/10 = −1/30, so i = −30 cm. The negative image distance means the image is virtual (behind the mirror). Magnification m = −i/o = −(−30)/10 = +3, so the image is upright and 3× larger than the object. The misconception in option A — that concave mirrors always form real images — is only true when the object is beyond the focal point. Inside the focal point, a concave mirror acts like a magnifying glass, forming a virtual image."

- question: "A car's convex rear-view mirror has a focal length of −25 cm. An object is 50 cm away. What does the negative image distance in the solution tell you?"
  type: multiple-choice
  options:
    - "The image is real and forms in front of the mirror where you can project it on a screen"
    - "The image is virtual and appears to be located behind the mirror's surface"
    - "The calculation is invalid because convex mirrors cannot form images of real objects"
    - "The object is on the wrong side of the mirror"
  answer: 1
  explanation: "For a convex mirror, f is negative. Solving: 1/(−25) = 1/50 + 1/i → 1/i = −1/25 − 1/50 = −3/50, so i ≈ −16.7 cm. The negative i means the image is behind the mirror — a virtual image that light rays never actually pass through. Your eye traces the diverging reflected rays backward and perceives the image as if it were behind the glass. This is the image you see in a rear-view mirror: always upright, always smaller, always virtual."

- question: "A concave mirror with a positive focal length always forms a real image, regardless of where the object is placed."
  type: true-false
  answer: false
  explanation: "A concave mirror forms a real image only when the object is beyond the focal point (o > f). When the object is between the focal point and the mirror (o < f), the reflected rays diverge and the mirror forms a virtual, upright, magnified image — the same principle used in makeup mirrors and shaving mirrors. The mirror equation reflects this: when o < f, the formula gives a negative image distance, indicating a virtual image. 'Concave always means real' is one of the most common misconceptions in mirror optics."

- question: "For a convex mirror, the focal length is negative because the focal point is located behind the mirror on the non-reflecting side."
  type: true-false
  answer: true
  explanation: "The sign convention is grounded in the direction of light travel: positive distances are measured in the direction from which light arrives (in front of the mirror), and negative distances are measured behind it. A convex mirror's center of curvature and focal point both lie behind the reflecting surface — they are in the region where light does not actually travel after reflection. Therefore f is negative for a convex mirror. This is why convex mirrors can only form virtual images: with f negative, i is always negative regardless of object distance."

- question: "Why does the sign convention for mirror equations define positive distances in the direction of incoming light rather than using some other arbitrary convention?"
  type: short-answer
  answer: "The sign convention encodes the physics of image formation. Distances measured in the direction light travels after reflection correspond to real images — places where reflected rays actually converge. Distances in the opposite direction correspond to virtual images — apparent locations behind the mirror where diverging rays seem to originate. A consistent convention tied to light propagation direction means the sign of the image distance directly tells you whether the image is real (positive) or virtual (negative), without needing separate rules for each case."
  explanation: "This is why the sign convention is not arbitrary: it aligns the mathematics with the physical distinction between real and virtual images. Real images can be projected on a screen; virtual images cannot. The formula's sign outputs this answer automatically when the convention is applied correctly, making the mathematics directly interpretable as physics."
```

## Explainer

You already know from the paraxial approximation that when rays travel at small angles to the optical axis, the geometry of reflection becomes linear. The **spherical mirror formula** is the direct payoff: a single equation, 1/f = 1/o + 1/i, that tells you where an image forms given the object distance and the mirror's focal length. The derivation follows from the paraxial geometry of a spherical mirror — tracing two paraxial rays from an off-axis object point and finding where they cross after reflection.

The key geometric fact is that a spherical mirror has a **center of curvature** C at distance R from the mirror surface, and a **focal point** F at distance R/2. Any ray parallel to the optical axis reflects through F; any ray directed toward C reflects straight back. These are the two standard construction rays for ray diagrams. The focal length f = R/2 is not a coincidence — it follows from the paraxial approximation applied to the law of reflection on a spherical surface. Without the paraxial assumption, rays from different heights would focus at slightly different points (spherical aberration), and a single focal length would not exist.

The **sign convention** is the part that trips students up most. The convention is defined by the physics: distances measured in the direction light travels from the object are positive; distances measured against that direction are negative. For a real object in front of a concave mirror, both o and f are positive, and the equation predicts where the real image forms on the same side as the object. For a convex mirror, f is negative (the focal point is behind the mirror, on the non-reflecting side), and the image distance i comes out negative too — indicating a **virtual image** behind the mirror that light rays never actually pass through, but that your eye perceives by tracing the diverging reflected rays backward. This is the image you see when looking into a car's convex rear-view mirror: always upright, always smaller than the object, always virtual.

The **magnification** m = −i/o ties the formula to what you actually observe. When m is negative, the image is inverted (real images from concave mirrors); when m is positive, the image is upright (virtual images). When |m| > 1, the image is enlarged; when |m| < 1, it is reduced. These four combinations — inverted/upright, real/virtual, enlarged/reduced — map cleanly onto the different regions of object distance relative to f and R, and understanding which combination applies in a given configuration is the practical skill the formula enables.
