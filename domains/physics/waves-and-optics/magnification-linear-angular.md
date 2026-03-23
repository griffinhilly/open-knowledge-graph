---
id: magnification-linear-angular
title: Linear and Angular Magnification in Optical Systems
domain: physics
course: waves-and-optics
prerequisites:
- id: lens-image-formation-ray-diagrams
  type: hard
builds-toward:
- optical-instruments
- microscope-design-components
- telescope-design-components
tags:
- magnification
- image-size
- angular-size
stage: formal-systems
status: validated
---

# Linear and Angular Magnification in Optical Systems

## Core Idea
Linear magnification m = -i/o relates image and object sizes, becoming negative for inverted images. Angular magnification M = θ'/θ compares angles subtended at the eye, used for instruments like microscopes and telescopes where angular resolution determines usefulness.

## Questions

```yaml
- question: "A lens produces an image with linear magnification m = −3. A student says: 'The image is 3 times smaller than the object and right-side-up.' Is she correct?"
  type: multiple-choice
  options:
    - "Yes — m = −3 means the image is 3 times smaller in linear size"
    - "No — m = −3 means the image is 3 times larger and inverted"
    - "No — m = −3 means the image is 3 times smaller and inverted"
    - "Yes — the negative sign indicates a real image, which is always smaller than the object"
  answer: 1
  explanation: "Linear magnification m = −i/o, so |m| = 3 means the image is 3 times the physical size of the object — larger, not smaller. The negative sign encodes orientation: m < 0 means the image is inverted (upside down), while m > 0 means upright. A positive |m| > 1 means the image is enlarged; |m| < 1 means reduced. The student confused the sign (which encodes orientation) with the magnitude (which encodes size ratio)."

- question: "A simple magnifying glass has a focal length of 5 cm and is used with the eye relaxed (image formed at infinity). What is the angular magnification?"
  type: multiple-choice
  options:
    - "5×, since M = 25 cm / f = 25/5"
    - "0.2×, since M = f / 25 cm = 5/25"
    - "−5×, since the magnifying glass inverts the image"
    - "Infinite, because the object is placed at the focal point and the image forms at infinity"
  answer: 0
  explanation: "For a relaxed eye (image at infinity), the object is placed at the focal point f. The angular magnification is M = 25 cm / f = 25/5 = 5×, where 25 cm is the conventional near-point distance. The image forming at infinity is not a problem — it means the eye views the image with no accommodation (relaxed). The magnification is finite because it compares the angle subtended with the instrument to the angle subtended at the near point without the instrument. The negative sign for inverted images applies to linear magnification, not angular magnification."

- question: "A shorter focal length produces greater angular magnification for a simple magnifying glass."
  type: true-false
  answer: true
  explanation: "Angular magnification M = 25 cm / f, so M increases as f decreases. A 2 cm focal length lens gives M = 12.5×, while a 10 cm lens gives M = 2.5×. This makes sense geometrically: a shorter focal length allows you to place the object very close to the lens and still form a usable image, making the object subtend a much larger angle than it would at the 25 cm near point."

- question: "For a telescope observing a distant star, linear magnification is the relevant measure of how much the telescope improves visibility."
  type: true-false
  answer: false
  explanation: "For objects effectively at infinity (like stars), linear magnification is not meaningful — the image is also effectively at infinity, and 'how many times bigger physically' becomes undefined. What matters for a telescope is angular magnification: how many times larger does the star field appear, and how well can the telescope resolve two nearby stars. Angular magnification M = f_objective / f_eyepiece is the relevant quantity. A telescope that produces a large physical intermediate image but no angular magnification increase would be useless."

- question: "Why is angular magnification, rather than linear magnification, the relevant quantity for evaluating optical instruments like microscopes and telescopes?"
  type: short-answer
  answer: "The human visual system judges the apparent size of objects by the angle they subtend at the eye, not their physical size at some plane in space. A nearby coin appears larger than a distant building because it subtends a larger angle, even though the coin is physically smaller. Optical instruments produce images that the eye observes — what matters is how large that image appears to the observer, which is its angular size. Linear magnification tells you the physical size of an intermediate image at a particular plane, which is irrelevant if the eye views it from varying distances. Angular magnification directly captures the perceptual gain: how many times larger does the viewed object appear compared to the unaided eye?"
  explanation: "This distinction becomes critical in multi-element systems. A microscope's objective provides high linear magnification (the intermediate image is much larger than the object), but the eyepiece then provides angular magnification of that image to the eye. Total angular magnification = M_objective × M_eyepiece. For a telescope, where the object is at infinity and linear magnification is undefined, angular magnification M = f_obj/f_eye is the only meaningful measure."
```

## Explainer

From your work with lens image formation and ray diagrams, you know that a converging lens bends parallel rays to a focal point and that placing an object at various distances from the lens produces images at different distances and sizes. **Linear magnification** (also called transverse magnification) quantifies the size relationship: m = −i/o, where i is the image distance and o is the object distance (both measured from the lens with sign conventions applied). The negative sign encodes the orientation — when the image forms on the opposite side of the lens from the light source (a real image), i and o have the same sign under standard convention, giving m a negative value, which indicates the image is inverted. A positive m means an upright (virtual) image, which occurs when the object is inside the focal length.

Linear magnification tells you how many times larger (or smaller) the image is than the object in absolute physical dimensions. If m = −3, the image is three times the physical size of the object and upside down. This is what matters when you want to know how big a projected image will be on a screen. But for instruments you hold up to your eye — a magnifying glass, microscope, or telescope — physical image size on a surface is not what determines usefulness. What matters is the **angle** the image subtends at your eye, because your visual system judges object size by angular size, not physical size. A nearby coin looks larger than a distant building because it subtends a larger angle at your eye, even though it is physically smaller.

**Angular magnification** M = θ'/θ captures this: it is the ratio of the angle the image subtends at the eye (θ') to the angle the object subtends when viewed without the instrument (θ). For a simple magnifying glass, the conventional comparison is the angle subtended at the near point — the closest comfortable viewing distance for the naked eye, typically taken as 25 cm. If the lens allows you to bring the object much closer than 25 cm while still forming a clear image, the object subtends a much larger angle, and M = 25 cm / f (for a relaxed eye focused at infinity). A 5× magnifying glass therefore has a focal length of 5 cm.

The distinction between linear and angular magnification becomes critical for multi-element instruments. A microscope uses an **objective lens** (short focal length, high linear magnification) to form a real, enlarged intermediate image, and then an **eyepiece** (acting as a magnifying glass) to provide angular magnification of that intermediate image. The total angular magnification is the product of the two: M_total = M_objective × M_eyepiece. A telescope, by contrast, uses a large objective to collect light from a distant object (where the object is effectively at infinity and linear magnification is not meaningful) and an eyepiece to magnify the angular size — M = f_objective / f_eyepiece. Knowing which type of magnification is relevant — and what limit you're trying to push — is the key to understanding optical instrument design.
