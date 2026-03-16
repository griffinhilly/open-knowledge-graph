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
status: draft
---

# Linear and Angular Magnification in Optical Systems

## Core Idea
Linear magnification m = -i/o relates image and object sizes, becoming negative for inverted images. Angular magnification M = θ'/θ compares angles subtended at the eye, used for instruments like microscopes and telescopes where angular resolution determines usefulness.

## Explainer

From your work with lens image formation and ray diagrams, you know that a converging lens bends parallel rays to a focal point and that placing an object at various distances from the lens produces images at different distances and sizes. **Linear magnification** (also called transverse magnification) quantifies the size relationship: m = −i/o, where i is the image distance and o is the object distance (both measured from the lens with sign conventions applied). The negative sign encodes the orientation — when the image forms on the opposite side of the lens from the light source (a real image), i and o have the same sign under standard convention, giving m a negative value, which indicates the image is inverted. A positive m means an upright (virtual) image, which occurs when the object is inside the focal length.

Linear magnification tells you how many times larger (or smaller) the image is than the object in absolute physical dimensions. If m = −3, the image is three times the physical size of the object and upside down. This is what matters when you want to know how big a projected image will be on a screen. But for instruments you hold up to your eye — a magnifying glass, microscope, or telescope — physical image size on a surface is not what determines usefulness. What matters is the **angle** the image subtends at your eye, because your visual system judges object size by angular size, not physical size. A nearby coin looks larger than a distant building because it subtends a larger angle at your eye, even though it is physically smaller.

**Angular magnification** M = θ'/θ captures this: it is the ratio of the angle the image subtends at the eye (θ') to the angle the object subtends when viewed without the instrument (θ). For a simple magnifying glass, the conventional comparison is the angle subtended at the near point — the closest comfortable viewing distance for the naked eye, typically taken as 25 cm. If the lens allows you to bring the object much closer than 25 cm while still forming a clear image, the object subtends a much larger angle, and M = 25 cm / f (for a relaxed eye focused at infinity). A 5× magnifying glass therefore has a focal length of 5 cm.

The distinction between linear and angular magnification becomes critical for multi-element instruments. A microscope uses an **objective lens** (short focal length, high linear magnification) to form a real, enlarged intermediate image, and then an **eyepiece** (acting as a magnifying glass) to provide angular magnification of that intermediate image. The total angular magnification is the product of the two: M_total = M_objective × M_eyepiece. A telescope, by contrast, uses a large objective to collect light from a distant object (where the object is effectively at infinity and linear magnification is not meaningful) and an eyepiece to magnify the angular size — M = f_objective / f_eyepiece. Knowing which type of magnification is relevant — and what limit you're trying to push — is the key to understanding optical instrument design.
