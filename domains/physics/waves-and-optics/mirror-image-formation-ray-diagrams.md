---
id: mirror-image-formation-ray-diagrams
title: Mirror Image Formation and Ray Diagrams
domain: physics
course: waves-and-optics
prerequisites:
- id: reflection-and-law-of-reflection
  type: hard
- id: geometric-optics-ray-approximation
  type: hard
- id: real-and-virtual-images-optics
  type: soft
- id: spherical-mirror-formula
  type: hard
builds-toward:
- spherical-mirrors
tags:
- mirror
- image-formation
- ray-diagram
stage: advanced
status: validated
---
# Mirror Image Formation and Ray Diagrams

## Core Idea
The mirror equation (1/f = 1/do + 1/di) and magnification (m = -di/do) apply to both converging (concave) and diverging (convex) mirrors, with sign conventions: concave mirrors have positive f and can form real or virtual images, while convex mirrors have negative f and always form virtual images. Ray diagrams showing three principal rays predict image properties.

## Questions

```yaml
- question: "An object is placed 5 cm in front of a concave mirror with focal length 10 cm (inside the focal point). What type of image forms?"
  type: multiple-choice
  options:
    - "A real, inverted image on the same side as the object"
    - "A virtual, upright, magnified image located behind the mirror"
    - "No image forms, because objects inside the focal length produce no reflection"
    - "A real, upright image located behind the mirror"
  answer: 1
  explanation: "When an object is inside the focal length of a concave mirror (d_o < f), the reflected rays diverge and must be extended backward to find their apparent source. This yields a virtual image (d_i < 0) behind the mirror that is upright and magnified. This is exactly how a makeup mirror works — you sit inside the focal length to get a magnified, upright view. The common misconception is that concave mirrors always form real images; they only do so when the object is beyond the focal point."

- question: "A convex mirror has a focal length of −20 cm. An object is placed 30 cm in front of it. What can be said with certainty about the image?"
  type: multiple-choice
  options:
    - "The image is real, inverted, and located in front of the mirror"
    - "The image is real, upright, and located behind the mirror"
    - "The image is virtual, upright, and located behind the mirror"
    - "The image location depends on where exactly the object is placed relative to the focal point"
  answer: 2
  explanation: "Convex mirrors have a negative focal length, which means their focal point is behind the mirror (virtual focus). Applying the mirror equation: 1/d_i = 1/f − 1/d_o = 1/(−20) − 1/30 = −5/60, so d_i = −12 cm. The negative value confirms the image is behind the mirror — virtual. Magnification m = −d_i/d_o = 12/30 > 0, so the image is upright and diminished. Convex mirrors ALWAYS produce virtual, upright, diminished images regardless of object position, which is why they are used for wide-angle surveillance."

- question: "A convex mirror always produces a virtual, upright, diminished image regardless of where the object is placed."
  type: true-false
  answer: true
  explanation: "This is true. Because a convex mirror has a negative focal length, the mirror equation always yields a negative d_i (image behind the mirror) and a positive magnification less than 1 for any positive object distance. The focal point is virtual (behind the mirror), so parallel rays never converge in front of it — no real image can form. This is the key difference from concave mirrors, which can produce either real or virtual images depending on object position."

- question: "A negative magnification value (m < 0) from the mirror equation indicates that the image is smaller than the object."
  type: true-false
  answer: false
  explanation: "The sign of magnification encodes orientation, not size. A negative magnification means the image is inverted (upside down) relative to the object. The absolute value |m| determines size: |m| > 1 means the image is enlarged, |m| < 1 means diminished, |m| = 1 means same size. For example, a concave mirror forming a real image far beyond the center of curvature gives m = −3, meaning the image is inverted AND three times larger than the object."

- question: "Why does placing an object inside the focal length of a concave mirror produce a virtual image rather than a real image? What does this mean physically?"
  type: short-answer
  answer: "When the object is inside the focal length, the reflected rays diverge after reflection — they never actually converge in front of the mirror. Instead, an observer sees rays appearing to come from a point behind the mirror. This apparent source is the virtual image: light does not actually pass through it, and it cannot be projected onto a screen. Mathematically, d_o < f makes 1/d_i negative (d_i < 0), confirming the image is behind the reflecting surface."
  explanation: "The key physical point is that 'image location' always means where rays converge or appear to diverge from. A real image occurs when reflected rays actually cross in space in front of the mirror — you could catch it on a screen. A virtual image occurs when reflected rays diverge; the eye traces them backward to an apparent source that has no actual light. The focal point is the dividing line: objects beyond f produce converging reflected rays (real image); objects inside f produce diverging reflected rays (virtual image)."
```

## Explainer

You already know that reflection obeys a simple rule: the angle of incidence equals the angle of reflection, measured from the normal to the surface. For a flat mirror, every reflected ray can be traced backward to a single apparent point behind the mirror — the virtual image of the source. Curved mirrors do the same thing, but because the normal direction changes across the mirror surface, different parts of the mirror redirect light differently. This controlled redirection is what allows curved mirrors to focus light or spread it, producing images that flat mirrors cannot.

The **ray diagram** is the tool that makes image location predictable without tracing every possible ray. For any curved mirror, three special rays from an object point are easy to draw: (1) a ray parallel to the optical axis reflects through the focal point; (2) a ray passing through the focal point reflects parallel to the axis; (3) a ray aimed at the center of curvature reflects straight back. Where any two of these three rays converge after reflection — that is the image. If the reflected rays diverge, you extend them backward; they appear to come from a point behind the mirror, forming a **virtual image** (not a real intersection of light, but a perceived source location).

The **mirror equation** 1/f = 1/d_o + 1/d_i encodes this geometry algebraically. The sign convention is: distances measured in front of the mirror (where light actually travels) are positive; distances behind the mirror are negative. A **concave mirror** — like the inside of a bowl — has a positive focal length because the focal point is in front of the surface. It can form real images (d_i > 0) when the object is beyond the focal point, and virtual images (d_i < 0) when the object is inside the focal point. A **convex mirror** — like the outside of a sphere — has a negative focal length; its focal point is behind the surface, so it always forms virtual, diminished, upright images. This is why convex mirrors are used for wide-field surveillance — they show a broad scene, though the images are smaller than reality.

Magnification m = −d_i / d_o tells you both size and orientation. A negative magnification means the image is inverted; positive means upright. Magnification greater than 1 in absolute value means the image is enlarged; less than 1 means diminished. For a concave makeup mirror, you place your face inside the focal length — the image appears virtual, upright, and magnified, precisely because d_i is negative and larger in magnitude than d_o. Learning to read the signs fluently is the key skill: each sign carries physical meaning about whether light really converges there or merely appears to.
