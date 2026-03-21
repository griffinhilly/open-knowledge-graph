---
id: lens-image-formation-ray-diagrams
title: Lens Image Formation and Ray Diagrams
domain: physics
course: waves-and-optics
prerequisites:
- id: thin-lens-equation
  type: hard
builds-toward:
- optical-instruments
tags:
- image-formation
- lens
- ray-diagram
stage: formal-systems
status: draft
---

# Lens Image Formation and Ray Diagrams

## Core Idea
Thin lens equation (1/f = 1/do + 1/di) and magnification (m = -di/do) predict image location, size, and orientation. Converging lenses form real, inverted images when objects are beyond the focal point, and virtual, upright magnified images when objects are closer than f. Diverging lenses always form virtual, upright, diminished images. Ray diagrams using principal rays visualize these relationships.

## Questions

```yaml
- question: "An object is placed between a converging lens and its focal point (do < f). What kind of image does the lens form?"
  type: multiple-choice
  options:
    - "A real, inverted image on the far side of the lens — converging lenses always form real images"
    - "A virtual, upright, magnified image on the same side as the object"
    - "No image is formed when the object is inside the focal length"
    - "A real, upright image projected onto a screen on the far side"
  answer: 1
  explanation: "When the object is closer than the focal length (do < f), the three principal rays diverge after passing through the lens. Tracing them backward, they appear to originate from a point on the same side as the object — a virtual image that is upright and magnified. This is how a magnifying glass works: the object (text, insect) is held inside the focal length, and the lens produces a larger, virtual, upright image. The common misconception is that converging lenses always form real images; they only do so when do > f."

- question: "A slide projector uses a converging lens. The film slide must be placed just beyond one focal length from the lens. The resulting image on the screen will be:"
  type: multiple-choice
  options:
    - "Real, upright, and enlarged — the projector magnifies the image to fill the screen"
    - "Real, inverted, and enlarged — which is why film must be loaded upside-down"
    - "Virtual, upright, and enlarged — virtual images can be projected if the screen is large enough"
    - "Real, inverted, and diminished — the screen is far away, so the image shrinks"
  answer: 1
  explanation: "When do is just slightly greater than f, the thin lens equation gives a very large di. Magnification m = −di/do is large in magnitude and negative — large because di >> do, and negative because the image is inverted. The projected image is greatly enlarged and upside-down. This is why film must be loaded inverted: the lens flips it, producing an upright image on the screen. Option A is wrong because converging lenses with do > f always produce inverted (negative m) real images."

- question: "A diverging lens can form a real image if the object is placed far enough from the lens."
  type: true-false
  answer: false
  explanation: "False. A diverging lens (negative f) always bends rays outward, spreading them apart. The three principal rays always diverge after passing through a diverging lens, regardless of object distance. Tracing them backward, they always appear to converge on the same side as the object — a virtual image. Diverging lenses cannot project images onto screens because they never produce real images. This is why they are used in corrective lenses for nearsightedness rather than as projectors."

- question: "A negative magnification (m < 0) means the image is inverted and real."
  type: true-false
  answer: true
  explanation: "True. Magnification m = −di/do. For a real image formed by a converging lens (object beyond focal point), di is positive and do is positive, so m = −di/do is negative. A negative m means the image is flipped relative to the object — inverted. Real images are always inverted for single converging lenses with do > f. Virtual images (formed when do < f for converging, or always for diverging) have positive di (measured on the same side as the object by sign convention), giving positive m and an upright image."

- question: "Why must film in a slide projector be loaded upside-down?"
  type: short-answer
  answer: "Because a converging lens forms a real, inverted image when the object is beyond the focal length. The lens flips the film image both horizontally and vertically. Loading the film upside-down means the lens's inversion cancels out, and the projected image on the screen appears right-side up. If film were loaded right-side up, the projected image would be inverted."
  explanation: "This is a direct consequence of m = −di/do being negative for real images. The lens inverts the image as it projects it. The projector is designed around this: do is set just barely beyond f so that di (the screen distance) is very large, giving high magnification. The −di/do formula tells you the image is inverted — loading film upside-down is the practical correction for this inevitable inversion."
```

## Explainer

You already know the thin lens equation: 1/f = 1/do + 1/di, where f is focal length, do is object distance, and di is image distance. The equation gives you numbers, but **ray diagrams** give you the geometry that makes those numbers make sense. A ray diagram traces three special rays through the lens to locate the image visually.

For a **converging lens** (positive f), the three principal rays are: (1) a ray parallel to the optical axis, which bends through the far focal point after the lens; (2) a ray through the lens center, which passes straight without bending; (3) a ray through the near focal point, which emerges parallel to the axis. Where all three rays meet on the far side of the lens is where the **real image** forms — inverted and projectable onto a screen. This geometry applies whenever the object is farther than one focal length from the lens (do > f). When the object is closer than f, the three rays diverge after the lens; tracing them backward, they appear to originate from a point on the same side as the object — a **virtual image**, upright and magnified, like what you see through a magnifying glass.

A **diverging lens** (negative f) always bends rays outward, spreading them apart. The principal rays for a diverging lens, traced backward on the exit side, always converge to a virtual, upright, diminished image on the same side as the object — regardless of where the object is. This is why a diverging lens cannot project an image but is used in corrective lenses for nearsightedness: it spreads incoming light so the eye's own lens can focus it on the retina.

The magnification equation m = −di/do ties the geometry to numbers. A negative m means the image is inverted (real image from a converging lens); positive m means upright (virtual image). |m| > 1 means larger than the object; |m| < 1 means smaller. A slide projector uses a converging lens with film placed just beyond one focal length: di is much larger than do, so |m| is large and negative — the projected image is greatly enlarged and inverted, which is why film must be loaded upside-down. A camera does the reverse: the subject is far away (do >> f), so di is only slightly larger than f, giving a small, real, inverted image on the sensor.
