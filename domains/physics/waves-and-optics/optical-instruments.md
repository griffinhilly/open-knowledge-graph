---
id: optical-instruments
title: Optical Instruments
domain: physics
course: waves-and-optics
prerequisites:
- id: thin-lens-equation
  type: hard
- id: lens-combinations
  type: hard
- id: mirror-equation
  type: soft
tags:
- camera
- microscope
- telescope
- angular magnification
- resolving power
stage: formal-systems
status: validated
---

# Optical Instruments

## Core Idea
Optical instruments use lens combinations to magnify or focus images. A simple magnifier uses a converging lens to produce a magnified virtual image at the near point. A compound microscope uses an objective (short focal length) to form a real magnified intermediate image, then an eyepiece to magnify that image again: M_total = M_obj × M_eye. A refracting telescope uses a large-aperture objective for light-gathering and an eyepiece for angular magnification M = −f_obj/f_eye. Resolution is ultimately limited by diffraction.

## How It's Best Learned
Build a simple telescope using two lenses in a cardboard tube; measure the angular magnification by comparing the apparent size of a distant ruler with and without the telescope. Derive the formula from the two-lens analysis.

## Common Misconceptions
- Magnification and resolution are distinct; a telescope can magnify greatly but still not resolve two close stars if the aperture is too small.
- The eyepiece of a microscope does not form a real image on the retina directly; it acts as a magnifier of the intermediate real image.

## Questions

```yaml
- question: "Telescope A has an objective focal length of 1000 mm and an eyepiece focal length of 10 mm. Telescope B has an objective focal length of 500 mm and the same eyepiece. Both observe two closely spaced stars. Which telescope resolves the stars better, and why?"
  type: multiple-choice
  options:
    - "Telescope A, because its longer focal length gives higher angular magnification"
    - "Neither — magnification and resolution are the same property and increase together"
    - "It depends entirely on which telescope has the larger objective aperture, not on the focal lengths"
    - "Telescope B, because shorter focal lengths produce sharper images"
  answer: 2
  explanation: "Resolution is diffraction-limited and depends on *aperture diameter*, not focal length or magnification. The Rayleigh criterion gives minimum resolvable angle ∝ λ/D, where D is the aperture diameter. A longer focal length gives higher magnification (M = f_obj/f_eye = 100× vs. 50×) but if both telescopes have the same aperture, they resolve the same minimum angular separation. 'Empty magnification' is the term for magnifying beyond what resolution supports — you get a bigger but blurrier image."

- question: "A compound microscope has an objective lens with magnification M_obj = 40× and an eyepiece with magnification M_eye = 10×. What is the total magnification, and what physical arrangement makes this possible?"
  type: multiple-choice
  options:
    - "50× total, because the magnifications add; both lenses are close together"
    - "400× total, because the magnifications multiply; the objective forms a real intermediate image that the eyepiece then magnifies"
    - "400× total, because the magnifications multiply; both lenses are at the same focal point"
    - "40× total, because only the objective contributes to resolving fine detail"
  answer: 1
  explanation: "Total magnification in a compound microscope is multiplicative: M_total = M_obj × M_eye = 40 × 10 = 400×. This multiplicative effect requires a physical separation: the objective lens (very short focal length, placed just past its focal point from the specimen) forms a real, inverted, enlarged intermediate image inside the microscope tube. That intermediate image acts as a new object for the eyepiece, which magnifies it again as a simple magnifier. The long tube length is necessary to place the intermediate image at the correct location."

- question: "A larger objective aperture on a telescope improves its ability to resolve two closely spaced stars."
  type: true-false
  answer: true
  explanation: "Angular resolution is diffraction-limited by the aperture diameter D. The minimum resolvable angle is approximately θ_min = 1.22 λ/D (Rayleigh criterion). Larger D means smaller θ_min, meaning finer angular detail can be distinguished. This is why the world's largest telescopes — from Hubble to ground-based giants — have enormous primary mirrors: aperture is what determines resolving power, independent of how much magnification is applied."

- question: "Increasing the magnification of a telescope always improves its ability to resolve two closely spaced stars."
  type: true-false
  answer: false
  explanation: "Magnification and resolution are independent properties. Resolution is set by aperture diameter (diffraction limit), not by magnification. Once you reach the diffraction limit, increasing magnification only makes the blurry disk larger — 'empty magnification.' Two stars that are closer together than θ_min = 1.22λ/D cannot be resolved regardless of how much the image is magnified. The only way to improve resolution is to increase the aperture."

- question: "Explain why magnification and resolution are distinct properties of an optical instrument, and what physical factor sets the limit for each."
  type: short-answer
  answer: "Magnification measures how much larger an image appears compared to the unaided eye — it is a ratio of angles or sizes and is set by the focal lengths of the lenses (M = f_obj/f_eye for a telescope). Resolution measures the smallest angular or spatial separation that can be distinguished as two separate features; it is set by diffraction at the aperture and scales as λ/D (aperture diameter D). A telescope can magnify a pair of stars to appear large yet still show them as a single blurred point if the aperture is too small to resolve them. Increasing magnification without increasing aperture yields empty magnification: a bigger but not sharper image."
  explanation: "The distinction matters practically: astronomers wanting to study binary stars or planetary surface detail need large apertures, not merely high magnification eyepieces. Conversely, a bright but isolated object like the moon can be usefully studied with high magnification even from a modest aperture, since the limit is not resolution but contrast and brightness. Understanding that these are independent design parameters is essential for choosing or designing instruments for specific observational goals."
```

## Explainer

You've worked through the thin lens equation and lens combinations — the geometry of how a single lens bends rays and where images form. Optical instruments take that foundation and engineer multi-lens systems for specific purposes: magnifying small nearby objects, resolving fine detail, or gathering light from astronomical distances. In each case, the design logic follows directly from the ray optics you already know.

The simplest instrument is the **magnifying glass**: a single converging lens positioned so the object lies inside its focal length. The lens intercepts the diverging rays from the object and bends them into a less-diverging bundle reaching your eye. Because the bundle is less diverging than it would be without the lens, your eye perceives the light as coming from a larger virtual image farther away. The **angular magnification** M = 25 cm / f measures the benefit: a 5 cm focal length lens magnifies 5×, meaning the object appears to subtend 5 times the angle it would at the standard near point of 25 cm.

A **compound microscope** stacks two magnifying stages to reach much higher magnifications than any single lens can provide. The **objective lens** — very short focal length, placed just beyond its focal point from the specimen — creates a real, inverted, greatly magnified intermediate image inside the tube. That intermediate image then becomes the object for the **eyepiece**, which acts as a simple magnifier to produce the final virtual image your eye observes. Total magnification is multiplicative: M_total = M_objective × M_eyepiece. This staged design explains the physical layout of a microscope: the long tube separates the two lenses to allow the objective to form its real intermediate image at the correct location for the eyepiece.

A **refracting telescope** has the opposite challenge: the objects are already far away, so the goal is not photographic magnification but **angular magnification** — making the small apparent angle between two stars seem larger. The large-aperture objective gathers parallel incoming rays from a distant point and brings them to focus at its focal point. The eyepiece then re-collimates those rays so your eye receives them as a parallel bundle from a wider angle. The magnification formula M = −f_objective / f_eyepiece shows why astronomical telescopes have long tubes: a long-focal-length objective yields high magnification, but it must be physically separated from the eyepiece by roughly f_obj + f_eye. Critically, **magnification and resolution are independent**: a small-aperture telescope can magnify a star enormously yet still cannot resolve whether it is a binary, because angular resolution is diffraction-limited by aperture diameter — the larger the objective, the finer the detail it can distinguish.
